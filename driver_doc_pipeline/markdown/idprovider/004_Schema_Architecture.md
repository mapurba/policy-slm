# 1.3 Schema Architecture

The Identity Vault’s schema must be extended to support the ID Provider driver functionality. The following two tables describe the schema attributes and classes.

*Table 1-1* Schema Attributes

| Attribute Name | Syntax | Attribute Flags | Description |
| DirXML-IDPolName | Case Ignore String | Single valued Synchronize immediately | ID Policy object name |
| DirXML-IDPolLastID | Numeric String | Single-valued Synchronize immediately | Last delivered ID |
| DirXML-IDPolMin | Numeric String | Single-valued | Minimum value for an ID |
| DirXML-IDPolMax | Numeric String | Single-valued | Maximum value for an ID |
| DirXML-IDPolPrefix | Case Ignore String | Single-valued | Prefix for a new ID |
| DirXML-IDPolFill | Boolean | Single-valued | True: Fill ID with 0 up to maximum length False or Empty: Do nothing |
| DirXML-IDPolArea | Case Ignore String | Single-valued | Exclude/Include list for generated IDs |
| DirXML-IDPolAreaEI | Boolean | Single-valued | True: IDPolArea = Include list False or Empty: IDPolArea = Exclude list |
| DirXML-IDPolAccessControl | Boolean | Single-valued | True: IDPolACL list is used False or Empty: IDPolACL list is not used |
| DirXML-IDPolACL | Case Ignore String | Single-valued | Comma-delimited list of ID clients to be allowed to request an ID from the ID server |
| DirXML-IDPolicyContainerDN | Distinguished Name | Single-valued | Link to the ID Policy Container |

*Table 1-2* Schema Classes

| Class Name | Contained By | Attributes Contained |
| ID Policy Container | Country, Domain, Locality, Organization, Organizational Unit, Tree Root | OU |
| ID Policy | ID Policy Container | * IDPolACL * IDPolAccessControl * IDPolArea * IDPolAreaEI * IDPolFill * IDPolLastID * IDPolMax * IDPolMin * IDPolName * IDPolPrefix |
