# A.6 Output Transforms

#### NTIQBBRTDC-otp-CheckRequiredAttrs

*Description:*
Ensure attributes required by Blackboard object types are set before sending document to the driver shim. Refer to [Table A-7](btyjyer.html#btym772) for required attributes.

*Table A-7* Attributes Required by Blackboard

| Blackboard Object Type | Attribute Settings Required by Blackboard |
| DirXML-BB-Person | * DirXML-BB-p-id * DirXML-BB-p-firstname * DirXML-BB-p-lastname * DirXML-BB-p-sys-role * DirXML-BB-p-portal-role * DirXML-BB-p-email * DirXML-BB-p-ext-key |
| DirXML-BB-Course | * DirXML-BB-c-id * DirXML-BB-c-course-title |
| DirXML-BB-Organization | * DirXML-BB-o-id * DirXML-BB-o-title |
| DirXML-BB-Enrollment | * DirXML-BB-enr-p-ext-key * DirXML-BB-enr-c-ext-key |
