# 5.3 Job Family Attributes

The below table lists Identity Vault Job Family attributes. These attributes can be retrieved using the Get\_Job\_Families API

*Table 5-3* Mapping of Job Family Attributes

| Attribute Name | nds-name | Workday SOAP Response Path | Description |
| wd-Inactive | wd-Inactive | wd:Job\_Family\_Data/wd:Inactive | Boolean attribute indicating if job family is inactive |
| wd-JobFamilyID | wd-JobFamilyID | wd:Job\_Family\_Data/wd:ID | Unique identifier for the job family |
| wd-JobFamilyName | wd-JobFamilyName | wd:Job\_Family\_Data/wd:Name | Text attribute identifying job family name |
| wd-WID | wd-WID | wd:Job\_Family\_Reference/wd:ID[@wd:type='WID'] | Unique identifier for the job family |
