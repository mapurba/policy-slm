# A.2 Matching

#### NTIQBBRTDC-sub-mp-SubscriberMatching

*Description:*
Search for a matching Blackboard object based on the type of Blackboard object type set in the BBObjectType operation property. Refer to [Table A-1](btyjyen.html#btylb7l) for matching attributes.

*Table A-1* Matching Attributes

| eDirectory Object Class | eDirectory Attribute | BBObjectType | Blackboard Attribute |
| User | Source Name | DirXMI-BB-Person | DirXML-BB-p-id |
| Group | Source Name | DirXML-BB-Course | DirXML-BB-c-id |
| Organization | Source Name | DirXML-BB-Organization | DirXML-BB-o-id |
| DirXML-BB-Enrollment\* | DirXML-BB-c-ext-key, DirXML-BB-p-ext-key | DirXML-BB-Enrollment | DirXML-BB-c-ext-key, DirXML-BB-p-ext-key |

*\**
The DirXML-BB-Enrollment class can represent objects using effective class DirXML-BB-Enrollment in eDirectory or can represent pseudo enrollment objects created in policy when using attributes on groups to represent enrollments. For more information see [Organization](btvj3fi.html#btvj5ft).
