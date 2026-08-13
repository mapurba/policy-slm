# 5.6 Location Attributes

The below table lists Identity Vault Location attributes. These attributes can be retrieved using the Get\_Locations API.

*Table 5-6* Mapping of Location Attributes

| Attribute Name | nds-name | Workday SOAP Response Path | Description |
| wd-AddressType | wd-AddressType | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Usage\_Data/wd:Type\_Data/wd:Type\_Reference/wd:ID[@wd:type='Communication\_Usage\_Type\_ID'] | Communication usage type ID for the address information of the location |
| wd-BusinessAddressLine1 | wd-BusinessAddressLine1 | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Address\_Line\_Data[@wd:Type='ADDRESS\_LINE\_1'] | Address line 1 of the address of the location |
| wd-BusinessCity | wd-BusinessCity | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Municipality | City part of the address of the location |
| wd-BusinessCountry | wd-BusinessCountry | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Country\_Reference/@wd:Descriptor | Text description of the country for the address of the location |
| wd-BusinessPostalcode | wd-BusinessPostalcode | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Postal\_Code | The postal code part of the address of the location |
| wd-BusinessState | wd-BusinessState | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Country\_Region\_Descriptor | The region part of the address of the location. For example, street name, street number, suite number, apartment etc. |
| wd-Inactive | wd-Inactive | wd:Location\_Data/wd:Inactive | Boolean attribute indicates if the location is inactive |
| wd-LocationID | wd-LocationID | wd:Location\_Data/wd:Location\_ID | The unique location ID |
| wd-LocationName | wd-LocationName | wd:Location\_Data/wd:Location\_Name | Name of the location |
| wd-LocationUsageID | wd-LocationUsageID | wd:Location\_Data/wd:Location\_Usage\_Reference/wd:ID[@wd:type='Location\_Usage\_ID'] | Unique identifier for the usage of the location. For example, business site, workspace etc. |
| wd-BusinessAddressLine2 | wd-BusinessAddressLine2 | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Address\_Line\_Data[@wd:Type='ADDRESS\_LINE\_2'] | Address line 2 of the address of the location |
| wd-BusinessAddressLine3 | wd-BusinessAddressLine3 | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Address\_Line\_Data[@wd:Type='ADDRESS\_LINE\_3'] | Address line 3 of the address of the location |
| wd-StateCode | wd-StateCode | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Country\_Region\_Reference/wd:ID[@wd:type='ISO\_3166-2\_Code'] | Unique identifier for the region part of the address of the location. For example, state/province information |
| wd-ShortCountryCode | wd-ShortCountryCode | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Country\_Reference/wd:ID[@wd:type='ISO\_3166-1\_Alpha-2\_Code'] | Two digit code representing the country |
| wd-LongCountryCode | wd-LongCountryCode | wd:Location\_Data/wd:Contact\_Data/wd:Address\_Data/wd:Country\_Reference/wd:ID[@wd:type='ISO\_3166-1\_Alpha-3\_Code'] | Three digit code representing the country |
| wd-WID | wd-WID | wd:Location\_Reference/wd:ID[@wd:type='WID'] | Unique identifier for the location |
