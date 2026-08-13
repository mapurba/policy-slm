# 3.2 Modifying the JSON/XML Payload

You can also customize the JSON/XML payload received in the Subscriber and Publisher channels through conversion policies. The conversion policies modify the format of the request and response documents for compatibility.

The conversion can be done using any of the following three methods:

* Use the default XDS to JSON conversion policy to transform the payload generated in the <driver-operation-data> to a format supported by your SCIM service.
* Create your own XDS to JSON conversion policy, and ensure to keep the payload in <driver-operation-data> so that the driver transfers the same to the connected application.
* Driver shim automatically performs the conversion without any conversion policies.
