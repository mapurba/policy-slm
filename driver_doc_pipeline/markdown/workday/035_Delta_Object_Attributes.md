# 5.8 Delta Object Attributes

The below table lists Identity Vault Delta Object attributes.

*Table 5-8* Mapping of Delta Object Attributes

| Attribute Name | nds-name | Workday SOAP Response Path | Description |
| wd-WDAssociation | wd-WDAssociation | NA | The associated value of the delta object |
| wd-IDVAssociation | wd-IDVAssociation | NA | The DN of the original object |
| wd-EffectiveDate | wd-EffectiveDate | NA | The event effective date |
| wd-creationDate | wd-creationDate | NA | The event creation date |
| wd-ChangelogValue | wd-ChangelogValue | NA | The differential information (in Base64 encrypted format) of the worker’s state, between creation and effective date. |
| wd-WorkerLogEntries | wd-WorkerLogEntries | NA | The transaction events of the worker |
| wd-ProcessingStatus | wd-ProcessingStatus | NA | The current status of the delta object. The values are as follows:  * 1: indicates a processed delta object * 0: indicates an unprocessed delta object |
