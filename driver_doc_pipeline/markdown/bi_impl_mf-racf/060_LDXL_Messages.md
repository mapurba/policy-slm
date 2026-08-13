# B.6 LDXL Messages

Messages beginning with LDXL are issued by the change log started task.

LDXL000 LOGGING STARTED AT hh:mm:ss ON mm/dd/yyyy.

Explanation:
The change log started task has initialized.

Action:
Informational only. No action is required.

LDXL001 MESSAGE LOG DISABLED, SYSPRINT DD MISSING.

Explanation:
During initialization, the change log started task was unable to open the SYSPRINT DD statement.

The change log started task continues processing, but no messages are written to SYSPRINT.

Possible cause:
The SYSPRINT DD statement is missing from the JCL for the change log started task.

Action:
Ensure that a SYSPRINT DD statement is present in the JCL and that it defines a file that the change log started task can write to.

LDXL002 EXECUTE STATEMENT PARAMETERS: parm-values.

Explanation:
During initialization, the change log started task found the listed parameters present on the EXEC statement PARM parameter.

Action:
Informational only. No action is required.

LDXL003 START COMMAND PARAMETERS: parameters.

Explanation:
During initialization, the change log started task found the listed parameters present on the command line.

Action:
Informational only. No action is required.

LDXL004 STOP COMMAND RECEIVED.

Explanation:
An operator entered a STOP command for the change log started task. The change log started task ends.

Action:
Informational only. No action is required.

LDXL005 MODIFY COMMAND PARAMETERS: parameters.

Explanation:
An operator entered a MODIFY command for the change log started task with the listed parameters.

Action:
Informational only. No action is required.

LDXL006 UNRECOGNIZED CIBVERB TYPE: X'hh', COMMAND IGNORED.

Explanation:
During processing, the change log started task received a command input buffer (CIB) with a verb other than STOP or MODIFY. Processing continues.

Possible cause:
Internal system error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.

LDXL007 OPERATOR CANCEL DETECTED, ATTEMPTING NORMAL SHUTDOWN.

Explanation:
An operator has issued a CANCEL command without the DUMP parameter for the change log started task. The change log started task attempts a clean shutdown.

Action:
Wait for the change log started task to end. If the change log started task does not end within a reasonable amount of time, issue another CANCEL command specifying the DUMP parameter. If you are unable to determine and correct the cause of the error, collect diagnostic information and contact NetIQ Technical Support.

LDXL008 EVENT TRACING ENABLED.

Explanation:
An operator has issued a MODIFY command for TRACE ON to the change log started task.

Event tracing is turned on.

Action:
Informational only. No action is required.

LDXL009 EVENT TRACING DISABLED.

Explanation:
An operator has issued a MODIFY command for TRACE OFF to the change log started task.

Event tracing is turned off.

Action:
Informational only. No action is required.

LDXL010 MODIFY COMMAND IGNORED, INVALID OR MISSING PARAMETERS.

Explanation:
An operator has issued a MODIFY command to the change log started task, but the command parameters are not recognized.

The MODIFY command is ignored.

Action:
Reissue the MODIFY command with the intended parameters.

LDXL011 EVENT RC(rc) DATA: event\_data.

Explanation:
Event tracing is turned on and an event has been processed.

The return code from ProcessEvent is rc. The content of the event record is event\_data.

Processing continues.

Action:
Informational only. No action is required.

LDXL012 TERMINATING BECAUSE LOGGING ALREADY ACTIVE.

Explanation:
On startup, the change log started task has detected that another change log started task is already running.

This instance of the change log started task terminates.

To detect this condition, the change log started task enqueues exclusively on qname ldxlogr, rname #LDXENVIRONTOKEN when it initializes. If the ENQ macro fails, this message is issued. The change log started task dequeues this resource on shutdown.

Possible cause:
A START command for the change log started task has been issued more than once.

Action:
Do not start more than one instance of the change log started task at a time.

LDXL013 LOGGING TO DATASET: dsname.

Explanation:
The name of the change log data set in use is dsname.

Action:
Informational only. No action is required.

LDXL999 LOGGING ENDED AT hh:mm:ss ON mm/dd/yyyy.

Explanation:
The change log started task is ending.

Possible cause:
An operator entered a STOP command for the change log started task.

Action:
Informational only. No action is required.
