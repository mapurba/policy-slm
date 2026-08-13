# B.9 OAP Messages

Messages beginning with OAP are issued by driver components while communicating among themselves.

OAP001E Error in SSL configuration. Verify system entropy.

Explanation:
Entropy could not be obtained for SSL.

Possible Cause:
A source of entropy is not configured for the system.

Action:
Obtain and configure a source of entropy for the system.

OAP002E Error in SSL connect. Network address does not match certificate.

Explanation:
The SSL client could not trust the SSL server it connected to, because the address of the server did not match the DNS name or IP address that was found in the certificate for the server

Possible Cause:
The appropriate credentials are missing from the configuration.

Action:
If you cannot resolve the error, collect diagnostic information and call NetIQ Support.

OAP003E Error in SSL connect. Verify address and port.

Explanation:
A TCP/IP connection could not be made.

Possible Cause:
The server is not running.

Possible Cause:
The configuration information does not specify the correct network address or port number.

Action:
Verify that the server is running properly.

OAP004E HTTP Error: cause.

Explanation:
The username or password provided failed basic authentication.

Possible Cause:
The username or password is incorrect.

Action:
Verify that username is in full context (cn=user,ou=ctx,o=org or user.ctx.org) and that the password was correctly typed.

OAP005E HTTP Error: Internal Server Error.

Explanation:
The server experienced an internal error that prevents the request from being processed.

Possible Cause:
A secure LDAP server is not available.

Action:
Ensure that the LDAP server is available.

Action:
Ensure that the LDAP host and port are configured correctly.
