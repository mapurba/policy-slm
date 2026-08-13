# A.7 Input Transforms

#### NTIQBBRTGBE-ipt-VetoPseudoEntitlementAssociation

*Description:*
When using group based enrollments no object exists in eDirectory that can hold an association for a corresponding Blackboard Enrollment Object. The driver shim returns a destination DN value of “pseudo-enrollment-object” if no source DN was present. This policy vetos add-association operations for pseudo-enrollment-objects.
