# A.3 Creation Policies

#### NTIQBBRT-sub-cp-SubscriberCreation

*Description:*
Check to see if required attributes are set for object creation in Blackboard. If not set and specified in the GCVs default values will be set for some of the required attributes. Refer to [Table A-2](btyjyeo.html#btyl2u9), [Table A-3](btyjyeo.html#btyl4wp) and [Table A-4](btyjyeo.html#btyl735) for required attributes.

*Table A-2* Required User Attributes (BBObjectType operation property = DirXML-BB-Person)

| Required User Attribute | Action |
| DirXML-BB-p-id | If not set and GCV auto\_set\_ids is true set to Source Name. |
| Internet Email Address | If not set and GCV auto\_set\_email is true set to CN + @ + GCV default\_email\_domain. |
| DirXML-BB-p-sys-role | If not set and GCV auto\_set\_roles is true set to value of GCV default\_user\_role. |
| DirXML-BB-p-portal-role | DirXML-BB-p-portal-role If not set and GCV auto\_set\_roles is true set to value of GCV default\_portal\_role. |
| DirXML-BB-p-ext-key | Set to Source Name with underscores replacing spaces. |

*Table A-3* Required Group Attributes (BBObjectType operation property = DirXML-BB-Course)

| Required Group Attribute | Action |
| DirXML-BB-c-course-title | If not set and GCV auto\_set\_title is true then set value to Source Name. |
| DirXML-BB-c-id | If not set and GCV auto\_set\_ids is true then set value to Source Name. |
| DirXML-BB-c-ext-key | Set to Source Name with underscores replacing spaces. |

*Table A-4* Required Organization Attributes (BBObjectType operation property = DirXML-BB-Organization)

| Required Organization Attribute | Action |
| DirXML-BB-o-title | If not set and GCV auto\_set\_title is true then set value to Source Name. |
| DirXML-BB-o-id | If not set and GCV auto\_set\_ids is true then set value to Source Name. |
| DirXML-BB-o-ext-key | Set to Source Name with underscores replacing spaces. |
