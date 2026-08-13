# 5.7 Organization Attributes

The below table lists Identity Vault Organization attributes. These attributes can be retrieved using the Get\_Organizations API.

*Table 5-7* Mapping of Organization Attributes

| Attribute Name | nds-name | Workday SOAP Response Path | Description |
| wd-Inactive | wd-Inactive | wd:Organization\_Data/wd:Inactive | Inactive indicator for the Organization |
| wd-OrganizationCode | wd-OrganizationCode | wd:Organization\_Data/wd:Organization\_Code | Text attribute identifying Organization code |
| wd-OrganizationID | wd-OrganizationID | wd:Organization\_Data/wd:Reference\_ID | Integration reference ID used for integration purposes |
| wd-OrganizationName | wd-OrganizationName | wd:Organization\_Data/wd:Name | Name of the Organization that appears on page and reports |
| wd-OrganizationSubType | wd-OrganizationSubType | wd:Organization\_Data/wd:Organization\_Subtype\_Reference/wd:ID[@wd:type='Organization\_Subtype\_ID'] | Unique identifier for the sub-type of the Organization |
| wd-OrganizationType | wd-OrganizationType | wd:Organization\_Data/wd:Organization\_Type\_Reference/wd:ID[@wd:type='Organization\_Type\_ID'] | Unique identifier for the type of the Organization |
| wd-SuperiorOrganizationID | wd-SuperiorOrganizationID | wd:Organization\_Data/wd:Hierarchy\_Data/wd:Superior\_Organization\_Reference/wd:ID[@wd:type='Organization\_Reference\_ID'] | Unique identifier for the immediately superior Organization to the Organization |
| wd-ManagerEID | wd-ManagerEID | wd:Organization\_Data/wd:Manager\_Reference/wd:ID[@wd:type='Employee\_ID'] | Unique identifier for the manager of teh Organization |
| wd-OrganizationLevel | wd-OrganizationLevel | wd:Organization\_Data/wd:Supervisory\_Data/wd:Staffing\_Restrictions\_Data/wd:Job\_Profile\_Restriction\_Summary\_Data/wd:Management\_Level\_Reference/@Descriptor | Display information used to describe management level |
| wd-WID | wd-WID | wd:Organization\_Reference/wd:ID[@wd:type='WID'] | Unique identifier to reference an Organization |
