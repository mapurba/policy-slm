# B.5 LDX0 Messages

Messages beginning with LDX0 are issued by the driver security system exit modules LDEVX01 and LDXRIX01 and the LDXSERV command.

LDX0001E There are old events on the LDX queue. Ensure that LDXLOGR is started.

Explanation:
The memory queue access routine in the security system exit found events in the memory queue that have been unprocessed for at least fifteen minutes. During normal operation, the change log started task processes events from the queue immediately.

Possible cause:
The change log started task is not running.

Action:
Ensure that the change log started task is running.

LDX0002I Unexpected RC xxxxxxxx during token processing routine.

Explanation:
An unexpected return code was received from z/OS name/token callable services by a driver component.

Possible cause:
Internal system error.

Action:
Collect diagnostic information and contact NetIQÂ® Technical Support.

LDX0103E Unable to parse command line.

Explanation:
The LDXSERV command contained invalid operands and was unable to prompt for correct information.

Action:
Correct the syntax of the LDXSERV command and reissue it. If the command was issued by the driver shim, collect diagnostic information and contact NetIQ Technical Support.

LDX0105E Internal error: description.

Explanation:
An unexpected error occurred in the LDXSERV command. The message contains a description of the problem.

Possible cause:
Internal error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.

LDX0106E Unable to open the log file.

Explanation:
LDXSERV was unable to open the change log data set.

Possible cause:
The user ID running the LDXSERV command does not have access to the change log data set.

Action:
Check the session log and message files for additional messages concerning the failure. If you are unable to determine and correct the cause of the error, collect diagnostic information and contact NetIQ Technical Support.

LDX0107E No preallocated log file and no valid environment.

Explanation:
The LDXSERV command was unable to find the change log data set because there was no LOGFILE DD statement and there was no valid LDX environment. The LDX environment is created when the security system exit is invoked for the first time after an IPL or when the change log started task first starts.

Action:
Ensure that you are logged on to a system where the driver is installed and that the security system exit has been properly installed and is active. If you are unable to determine and correct the cause of the error, collect diagnostic information and contact NetIQ Technical Support.

LDX0108E No preallocated log file and logger is not active.

Explanation:
The LDXSERV command was unable to find the change log data set because there was no LOGFILE DD statement and the change log started task was not active.

Action:
If you are unable to determine and correct the cause of the error, collect diagnostic information and contact NetIQ Technical Support.

LDX0109E Dynamic allocation failed for log file dsname, s99rc=rc, s99error=err.

Explanation:
The LDXSERV command was unable to dynamically allocate the change log data set. The dynamic allocation return code and reason codes are given in the message by rc and err respectively.

Dynamic allocation return codes and reason codes are documented in the IBM publication z/OS Programming: Authorized Assembler Services Guide.

Action:
If you are unable to determine and correct the cause of the error, collect diagnostic information and contact NetIQ Technical Support.
