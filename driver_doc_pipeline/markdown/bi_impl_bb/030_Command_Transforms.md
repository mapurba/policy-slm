# A.4 Command Transforms

#### NTIQBBRTDC-ctp-TransformLoginDisabled

*Description:*
Transform changes on user object attribute “Login Disabled” to Blackboard DirXML-BB-Person object attributes DirXML-BB-p-row-status and DirXML-BB-p-available-ind. Refer to [Table A-5](btyjyep.html#btylxb0) for attribute value settings.

*Table A-5* Attribute Values

| Login Disabled | DirXML-BB-p-row-status | DirXML-BB-p-available-ind |
| True | ENABLED | True |
| False | ENABLED | False |

#### NTIQBBRTDC-ctp-SetClassnameForGroups

*Description:*
Set the operation object class for groups to the Blackboard object class type based on the value in the BBObjectType operation property. BBObjectType is set in the NTIQBBRTDC-evt-DetermineBBObjectType policy. Group objects can represent a Blackboard Course or Organization so the object class determines which one the operation maps to.

#### NTIQBBRTGBE-sub-ctp-TransformGroupAttrsToEnrollmentObjects

*Description:*
Transforms changes on Group attributes listed in the “attribute\_role\_map” GCV to DirXML-BB-Enrollment object events.
