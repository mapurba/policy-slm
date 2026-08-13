# D.6 AUDR Messages

Messages beginning with AUDR are issued by Audit Services to report actions taken during Receiver script processing.

AUDR001I Add User on Platform platform\_object: eUser eUser, UID uid, Platform Association platform\_association.

Explanation:
An Add User was processed by the platform identified by platform\_object for eUser eUser. The association platform\_association was returned for the user. The Linux/UNIX UID number for the user is uid.

Action:
None. Informational only.

AUDR002I Modify User on Platform platform\_object: eUser eUser, UID uid, Platform Association platform\_association.

Explanation:
A Modify User was processed by the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association. The Linux/UNIX UID number for the user is uid.

Action:
None. Informational only.

AUDR003I Delete User on Platform platform\_object: eUser eUser, Platform Association platform\_association.

Explanation:
A Delete User was processed by the platform identified by platform\_object for eUser eUser. The association for the user was platform\_association.

Action:
None. Informational only.

AUDR004I Enable User on Platform platform\_object: eUser eUser, Platform Association platform\_association.

Explanation:
An Enable User was processed by the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
None. Informational only.

AUDR005I Disable User on Platform platform\_object: eUser eUser, Platform Association platform\_association.

Explanation:
A Disable User was processed by the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
None. Informational only.

AUDR006I Rename User on Platform platform\_object: eUser eUser, Old Platform Association old\_platform\_association, New Platform Association new\_platform\_association.

Explanation:
A Rename User was processed by the platform identified by platform\_object for eUser eUser. The old association for the user was old\_platform\_association. The new association new\_platform\_association was returned for the user.

Action:
None. Informational only.

AUDR007I Move User on Platform platform\_object: eUser eUser, Old Platform Association old\_platform\_association, New Platform Association new\_platform\_association.

Explanation:
A Move User was processed by the platform identified by platform\_object for eUser eUser. The old association for the user was old\_platform\_association. The new association new\_platform\_association was returned for the user.

Action:
None. Informational only.

AUDR008I Add User to Group on Platform platform\_object: eUser eUser, eUser Platform Association eUser\_platform\_association, eGroup eGroup, eGroup Platform Association eGroup\_platform\_association.

Explanation:
An Add User to Group was processed by the platform identified by platform\_object for eUser eUser. The Group is eGroup. The association for the user is eUser\_platform\_association. The association for the group is eGroup\_platform\_association.

Action:
None. Informational only.

AUDR009I Remove User from Group on Platform platform\_object: eUser eUser, eUser Platform Association eUser\_platform\_association, eGroup eGroup, eGroup Platform Association eGroup\_platform\_association.

Explanation:
A Remove User from Group was processed by the platform identified by platform\_object for eUser eUser. The Group is eGroup. The association for the user is eUser\_platform\_association. The association for the group is eGroup\_platform\_association.

Action:
None. Informational only.

AUDR010I Add Group on Platform platform\_object: eGroup eGroup, GID gid, Platform Association platform\_association.

Explanation:
An Add Group was processed by the platform identified by platform\_object for eGroup eGroup. The association platform\_association was returned for the group. The Linux/UNIX GID number for the group is gid.

Action:
None. Informational only.

AUDR011I Modify Group on Platform platform\_object: eGroup eGroup, GID gid, Platform Association platform\_association.

Explanation:
A Modify Group was processed by the platform identified by platform\_object for eGroup eGroup. The association for the group is platform\_association. The Linux/UNIX GID number for the group is gid.

Action:
None. Informational only.

AUDR012I Delete Group on Platform platform\_object: eGroup eGroup, Platform Association platform\_association.

Explanation:
A Delete Group was processed by the platform identified by platform\_object for eGroup eGroup. The association for the group was platform\_association.

Action:
None. Informational only.

AUDR013I Rename Group on Platform platform\_object: eGroup eGroup, Old Platform Association old\_platform\_association, New Platform Association new\_platform\_association.

Explanation:
A Rename Group was processed by the platform identified by platform\_object for eGroup eGroup. The old association for the group was old\_platform\_association. The new association new\_platform\_association was returned for the group.

Action:
None. Informational only.

AUDR014I Move Group on Platform platform\_object: eGroup eGroup, Old Platform Association old\_platform\_association, New Platform Association new\_platform\_association.

Explanation:
A Move Group was processed by the platform identified by platform\_object for eGroup eGroup. The old association for the group was old\_platform\_association. The new association new\_platform\_association was returned for the group.

Action:
None. Informational only.

AUDR015I Replicate Password on Platform platform\_object: eUser eUser.

