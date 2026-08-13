# D.5 AUDG Messages

Messages beginning with AUDG are issued by Audit Services for general components.

AUDG001I component\_object started: Version version ID= code\_id\_string, Tree tree\_name, ASAM System Container system\_container, ASAM Master User master\_user, Command Line command\_line.

Explanation:
The component identified by component\_object has started. It is version version with code identification code\_id\_string. The directory tree used is tree\_name. The system container in use is system\_container. The Master User is master\_user. The command line used to start the component was command\_line.

Action:
None. Informational only.

AUDG002I component\_object ended. Start time was time\_stamp.

Explanation:
The component identified by component\_object has ended. It was started at time\_stamp.

Action:
None. Informational only.

AUDG003I component\_object Interval Start Time: interval\_start\_time: name = value.

Explanation:
The component identified by component\_object is reporting periodic statistical information. The measurement interval began at interval\_start\_time. The statistic name is name. The statistic value is value.

Action:
None. Informational only.

AUDG004I component\_object Interval Start Time: interval\_start\_time: Platform: platform\_object name = value.

Explanation:
The Core Driver identified by component\_object is reporting periodic statistical information for services to the platform identified by platform\_object. The measurement interval began at interval\_start\_time. The statistic name is name. The statistic value is value.

Action:
None. Informational only.

AUDG007E Unable to write to log file because of insufficient memory.

Explanation:
Insufficient memory was available to write a message to the log file. An attempt is made to write the message to the system log.

Possible Cause:
Insufficient memory.

Action:
Determine and correct the cause of the memory problem.

AUDG008E Unable to open log file filename.

Explanation:
Audit Services could not open filename in order to write a log message. An attempt is made to write the message to the system log.

Possible Cause:
The ASAM Directory driver configuration parameter is incorrect.

The Core Driver does not have the necessary file system rights.

Action:
Examine the system log. Determine and correct the cause of the problem.

AUDG009E Unable to write to logtype log file. Failed with errno errno.

Explanation:
Audit Services could not write a message to the logtype log. An attempt is made to write the message to the system log.

Action:
Examine the system log. Determine and correct the cause of the problem.

AUDG010E Unable to write to logtype log file index. Failed with errno errno.

Explanation:
Audit Services could not write a message to the logtype log because of a problem writing to the log index. An attempt is made to write the message to the system log.

Action:
Examine the system log. Determine and correct the cause of the problem.

AUDG011E Error logging message to log file. Internal error interr symbolicname.

Explanation:
Audit Services could not write a message to the log. The message is identified by symbolicname. An attempt is made to write the message to the system log.

Action:
Examine the system log. Determine and correct the cause of the problem.
