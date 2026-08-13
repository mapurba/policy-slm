# D.3 AGT Messages

Messages beginning with AGT are issued by the Core Driver for Authentication Services.

AGT001I Password Migration Mode is enabled.

Explanation:
Password Migration Mode is enabled for this Core Driver. This mode is enabled by setting the Migration Password parameter for the Driver object.

Action:
None. Informational only.

AGT002I < thread\_id> Processing compatibility mode request from ipAddress on port portNumber.

Explanation:
A new platform request identified by thread\_id has been started from ipAddress on portNumber.

Action:
None. Informational only.

AGT003E < thread\_id> Error reading from socket connected to ip\_address.

Explanation:
The Core Driver was unable to read data from the socket connection. The current request is discarded.

Possible Cause:
The platform might have dropped the connection.

Action:
If this error occurs frequently, check for network connectivity problems between the platform and the Core Driver.

AGT004I < thread\_id> Compatibility mode request has ended.

Explanation:
The platform request identified by thread\_id has ended.

Action:
None. Informational only.

AGT005E < thread\_id> Invalid request was received from the platform.

Explanation:
The platform sent an invalid request to the Core Driver.

Possible Cause:
The platform is configured with an invalid DES key.

The platform host is running a down-level version of the platform software.

Action:
Ensure that the DES key in the Platform Configuration file matches the DES key for the Platform object in eDirectory™.

AGT006W < thread\_id> Request received from an unauthorized platform ip\_address.

Explanation:
A request was received from a platform that is not known. The request is discarded.

Possible Cause:
The IP address or host name of the platform does not match the IP addresses or host names listed for the Platform object in eDirectory.

Someone might be attempting to breach security.

Action:
Use the Web interface to add the network address for the platform to its corresponding Platform object in eDirectory if appropriate.

AGT007E < thread\_id> DES key has expired for Platform ip\_address.

Explanation:
The DES key being used by the platform on IP address ip\_address has expired. The request is discarded.

Possible Cause:
A new DES key was set for the platform using the Web interface, but the platform has not been changed to use the new DES key. The old DES key is expired and unusable.

Action:
Update the Platform Configuration file with the new DES key.

AGT008W < thread\_id> Response to request\_type request from ip\_address for objectDN is: answer.

Explanation:
A request was received from ip\_address by the Core Driver for request\_type and was sent the response answer.

Action:
None. Informational only.

AGT009W < thread\_id> Response to request\_type request from ip\_address is: answer.

Explanation:
A request was received by the Core Driver for request\_type and was sent the response answer.

Action:
None. Informational only.

AGT010E < thread\_id> Error writing to socket connected to ip\_address.

Explanation:
The Core Driver was unable to write data to the socket connection for ip\_address. The current request is discarded.

Possible Cause:
The platform might have dropped the connection.

Action:
If this error occurs frequently, check for network connectivity problems between the platform and the Core Driver.

AGT018E Password replication for user user failed with error code code.

Explanation:
The Core Driver could not store its encrypted copy of the password to eDirectory. No more attempts are made to do so. The user's password is not replicated to any platforms.

Possible Cause:
For ePassword operation, the most likely cause is that the LDAP server specified in the driver parameters is down or misconfigured. For more information, see message AGT023E.

Action:
See message AGT023E.

AGT023E Write of ePassword for user user failed with error code code. (LDAP server: server: port).

Explanation:
The Core Driver could not store the user's ePassword in eDirectory. Without an ePassword, the user cannot be replicated to platforms that require password synchronization. The Core Driver might be able to recover from this problem.

Possible Cause:
The LDAP server specified in the driver configuration parameters is down or misconfigured. This generally results in error codes 80 or 81.

Action:
Verify that the LDAP server specified in the driver parameters is the correct server.

Verify that the LDAP server specified in the driver parameters is running and configured properly. For information about the LDAP server, refer to your eDirectory documentation.

Verify that the computer running the Core Driver can communicate with the LDAP server using TCP/IP.

Check the eDirectory replication status.

AGT025I Password Change Validation Exit Registered using function from library library.

Explanation:
A Password Change Validation Exit was registered using the indicated function and library.

Action:
None

AGT026E Could not open library library for Password Change Validation Exit.

Explanation:
The Core Driver could not open the library specified for the Password Change Validation Exit.

Action:
Make sure the library exists in the location you specified.

AGT027E Could not import function function from library library for Password Change Validation Exit.

Explanation:
The Core Driver could not import the specified function from the specified library for the Password Change Validation Exit.

Action:
Make sure the function is exported from the library.

AGT028E The Password Change Validation Exit has rejected the password change for user user. Reason: reason.

Explanation:
The registered Password Change Validation Exit has applied a user-defined set of rules to the attempted password change and determined that the new password is not valid. A reason is displayed if the exit provided one.

Action:
None.
