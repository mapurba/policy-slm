# D.0 Appendix D 芒聙聯 Supported Epic EMP Attributes

The following Epic EMP attributes are supported by the Epic Driver:

| Address  User芒聙聶s address.  * Type: Address[] * Example: { "City": "String", "Country": "String", 芒聙聹County芒聙聺: 芒聙聹String芒聙聺, 芒聙聹District芒聙聺: 芒聙聹String芒聙聺, 芒聙聹HouseNumber芒聙聺: 芒聙聹String芒聙聺. 芒聙聹Lines芒聙聺: [ 芒聙聹String芒聙聺 ], 芒聙聹State芒聙聺: 芒聙聹String芒聙聺, 芒聙聹ZipCode芒聙聺: 芒聙聹String芒聙聺 } |
| AuthenticationConfigurationID  The authentication configuration to use for this user.  * Type: IDType * Example: { "ID": "String", "Type": "String" } |
| AuthorizedServiceAreas  A list of the authorized service areas.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| BlockStatus  Complex type representing a user's block status.  * Type: BlockStatus * Example: { "Comment": "String", "IsBlocked": true, "Reason": "String" } |
| BIDefaultUser  The BI default user name for the Hyperspace user, which will be used by Hyperspace to connect to BI applications.  * Type: String * Example: 芒聙聹String" |
| CategoryReportGrouper1  A list of values for the user's first category report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: 芒聙聹String" |
| CategoryReportGrouper2  A list of values for the user's second category report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: "String" |
| CategoryReportGrouper3  A list of values for the user's third category report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: "String" |
| CategoryReportGrouper4  A list of values for the user's fourth category report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: "String" |
| CategoryReportGrouper5  A list of values for the user's fifth category report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: "String" |
| CategoryReportGrouper6  A list of values for the user's sixth category report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: "String" |
| ContactComment  Contact comment that will appear for the initial contact.  * Type: String * Example: "String" |
| ContactDate  Date to use for the newly created contact. Defaults to current date if not set.  * Type: String * Example: "String" |
| CustomUserDictionaries  List of new values for custom user dictionary files.  * Type: String * Example: "String" |
| Deactivated  Signifies a user should no longer have access to the application.  * Type: String * Example: "String" |
| DefaultLoginDepartmentID  The login department to use for this user by default.  * Type: IDType * Example: { "ID": "String", "Type": "String" } |
| DepartmentFilterSetting  Whether the department filter list is inclusive or exclusive. The default value is exclusive.  * Type: String * Example: "String" |
| EmailAddress  User芒聙聶s e-mail address.  * Type: String * Example: "String" |
| EmployeeDemographics  Customizable items used for demographic information about a user specific to a contact.  * Type: EmployeeDemographics[] * Example: { "EmployeeDemographic1": "String", "EmployeeDemographic2": "String", "EmployeeDemographic3": "String", 芒聙聹Index芒聙聺: "String" } |
| EndDate  The date at which the user becomes inactive. Format of 芒聙聵mm-dd-yyyy芒聙聶.  * Type: String * Example: "String" |
| ExternalIdentifiers  List of external ID items to set for this user.  * Type: ExternalIdentifier[] * Example: { "Identifier": "String", "IdentifierType": "String", "IsActive": true } |
| ExternalPasswords  Array of passwords to set for specific external ID types.  * Type: ExternalPassword[] * Example: { "IDType": "externalIdType", "Password": "password" } |
| FacilityDepartmentList  A list of the departments.  * Type: IndexedRecordIn * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| IdentityIDs  List of Identity IDs to assign to the user.  * Type: IDType[] * Example: { "ID": "String", "Type": "String" } |
| InBasketClassifications  List of values for user In Basket classifications.  * Type: String * Example: "String" |
| IsActive  Whether the user record should be set to active or inactive.  * Type: Boolean * Example: true |
| LDAPOverrideID  A string that can be provided to identify the user to the LDAP server in place of the SystemLogin. Need not be unique. Maximum length 254 characters.  * Type: String * Example: "String" |
| LinkedProviderID  Provider record to link to this user record.  * Type: IDType[] * Example: { "ID": "String", "Type": "String" } |
| LinkedTemplatesConfig  The linked template setup for the user.  * Type: LinkedTemplatesConfig * Example: { "AppliedTemplateID": { "ID": "String", "Type": "String" }, "DefaultTemplateID": { "ID": "String", "Type": "String" }, "AvailableLinkableTemplates": [ { "EndDate": "String", "StartDate": "String", "LoginTypes": "String", "LinkedTemplateID": { "ID": "String", "Type": "String" } } ] } |
| LoginDepartmentFilterList  The list of departments to use when limiting access for the user.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| Name  User's name in LAST, FIRST MI format. If a UserComplexName is provided this is ignored. If one is not, this is required.  * Type: String * Example: "String" |
| Notes  Up to 2,000 characters of free text notes about the user.  * Type: String * Example: "String" |
| PagerID  The pager ID value for the user.  * Type: String * Example: "String" |
| PhoneNumber  User芒聙聶s phone number.  * Type: String * Example: "String" |
| PreferredLoginDepartments  The departments on the user's preferred list.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| PrimaryManager  The primary manager of this user.  * Type: IDType * Example: { "ID": "String", "Type": "String" } |
| ProviderAtLoginOption  How the user should be prompted for a provider when logging in.  * Type: String * Example: "String" |
| ReceiveExternalEmail  This controls whether users receive notification emails from EpicCare link.  * Type: Boolean * Example: true |
| ReceiveGroupNotifications  This controls whether users receive group notification emails from EpicCare link.  * Type: Boolean * Example: true |
| ReportAuthorizedDepartmentGroups  A list of department groups for which the user has access.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| ReportAuthorizedDepartments  A list of departments for which the user has access.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| ReportAuthorizedLocations  A list of locations for which the user has access.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| ReportAuthorizedProviders  A list of providers (SER) for which the user has access.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| ReportAuthorizedServiceArea  A list of service areas for which the user has access.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| ReportAuthorizedUsers  A list of users (EMP) for which the user has access.  * Type: IndexedRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| ReportGrouper1  Value for the user's first free-text report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: "String" |
| ReportGrouper2  Value for the user's second free-text report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: "String" |
| ReportGrouper3  Value for the user's third free-text report grouper item, which does not have an Epic-defined meaning.  * Type: String * Example: "String" |
| Sex  The sex of the user.  * Type: String * Example: "Male" |
| SiteManagerContexts  This links users to EpicCare Link user context groups for the purposes of site management.  * Type: String[] * Example: "String" |
| StartDate  The date on which the user becomes active. Defaults to the current date if not set. Format of 芒聙聵mm-dd-yyyy芒聙聶.  * Type: String * Example: "String" |
| SystemLoginID  Value for the user's system login. Must be unique. Maximum length 254 characters.  * Type: String * Example: "String" |
| UserAlias  Value for the user's alias.  * Type: String * Example: "String" |
| UserComplexName  Individual pieces of a user's name. If UserName is not provided, this is required. If this is given, it will be used instead of UserName.  * Type: PersonName * Example: { "FirstName": "String", "GivenNameInitials": "String", "LastName": "String", MiddleName": "String" } |
| UserContexts  This links users to EpicCare Link user context groups.  * Type: String[] * Example: "String" |
| UserDictionaryPath  Value of the path to user dictionary file. Starting in Epic May 2020, this element is no longer supported.  * Type: String * Example: "String" |
| UserGroups  The values for the User Groups item.  * Type: String[] * Example: "String" |
| UserInternalID  An internal ID to assign for the new user, or \* to automatically generate one.  * Type: String * Example: "String" |
| UserPhotoPath  A URL or file path identifying the location of a picture to show for this user. Maximum length 260 characters.  * Type: String * Example: "String" |
| UserRoleIDs  List of default roles for the user. The role descriptor can be used to identify a record by selecting an ID Type of Alias.  * Type: IndexRecordIn[] * Example: { "Identifier": { "ID": "10", "Type": "External" }, "Index": "1" } |
| UsersManagers  List of this user's managers. If provided, should include the PrimaryManager.  * Type: IDType[] * Example: { "ID": "String", "Type": "String" } |
| UserSubtemplateIDs  The subtemplates linked to this user. Subtemplates with a lower index take priority. Maximum of 7 allowed.  * Type: IndexRecordIn[] * Example: { "Identifier": { "ID": "10","Type": "External" }, "Index": 1" } |
| WebExternalIdentifier  External system Login ID.  * Type: String * Example: "String" |
