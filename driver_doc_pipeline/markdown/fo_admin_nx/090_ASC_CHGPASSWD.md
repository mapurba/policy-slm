# ASC\_CHGPASSWD

Changes the password of a user.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_CHGPASSWD(ASCENV *asce, char *user, char *oldpass, char *newpass);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| user | The Enterprise User ID whose password is to be changed. |
| oldpass | The old password for the user. |
| newpass | The new password for the user. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | Password changed |
| AS\_NO | Old password is invalid |
| AS\_NOUSER | User inactive or not found in the Census |
| AS\_REVOKED | User's password is okay, but the user is disabled |
| AS\_INTRUDER | Intruder lockout is enabled for this user |
| AS\_PASSDUPLICATE | New password has been used previously |
| AS\_PASSTOOSHORT | New password is too short |
| AS\_BADCLIENT | Local host not authorized to query the Core Driver |
| AS\_NOAGENT | No Core Driver could be contacted |
| AS\_NOAUTHENV | No environment has been established |
| AS\_INVALIDREQ | Call rejected by the Core Driver as not valid or not supported |
| AS\_INVALIDARGS | Invalid arguments supplied to the function |
| AS\_KEYEXPIRED | Old key rejected by the Core Driver because the expiration date has passed |

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

main(int argc, char *argv[])
{
  ASCENV *asce;
  ASCUSER ascu;
  char *user, *oldpass, *newpass;
  int rc;

  if (argc != 4) {
    fprintf(stderr, "usage: %s <user> <oldpass> <newpass>\n",
            argv[0]);
    exit(EXIT_FAILURE);
  }

  user    = argv[1];
  oldpass = argv[2];
  newpass = argv[3];

  /* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* change the user's password */
  rc = ASC_CHGPASSWD(asce, user, oldpass, newpass);
  if (rc == AS_OK)
    printf("password has been changed\n");
  else if (rc == AS_NO)
    printf("password has not been changed\n");
  else
    printf("RC=%d, %s", rc, ASC_STRERROR(rc));
```

```
  /* now terminate the authentication environment */
  ASC_TERM(asce);
  return 0;
}
```

## See Also

[ASC\_INIT](babbgdde.html)

[ASC\_INIT\_EXT](babiiiag.html)

[ASC\_TERM](babeeidi.html)

[ASC\_STRERROR](babgiddd.html)
