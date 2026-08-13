# 4.1 Attributes Required for Blackboard Object Creation

The Subscriber channel issues Blackboard REST API calls to process XDS commands received for objects and attributes represented in the Blackboard schema. It is up to the policy writer to ensure all required attributes are sent for Blackboard object creation. The sample policies can be configured on driver import or through global configuration values to ensure all required attributes are set on creation. The Blackboard REST API places restrictions on attribute values. It is up to the policy writer to ensure attributes mapped to Blackboard attributes contain values that conform to Blackboard attribute restrictions. The following tables list attributes required for Person, Course, Enrollment, and Organization creation in Blackboard. For information about restrictions on values for these attributes consult Blackboard documentation.

*Table 4-1* Person Attributes Required For Creation

| Blackboard Schema | Blackboard Attribute |
| DirXML-BB-p-ext-key | EXTERNAL\_PERSON\_KEY |
| DirXML-BB-p-id | USER\_ID |
| DirXML-BB-p-sys-role | SYSTEM\_ROLE |
| DirXML-BB-p-firstname | FIRSTNAME |
| DirXML-BB-p-lastname | LASTNAME |
| DirXML-BB-p-email | EMAIL |

*Table 4-2* Course Attributes Required For Creation

| Blackboard Schema | Blackboard Attribute |
| DirXML-BB-c-id | COURSE\_ID |
| DirXML-BB-c-course-title | COURSE\_NAME |

*Table 4-3* Organization Attributes Required For Creation

| Blackboard Schema | Blackboard Attribute |
| DirXML-BB-o-id | ORGANIZATION\_ID |
| DirXML-BB-o-title | ORGANIZATION\_NAME |

*Table 4-4* Course Enrollment Attributes Required For Creation

| Blackboard Schema | Blackboard Attribute |
| DirXML-BB-enr-c-ext-key | EXTERNAL\_COURSE\_KEY |
| DirXML-BB-enr-p-ext-key | EXTERNAL\_PERSON\_KEY |

*Table 4-5* Organization Enrollment Attributes Required For Creation

| Blackboard Schema | Blackboard Attribute |
| DirXML-BB-enr-o-ext-key | EXTERNAL\_ORGANIZATION\_ID |
| DirXML-BB-enr-p-ext-key | EXTERNAL\_PERSON\_KEY |
