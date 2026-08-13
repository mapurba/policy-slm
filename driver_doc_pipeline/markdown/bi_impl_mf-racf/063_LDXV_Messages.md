# B.9 LDXV Messages

Messages beginning with LDXV are issued by the IDMGETV and IDMSETV commands.

LDXV001E IDM token not present.

Source:
IDMGETV command, IDMSETV command

Explanation:
The data areas that the driver shim sets up for the IDMGETV or IDMSETV command before calling a script are not present.

Possible Cause:
The command was not called by the driver shim.

Action:
Ensure that the commands are invoked by the driver shim. They are not intended to be used outside of this environment.

LDXV002E Unable to parse command.

Source:
IDMGETV command, IDMSETV command

Explanation:
The TSO parsing routine detected an error in the command and was unable to prompt for a correction.

Possible Cause:
The command had a syntax error. It was not called from an interactive session and could not prompt for a correction.

Action:
Examine the associated messages from the TSO parsing routine that describe the error. Correct the operands of the command.

LDXV003E Error from TSO service routine IKJCT441, RC <rc>.

Source:
IDMGETV command

Explanation:
TSO routine IKJCT441 detected a problem and ended with return code rc (decimal).

Possible Cause:
Internal error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.

LDXV004W <variablename> contains invalid characters to be a REXX variable.

Source:
IDMGETV command, IDMSETV command

Explanation:
The command was directed to create the variable named in the message, but the variable name contained characters that are not acceptable in a REXX variable name. The acceptable characters are as follows:

| Alphanumeric characters | A–Z, a–z, 0–9 |
| “At” sign | @ |
| Octothorpe | # |
| “Dollar” sign | $ |
| Exclamation mark | ! |
| Question mark | ? |
| Period | . |
| Underscore | \_ |

Possible Cause:
The variable named in the message was defined in eDirectory™ using one or more characters not in the list of acceptable characters. For example, some attribute names might contain spaces.

Action:
Use the driver mapping rules to rename the variable to a name that meets the REXX naming requirements.

LDXV005E IDMGETV was not called from a CLIST or REXX exec.

Source:
IDMGETV command

Explanation:
The IDMGETV command must be called from a REXX exec, because it creates and manipulates REXX variables.

Possible Cause:
The command was not called from within the REXX environment.

Action:
Call the command from within the REXX environment.

LDXV006E GROUP or USER list required.

Source:
IDMSETV command

Explanation:
The IDMSETV command requires either the GROUP(grouplist) or USER(userlist) operand.

Possible Cause:
Use one of the required operands.

Action:
Correct the operands of the command.

LDXV007E GROUP and USER operands are mutually exclusive.

Source:
IDMSETV command

Explanation:
The command found both the USER and GROUP operands on the command line. These are mutually exclusive.

Possible Cause:
Both GROUP and USER were specified on the IDMSETV command.

Action:
Correct the command.

LDXV008E Error returned from <service>: RC <rc>.

Source:
IDMGETV command, IDMSETV command

Explanation:
The IBM service routine service returned the return code rc (decimal).

Possible Cause:
Internal error.

Action:
Collect diagnostic information and contact NetIQ Technical Support.
