# 1.4 Differences Between eDirectory and Blackboard

## 1.4.1 Organization

Blackboard is similar to eDirectory in the way information is organized with the exception of Blackboard Enrollments.

User objects in eDirectory map directly to Person objects in Blackboard. Group objects in eDirectory map directly to Course and Organization objects in Blackboard. Course and Organization objects are differentiated by the NTIQBBRTDC-sub-evt-DetermineBBObjectType Event Transform Policy. Blackboard Enrollments have additional attributes that eDirectory Group memberships do not support. In order to support Blackboard Enrollments, use the Group Member and Owner attributes to represent enrollments in Blackboard. The disadvantage of using the Member and Owner attributes is that enrollments can only be removed rather than being disabled.

While eDirectory is hierarchical, Blackboard is flat—there is no concept of a move function. The Subscriber channel rejects move commands. The sample Subscriber Event policy vetoes move events. You can change this policy to perform installation-specific processing of move events if required.

User object deletions in eDirectory result in the associated Person object in Blackboard being deleted. Group object deletions in eDirectory result in the associated Course or Organization object in Blackboard being deleted. There is no concept of rename in Blackboard. Blackboard is not hierarchical. There is no move function.

## 1.4.2 Passwords

Identity Manager uses the nspmDistributionPassword attribute to provide passwords from eDirectory. The mapping policy in the preconfigured sample policies maps nspmDistributionPassword to DirXML-BB-p-password.
