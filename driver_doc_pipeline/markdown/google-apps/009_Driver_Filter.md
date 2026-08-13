# 3.2 Driver Filter

The driver supports Contacts, Users, Groups and Organizational Units classes. For Users and Contacts the following table lists the default list of attributes. These classes support many more attributes that can be found by refreshing the application schema and mapping them to an eDirectory attribute in the schema mapping rule.

*Table 3-1* Contact and User Attributes for Driver Filters

| Class | Attribute | Notes |
| OrganizationUnit | Description |  |
|  | OU | This is the naming value of the attribute |
| Group | Member |  |
|  | Owner |  |
|  | CN | Required |
|  | DirXML-GAGroupEMailAddress | This attribute is required in order to determine which email domain the group belongs to. The value should be in the form of an email address i.e.Â info@yourcompany.com. |

| Class | Attribute | Notes |
| User | DirXML-EntitlementRef | Required if using entitlements |
|  | nspmDistributionPassword | Required if synchronizing user passwords. Note that it is required to set a password for a new user. Even if you are using SAML for authentication you will need to set a password on the account to have it provision to GÂ Suite.Â |
|  | Given Name | Required |
|  | Surname | Required |
|  | Login Disabled |  |
|  | assistant | See manager attribute |
|  | manager | Assistant and Manager are DN attributes in eDirectory. In Google, these map to text fields. It is recommended that the developer decide what should be synchronized to Google (i.e. Given Name Last Name) and write a transformation for displaying that information in the Google Contacts application.Â |
|  | Telephone Number |  |
|  | Mobile |  |
|  | Company |  |
|  | L |  |
|  | OU | Department |
|  | Title |  |
|  | preferredName | preferredName is mapped by default to the Alias attribute in GÂ Suite. This should be in the form of an email address: i.e.Â name@yourcompany.com.Â |

| Class | Attribute | Notes |
| DirXML-GAContact | Surname | Required |
|  | Facsimile Telephone Number |  |
|  | Given Name | Required |
|  | Mobile |  |
|  | OU |  |
|  | L |  |
|  | Title |  |
|  | Pager |  |
|  | Telephone Number |  |
|  | Company |  |
|  | Internet Email Address | Required |
| Group | EmailAddress | Required naming attribute |
|  | Name | Group descriptive name |
|  | Description | Description of the group |
|  | Members | List of members |
|  | Owners | List of owners. In Google, owners are just members with an owner flag set. |
|  | AllowExternalMembers | Allows external members to view and join the group. Possible values are TRUE or FALSE. |
|  | AllowGoogleCommunication | Allows Google to contact group administrators. Possible values are TRUE or FALSE. |
|  | AllowWebPosting | Allows posting to the group web forum. Possible values are TRUE or FALSE. |
|  | ArchiveOnly | Allows the group to be only archived. Possible values are TRUE or FALSE. |
|  | IsArchived | Allows the contents of the group to be archived. Possible values are TRUE or FALSE. |
|  | MaxMessageBytes | Maximum size of a message. Default is 1Â Mbyte. |

| Class | Attribute | Notes |
|  | MessageModerationLevel | * MODERATE\_ALL\_MESSAGES * MODERATE\_NEW\_MESSAGES * MODERATE\_NONE * MODERATE\_NONMEMBERS |
|  | SpamModerationLevel | * ALLOW * MODERATE * SILENTLY\_MODERATE * REJECT |
|  | ReplyTo | * REPLY\_TO\_CUSTOM * REPLY\_TO\_IGNORE * REPLY\_TO\_LIST * REPLY\_TO\_MANAGERS * REPLY\_TO\_OWNER * REPLY\_TO\_SENDER |
|  | CustomReplyTo | Custom REPLY\_TO message |
|  | SendMessageDenyNotification | Allows member to be notified if his message is denied by the owner. Possible values are TRUE or FALSE. |
|  | DefaultMessageDenyNotificationText | Notification message text sent when a message is denied. |
|  | ShowInGroupDirectory | Allows groups to be listed in the Groups directory. Possible values are TRUE or FALSE. |
|  | MembersCanPostAsTheGroup | Allows members to post using the group email address. Possible values are TRUE or FALSE. |
|  | PrimaryLanguage | Group Primary Language. SeeÂ âGoogle Language Tagsâ at <https://developers.google.com/admin-sdk/email-settings/#language_tags> |
|  | MessageDisplayFont | Default message display font:  * DEFAULT\_FONT * FIXED\_WIDTH\_FONT |
|  | IncludeInGlobalAddressList | Enables the group to be included in the Global Address List. Possible values are TRUE or FALSE. |

| Class | Attribute | Notes |
|  | WhoCanJoin | Permission to join the group  * ALL\_IN\_DOMAIN\_CAN\_JOIN * ANYONE\_CAN\_JOIN * CAN\_REQUEST\_TO\_JOIN * INVITED\_CAN\_JOIN |
|  | WhoCanViewMembership | * ALL\_IN\_DOMAIN\_CAN\_VIEW * ALL\_MANAGERS\_CAN\_VIEW * ALL\_MEMBERS\_CAN\_VIEW |
|  | WhoCanViewGroup | * ALL\_IN\_DOMAIN\_CAN\_VIEW * ALL\_MANAGERS\_CAN\_VIEW * ALL\_MEMBERS\_CAN\_VIEW * ANYONE\_CAN\_VIEW |
|  | WhoCanInvite | * ALL\_MEMBERS\_CAN\_INVITE * ALL\_MANAGERS\_CAN\_INVITE * NONE\_CAN\_INVITE |
|  | WhoCanPostMessage | * ALL\_IN\_DOMAIN\_CAN\_POST * ALL\_MANAGERS\_CAN\_POST * ALL\_MEMBERS\_CAN\_POST * ANYONE\_CAN\_POST * NONE\_CAN\_POST |
|  | WhoCanLeaveGroup | * ALL\_MANAGERS\_CAN\_LEAVE * ALL\_MEMBERS\_CAN\_LEAVE * NONE\_CAN\_LEAVE |
|  | WhoCanContactOwner | ALL\_IN\_DOMAIN\_CAN\_CONTACT  ALL\_MANAGERS\_CAN\_CONTACT  ALL\_MEMBERS\_CAN\_CONTACT  ANYONE\_CAN\_CONTACT |
|  |  |  |
