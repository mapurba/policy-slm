# 5.5 Photo Attributes

The below table lists Identity Vault Photo attributes. These attributes can be retrieved using the Get\_Worker\_Photos API.

*Table 5-5* Mapping of Photo Attributes

| Attribute Name | nds-name | Workday SOAP Response Path | Description |
| wd-photo | wd-photo | wd:Worker\_Photo\_Data/wd:File | Photo file content in base64Binary format |
| wd-photoFilename | wd-photoFilename | wd:Worker\_Photo\_Data/wd:Filename | File name of the photo |
| wd-photoID | wd-photoID | For worker photo: wd:Worker\_Photo\_Reference/wd:ID[@wd:type='Employee\_ID'] -E  For contingent worker’s photo: wd:Worker\_Photo\_Reference/wd:ID[@wd:type='Contingent\_Worker\_ID'] -C | For worker, the SOAP response path is appended with -E option and for contingent workers, the SOAP response path is appended with -C option. |
| wd-originalPhoto | wd-originalPhoto | wd:Worker\_Photo\_Data/wd:File | This attribute holds the data and specifications of the worker’s original photo. |
