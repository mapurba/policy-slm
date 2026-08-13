# 12.8 SQL Queries

To fully support the query capabilities of a database and avoid the difficulty of translating native SQL queries into an XDS format, the driver supports native SQL query processing. You can embed select statements in XDS documents in exactly the same way as any other SQL statement.

For example, assume that the table usr has the following contents:

*Table 12-2* Example Contents

| idu | fname | lname |
| 1 | John | Doe |

The XML document below results in an output document containing a single result set.

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <jdbc:statement jdbc:type="query">
        <jdbc:sql>SELECT * FROM indirect.usr</jdbc:sql>
    </jdbc:statement>
</input>
```

```
<output xmlns:jdbc="urn:dirxml:jdbc">
    <jdbc:result-set jdbc:number-of-rows="1">
        <jdbc:row jdbc:number="1">
            <jdbc:column jdbc:name="idu"
                         jdbc:position="1"
                         jdbc:type="java.sql.Types.BIGINT
                <jdbc:value>l</jdbc:value>
            </jdbc:column>
            <jdbc:column jdbc:name="fname"
                         jdbc:position="2"
                         jdbc:type="java.sql.Types.VARCHAR>
                <jdbc:value>John</jdbc:value>
            </jdbc:column>
            <jdbc:column jdbc:name="lname"
                         jdbc:position="3"
                         jdbc:type="java.sql.Types.VARCHAR>
                <jdbc:value>Doe</jdbc:value>
            </jdbc:column>
        </jdbc:row>
    </jdbc:result-set>
    <status level="success"/>
</output>
```

SQL queries always produce a single <jdbc:result-set> element whether or not the result set contains any rows. If the result set is empty, the jdbc:number-of-rows attribute is set to zero.

You can embed more than one query in a document. SQL queries don’t require that the referenced tables/views in the synchronization schema be visible to the driver. However, XDS queries do.

If you are building an event to be sent via the Command Processor instead of part of the regular event flow, you need to build the XML in a nodeset variable and use the Parse XML token before issuing the command. For more information, see "[XML Parse](../../../identity-manager-48/policy_designer/data/tokenxmlparse.html#tokenxmlparse)" in the [NetIQ Identity Manager - Using Designer to Create Policies](../../../identity-manager-48/policy_designer/data/using-designer-to-create-policies.html#using-designer-to-create-policies).

Example logic XML:

```
<policy xmlns:cmd="http://www.novell.com/nxsl/java/com.novell.nds.dirxml.driver.XdsCommandProcessor">
  <rule>
    <description>generate SQL Select Statement</description>
    <conditions>
      <and>
        <if-class-name op="equal">User</if-class-name>
      </and>
    </conditions>
    <actions>
      <do-set-local-variable name="sqlstatement">
        <arg-node-set>
          <token-xml-parse>
            <token-text xml:space="preserve">&lt;input xmlns:jdbc="urn:dirxml:jdbc">&lt;jdbc:statement jdbc:type="query">&lt;jdbc:sql></token-text>
            <token-text xml:space="preserve">SELECT * FROM lab.users;</token-text>
            <token-text xml:space="preserve">&lt;/jdbc:sql>&lt;/jdbc:statement>&lt;/input></token-text>
          </token-xml-parse>
        </arg-node-set>
      </do-set-local-variable>
      <do-trace-message color="yellow" level="1">
        <arg-string>
          <token-xpath expression="cmd:execute($destCommandProcessor, $sqlstatement)"/>
        </arg-string>
      </do-trace-message>
      <do-veto/>
    </actions>
  </rule>
</policy
```

*NOTE:*The queries on the Publisher channel with srcCommandProcessor are scheduled for execution on the Subscriber channel and the script processing does not wait for the result to become available.