Explanation:
A Replicate Password was processed by the platform identified by platform\_object for eUser eUser.

Action:
None. Informational only.

AUDR016E Add User failed on Platform platform\_object: eUser eUser, UID uid.

Explanation:
An Add User failed on the platform identified by platform\_object for eUser eUser. The Linux/UNIX UID number for the user is uid.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR017E Modify User failed on Platform platform\_object: eUser eUser, UID uid, Platform Association platform\_association.

Explanation:
A Modify User failed on the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association. The Linux/UNIX UID number for the user is uid.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR018E Delete User failed on Platform platform\_object: eUser eUser, Platform Association platform\_association.

Explanation:
A Delete User failed on the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR019E Enable User failed on Platform platform\_object: eUser eUser, Platform Association platform\_association.

Explanation:
An Enable User failed on the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR020E Disable User failed on Platform platform\_object: eUser eUser, Platform Association platform\_association.

Explanation:
A Disable User failed on the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR021E Rename User failed on Platform platform\_object: eUser eUser, Old Platform Association platform\_association.

Explanation:
A Rename User failed on the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR022E Move User failed on Platform platform\_object: eUser eUser, Old Platform Association platform\_association.

Explanation:
A Move User failed on the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR023E Add User to Group failed on Platform platform\_object: eUser eUser, eUser Platform Association eUser\_platform\_association, eGroup eGroup, eGroup Platform Association eGroup\_platform\_association.

Explanation:
An Add User to Group failed on the platform identified by platform\_object for eUser eUser. The Group is eGroup. The association for the user is eUser\_platform\_association. The association for the group is eGroup\_platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR024E Remove User from Group failed on Platform platform\_object: eUser eUser, eUser Platform Association eUser\_platform\_association, eGroup eGroup, eGroup Platform Association eGroup\_platform\_association.

Explanation:
A Remove User from Group failed on the platform identified by platform\_object for eUser eUser. The Group is eGroup. The association for the user is eUser\_platform\_association. The association for the group is eGroup\_platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR025E Add Group failed on Platform platform\_object: eGroup eGroup, GID gid.

Explanation:
An Add Group failed on the platform identified by platform\_object for eGroup eGroup. The Linux/UNIX GID number for the group is gid.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR026E Modify Group failed on Platform platform\_object: eGroup eGroup, GID gid, Platform Association platform\_association.

Explanation:
A Modify Group failed on the platform identified by platform\_object for eGroup eGroup. The association for the group is platform\_association. The Linux/UNIX GID number for the group is gid.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR027E Delete Group failed on Platform platform\_object: eGroup eGroup, Platform Association platform\_association.

Explanation:
A Delete Group failed on the platform identified by platform\_object for eGroup eGroup. The association for the group is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR028E Rename Group failed on Platform platform\_object: eGroup eGroup, Old Platform Association platform\_association.

Explanation:
A Rename Group failed on the platform identified by platform\_object for eGroup eGroup. The association for the group is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR029E Move Group failed on Platform platform\_object: eGroup eGroup, Old Platform Association platform\_association.

Explanation:
A Move Group failed on the platform identified by platform\_object for eGroup eGroup. The association for the group is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR030E Replicate Password failed on Platform platform\_object: eUser eUser.

Explanation:
A Replicate Password failed on the platform identified by platform\_object for eUser eUser.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR031I Pending Delete User on Platform platform\_object: eUser eUser, Platform Association platform\_association.

Explanation:
A Pending Delete User was processed by the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
None. Informational only.

AUDR032I Pending Delete Group on Platform platform\_object: eGroup eGroup, Platform Association platform\_association.

Explanation:
A Pending Delete Group was processed by the platform identified by platform\_object for eGroup eGroup. The association for the group is platform\_association.

Action:
None. Informational only.

AUDR033E Pending Delete User failed on Platform platform\_object: eUser eUser, Platform Association platform\_association.

Explanation:
A Pending Delete User failed on the platform identified by platform\_object for eUser eUser. The association for the user is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR034E Pending Delete Group failed on Platform platform\_object: eGroup eGroup, Platform Association platform\_association.

Explanation:
A Pending Delete Group failed on the platform identified by platform\_object for eGroup eGroup. The association for the group is platform\_association.

Action:
Examine the log on the platform to determine the cause of the failure, and take action as appropriate.

AUDR035I User user authentication result is returnCode (reasonString) [elapsedTime elapsed seconds].

Explanation:
This message displays the result of an authentication attempt.

Possible Cause:
This message is the result of an authentication request.

Action:
None.
