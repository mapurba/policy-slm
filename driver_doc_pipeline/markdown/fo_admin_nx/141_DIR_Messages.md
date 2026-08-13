# D.12 DIR Messages

Messages beginning with DIR are issued by the Core Driver during LDAP directory access.

DIR001E Attribute Not Supported.

Explanation:
A call was made to the API routine to read the value of an attribute for an object, but the attribute specified is not supported. Only the Home Directory attribute is supported.

Action:
Correct the API call in the application program.

DIR002E Request Build Error.

Explanation:
The directory interface routine was unable to create a request to perform a directory action. This is an internal error.

Action:
Examine the log for related messages.

DIR003D Error.

Explanation:
This is a general error indication. This message is accompanied by other messages that provide additional details.

Action:
Examine the log for related messages.

DIR004D Success.

Explanation:
A directory operation was successful.

Action:
No action is required.

DIR005D Operations Error.

Explanation:
An LDAP operation returned LDAP\_OPERATIONS\_ERROR. This indicates an internal error. The server is unable to respond with a more specific error and is also unable to properly respond to a request. It does not indicate that the client has sent an erroneous message.

Action:
Examine the log for related messages.

DIR006D Protocol Error.

Explanation:
An LDAP operation returned LDAP\_PROTOCOL\_ERROR. This indicates that the server has received an invalid or malformed request from the client.

Action:
Examine the log for related messages.

DIR007D Time Limit Exceeded.

Explanation:
An LDAP operation returned LDAP\_TIMELIMIT\_EXCEEDED. This indicates that the operation's time limit specified by either the client or the server has been exceeded. On search operations, incomplete results are returned.

Action:
Examine the log for related messages. Check the health of the server hosting LDAP.

DIR008D Size Limit Exceeded.

Explanation:
An LDAP operation returned LDAP\_SIZELIMIT\_EXCEEDED. This indicates that in a search operation, the size limit specified by the client or the server has been exceeded. Incomplete results are returned.

Action:
Examine the log for related messages.

DIR009D Compare False.

Explanation:
An LDAP operation returned LDAP\_COMPARE\_FALSE. This does not indicate an error condition. It indicates that the results of a compare operation are false.

Action:
No action is required.

DIR010D Compare True.

Explanation:
An LDAP operation returned LDAP\_COMPARE\_TRUE. This does not indicate an error condition. It indicates that the results of a compare operation are true.

Action:
No action is required.

DIR011D Authentication Method Not Supported.

Explanation:
An LDAP operation returned LDAP\_AUTH\_METHOD\_NOT\_SUPPORTED. This indicates that during a bind operation the client requested an authentication method not supported by the LDAP server.

Action:
Examine the log for related messages. Make sure your LDAP server is running the most current version.

DIR012D Strong Authentication Required.

Explanation:
An LDAP operation returned LDAP\_STRONG\_AUTH\_REQUIRED. This indicates one of the following:

In bind requests, the LDAP server accepts only strong authentication.

In a client request, the client requested an operation, such as delete, that requires strong authentication.

In an unsolicited notice of disconnection, the LDAP server discovers the security protecting the communication between the client and server has unexpectedly failed or been compromised.

Possible Cause:
LDAPHOST port set to the unencrypted port 289 instead of the default of 636.

Action:
Examine the log for related messages. Make sure your LDAP server is running the most current version.

DIR013D Partial Results.

Explanation:
An LDAP operation returned LDAP\_PARTIAL\_RESULTS. This should not occur. The server should return LDAP\_REFERRAL instead.

Action:
Examine the log for related messages.

DIR014D Referral.

Explanation:
An LDAP operation returned LDAP\_REFERRAL. This does not indicate an error condition. In LDAPv3, it indicates that the server does not hold the target entry of the request, but that the servers in the referral field might hold the target.

Action:
No action is required.

DIR015D Admin Limit Exceeded.

