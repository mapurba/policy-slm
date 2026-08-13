# B.0 Class and Attribute Descriptions

[Table B-1](class-attribute.html#b1d2rcwj) lists the GroupWise attributes included in the Schema Mapping policy. You might need to customize them to meet your requirement.

*Table B-1* Classes and Attributes Included in the Schema Mapping Policy

| eDirectory Class or Attribute | GroupWise Attribute | Description |
| User |  |  |
| CN | None | Common Name of a User object. This attribute is not included in the Schema Mapping policy, but the driver internally maps it with a corresponding GroupWise attribute.  When a GroupWise account is created or renamed, this value is used to name the GroupWise account. For all other operations, this value is ignored. |
| Given Name | 50091 | User’s first name  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Surname | 50093 | User’s last name  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Title | 50096 | User’s title  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| OU | 50089 | User’s department  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Telephone Number | 50095 | User’s telephone number  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Facsimile Telephone Number | 50145 | User’s facsimile telephone number  Only synchronizes the telephone number portion from eDirectory to GroupWise on Create and Modify events. |
| Company | 50310 | User’s company  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Initials | 50322 | Middle initials, up to 8 characters |
| Generational Qualifier | 50323 | Jr., III, and so forth, up to 8 characters |
| personalTitle | 50324 | Dr., Mr., Ms., and so forth, up to 8 characters |
| Login Disabled | 50058 | A Boolean value that indicates whether eDirectory login (authentication) is allowed.  Synchronizes from eDirectory to GroupWise on Create and Modify events. The shim converts true to 1 and false to 0. Setting the GroupWise 50058 attribute to 1 disables the GroupWise account. See the note at the end of this table for additional information. |
| Login Expiration Time | 50138 | Synchronizes from eDirectory to GroupWise on Create and Modify events. Setting the GroupWise 50138 attribute to 1 expires the GroupWise account. |
| OU | 50089 | User’s department.  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Group |  |  |
| Member of a group | Member To | On eDirectory user Modify events, a set of distribution lists can be specified. The user can be added as a Member, BC, or CC. On a Modify event, a user can be removed from a specified distribution list (member, BC or CC) or from all distribution lists (member, BC or CC). The shim removes the user from the appropriate distribution list. |
| Organizational Unit |  |  |
| OU | CN | User’s department  Synchronizes from eDirectory to GroupWise on Create and Modify events. |

[Table B-2](class-attribute.html#b1eob7bu) lists the attributes that are available in the upgraded GroupWise driver. You might need to customize them to meet your requirement.

*Table B-2* Classes and Attributes Included in the Schema Mapping Policy for the Upgraded Driver

| eDirectory Class or Attribute | GroupWise Attribute | Description |
| User |  |  |
| Given Name | 50091 | User’s first name  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Surname | 50093 | User’s last name  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Title | 50096 | User’s title  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| OU | 50089 | User’s department  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Telephone Number | 50095 | User’s telephone number  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Facsimile Telephone Number | 50145 | User’s facsimile telephone number  Only synchronizes the telephone number portion from eDirectory to GroupWise on Create and Modify events. |
| NGW: Object ID | 50073 | GW mailbox name. The name must be unique within a post office. The name contains 1 to 256 characters, and cannot contain the ()@.:",{}\* characters.  This attribute takes its value from the CN attribute. It is set when an account is created and modified, and when an account is renamed. Modifying this value might cause the following attributes to be modified:  * Email Address * Internet Email Address * NGW: GroupWise ID * Identity Manager association key |
| NGW Account ID | 50116 | Optional field for accounting. It can contain a cost account used for posting charges to this user.  Normally the driver does not set this value. However, this attribute can be set through the Create rule or Create style sheet. |
| NGW: Gateway Access | 59001 | Normally the driver does not set this value. However, this attribute can be set through the Create rule or style sheet. |
| NGW: Mailbox Expiration Time | 50138 | This attribute is used to set the NGW: Expiration Time attribute which in turn will set the GroupWise attribute 50058. |
| Login Disabled | 50058 | A Boolean value that indicates whether eDirectory login (authentication) is allowed.  Synchronizes from eDirectory to GroupWise on Create and Modify events. The shim converts true to 1 and false to 0. Setting the GroupWise 50058 attribute to 1 disables the GroupWise account. See the note at the end of this table for additional information. |
| NGW: File ID | 50038 | Three characters used to name system files for the user. The value must be unique within a post office. This value is set by GroupWise.  A Move event could cause this attribute to change. This attribute should not be modified in any style sheet. |
| NGW: Visibility | 50076 | Used to specify the databases into which an object should be replicated. Controls whether objects appear in the address book.  This attribute can be set through the Create rule or style sheet. To set it, add code to the Create rule. Use SYSTEM for global visibility, or NONE for no visibility. The value to set the visibility for Post Office is POST\_OFFICE and Domain is DOMAIN. |
| Group |  |  |
| NGW: Visibility | 50076 | Used to specify the databases into which an object should be replicated. Controls whether objects appear in the address book.  This attribute can be set through the Create rule or style sheet. To set it, add code to the Create rule. Use SYSTEM for global visibility, or NONE for no visibility. The value to set the visibility for Post Office is POST\_OFFICE and Domain is DOMAIN. |
| Member | Member To | On eDirectory user Modify events, a set of distribution lists can be specified. The user can be added as a Member, BC, or CC. On a Modify event, a user can be removed from a specified distribution list (member, BC or CC) or from all distribution lists (member, BC or CC). The shim removes the user from the appropriate distribution list. |
| GroupWise Distribution List |  |  |
| NGW: Visibility | 50076 | Used to specify the databases into which an object should be replicated. Controls whether objects appear in the address book.  This attribute can be set through the Create rule or style sheet. To set it, add code to the Create rule. Use SYSTEM for global visibility, or NONE for no visibility. The value to set the visibility for Post Office is POST\_OFFICE and Domain is DOMAIN. |
| Member | Member To | On eDirectory user Modify events, a set of distribution lists can be specified. The user can be added as a Member, BC, or CC. On a Modify event, a user can be removed from a specified distribution list (member, BC or CC) or from all distribution lists (member, BC or CC). The shim removes the user from the appropriate distribution list. |
| NGW: Carbon Copy Member | Member CC | Use the gw:participation=“cc” attribute to have the driver set this information. |
| NGW: Blank Copy Member | Member BC | Use the gw:participation=“bc” attribute to have the driver set this information. |
| GroupWise External Entity |  |  |
| Given Name | 50091 | User’s first name  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Surname | 50093 | User’s last name  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Title | 50096 | User’s title  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| OU | 50089 | User’s department  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Telephone Number | 50095 | User’s telephone number  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
| Facsimile Telephone Number | 50145 | User’s facsimile telephone number  Only synchronizes the telephone number portion from eDirectory to GroupWise on Create and Modify events. |
| NGW: Object ID | 50073 | GW mailbox name. The name must be unique within a post office. The name contains 1 to 256 characters, and cannot contain the ()@.:",{}\* characters.  This attribute takes its value from the CN attribute. It is set when an account is created and modified, and when an account is renamed. Modifying this value might cause the following attributes to be modified:  * Email Address * Internet Email Address * NGW: GroupWise ID * Identity Manager association key |
| NGW Account ID | 50116 | Optional field for accounting. It can contain a cost account used for posting charges to this user.  Normally the driver does not set this value. However, this attribute can be set through the Create rule or Create style sheet. |
| NGW: External Net ID | 50094 |  |
| NGW: Mailbox Expiration Time | 50138 | This attribute is used to set the NGW: Expiration Time attribute which in turn will set the GroupWise attribute 50058. |
| Login Disabled | 50058 | A Boolean value that indicates whether eDirectory login (authentication) is allowed.  Synchronizes from eDirectory to GroupWise on Create and Modify events. The shim converts true to 1 and false to 0. Setting the GroupWise 50058 attribute to 1 disables the GroupWise account. See the note at the end of this table for additional information. |
| NGW: File ID | 50038 | Three characters used to name system files for the user. The value must be unique within a post office. This value is set by GroupWise.  A Move event could cause this attribute to change. This attribute should not be modified in any style sheet. |
| NGW: Visibility | 50076 | Used to specify the databases into which an object should be replicated. Controls whether objects appear in the address book.  Normally, the driver does not set this value. However, this attribute can be set through the Create rule or style sheet. To set it, add code to the Create rule. Use SYSTEM for global visibility, or NONE for no visibility.  The value to set the visibility for Post Office is POST\_OFFICE and Domain is DOMAIN. |
| GroupWise Resource |  |  |
| NGW: Owner | 50081 | The user (NGW: Object ID) that owns the resource. An owner is identified by its Object Name. |
| Organizational Unit |  |  |
| CN | OU | The corresponding GroupWise class is GroupWise Post Office. |

[Table B-3](class-attribute.html#b1d2vlhy) lists additional GroupWise attributes that you can customize through policies to meet your business requirements.

*Table B-3* Custom Attributes That Are Not Part of the Default Schema Mapping Policy

| eDirectory Class or Attribute | GroupWise Attribute | Description |
| User |  |  |
|  | 50319 | Preferred Internet eMail ID. For example: JohnDoe  “mapi” is not allowed because it is reserved.  This ID must be unique in the entire GroupWise system. It contains 1 to 256 characters, and cannot contain the ( ) @ : , { } \* ” characters. The ID must be unique within its namespace (UserID, nicknames, resources, and distribution lists share the same namespace.) |
|  | 50045 | Internet domain name  The attribute 50045 takes a string value. Ensure that you convert this attribute to a structured attribute because GroupWise accepts some attributes only in a structured format. For more information, see [Converting String Attributes to Structured Attributes](modify-policies.html#b1ey3xc1).  Example: MyDomain.com |
|  | 50094 | Net ID  This can either be a fully distinguished name or the common name. |
|  | 58004 | DS\_DN  This is always the fully distinguished name. |
|  | 58056 | LDAP authentication ID in typeful format. For example: cn=admin, o=novell |
|  | 50013 | Preferred Internet address format  (numeric value)  0 - Full (Name.  PostOffice.Domain@IDomain.com) 1 - Host and User ID (Name.PostOffice@IDomain.com) 2 - User ID (Name@IDomain.com) 3 - Lastname.firstname 4 - Firstname.lastname 5 - No setting (reserved) 6 - First initial and last name |
|  | 50320 | Allowed Addressing formats  (bit settings)  0 - None 1 - Full (never set this bit) 2 - Host 4 - User ID 8 - Lastname.Firstname 16 - Firstname.Lastname 32 - First initial and last name  You should not set bit one in this attribute value. It is an illegal operation to disallow the Full format. You can “or” values together. For instance, to allow only full name you use a value of 62 (0x3E). |
|  | 50157 | Exclusive use of Internet domain name  You can set the Exclusive Use of Internet Domain Name by using the 50157 attribute in the legacy GroupWise driver and 50045 attribute in the GroupWise driver. The attribute 50045 takes a string value. Ensure that you convert this attribute to a structured attribute because GroupWise accepts some attributes only in a structured format. For more information, see [Converting String Attributes to Structured Attributes](modify-policies.html#b1ey3xc1).  True. Requires setting an Internet domain name: 50045. False. Only recognizes the domain name set in the Internet domain name: 50045. |
| GroupWise External Entity |  |  |
|  | 50319 | Preferred Internet eMail ID  Example: JohnDoe  “mapi” is not allowed because it is reserved.  This ID must be unique in the entire GroupWise system. It contains 1 to 256 characters, and cannot contain the ( ) @ : , { } \* ” characters. The ID must be unique within its namespace (UserID, nicknames, resources, and distribution lists share the same namespace.) |
|  | 50045 | Internet domain name  Example: MyDomain.com  The attribute 50045 takes a string value. Ensure that you convert this attribute to a structured attribute because GroupWise accepts some attributes only in a structured format. For more information, see [Converting String Attributes to Structured Attributes](modify-policies.html#b1ey3xc1). |
|  | 58056 | LDAP authentication ID in typeful format  Example: cn=admin, o=novell |
|  | 50013 | Preferred Internet address format.  (numeric value)  0 - Full (Name.PostOffice.Domain@IDomain.com) 1 - Host and User ID (Name.PostOffice@IDomain.com) 2 - User ID (Name@IDomain.com) 3 - Lastname.firstname 4 - Firstname.lastname 5 - No setting (reserved) 6 - First initial and last name |
|  | 50320 | Allowed addressing formats.  (bit settings)  0 - None 1 - Full (never set this bit) 2 - Host 4 - User ID 8 - Lastname.Firstname 16 - Firstname.Lastname 32 - First initial and last name  You should not set bit one in this attribute value. It is an illegal operation to disallow the Full format. You can “or” values together. For instance, to allow only full name you use a value of 62 (0x3E). |
|  | 50157 | Exclusive use of Internet domain name.  You can set the Exclusive Use of Internet Domain Name by using the 50157 attribute in the legacy GroupWise driver and 50045 attribute in the GroupWise driver. The attribute 50045 takes a string value. Ensure that you convert this attribute to a structured attribute because GroupWise accepts some attributes only in a structured format. For more information, see [Converting String Attributes to Structured Attributes](modify-policies.html#b1ey3xc1).  True. Requires setting an Internet domain name: 50045. False. Only recognizes the domain name set in the Internet domain name: 50045. |
| Description | 50032 | Provides additional information.  Synchronizes from eDirectory to GroupWise on Create and Modify events. |
