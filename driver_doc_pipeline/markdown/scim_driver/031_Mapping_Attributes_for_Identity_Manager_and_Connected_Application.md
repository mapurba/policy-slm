# C.0 Mapping Attributes for Identity Manager and Connected Application

The following table shows the default mapping of the User class and Group class SCIM attributes between the SCIM compliant connected application and the Identity Manager.

*Table C-1* Mapping of User Attributes

| Identity Manager Attribute | SCIM Attribute | Description |
| User | urn:ietf:params:scim:schemas:core:2.0:User | User class |
| city | addresses:worklocality | The work city of the user. |
| CN | userName | The user’s name. |
| co | addresses:workcountry | The user’s country of work. |
| costCenter | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User+costCenter | The cost center to which the user belongs. |
| displayName | displayName | The name of the user that is displayed in the application. |
| employeeType | userType | The user's employment type. |
| Full Name | name:formatted | User’s full name.  For example, the full name Ms. Barbara J Jensen, III. |
| Generational Qualifier | name:honorificSuffix | The user’s honorific suffix.  For example, III, given the full name Ms. Barbara J Jensen, III. |
| Given Name | name:givenName | User’s first name or given name.  For example, Barbara, given the full name Ms. Barbara J Jensen, III. |
| Group Membership | groups:value | The group identification value of the user. |
| homeCity | addresses:home:locality | The user’s city. |
| homeEmailAddress | emails:home:value | The user’s home email address. |
| homeState | addresses:home:region | The user’s home state. |
| homeZipCode | addresses:home:postalCode | The home postal zip code of the user. |
| Initials | name:middleName | The user’s initials.  For example, J, given the full name Ms. Barbara J Jensen, III. |
| Internet EMail Address | emails:work:value | The user's work email address. |
| Login Disabled | active | A boolean value indicating the user's administrative status. |
| managerWorkforcelD | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User+manager:value | The manager’s employee identification number. |
| OU | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User+department | Organization detail of the user. |
| personalTitle | name:honorificPrefix | The user’s honorofic prefixes.  For example, Ms, in the name Ms. Barbara J Jensen, III. |
| Postal Code | addresses:work:postalCode | The work postal zip code of the user. |
| preferredName | nickName | The user's preferred name. |
| S | addresses:work:region | The user’s regional state of work location. |
| SA | addresses:work:streetAddress | The user’s street address of work location. |
| Surname | name:familyName | User’s last name or family name.  For example, Jensen, given the full name Ms. Barbara J Jensen, III. |
| Telephone Number | phoneNumbers:work:value | The user's phone number. |
| Title | title | The user's designation. |
| workforcelD | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User+employeeNumber | The user's employee identification number. |

*Table C-2* Mapping of Group Attributes

| Identity Manager Attribute | SCIM Attribute | Description |
| Group | urn:ietf:params:scim:schemas:core:2.0:Group | Group class |
| CN | displayName | The name of the group displayed in the application. |
| Member | members:value | The name of the member displayed in the application. |

*IMPORTANT:*The above tables show the default attributes that are available as a part of [SCIM 2.0 RFC](https://datatracker.ietf.org/doc/html/rfc7643). If these default values are not applicable for your business environment, you can change the attribute mapping in the schema mapping policy.
