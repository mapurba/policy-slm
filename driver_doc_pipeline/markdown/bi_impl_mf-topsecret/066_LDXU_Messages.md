# B.8 LDXU Messages

Messages beginning with LDXU are issued by the log file utility LDXUTIL.

LDXU000I Log File Utility started on mm/dd/yyyy at hh:mm:ss.

Explanation:
The log file utility has initialized.

Action:
Informational only. No action is required.

LDXU001W Message log disabled, SYSPRINT DD missing.

Explanation:
During initialization, the log file utility was unable to open the SYSPRINT DD statement. The log file utility continues processing, but no messages are written to SYSPRINT.

Possible cause:
The SYSPRINT DD statement is missing from the JCL for the log file utility.

Action:
Ensure that a SYSPRINT DD statement is present in the JCL and that it defines a file that the log file utility can write to.

LDXU002I Execute statement parameters: parm-values.

Explanation:
During initialization, the log file utility found the listed parameters present on the EXEC statement PARM parameter.

Action:
Informational only. No action is required.

LDXU003E Open failed for log file.

Explanation:
The log file utility could not open the change log data set.

Possible cause:
The LOGFILE DD statement is missing from the JCL for the log file utility.

Action:
Ensure that a LOGFILE DD statement is present in the JCL and that it defines a data set that the log file utility can write to.

LDXU004I Log file blocksize: blksize.

Explanation:
The log file utility is initializing the change log data set with a blocksize of blksize.

Action:
Informational only. No action is required.

LDXU005I Log file blocks written: block-count.

Explanation:
While initializing the change log data set, the log file utility has written block-count blocks of empty records.

Action:
Informational only. No action is required.

LDXU006E Open failed for LOADIN file.

Explanation:
The log file utility load function could not open the LOADIN ddname.

Possible cause:
The LOADIN DD statement is missing from the JCL for the log file utility.

Action:
Ensure that a LOADIN DD statement is present in the JCL and that it defines a file that the log file utility can read.

LDXU007E Unrecognized or missing execute statement parameter.

Explanation:
The log file utility found an unknown parameter in the EXEC statement PARM parameter.

Processing ends.

Possible cause:
The EXEC statement PARM value is missing or does not contain one of the following functions:

* INITIALIZE
* DUMP
* LOAD

Action:
Correct the PARM value and resubmit the job.

LDXU008I Log file events loaded: event-count.

Explanation:
The log file utility load function has successfully loaded event-count events into the change log data set from the input file.

Action:
Informational only. No action is required.

LDXU009E Add event failed, error code code.

Explanation:
The log file utility load function was unable to add an event record to the change log data set. The LDXLADD LDXIOERR code was code.

Possible cause:
Internal system error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.

LDXU010E Read header failed, error code code.

Explanation:
The log file utility dump function was unable to read the header record of the change log data set. The LDXLGETE LDXIOERR code was code.

Possible cause:
Internal system error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.

LDXU011E Read event failed, error code code.

Explanation:
The log file utility dump function was unable to read an event record from the change log data set. The LDXLGETE LDXIOERR code was code.

Possible cause:
Internal system error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.

LDXU990I Open BDAM log succeeded.

Explanation:
The log file utility has initialized the change log data set with empty records and has successfully opened it to complete the initialization by updating the header information.

Action:
Informational only. No action is required.

LDXU991E Open BDAM log failed.

Explanation:
The log file utility has initialized the change log data set with empty records, but could not reopen it to complete the initialization by updating the header information.

Possible cause:
Internal system error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.

LDXU999I Log File Utility ended on mm/dd/yyyy at hh:mm:ss.

Explanation:
The log file utility has completed processing.

Action:
Informational only. No action is required.