Explanation:
An LDAP operation returned LDAP\_ADMINLIMIT\_EXCEEDED. This indicates that an LDAP server limit set by an administrative authority has been exceeded.

Action:
Examine the log for related messages. Check the health of the server hosting LDAP.

DIR016D Unavailable Critical Extension.

Explanation:
An LDAP operation returned LDAP\_UNAVAILABLE\_CRITICAL\_EXTENSION. This indicates that the LDAP server was unable to satisfy a request because one or more critical extensions were not available. Either the server does not support the control or the control is not appropriate for the operation type.

Action:
Examine the log for related messages. Make sure your LDAP server is running the most current version.

DIR017D Confidentiality Required.

Explanation:
An LDAP operation returned LDAP\_CONFIDENTIALITY\_REQUIRED. This indicates that the session is not protected by a protocol such as Transport Layer Security (TLS), which provides session confidentiality.

Action:
Examine the log for related messages. Make sure your LDAP server is running the most current version.

DIR018D SASL Bind in Progress.

Explanation:
An LDAP operation returned LDAP\_SASL\_BIND\_IN\_PROGRESS. This does not indicate an error condition, but indicates that the server is ready for the next step in the process. The client must send the server the same SASL mechanism to continue the process.

Action:
No action is required.

DIR019D No Such Attribute.

Explanation:
An LDAP operation returned LDAP\_NO\_SUCH\_ATTRIBUTE. This indicates that the attribute specified in the modify or compare operation does not exist in the entry.

Action:
Examine the log for related messages. Many times this requires no action.

DIR020D Undefined Type.

Explanation:
An LDAP operation returned LDAP\_UNDEFINED\_TYPE. This indicates that the attribute specified in the modify or add operation does not exist in the LDAP server's schema.

Action:
Make sure the schema has been properly extended.

DIR021D Inappropriate Matching.

Explanation:
An LDAP operation returned LDAP\_INAPPROPRIATE\_MATCHING. This indicates that the matching rule specified in the search filter does not match a rule defined for the attribute's syntax.

Action:
Examine the log for related messages.

DIR022D Constraint Violation.

Explanation:
An LDAP operation returned LDAP\_CONSTRAINT\_VIOLATION. This indicates that the attribute value specified in a modify, add, or modify DN operation violates constraints placed on the attribute. The constraint can be one of size or content (string only, no binary).

Possible Cause:
Password rules, such as uniqueness and length, are violated.

Action:
Examine the log for related messages.

DIR023D Type or Value Exists.

Explanation:
An LDAP operation returned LDAP\_TYPE\_OR\_VALUE\_EXISTS. This indicates that the attribute value specified in a modify or add operation already exists as a value for that attribute.

Action:
Examine the log for related messages. This might not require any action.

DIR024D Invalid Syntax.

Explanation:
An LDAP operation returned LDAP\_INVALID\_SYNTAX. This indicates that the attribute value specified in an add, compare, or modify operation is an unrecognized or invalid syntax for the attribute.

Action:
Examine the log for related messages.

DIR025D No Such Object.

Explanation:
An LDAP operation returned LDAP\_NO\_SUCH\_OBJECT. This indicates the target object cannot be found. This code is not returned on the following operations:

Search operations that find the search base but cannot find any entries that match the search filter.

Bind operations.

Action:
Examine the log for related messages. Make sure the application is installed and configured correctly.

DIR026D Alias Problem.

Explanation:
An LDAP operation returned LDAP\_ALIAS\_PROBLEM. This indicates that an error occurred when an alias was dereferenced.

Action:
Examine the log for related messages. Check the server health of the LDAP host.

DIR027D Invalid DN Syntax.

