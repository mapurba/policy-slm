# 1.2 SCIM Driver Packages

In Designer, navigate to Help > Package Updates to update the SCIM driver packages. When you update the required driver packages in designer, the designer updates the policies, rules and the parameters that are associated with the driver object. These rules, policies, and associated parameters are used to establish communication and synchronize data between Identity Manager and the connected application.

The SCIM driver packages and the details are:

* SCIM Base (NETQSCIMBASE): Contains the mandatory basic SCIM configurations required for SCIM driver. The base configurations include:

  + Driver Authentication methods such as Basic and OAuth2.0.
  + Subscriber settings with HTTPS error codes to retry such as 307, 400 etc,.
  + Publisher settings with Polling interval, Heartbeat interval, and Polling Resource option.
  + Advanced settings with the Schema and Modifier setting options.
  + Options for Remote Loader settings.
* SCIM Default (NETQSCIMDCFG): Contains the mandatory default configurations required for configuring the SCIM driver. The default configurations include the policies as shown below:

  + Matching policy: This policy finds the matches for objects based on attributes. SCIM Driver by default, has implementation for generating filters for simple and complex attributes. It does not have capability to provide filter for complex multivalue attribute.

    If the attribute is complex multivalued, then the SCIM driver generates the filter using the value enclosed within the “Value” element in the query.

    For Example:

    ```
    <nds dtdversion="4.0" ndsversion="8.x">
            <source>
            <product edition="Advanced" version="4.8.0.0">DirXML</product>
            <contact>NetIQ Corporation</contact>
            </source>
            <input>
            <query class-name="Users" event-id="0" scope="subtree">
              <search-class class-name="Users"/>
              <search-attr attr-name="Internet Email address">
              <value>asdhscnSL@mf.com</value>
              </search-attr>
              <read-attr/>
            </query>
            </input>
          </nds>
    ```

    Since search-attr attr-name is Internet Email address, it is a complex multivalue. SCIM driver generates the filter using the “Value” element as follows:

    https://<Base Url>/scim/Users?filter=asdhscnSL@mf.com

    Appropriate filter must be provided by the user using the policy.

    The below sample snippet is the output Transformation Policy to provide an appropriate filter for complex multivalue.

    ```
    <?xml version="1.0" encoding="UTF-8"?><policy>
      <rule>
        <description>Replace search-attr value with appropriate filter.</description>
        <conditions>
          <and>
            <if-class-name op="equal">urn:ietf:params:scim:schemas:core:2.0:User</if-class-name>
            <if-operation op="equal">query</if-operation>
          </and>
        </conditions>
        <actions>
          <do-for-each>
            <arg-node-set>
              <token-xpath expression="search-attr"/>
            </arg-node-set>
            <arg-actions>
              <do-set-local-variable name="searchAttr">
                <arg-node-set>
                  <token-xpath expression="$current-node/@attr-name"/>
                </arg-node-set>
              </do-set-local-variable>
              <do-if>
                <arg-conditions>
                  <and>
                    <if-local-variable name="searchAttr" op="equal">emails:work:value</if-local-variable>
                  </and>
                </arg-conditions>
                <arg-actions>
                  <do-set-local-variable name="emailValue">
                    <arg-string>
                      <token-xpath expression="$current-node/value"/>
                    </arg-string>
                  </do-set-local-variable>
                  <do-strip-xpath expression="$current-node/value"/>
                  <do-append-xml-element expression="$current-node" name="value"/>
                  <do-append-xml-text expression="$current-node/value">
                    <arg-string>
                      <token-text xml:space="preserve">emails eq </token-text>
                      <token-text xml:space="preserve">"</token-text>
                      <token-local-variable name="emailValue"/>
                      <token-text xml:space="preserve">"</token-text>
                    </arg-string>
                  </do-append-xml-text>
                </arg-actions>
                <arg-actions/>
              </do-if>
            </arg-actions>
          </do-for-each>
        </actions>
      </rule>
    </policy>
    ```

  + Creation policy: The creation policy defines the conditions that must be met to create a new object. The creation policy is of two types, Subscriber Creation policy and Publisher Creation policy. The policy definitions can be same or different for the respective channels.

    For example, if you try to create a new user in Identity Manager by providing only the user's name and user ID, the user is created in Identity Manager but does not sync to the connected application. This happens when the definitions for creating the user are not specified completely in the creation policy. You can add templates in the creation policy to ensure that all the required definitions are specified.

    The Creation Policies are commonly used to:

    - Reject the creation of objects that don’t qualify, possibly because of a missing attribute.
    - Provide default attribute values.
  + Placement policy: This policy specifies the containers where objects are to be placed.
  + Command Transformation policy: This policy is to provide the final processing commands that are sent to the Identity Manager or to the connected application.
  + Schema Mapping policy: The Schema Mapping policies store the definition of the class and attribute mappings between the Identity Manager and the connected application.
  + Filter: Filter allows the object and its specific attributes to synchronize between the Identity Manger and the connected application.
* SCIM JSON (NETQSCIMJSON): (Optional) This package contains the JSON configurations for SCIM driver to implement XDS to JSON conversion. The JSON that is created by using this package will be compatible with the connected application, to perform required operations.
