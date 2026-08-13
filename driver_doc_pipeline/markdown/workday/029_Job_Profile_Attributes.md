# 5.2 Job Profile Attributes

The below table lists Identity Vault Job Profile attributes. These attributes can be retrieved using the Get\_Job\_Profiles API.

*Table 5-2* Mapping of Job Profile Attributes

| Attribute Name | nds-name | Workday SOAP Response Path | Description |
| wd-CompensationGradeID | wd-CompensationGradeID | wd:Job\_Profile\_Data/wd:Job\_Profile\_Compensation\_Data/wd:Compensation\_Grade\_Reference/wd:ID[@wd:type='Compensation\_Grade\_ID'] | Unique identifier for the compensation grade |
| wd-CompensationGradeProfileID | wd-CompensationGradeProfileID | wd:Job\_Profile\_Data/wd:Job\_Profile\_Compensation\_Data/wd:Compensation\_Grade\_Profile\_Reference/wd:ID[@wd:type='Compensation\_Grade\_Profile\_ID'] | Unique identifier for the compensation grade profile |
| wd-Inactive | wd-Inactive | wd:Job\_Profile\_Basic\_Data/wd:Inactive | Boolean attribute indicating if job profile is inactive |
| wd-JobCode | wd-JobCode | wd:Job\_Profile\_Data/wd:Job\_Code | Job code for the job profile |
| wd-JobFamilyID | wd-JobFamilyID | wd:Job\_Profile\_Basic\_Data/wd:Job\_Family\_Data/wd:Job\_Family\_Reference/wd:ID[@wd:type='Job\_Family\_ID'] | Unique identifier for the job family of the job profile. |
| wd-JobProfileID | wd-JobProfileID | wd:Job\_Profile\_Data/wd:Job\_Code | Job code for the job profile. |
| wd-JobTitle | wd-JobTitle | wd:Job\_Profile\_Basic\_Data/wd:Job\_Title | Name of the job profile. |
| wd-WID | wd-WID | wd:Job\_Profile\_Reference/wd:ID[@wd:type='WID'] | Unique identifier for the job profile. |
| wd-UnionRequired | wd-UnionRequired | wd:Unions\_Data/wd:Requirement\_Option\_Reference/wd:ID[@wd:type='Requirement\_ID'] | Indicates if the worker should be assigned to a union. |
