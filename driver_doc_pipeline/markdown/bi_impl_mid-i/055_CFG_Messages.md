# B.1 CFG Messages

Messages beginning with CFG are issued by configuration file processing.

CFG001E Could not open configuration file filename.

Explanation:
Could not open the configuration file.

Possible cause:
The file does not exist.

Possible cause:
You don’t have permission to read the file.

Action:
Ensure that the configuration file exists at the correct location and that you have file system rights to read it.

CFG002E Error parsing configuration file line: <configline>.

Explanation:
The line is not formatted as a valid configuration statement and cannot be parsed.

Action:
Correct the line in the configuration file.

CFG003W Configuration file line was ignored. No matching statement name found: <configline>.

Explanation:
This line is formatted as a valid configuration file statement, but the statement is not recognized. The line is ignored.

Possible cause:
The statement is incorrectly typed or the statement name is used only in a newer version of the software.

Action:
Correct the statement.

CFG004E Error parsing configuration file line. No statement name was found: <configLine>.

Explanation:
Could not find a statement name on the configuration line.

Action:
Correct the line in the configuration file to supply the required statement.

CFG005E A required statement statement\_id is missing from the configuration file.

Explanation:
The statement\_id statement was not specified in the configuration file, but is required for the application to start.

Action:
Add the required statement to the configuration file.