Explanation:
An LDAP operation returned LDAP\_INVALID\_DN\_SYNTAX. This indicates that the syntax of the DN is incorrect. (If the DN syntax is correct, but the LDAP server's structure rules do not permit the operation, the server returns LDAP\_UNWILLING\_TO\_PERFORM.)

Action:
Examine the log for related messages.

DIR028D Is Leaf.

Explanation:
An LDAP operation returned LDAP\_IS\_LEAF. This indicates that the specified operation cannot be performed on a leaf entry.

Action:
Examine the log for related messages.

DIR029D Alias Dereference Problem.

Explanation:
An LDAP operation returned LDAP\_ALIAS\_DEREF\_PROBLEM. This indicates that during a search operation, either the client does not have access rights to read the aliased object's name or dereferencing is not allowed.

Action:
Examine the log for related messages. Check the health of the LDAP host.

DIR030D Inappropriate Authentication.

Explanation:
An LDAP operation returned LDAP\_INAPPROPRIATE\_AUTH. This indicates that during a bind operation, the client is attempting to use an authentication method that the client cannot use correctly. For example, the following can cause this error:

The client returns simple credentials when strong credentials are required.

The client returns a DN and a password for a simple bind when the entry does not have a password defined.

Action:
Examine the log for related messages.

DIR031D Invalid Credentials.

Explanation:
An LDAP operation returned LDAP\_INVALID\_CREDENTIALS. This indicates that during a bind operation one of the following occurred:

The client passed either an incorrect DN or password.

The password is incorrect because it has expired, intruder detection has locked the account, or some other similar reason.

Action:
Examine the log for related messages.

DIR032D Insufficient Access.

Explanation:
An LDAP operation returned LDAP\_INSUFFICIENT\_ACCESS. This indicates that the caller does not have sufficient rights to perform the requested operation.

Action:
Examine the log for related messages.

DIR033D Busy.

Explanation:
An LDAP operation returned LDAP\_BUSY. This indicates that the LDAP server is too busy to process the client request at this time, but if the client waits and resubmits the request, the server might be able to process it later.

Action:
Examine the log for related messages. Check the health of the LDAP server.

DIR034D Unavailable.

Explanation:
An LDAP operation returned LDAP\_UNAVAILABLE. This indicates that the LDAP server cannot process the client's bind request, usually because it is shutting down.

Action:
Examine the log for related messages. Check the LDAP server's health.

DIR035D Unwilling to Perform.

Explanation:
An LDAP operation returned LDAP\_UNWILLING\_TO\_PERFORM. This indicates that the LDAP server cannot process the request because of server-defined restrictions. This error is returned for the following reasons:

The add entry request violates the server's structure rules.

The modify attribute request specifies attributes that users cannot modify.

Password restrictions prevent the action.

Connection restrictions prevent the action.

Action:
Examine the log for related messages.

DIR036D Loop Detected.

Explanation:
An LDAP operation returned LDAP\_LOOP\_DETECT. This indicates that the client discovered an alias or referral loop, and is thus unable to complete this request.

Action:
Examine the log for related messages.

DIR037D Naming Violation.

Explanation:
An LDAP operation returned LDAP\_NAMING\_VIOLATION. This indicates that the add or modify DN operation violates the schema's structure rules. For example:

The request places the entry subordinate to an alias.

The request places the entry subordinate to a container that is forbidden by the containment rules.

The RDN for the entry uses a forbidden attribute type.

Action:
Examine the log for related messages.

DIR038D Object Class Violation.

Explanation:
An LDAP operation returned LDAP\_OBJECT\_CLASS\_VIOLATION. This indicates that the add, modify, or modify DN operation violates the object class rules for the entry. For example, the following types of request return this error:

The add or modify operation tries to add an entry without a value for a required attribute.

The add or modify operation tries to add an entry with a value for an attribute that the class definition does not contain.

The modify operation tries to remove a required attribute without removing the auxiliary class that defines the attribute as required.

Action:
Examine the log for related messages.

DIR039D Not Allowed on Non Leaf Object.

Explanation:
An LDAP operation returned LDAP\_NOT\_ALLOWED\_ON\_NONLEAF. This indicates that the requested operation is permitted only on leaf entries. For example, the following types of requests return this error:

The client requests a delete operation on a parent entry.

The client requests a modify DN operation on a parent entry.

Action:
Examine the log for related messages.

DIR040D Not Allowed on RDN (Relative Distinguished Name).

Explanation:
An LDAP operation returned LDAP\_NOT\_ALLOWED\_ON\_RDN. This indicates that the modify operation attempted to remove an attribute value that forms the entry's relative distinguished name.

Action:
Examine the log for related messages.

DIR041D Already Exists.

Explanation:
An LDAP operation returned LDAP\_ALREADY\_EXISTS. This indicates that the add operation attempted to add an entry that already exists, or that the modify operation attempted to rename an entry to the name of an entry that already exists.

Action:
Examine the log for related messages. This message might not require any action.

DIR042D No Object Class Modifications.

Explanation:
An LDAP operation returned LDAP\_NO\_OBJECT\_CLASS\_MODS. This indicates that the modify operation attempted to modify the structure rules of an object class.

Action:
Examine the log for related messages.

DIR043D Results Too Large.

Explanation:
An LDAP operation returned LDAP\_RESULTS\_TOO\_LARGE. This indicates that the results of the request are too large.

Action:
Examine the log for related messages.

DIR044D Affects Multiple DSAS.

Explanation:
An LDAP operation returned LDAP\_AFFECTS\_MULTIPLE\_DSAS. This indicates that the modify DN operation moves the entry from one LDAP server to another and thus requires more than one LDAP server.

Action:
Examine the log for related messages.

DIR045D Other.

Explanation:
An LDAP operation returned LDAP\_OTHER. This indicates an unknown error condition. This is the default value for error codes that do not map to other LDAP error codes.

Action:
Examine the log for related messages.

Use DSTRACE to gather more specific error information.

DIR046D Server Down.

Explanation:
An LDAP operation returned LDAP\_SERVER\_DOWN. This indicates that the LDAP libraries cannot establish an initial connection with the LDAP server. Either the LDAP server is down or the specified host name or port number is incorrect.

Action:
Examine the log for related messages. Check LDAP server health.

DIR047D Local Error.

Explanation:
An LDAP operation returned LDAP\_LOCAL\_ERROR. This indicates that the LDAP client has an error. This is usually a failed dynamic memory allocation error.

Action:
Examine the log for related messages. Check LDAP server health.

DIR048D Encoding Error.

Explanation:
An LDAP operation returned LDAP\_ENCODING\_ERROR. This indicates that the LDAP client encountered errors when encoding an LDAP request intended for the LDAP server.

Action:
Examine the log for related messages. Check LDAP server health.

DIR049D Decoding Error.

Explanation:
An LDAP operation returned LDAP\_DECODING\_ERROR. This indicates that the LDAP client encountered errors when decoding an LDAP response from the LDAP server.

Action:
Examine the log for related messages.

DIR050D Time Out.

Explanation:
An LDAP operation returned LDAP\_TIMEOUT. This indicates that the time limit of the LDAP client was exceeded while waiting for a result.

Action:
Examine the log for related messages. Check LDAP server health.

DIR051D Authentication Unknown.

Explanation:
An LDAP operation returned LDAP\_AUTH\_UNKNOWN. This indicates that the ldap\_bind or ldap\_bind\_s function was called with an unknown authentication method.

Action:
Examine the log for related messages.

DIR052D Filter Error.

Explanation:
An LDAP operation returned LDAP\_FILTER\_ERROR. This indicates that the ldap\_search function was called with an invalid search filter.

Action:
Examine the log for related messages.

DIR053D User Cancelled.

Explanation:
An LDAP operation returned LDAP\_USER\_CANCELLED. This indicates that the user cancelled the LDAP operation.

Action:
Examine the log for related messages.

DIR054D Parameter Error.

Explanation:
An LDAP operation returned LDAP\_PARAM\_ERROR. This indicates that an LDAP function was called with an invalid parameter value (for example, the ld parameter is NULL).

Action:
Examine the log for related messages.

DIR055D No Memory.

Explanation:
An LDAP operation returned LDAP\_NO\_MEMORY. This indicates that a dynamic memory allocation function failed when calling an LDAP function.

Action:
Examine the log for related messages. Check LDAP server health.

DIR056D Connect Error.

Explanation:
An LDAP operation returned LDAP\_CONNECT\_ERROR. This indicates that the LDAP client has either lost its connection or cannot establish a connection to the LDAP server.

Action:
Examine the log for related messages.

DIR057D Not Supported.

Explanation:
An LDAP operation returned LDAP\_NOT\_SUPPORTED. This indicates that the requested functionality is not supported by the client. For example, if the LDAP client is established as an LDAPv2 client, the libraries return this error code when the client requests LDAPv3 functionality.

Action:
Examine the log for related messages.

DIR058D Control Not Found.

Explanation:
An LDAP operation returned LDAP\_CONTROL\_NOT\_FOUND. This indicates that the client requested a control that the libraries cannot find in the list of supported controls sent by the LDAP server.

Action:
Examine the log for related messages.

DIR059D No Results Returned.

Explanation:
An LDAP operation returned LDAP\_NO\_RESULTS\_RETURNED. This indicates that the LDAP server sent no results. When the ldap\_parse\_result function is called, no result code is included in the server's response.

Action:
Examine the log for related messages.

DIR060D More Results to Return.

Explanation:
An LDAP operation returned LDAP\_MORE\_RESULTS\_TO\_RETURN. This indicates that more results are chained in the result message. The libraries return this code when the call to the ldap\_parse\_result function reveals that additional result codes are available.

Action:
Examine the log for related messages.

DIR061D Client Loop.

Explanation:
An LDAP operation returned LDAP\_CLIENT\_LOOP. This indicates the LDAP libraries detected a loop. Usually this happens when following referrals.

Action:
Examine the log for related messages.

DIR062D Referral Limit Exceeded.

Explanation:
An LDAP operation returned LDAP\_REFERRAL\_LIMIT\_EXCEEDED. This indicates that the referral exceeds the hop limit. The hop limit determines how many servers the client can hop through to retrieve data. For example, assume the following conditions:

The hop limit is two.

The referral is to server D, which can be contacted only through server B (1 hop) which contacts server C (2 hops) which contacts server D (3 hops)

With these conditions, the hop limit is exceeded and the LDAP libraries return this code.

Action:
Examine the log for related messages.

DIR063D No Such Object.

Explanation:
A call was made to the API routine to determine if a user has security equivalence to an object, but the object does not exist.

Action:
This can be normal. The application should handle this as appropriate.

DIR064D Invalid Argument.

Explanation:
An argument to a directory routine was not valid.

Action:
Examine the log for related messages.

DIR065D Revoked.

Explanation:
In a directory operation involving a User object, the user was found to have the login disabled flag set.

Action:
Examine the log for related messages and handle the event as appropriate.

DIR066W Unable to connect to LDAP. Component will retry connection periodically.

Explanation:
An attempt to connect to the configured LDAP server failed. The component issuing this message periodically retries the connection. When the connection is successful, the component continues processing.

Possible Cause:
The configured LDAP server is not started or is unreachable.

Action:
Make sure that an LDAP server is running at the configured LDAP host and port.

DIR067W Directory Services returned rc.

Explanation:
An LDAP error occurred. The LDAP return code is given by rc.

Action:
Check LDAP server health.

DIR068E LDAP Server server is not responding correctly. RC = rc.

Explanation:
The LDAP server specified by the LDAP Host and Port Driver object configuration parameter is not responding to a search request on the ASAM System container.

Action:
Restart the LDAP server and make sure LDAP services are available.

DIR069I LDAP Server is now responding to requests.

Explanation:
The LDAP server specified by the LDAP Host and Port Driver object configuration parameter is now up and responding correctly to requests.

Action:
None.
