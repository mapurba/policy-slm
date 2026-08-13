# 9.3 Planning for Authentication Services

When planning for Authentication Services, include the following considerations:

* If you don’t plan to use Authentication Services to authenticate system users or provide password change information to Core Drivers, you don’t need to install the System Intercept.
* If you don't plan to use the AS Client API or Authentication Services, you don't need to run the Platform Services Process.
* If your use of Authentication Services and the AS Client API is infrequent and does not require high performance, consider using the DIRECTTOAUTHENTICATION statement in the platform configuration file. This configuration does not use the Platform Services Process. For details about the DIRECTTOAUTHENTICATION statement, see [DIRECTTOAUTHENTICATION Statement](beiffigc.html#chdecfdc).
* You might need to permanently exclude some users from Authentication Services processing. You might want to phase in your implementation by using a subset of your users to start with. For details about excluding users from Authentication Services processing, see [AS.USER.INCLUDE Statement / AS.USER.EXCLUDE Statement](beiffigc.html#chdgehfb).
* You must specify which Core Drivers are used for Authentication Services. You might want to establish different preference groups for sets of these Core Drivers based on their network connectivity or other issues. For details, see [AUTHENTICATION Statement](beiffigc.html#brg3ydt).
