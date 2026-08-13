# 5.10 Attribute Filter Settings

This section provides information about the Identity Vault Filter settings in the driver. The Workday will be the authoritative source for all the above attributes except user ID and Email address which are generated in the Identity Manager.

* [Users Attributes Filter Settings](t4b2ostg4jt0.html#t4b2ow226dn9)
* [Relations Attributes Filter Settings](t4b2ostg4jt0.html#t4b2owbqc9zo)
* [Job Family Attributes Filter Settings](t4b2ostg4jt0.html#t4b2p77xx51q)
* [Location Attributes Filter Settings](t4b2ostg4jt0.html#t4b2p7qglixw)
* [Photo Attributes Filter Settings](t4b2ostg4jt0.html#t4b2p9ab87bz)
* [Job Profile Attributes Filter Settings](t4b2ostg4jt0.html#t4b2p9psjyo1)
* [Organization Attributes Filter Settings](t4b2ostg4jt0.html#t4b2pazry1fr)
* [Delta Object Attributes Filter Settings](t4b2ostg4jt0.html#delta_obj_filt_set)

## 5.10.1 Users Attributes Filter Settings

The following table provides information about the Users Attributes Filter settings:

*Table 5-10* Users Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| Given Name | app | sync | reset |
| managerWorkforceID | app | sync | reset |
| Surname | app | sync | reset |
| wd-WorkerIDType | app | sync | reset |
| workforceID | app | sync | reset |
| wd-WID | app | sync | reset |
| wd-UserName | app | sync | reset |
| wd-E-Active | app | sync | reset |
| wd-C-Active | app | sync | reset |
| wd-HomePrimaryPhone | app | sync | sync |
| wd-HomePrimaryDeviceType | app | sync | sync |
| wd-WorkPrimaryPhone | app | sync | sync |
| wd-WorkPrimaryDeviceType | app | sync | sync |
| Internet Email Address | app | sync | sync |
| homeEmailAddress | app | sync | sync |
| DirXML-EntitlementRef | Identity Vault | Ignore | Notify |

*NOTE:*Only the following attributes can be updated on Subscriber channel:

* User ID
* Phone Numbers
* E-Mail Address
* Custom IDs

Modifying any other attribute on the Subscriber channel is not supported. For more information on the procedure to update phone numbers, see [Configuring Phone Contact Information in Subscriber Channel](t4finm0426n2.html).

## 5.10.2 Relations Attributes Filter Settings

The following table provides information about the Relations Attributes Filter settings:

*Table 5-11* Relations Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| L | app | sync | reset |
| managerWorkforceID | app | sync | reset |
| Title | app | sync | reset |
| wd-BusinessAddressLine1 | app | sync | reset |
| wd-BusinessCity | app | sync | reset |
| wd-BusinessCountry | app | sync | reset |
| wd-BusinessPostalcode | app | sync | reset |
| wd-BusinessState | app | sync | reset |
| wd-FullTimeEquivalent | app | sync | reset |
| wd-JobClassificationType | app | sync | reset |
| wd-JobFamilyID | app | sync | reset |
| wd-JobGroupReference | app | sync | reset |
| wd-JobProfileName | app | sync | reset |
| wd-LocationID | app | sync | reset |
| wd-PayRateType | app | sync | reset |
| wd-PositionEffectiveDate | app | sync | reset |
| wd-PositionEndDate | app | sync | reset |
| wd-PositionID | app | sync | reset |
| wd-PositionstartDate | app | sync | reset |
| wd-PositionTimeType | app | sync | reset |
| wd-PositionTitle | app | sync | reset |
| wd-Primary | app | sync | reset |
| wd-RelationID | app | sync | reset |
| wd-WorkerIDType | app | sync | reset |
| wd-WorkerType | app | sync | reset |
| workforceID | app | sync | reset |
| wd-WID | app | sync | reset |

## 5.10.3 Job Family Attributes Filter Settings

The following table provides information about the Job Family Attributes Filter settings:

*Table 5-12* Job Family Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| wd-Inactive | app | sync | reset |
| wd-JobFamilyID | app | sync | reset |
| wd-JobFamilyName | app | sync | reset |
| wd-WID | app | sync | reset |

## 5.10.4 Location Attributes Filter Settings

The following table provides information about the Location Attributes Filter settings:

*Table 5-13* Location Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| wd-AddressType | app | sync | reset |
| wd-BusinessAddressLine1 | app | sync | reset |
| wd-BusinessCity | app | sync | reset |
| wd-BusinessCountry | app | sync | reset |
| wd-BusinessPostalcode | app | sync | reset |
| wd-BusinessState | app | sync | reset |
| wd-Inactive | app | sync | reset |
| wd-LocationID | app | sync | reset |
| wd-LocationName | app | sync | reset |
| wd-LocationUsageID | app | sync | reset |
| wd-BusinessAddressLine2 | app | sync | reset |
| wd-BusinessAddressLine3 | app | sync | reset |
| wd-StateCode | app | sync | reset |
| wd-ShortCountryCode | app | sync | reset |
| wd-LongCountryCode | app | sync | reset |
| wd-WID | app | sync | reset |

## 5.10.5 Photo Attributes Filter Settings

The following table provides information about the Photo Attributes Filter settings:

*Table 5-14* Photo Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| photo | app | sync | sync |
| wd-photoFilename | app | sync | sync |
| wd-photoID | app | sync | sync |
| wd-originalPhoto | app | sync | Ignore |

## 5.10.6 Job Profile Attributes Filter Settings

The following table provides information about the Job Profile Attributes Filter settings:

*Table 5-15* Job Profile Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| wd-CompensationGradeID | app | sync | reset |
| wd-CompensationGradeProfileID | app | sync | reset |
| wd-Inactive | app | sync | reset |
| wd-JobCode | app | sync | reset |
| wd-JobFamilyID | app | sync | reset |
| wd-JobTitle | app | sync | reset |
| wd-WID | app | sync | reset |

## 5.10.7 Organization Attributes Filter Settings

The following table provides information about the Organization Attributes Filter settings:

*Table 5-16* Organization Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| wd-Inactive | app | sync | reset |
| wd-OrganizationCode | app | sync | reset |
| wd-OrganizationID | app | sync | reset |
| wd-OrganizationName | app | sync | reset |
| wd-OrganizationSubType | app | sync | reset |
| wd-OrganizationType | app | sync | reset |
| wd-SuperiorOrganizationID | app | sync | reset |
| wd-ManagerEID | app | sync | reset |
| wd-OrganizationLevel | app | sync | reset |
| wd-WID | app | sync | reset |

## 5.10.8 Delta Object Attributes Filter Settings

The following table provides information about the Organization Attributes Filter settings:

*Table 5-17* Delta Object Attributes Filter Settings

| Attribute Name | Merge Authority | Publisher | Subscriber |
| CN | Default | Ignore | Notify |
| wd-ProcessedEntries | Default | Ignore | Notify |
| wd-ProcessingStatus | Default | Ignore | Notify |
