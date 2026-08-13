# B.7 LDXS Messages

Messages beginning with LDXS are issued by the driver shim change log API.

LDXS000I nameversion Copyright 2006 Omnibond Systems, LLC. ID=code\_id\_string.

Explanation:
This message identifies the system component version.

Action:
No action is required.

LDXS001A Error executing script scriptName. The return code is returnCode, the reason code is reasonCode, the abend code is abendCode.

Explanation:
The driver shim could not execute scriptName.

Possible cause:
The script or command does not exist or is not valid.

Action:
Ensure that the driver shim is correctly configured to execute the command or script and that the command or script exists and is valid.

LDXS002A The change log service startup failed, rc = rc.

Explanation:
The change log API failed to initialize.

Possible cause:
The change log data set has not been initialized.

Possible cause:
The driver load library is not properly configured.

Possible cause:
The driver does not have the required rights to access the change log data set.

Action:
Ensure that all of the steps of the installation procedure have been performed correctly and have not subsequently been reversed.

LDXS003A Unable to create token, return code from IEANTCR is rc.

Explanation:
z/OS name/token callable services failed to create a token. The return code from IEANTCR is rc.

Possible cause:
Internal error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.
