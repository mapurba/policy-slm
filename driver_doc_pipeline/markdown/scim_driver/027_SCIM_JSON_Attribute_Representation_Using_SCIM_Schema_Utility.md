# 6.3 SCIM JSON Attribute Representation Using SCIM Schema Utility

The schema mapping policy comprises all the resource attributes. The attributes are represented with their sub-attributes, or their canonical types, or both. These attributes are modified to the required format as explained in the following sections.

## 6.3.1 Attribute Representation Using SCIM Utility Grammar With Delimiters

The resource attributes in the Identity Manager are in the JSON format. These attributes are of singular, complex, complex multivalued types. For schema mapping, the resource attributes can be from a core class or from an extension. The SCIM driver modifies the JSON format to a linear SCIM format using delimiters, as shown below:

* + as the urn(Resource) delimiter
* : as the attribute-Sub attributes delimiter

The delimiters as mentioned earlier are used to represent the SCIM attributes as shown below:

* Core attributes: The core attributes are of three types and are delimited by : , as shown below:

  + Singular: <attribute>
  + Complex Singular: <attribute>:<subattribute>
  + Complex Multi-valued: <attribute>:<cannonicalType>:<subattribute>
* Extensions attributes: The extension attributes are associated to the URN with a +, as shown below:

  + Singular: <urn>+<attribute>
  + Complex Singular: <urn>+<attribute>:<subattribute>
  + Complex Multi-valued: <urn>+<attribute>:<cannonicalType>:<subattribute>

## 6.3.2 Formatting JSON Structures to SCIM Attributes

The SCIM driver formats the JSON structure into a linear format SCIM attribute using delimiters. The following table shows how the JSON structures are transformed into linear SCIM attributes using utility grammar.

| JSON Structure | SCIM Attributes | Grammar |
| Singular Attribute  "userName":johndoe@microfocus.com | username | <attribute> |
| Complex Attribute   ``` "phoneNumbers":[ {"type":"work", "value":"09663502443"},], ``` | * phoneNumbers * phoneNumbers:work * phoneNumbers:value * phoneNumbers:work:value | * <attribute> * <attribute>:<cannonicalType> * <attribute>:<subattribute> * <attribute>:<cannonicalType>:<subattribute> |
| Extension Attribute   ``` "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User":  {    "organization":"00D2v000002mBdQEAU","employeeNumber":"21212"  }, ``` | * urn:ietf:params:scim:schemas:extension:enterprise:2.0:User+Organization * urn:ietf:params:scim:schemas:extension:enterprise:2.0:User+employeeNumber | <urn>+<attribute> |
| Complex Values in Extension Attribute   ``` "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {  "manager": [  { "displayName":"John Doe" },  ],  }, ``` | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User+Manager:displayName | * <urn>+<attribute>:<cannonicalType>:<subattribute> * <urn>+<attribute>:<subattribute> |
