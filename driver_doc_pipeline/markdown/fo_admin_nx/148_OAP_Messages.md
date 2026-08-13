# D.19 OAP Messages

Messages beginning with OAP are issued by driver components when communicating among themselves.

OAP001E Error in SSL configuration. Check system for entropy.

Explanation:
Entropy could not be obtained for SSL.

Possible Cause:
A source of entropy is not configured for the system.

Action:
Obtain and configure a source of entropy for the system.

OAP002E Error in SSL connect. Network address does not match certificate.

Explanation:
The SSL client could not trust the SSL server it connected to because the address of the server did not match the DNS name or IP address that was found in the certificate for the server.

Possible Cause:
The Core Driver dn is missing from the driver XML.

Action:
If you cannot resolve the error, collect diagnostic information and call Support.

OAP003E Error in SSL connect. Check address and port.

Explanation:
A TCP/IP connection could not be made.

Possible Cause:
The server is not running.

The configuration information does not specify the correct network address or port number.

Action:
Verify that the server is running properly.

Correct the configuration.

OAP004E HTTP Error: cause.

Explanation:
The username/password provided for basic authentication failed.

Possible Cause:
The username or password was incorrect.

Action:
Check that username was in full context (cn=user,ou=ctx,o=org or user.ctx.org) and the password was correctly typed in.

OAP005E HTTP Error: Internal Server Error.

Explanation:
The server experienced an internal error that prevents the request from being processed.

Possible Cause:
A secure LDAP server is not available.

Action:
Ensure that the LDAP server is available.

Ensure that the LDAP Host and Port Driver object configuration parameter is specified correctly.
