# 5.4 Relation Attributes

The below table lists Identity Vault Relation attributes. These attributes can be retrieved using the Get\_Workers API.

*Table 5-4* Mapping of Relation Attributes

| Attribute Name | NDS-Name | Workday SOAP Response Path | Description |
| wd-ManagerWorkforceID | managerWorkforceID | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Organizations\_Data//wd:Organization\_Support\_Role/wd:Organization\_Role\_Data/wd:Worker\_Reference/wd:ID[@wd:type='Employee\_ID' or @wd:type='Contingent\_Worker\_ID' ] | Workforce ID of the manager of the position |
| wd-BusinessTitle | Title | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Business\_Title | Business title for the position |
| wd-BusinessAddressLine1 | wd-BusinessAddressLine1 | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Address\_Data/wd:Address\_Line\_Data | Address line 1 of the position |
| wd-BusinessCity | wd-BusinessCity | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Address\_Data/wd:Municipality | City part of address of the position |
| wd-BusinessCountry | wd-BusinessCountry | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Address\_Data/wd:Country\_Reference/@wd:Descriptor | Description for the country of the position |
| wd-BusinessPostalcode | wd-BusinessPostalcode | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Address\_Data/wd:Postal\_Code | Postal code part of the address of the position |
| wd-BusinessState | wd-BusinessState | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Address\_Data/wd:Country\_Region\_Reference/@wd:Descriptor | Region part of the address for the position. For example, state/province information |
| wd-JobClassificationType | wd-JobClassificationType | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Job\_Classification\_Reference/@wd:Descriptor | Display information for the job classification of the position |
| wd-JobGroupReference | wd-JobGroupReference | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Job\_Group\_Reference/@wd:Descriptor | Display information for the job group of the position |
| wd-JobProfileName | wd-JobProfileName | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Job\_Profile\_Name | The name of the job profile |
| wd-JobProfileID | jobCode | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Job\_Profile\_Reference/wd:ID[@wd:type='Job\_Profile\_ID'] | Unique identifier for the job profile |
| wd-LocationID | wd-LocationID | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Location\_Reference/wd:ID[@wd:type='Location\_ID'] | Unique identifier for the location of the position |
| wd-LocationName | L | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Business\_Site\_Summary\_Data/wd:Name | Name of the location for the position |
| wd-PayRateType | wd-PayRateType | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Pay\_Rate\_Type\_Reference/@wd:Descriptor | Text attribute identifying the pay rate type for the position |
| wd-PositionEffectiveDate | wd-PositionEffectiveDate | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/@wd:Effective\_Date | Effective date for position |
| wd-PositionEndDate | wd-PositionEndDate | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:End\_Date | The effective date of the end employment business process |
| wd-PositionID | wd-PositionID | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Position\_ID | Text attribute identifying the position |
| wd-PositionstartDate | wd-PositionstartDate | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Start\_Date | Date the worker first started working in this position |
| wd-PositionTimeType | wd-PositionTimeType | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Position\_Time\_Type\_Reference/@wd:Descriptor | Text attribute identifying the position time type |
| wd-PositionTitle | wd-PositionTitle | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Position\_Title | Text attribute identifying the position title |
| wd-RelationID | wd-RelationID | wd:Worker\_Data/wd:Worker\_ID-C/E:wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Position\_ID | Unique identifier for the relation based on the worker ID, worker type and position ID |
| wd-WorkerIDType | wd-WorkerIDType | wd:Worker\_Data/wd:Worker\_ID/wd:Worker\_Reference[wd:ID[@wd:type='Employee\_ID']] | Employee ID / Contingent Worker ID |
| wd-WorkerType | wd-WorkerType | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Worker\_Type\_Reference/@wd:Descriptor | The worker type for the position |
| workforceID | workforceID | wd:Worker\_Data/wd:Worker\_ID | The ID for the worker or the contingent worker |
| wd-WID | wd-WID | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Position\_Reference/wd:ID[@wd:type='WID'] | Unique identifier for the position of the worker |
| wd-Primary | wd-Primary | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/@wd:Primary\_Job | Boolean attribute indicates whether the position is the primary position for a worker |
| wd-ShortCountryCode | wd-ShortCountryCode | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Address\_Data/wd:Country\_Reference/wd:ID[@wd:type='ISO\_3166-1\_Alpha-2\_Code'] | To character code representing country of the position |
| wd-JobClassificationSummaryData | wd-JobClassificationSummaryData | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Job\_Classification\_Summary\_Data/wd:Job\_Group\_Reference/wd:ID[@wd:type='Job\_Classification\_Group\_ID'] ||| wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Job\_Classification\_Summary\_Data/wd:Job\_Classification\_Reference/@wd:Descriptor ||| wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Job\_Classification\_Summary\_Data/wd:Job\_Classification\_Reference/wd:ID[@wd:type='Job\_Classification\_Reference\_ID'] | Contains job classification from the job profile for the position and additional job classification specified for the position |
| wd-StandardHours | wd-StandardHours | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Scheduled\_Weekly\_Hours | Scheduled weekly hours for the position |
| wd-FullTimeEquivalent | wd-FullTimeEquivalent | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data/wd:Full\_Time\_Equivalent\_Percentage | Full time equivalent percentage for position |
| wd-ShortStateCode | wd-ShortStateCode | wd:Worker\_Data/wd:Employment\_Data/wd:Worker\_Job\_Data/wd:Position\_Data//wd:Address\_Data/wd:Country\_Region\_Reference/wd:ID[@wd:type='ISO\_3166-2\_Code'] | Two character code representing region part of the address |
