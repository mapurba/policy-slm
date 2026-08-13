# ASC\_ADMINRSTPASSWD

Performs an administrative reset of a user's password. The new password is marked as being expired unless it is non-expiring.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_ADMINRSTPASSWD(ASCENV *asce, char *adminUser, char *adminPassword, char *user, char *newpass);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| adminUser | The Enterprise User ID of an administrative user with rights to change the target user's password. |
| adminPassword | The password of the administrative user ID. |
| user | The Enterprise User ID whose password is to be changed. |
| newpass | The new password for the user. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | Password changed |
| AS\_NOUSER | User inactive or not found in the Census |
| AS\_BADCLIENT | Local host not authorized to query the Core Driver |
| AS\_NOAGENT | No Core Driver could be contacted |
| AS\_NOAUTHENV | No environment has been established |
| AS\_INVALIDREQ | Call rejected by the Core Driver as not valid or not supported |
| AS\_INVALIDARGS | Invalid arguments supplied to the function |
| AS\_KEYEXPIRED | Old key rejected by the Core Driver because the expiration date has passed |
| AS\_INSUFFICIENTRIGHTS | Administrative user does not exist, administrative user does not have rights to change the password, or administrative user password not valid |

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

main(int argc, char *argv[])
{
  ASCENV *asce;
  ASCUSER ascu;
  char *adminUser, *adminPass, *user, *newpass;
  int rc;

  if (argc != 5) {
    fprintf(stderr, "usage: %s <adminUser> <adminPass> <user> <newpass>\n",
            argv[0]);
    exit(EXIT_FAILURE);
  }

  adminUser = argv[1];
  adminPass = argv[2];
  user      = argv[3];
  newpass   = argv[4];

  /* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* change the user's password */
  rc = ASC_ADMINRSTPASSWD(asce, adminUser, adminPass, user, newpass);
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
