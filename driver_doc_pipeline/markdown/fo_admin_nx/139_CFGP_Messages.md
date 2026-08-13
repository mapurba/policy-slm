# D.10 CFGP Messages

Messages beginning with CFGP are issued by platform configuration file processing.

CFGP001E Invalid statement\_name statement.

Explanation:
The statement\_name statement is not valid.

Action:
Correct the statement.

CFGP002I There are no Core Drivers configured for provisioning. If you want to provision to this platform, specify a PROVISIONING statement.

Explanation:
No PROVISIONING statement was found in the platform configuration file.

Possible Cause:
None was coded.

Action:
If you want to provision users and groups to this platform, add a PROVISIONING statement to the platform configuration file.

CFGP003I There are no Core Drivers configured for authentication. If you want to use authentication redirection or APIs on this platform, specify an AUTHENTICATION statement.

Explanation:
No AUTHENTICATION statement was found in the platform configuration file.

Possible Cause:
None was coded.

Action:
If you want to allow authentication redirection for this platform, add an AUTHENTICATION statement to the platform configuration file.
