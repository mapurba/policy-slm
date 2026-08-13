# 2.7 Epic Setup

* [Epic Service Account Setup](t4oqvdeiqhxm.html#t4oqvdfyxdbo)
* [Epic ID Type Setup](t4oqvdeiqhxm.html#t4oqve5le71b)
* [Web Service Information](t4oqvdeiqhxm.html#t4oqvehm2brf)
* [Epic Interconnect Username Security Policy Setup](t4oqvdeiqhxm.html#t4or384liji1)

## 2.7.1 Epic Service Account Setup

The Epic driver requires an Epic user for username token authentication (Basic Auth) to the Epic database. This user is used by Interconnect to authenticate the driver芒聙聶s web service calls. Communicate to your Interconnect Admin the ID (EMP .1) and Password (EMP 40) of this user after you create it. Note that both the ID and Password fields are case-sensitive.

* This should be an active foreground user and should have a password set to not expire.
* It is recommended to create new security classes or to use static security classes (see relevant EMP security points below), as changes to this user芒聙聶s security impacts the Epic driver芒聙聶s functionality, and then add this security class to this user record.
* The security points for the user must be set using the default security class for a given Epic application. Note that the user芒聙聶s security will not inherit security class overrides by service area or location.

## 2.7.2 Epic ID Type Setup

Epic requires each customer to have a unique Epic identifier to hold the SER record ID for the Epic Driver, similar to an NPI identifier. If a desired type does not already exist, a new Epic type will need to be created.

Ensure that a HL7 assigning authority is configured in the settings for this ID type such that the Type.text is available when reading Provider records.

## 2.7.3 Web Service Information

The Epic driver is scoped for the following web services:

| Web Service Name | Web Service Category | Web Service Class |
| ActivateUser | Security | PersonnelManagement |
| CreateUser (2014) | Security | PersonnelManagement |
| DeleteUser | Security | PersonnelManagement |
| GetImportDataLog | Core | DataUtility |
| GetInternalIdentifier | Common | Utility |
| GetUserPagerID | Security | PersonnelManagement |
| ImportData (2019) | Core | DataUtility |
| InactivateUser | Security | PersonnelManagement |
| Practitioner.Read (R4) | FHIR | R4 |
| Practitioner.Search (R4) | FHIR | R4 |
| PractitionerRole.Read (R4) | FHIR | R4 |
| PractitionerRole.Search (R4) | FHIR | R4 |
| SetReportSelectionCriteria | Security | PersonnelManagement |
| SerUserExternalPasswords | Security | PersonnelManagement |
| SetUserPagerID | Security | PersonnelManagement |
| SetUserPassword | Security | PersonnelManagement |
| UpdateAuthorizedServiceAreas | Security | PersonnelManagement |
| UpdateBIDefaultUser | Security | PersonnelManagement |
| UpdateCommunityUser | Security | PersonnelManagement |
| UpdateFacilityDepartmentList | Security | PersonnelManagement |
| UpdateLoginDepartments | Security | PersonnelManagement |
| UpdateUser (2014) | Security | PersonnelManagement |
| UpdateUserDemographics | Common | User |
| UpdateUserGroups | Security | PersonnelManagement |
| ViewAuthorizedServiceAreas | Security | PersonnelManagement |
| ViewBIDefaultUser | Security | PersonnelManagement |
| ViewCommunityUser | Security | PersonnelManagement |
| ViewCurrentReportSelectionCriteria | Security | PersonnelManagement |
| ViewFacilityDepartmentList | Security | PersonnelManagement |
| ViewLoginDepartments | Security | PersonnelManagement |
| ViewUser (2014) | Security | PersonnelManagement |
| ViewUserGroups | Security | PersonnelManagement |

## 2.7.4 Epic Interconnect Username Security Policy Setup

Epic Interconnect needs to be set up to allow the Epic driver to access data in Epic.

| Recommended Location | Server: Background  Instance: Web Service Host |
| Role | General Web Service Host |
| Cache Listeners | N/A |
| Business Services | Integration-specific web services  * DataUtility (Core) (WSC) * PersonnelManagement (Security) (WSC) * R4 (FHIR) (WSC) * Utility (Common) (WSC) * User (Common) (WSC)  See [Web Service Information](t4oqvdeiqhxm.html#t4oqvehm2brf) for the full list of web services user by the Epic driver. |
| Security Policy | Policy Name: EpicDriverBasicAuth  * Services: Application services from above * Authentication: Username tokens (use the EMP ID from the [Epic Service Account Setup](t4oqvdeiqhxm.html#t4oqvdfyxdbo) section) * Encryption: TLS * Bindings: Rest |
| Reverse Proxy Pattern(s) | Be sure you have configured your reverse proxy (see the Configure ARR Manually section in Epic芒聙聶s Interconnect Setup & Support Guide).  Create a rewrite rule for each pattern below using Wildcards instead of the default Regular Expressions:  * api/fhir/\* * api/epic/2011/Common/User/UPDATEUSERDEMOGRAPHICS/\* * api/epic/2010/Common/Utility/GETINTERNALIDENTIFIER/\* * api/epic/2016/Core/DataUtility/GetImportDataLog/\* * api/epic/2019/Core/DataUtility/ImportData/\* * api/epic/2012/Security/PersonnelManagement/ActivateUser/\* * api/epic/2012/Security/PersonnelManagement/DeleteUser/\* * api/epic/2012/Security/PersonnelManagement/InactivateUser/\* * api/epic/2012/Security/PersonnelManagement/SetUserExternalPasswords/\* * api/epic/2012/Security/PersonnelManagement/SetUserPassword/\* * api/epic/2014/Security/PersonnelManagement/CreateUser/\* * api/epic/2014/Security/PersonnelManagement/UpdateUser/\* * api/epic/2014/Security/PersonnelManagement/ViewUser\* * api/epic/2015/Security/PersonnelManagement/SetReportSelectionCriteria\* * api/epic/2015/Security/PersonnelManagement/ViewCurrentReportSelectionCriteria/\* * api/epic/2016/Security/PersonnelManagement/UpdateCommunityUser/\* * api/epic/2016/Security/PersonnelManagement/UpdateLoginDepartments/\* * api/epic/2016/Security/PersonnelManagement/UpdateUserGroups/\* * api/epic/2016/Security/PersonnelManagement/ViewCommunityUser/\* * api/epic/2016/Security/PersonnelManagement/ViewLoginDepartments/\* * api/epic/2016/Security/PersonnelManagement/ViewUserGroups/\* * api/epic/2017/Security/PersonnelManagement/UpdateAuthorizedServiceAreas/\* * api/epic/2017/Security/PersonnelManagement/UpdateFacilityDepartmentList/\* * api/epic/2017/Security/PersonnelManagement/GetUserPagerID/\* * api/epic/2017/Security/PersonnelManagement/SetUserPagerID/\* * api/epic/2017/Security/PersonnelManagement/ViewAuthorizedServiceAreas/\* * api/epic/2017/Security/PersonnelManagement/ViewFacilityDepartmentList/\* * api/epic/2017/Security/PersonnelManagement/UpdateBIDefaultUser/\* * api/epic/2017/Security/PersonnelManagement/ViewBIDefaultUser/\*  Each rule should use Wildcards and rewrite to: https://[hostname]/[instance]/{R:0}  *NOTE:*: These Reverse Proxy rules are related to Microsoft芒聙聶s Application Request Routing (ARR) for IIS. If you use another reverse proxy solution, check with your Client Systems Web and Service Server TS for assistance. |
