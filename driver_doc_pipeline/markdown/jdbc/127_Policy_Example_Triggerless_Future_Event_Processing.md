# L.0 Policy Example: Triggerless Future Event Processing

The following example assumes that a “commence” attribute exists and does the following:

* Holds the time stamp value indicating when an event should be processed
* Contains an integer or Java string time stamp value. See [Time Syntax](configure-jdbc-driver-specific-parameters.html#b1pu3jg).

```
<policy    xmlns:Timestamp="http://www.novell.com/nxsl/java/java.sql.Timestamp"
  xmlns:TimestampUtil="http://www.novell.com/nxsl/java/com.novell.nds.dirxml.driver.jdbc.db.TimestampUtil"
  xmlns:jdbc="urn:dirxml:jdbc">
<rule>
<description>Get commencement date from datasource.</description>
  <conditions>
    <and>
      <if-xpath op="true">.</if-xpath>
    </and>
  </conditions>
  <actions>
    <do-set-local-variable name="commence">
      <arg-string>
        <token-src-attr class-name="User" name="commence"/>
      </arg-string>
    </do-set-local-variable>
  </actions>
</rule>
```

```
<rule>
  <description>Break if commencement date unavailable.</description>
  <conditions>
    <and>
      <if-local-variable name="commence" op="equal"/>
    </and>
  </conditions>
  <actions>
    <do-break/>
  </actions>
</rule>
```

```
<rule>
<description>Parse times.</description>
  <conditions>
    <and>
      <if-xpath op="true">.</if-xpath>
    </and>
  </conditions>
  <actions>
    <do-set-local-variable name="dbTime">
      <arg-object>
        <token-xpath expression="Timestamp:valueOf(@jdbc:database-local-time)"/>
      </arg-object>
    </do-set-local-variable>
    <do-set-local-variable name="eventTime">
      <arg-object>
        <token-xpath expression="Timestamp:valueOf($commence)"/>
      </arg-object>
    </do-set-local-variable>
  </actions>
</rule>
<rule>
  <description>Is commencement date after database time?</description>
  <conditions>
    <and>
      <if-xpath op="true">.</if-xpath>
    </and>
  </conditions>
  <actions>
    <do-set-local-variable name="after">
      <arg-string>
        <token-xpath expression="TimestampUtil:after($eventTime, $dbTime)"/>
      </arg-string>
    </do-set-local-variable>
  </actions>
</rule>
```

```
<rule>
<description>Retry if future event.</description>
  <conditions>
    <and>
      <if-local-variable name="after" op="equal">true</if-local-variable>
    </and>
  </conditions>
  <actions>
    <do-status level="retry">
      <arg-string>
        <token-text xml:space="preserve">Future event detected.</token-text>
      </arg-string>
    </do-status>
  </actions>
</rule>
</policy>
```
