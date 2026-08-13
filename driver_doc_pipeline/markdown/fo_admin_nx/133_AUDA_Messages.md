# D.4 AUDA Messages

Messages beginning with AUDA are issued by Audit Services for Authentication Services.

AUDA001I Administrative Password Reset by driver\_name for Platform platform\_name IP address platform\_ip\_address: eUser eUser, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed an Administrative Password Reset request for the platform identified by platform\_name and platform\_ip\_address. The eUser whose password was reset is eUser. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.

AUDA002W Connection Rejected by driver\_name for Platform platform\_name IP address platform\_IP\_address: Reason reason.

Explanation:
The Core Driver identified by driver\_name rejected a connection attempt from the platform identified by platform\_name and platform\_IP\_address. If the request was from a platform that does not have a configuration object in the ASAM System container, platform\_name is empty. The reason the connection attempt was rejected is given by reason.

Action:
Correct the cause of the error based on the reason given by reason.

AUDA003I Check Password by driver\_name for Platform platform\_name IP address platform\_ip\_address: eUser eUser, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed a Check Password request for the platform identified by platform\_name and platform\_ip\_address. If the request was from a platform that does not have a configuration object in the ASAM System container, platform\_name is empty. The eUser whose password was checked is eUser. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.

AUDA004I Change Password by driver\_name for Platform platform\_name IP address platform\_ip\_address: eUser eUser, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed a Change Password request for the platform identified by platform\_name and platform\_ip\_address. If the request was from a platform that does not have a configuration object in the ASAM System container, platform\_name is empty. The eUser whose password was to be changed is eUser. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.

AUDA005I Get Context by driver\_name for Platform platform\_name IP address platform\_ip\_address: eUser eUser, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed a Get Context request for the platform identified by platform\_name and platform\_ip\_address. If the request was from a platform that does not have a configuration object in the ASAM System container, platform\_name is empty. The eUser whose context was to be obtained is eUser. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.

AUDA006I Get Security Equivalents by driver\_name for Platform platform\_name IP address platform\_ip\_address: eUser eUser, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed a Get Security Equivalents request for the platform identified by platform\_name and platform\_ip\_address. The eUser whose security equivalences list was to be obtained is eUser. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.

AUDA007I Get Group Members by driver\_name for Platform platform\_name IP address platform\_ip\_address: Group group, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed a Get Group Members request for the platform identified by platform\_name and platform\_ip\_address. The group whose member list was to be obtained is group. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.

AUDA008I Check Security Equivalence by driver\_name for Platform platform\_name IP address platform\_ip\_address: eUser eUser to object object, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed a Check Security Equivalence request for the platform identified by platform\_name and platform\_ip\_address. The eUser eUser was checked for security equivalence to the object object. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.

AUDA009I Check Rights to Attribute by driver\_name for Platform platform\_name IP address platform\_ip\_address: Object1 object1, Rights [rights], Attribute attribute\_name, Object2 object2, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed a Check Rights to Attribute request for the platform identified by platform\_name and platform\_ip\_address. The object object1 was checked for the rights rights to the attribute attribute\_name of object object2. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.

AUDA010I Get Attribute by driver\_name for Platform platform\_name IP address platform\_ip\_address: Object object, Attribute attribute\_name, Return Value rc, Elapsed Time seconds.

Explanation:
The Core Driver identified by driver\_name processed a Get Attribute request for the platform identified by platform\_name and platform\_ip\_address. The value of the attribute attribute\_name for object object was to be obtained. The return code from the Core Driver to the platform was rc. The Core Driver took seconds seconds to process the request.

Action:
None. Informational only.
