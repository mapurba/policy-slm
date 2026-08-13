# 10.4 Using Include and Exclude Configuration Statements

The various Include and Exclude statements can be used in the platform configuration file to determine which users are authenticated through Platform Services and which users are authenticated locally, and which users and groups are managed based on provisioning events and which users and groups are managed locally.

These statements allow the use of masking characters to specify a mask that can match more than one user ID or group.

For details about each Include and Exclude statement, see the corresponding statement description.

* [AM.GROUP.INCLUDE Statement / AM.GROUP.EXCLUDE Statement](beiffigc.html#chddjjje)
* [AM.USER.INCLUDE Statement / AM.USER.EXCLUDE Statement](beiffigc.html#chdiefij)
* [AS.USER.INCLUDE Statement / AS.USER.EXCLUDE Statement](beiffigc.html#chdgehfb)

Certain special users and groups are always processed locally unless you specify the IGNORESTANDARDEXCLUDES statement. For more information about this statement, see [IGNORESTANDARDEXCLUDES Statement](beiffigc.html#chdeccja). For a list of the users and groups in the standard exclude list, see [Standard Exclude List](babchigb.html).

## 10.4.1 Mask Characters and Examples

You can use masks to match more than one user ID or group in Include and Exclude statements. The following tables list mask characters and provide examples of masks.

*Table 10-2* Mask Characters

| Mask Character | Matches |
| \* | Any string of zero or more characters. The asterisk (\*) mask character can only be used at the end of a mask. |
| % | Any single character |
| ? | Any single character |
| \? | Any single character |
| \a | A single alphabetic character |
| \n | A single numeric character |
| \x | A single alphanumeric character |
| \s | A single @, #, $, or other OS-dependent non-alphanumeric special character |

*Table 10-3* Example Masks

| Mask | Matches |
| Z\* | ZEBRA ZULU ZED ZABRZE Z9 |
| Z\n\* | Z9 Z9WWW |
| \s\a\a\n\? | #BB29 #BB2A #AB9\_ |
| \aFF | AFF BFF CFF DFF EFF |
| \* | All strings |
| %%%%% | All five-character strings |
| ????? | All five-character strings |
| \?\?\?\?\? | All five-character strings |

## 10.4.2 Rules by Which Masks Are Matched Against User IDs and Groups

* The order in which INCLUDE and EXCLUDE statements are specified does not matter.
* If more than one mask matches a given user ID or group, the most specific mask is used.
* The mask is case-insensitive.
* Specifying the same mask on both an INCLUDE and an EXCLUDE statement is a syntax error.
* Unless EXCLUDE \* is coded, INCLUDE \* is assumed for each statement type. Certain special users and groups are excluded unless the IGNORESTANDARDEXCLUDES statement is specified. For details, see [IGNORESTANDARDEXCLUDES Statement](beiffigc.html#chdeccja).
* Do not code both an INCLUDE \* statement and an EXCLUDE \* statement of the same type.
