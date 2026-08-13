# B.1 Default Attributes

| assistant | homeState | Postal Code |
| assistantPhone | homeZipCode | Postal Office Box |
| businessCategory | Initials | instantMessagingID |
| C | instantMessagingID | preferredDeliveryMethod |
| city | Internet EMail Address | preferredName |
| CN | jackNumber | registeredAddress |
| co | jobCode | roomNumber |
| company | L | S |
| costCenter | Language | SA |
| costCenterDescription | Login Disabled | Security Equals |
| children | Mailbox ID | See Also |
| departmentNumber | Mailbox Location | siteLocation |
| Description | mailstop | spouse |
| directReports | manager | Surname |
| EMail Address | managerWorkforceID | Telephone Number |
| employeeStatus | Member | teletexTerminalIdentifier |
| employeeType | mobile | telexNumber |
| Equivalent To Me | NSCP:employeeNumber | Timezone |
| Facsimile Telephone Number | nspmDistributionPassword | Title |
| Full Name | O | tollFreePhoneNumber |
| Generational Qualifier | otherPhoneNumber | UID |
| Given Name | OU | uniqueID |
| Group Membership | pager | userCertificate |
| homeCity | personalMobile | vehicleInformation |
| homeEmailAddress | personalTitle |  |
| homeFax | Postal Address |  |
| homePhone | photo | workforceID |
| homePostalAddress | Physical Delivery Office Name | User |

*NOTE:*After installing and configuring the driver object, you must perform the following steps to ensure that the driver does not fail to register or to avoid CL\_entryid\_drivername.cfg file populating incorrectly:

1. In Identity Console, go to Configuration > Engine Control Values.
2. Set Include driver filter in Subscriber initialization document to true. By default, this option will be set to false.
