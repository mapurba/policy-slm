# 5.5 Managing Driver Operation Data

The driver shim applies special handling to Subscriber commands based on the <driver-operation-data> element. On the Subscriber channel, the <driver-operation-data> element can be added to a command for two purposes:

* Specify XML data that you want included with the command result. In this way, you can match commands with the responses they generate, which is useful for creating associations.
* Override default Subscriber options on a per-command basis.

As discussed in [Understanding Driver Operation Data](soap-driver-concepts.html#bvp9xer), the <driver-operation-data> element is added to the command from one of the Subscriber channel policies. The driver shim removes the operation data from the command before it is sent to the application, and restores the <driver-operation-data> element (and all child elements) to the resulting response.

```
<nds dtdversion="4.0" ndsversion="8.x">
   <source>
      <product edition="Advanced" version="4.0.2.0">DirXML</product>
         <contact>Novell, Inc.</contact>
    </source>
           <input>
            <user email="thomas.wagner@example.COM" enabled="true"
ns1:password="Password1!" username="thomas.wagner"
xmlns:ns1="http://docs.openstack.org/identity/api/ext/OS-KSADM/v1.0"
xmlns:ns2="http://docs.openstack.org/identity/api/v2.0">
           <driver-operation-data>
                 <request-headers remove-existing="true">
                    <request-header name="accept">application/xml
                    </request-header>
                 <request-header
             name="X-Auth-Token">262f9eefc1e9488fa65474c5aa0f5ca1</request-header>
                 </request-headers>
           </driver-operation-data>
          </user>
         </input>
</nds>
```

<driver-operation-data> must be a child element of the operation node which is the <user> node in this example. Otherwise, <user> and <driver-operation-data> are considered as separate operations and will not be applied to the <user> operation.

Consider another example below.

```
<input>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
        <soapenv:Header>
            <soapenv:Body>
                <ser:findRoleByExampleWithOperatorRequest xmlns:ser="http://www.novell.com/role/service">
                    <ser:role>
                        <ser:name>abRole</ser:name>
                    </ser:role>
                    <ser:operator>false</ser:operator>
                </ser:findRoleByExampleWithOperatorRequest>
            </soapenv:Body>
        </soapenv:Header>
        <driver-operation-data VALUE="true" VALUE2="This is valid. driver-operation-data can also be in the child nodes also from here." />
    </soapenv:Envelope>
    <driver-operation-data VALUE="true" VALUE2="This should not be placed here. It does not satisfy condition 1" />
</input>
```

In this example, <driver-operation-data> is a child element of <soapenv:Envelope> operation node.

* [Using Driver Operation Data to Specify XML to Be Returned on the Result](manage-driver-operation-data.html#b1kgdlv)
* [Using Driver Operation Data to Override Default Subscriber Options](manage-driver-operation-data.html#b1kghug)

## 5.5.1 Using Driver Operation Data to Specify XML to Be Returned on the Result

The <driver-operation-data> is appended as a child element of the root node when it is restored on the response. You can override this by providing one or more parent-node-n attributes to the <driver-operation-data> element, where n is a number beginning with 1 that is incremented for each parent specifier provided. The driver shim looks for parent-node-n attributes. If the attribute is found, the attribute is checked to see if the named node exists. If the node is found, the driver shim uses it as the parent for the <driver-operation-data> element on the response.

The following example shows the usage of parent-node-n in driver-operation-data when requesting and returning commands:

```
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
      <soap-env:Body>
        <batchRequest xmlns="urn:oasis:names:tc:DSML:2:0:core" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <searchRequest derefAliases="neverDerefAliases" dn="data\users\so1user120" requestID="0" scope="baseObject" sizeLimit="100">
            <filter>
              <and>
                <equalityMatch name="objectclass">
                  <value>inetOrgPerson</value>
                </equalityMatch>
              </and>
            </filter>
            <attributes>
              <attribute name="1.1"/>
            </attributes>
            <driver-operation-data parent-node-1="searchResponse" parent-node-2="errorResponse">
              <return-to-me class-name="inetOrgPerson" command="query" dest-dn="data\users\so1user120" event-id="0" scope="entry"/>
            </driver-operation-data>
          </searchRequest>
        </batchRequest>
      </soap-env:Body>
    </soap-env:Envelope>
```

The driver shim checks for <searchResponse> or <errorResponse> nodes in the applications’ response. If one of these nodes is present in the response, the driver shim appends the <driver-operation-data> as a child element of the <searchResponse> node similar to below.

```
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
      <soap-env:Body>
        <batchResponse xmlns="urn:oasis:names:tc:DSML:2:0:core" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <searchResponse>
            <searchResultDone requestID="searchRequest">
              <resultCode code="0" descr="success" xmlns=""/>
            </searchResultDone>
            <driver-operation-data parent-node-1="searchResponse" parent-node-2="errorResponse">
              <return-to-me class-name="inetOrgPerson" command="query" dest-dn="data\users\so1user120" event-id="0" scope="entry"/>
            </driver-operation-data>
          </searchResponse>
        </batchResponse>
      </soap-env:Body>
    </soap-env:Envelope>
```

## 5.5.2 Using Driver Operation Data to Override Default Subscriber Options

There are three ways to override default Subscriber options for a command:

* [Creating and Using Multiple Subscriber Option Sets (Connections)](manage-driver-operation-data.html#b1kgj83)
* [Overriding Single Subscriber Options](manage-driver-operation-data.html#b1kgo7h)
* [Overriding the Authorization Header](manage-driver-operation-data.html#bfkckmf)

### Creating and Using Multiple Subscriber Option Sets (Connections)

You can override the default Subscriber option by creating multiple sets of the Subscriber options (called connections) in your configuration, and by using the <driver-operation-data> element to specify which connection set to use for the current command.

To use the <driver-operation-data> element to override the default Subscriber connection parameters:

1. Edit the Subscriber Settings section of the driver configuration.
2. Using the XML edit feature of Identity Console, find each Subscriber setting that ends with a dash and the number 1, such as subURL-1, duplicate it, and increment the number.

   For example: subURL-2
3. Edit the values of the new settings to be the values you want to use for the second connection.

   You can configure any number of connections this way if the numbers you use are incremental without gaps.
4. Add an attribute to the <driver-operation-data> element called connection and give it the value of the connection number you want to use.

   For example:

   ```
   <driver-operation-data connection="2">
     ...(other driver-operation-data elements)
   </driver-operation-data>
   ```

### Overriding Single Subscriber Options

Instead of using the concept of connections to override multiple Subscriber options, you can override only the URL, the HTTP method, or the soap-action values, by directly using attributes on an <driver-operation-data> element. The following table lists the attributes that can be used and the Subscriber option they are meant to override.

| <driver-operation-data> Attribute | Subscriber Option Being Overridden | Description |
| url | subURL-1 | This is the URL or (or URI) of the Web Service or HTTP application. Overriding the URL might be useful if the application has one Web Service for adding a user and a different Web Service for deleting a user. |
| method | subHttpMethod-1 | This is POST by default but can be set to other methods as defined in RFC 2616 Section 9. |
| soap-action | HTTP Request-Header field with the “SOAPAction” key | With the DSML and SPML samples, this value is always #batchRequest. However, there are some Web services that require this value to change, depending on the command. |

Examples:

```
      <driver-operation-data url="http://137.66.10.13:18180/soap">
          ...(other driver-operation-data elements if required)
      </driver-operation-data>

        <driver-operation-data method="GET">
          ...(other driver-driver-operation-data elements if required)
        </driver-operation-data>

             <driver-operation-data soap-action="addUser">
               ...(other driver-operation-data elements if required)
             </driver-operation-data>
```

### Overriding the Authorization Header

You can set the Authorization header dynamically (from within policy) in the <driver-operation data>.

Example:

```
<driver-operation-data>
    <request-headers remove-existing="true">
        <request-header name="Authorization">Basic
cn=admin,o=n:n</request-header>
        <request-header name="SOAPAction">#batchRequest</request-header>
    </request-headers>
</driver-operation-data>
```

By default, the driver encodes the Authorization header value sent as part of the <driver-operation data>. In this scenario, you must specify the authorization information in clear text format.

Example:

```
<driver-operation-data>
    <request-headers remove-existing="true">
        <request-header name="Authorization">Basic
cn=admin,o=n:n</request-header>
        </request-headers>
</driver-operation-data>
```

If you do not want the driver to encode the Authorization header value, set the flag "encode=false”. In this scenario, you must specify the authorization information in base64 format.

Example:

```
<driver-operation-data>
    <request-headers remove-existing="true">
        <request-header encode="false" name="Authorization">Basic
c2VydmVyMTpub3ZlbGw=</request-header>
    </request-headers>
</driver-operation-data>
```

The remove-existing flag defines whether the set of request-headers defined in the Subscriber-options should be used in addition to the new headers defined in the <driver-operation-data> or should replace the existing request-headers.

* If the remove-existing flag is set to true, the set of request-headers defined in the <driver-operation-data> replaces the existing ones defined in the Subscriber option.
* If the remove-existing flag is set to false, the set of request-headers defined in the Subscriber options is used in addition to the new headers defined in the <driver-operation-data>.

If the Authorization header already exists, it is overridden. Otherwise, it is added as new.
