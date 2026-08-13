# 3.1 Password Check for Login

A user logs in to a platform.

1. The user enters user ID and password information in response to a login prompt from the operating system, and the System Intercept receives control.
2. The System Intercept calls the Check Password API function (unless the user is excluded from processing based on the specifications in the platform configuration file).
3. The Platform Services Process uses its load-balancing algorithm to select a Core Driver for Authentication Services. (Platform Services establishes a connection with each Core Driver for Authentication Services upon startup.)
4. The Platform Services Process makes a Check Password request to Authentication Services.
5. Authentication Services obtains from the Census the eUser object whose name matches the user ID. Authentication Services gets from that eUser object the distinguished name of the corresponding User object (or Alias object) in eDirectory™.
6. Authentication Services checks the password against the object in eDirectory that corresponds to the eUser.
7. If the password is not already present in the eUser object, Authentication Services stores the password there for the Provisioning Manager to use for password replication.
8. Authentication Services returns the result of the Check Password request to the Platform Services Process.
9. Authentication Services notifies Audit Services, which records the action in the Audit Log.
10. The Platform Services Process returns the result to the System Intercept.
11. The System Intercept returns the result to the local security system.
