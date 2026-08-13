# B.10 NXPAM Messages

Messages beginning with NXPAM are issued by the driver PAM module.

NXPAM000I nameversion Copyright 2006 Omnibond Systems, LLC. ID=code\_id\_string.

Explanation:
This message identifies the system component version.

Action:
No action is required.

NXPAM001W Password Change was not submitted for user.

Explanation:
When a user changes the password using a PAM-enabled application, the PAM module for the driver submits the password change to the change log. An error occurred that prevents the change being submitted to the change log.

Possible cause:
If the PAM module is running locally on the same system with the driver shim, certain files or directories could be missing, such as the /usr/local/nxdrv/keys/lpwd1f40 driver shim key file or the /usr/local/nxdrv/changelog change log directory.

Possible cause:
If the PAM module is running remotely from the system with the driver shim, the PAM module could not connect to the driver shim. This could be caused by a network problem or a problem with the driver shim.

Possible cause:
The PAM module might not be configured properly.

Action:
Ensure that the PAM module is installed and configured correctly.

Action:
Ensure that the driver shim is running and healthy.

Action:
If the PAM module is running remotely, verify connectivity to the driver shim system.
