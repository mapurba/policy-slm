# ASC\_CHKPASSWD

Verifies the password of a user.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_CHKPASSWD(ASCENV *asce, char *user, char *pass, ASCUSER *ascu);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| user | The Enterprise User ID to be checked. |
| pass | The password to be checked for the user. |
| ascu | The ASCUSER structure (defined in ascauth.h) to be filled in by ASC\_CHKPASSWD() if the password is valid. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | Password is okay |
| AS\_NO | User ID/Password combination is invalid |
| AS\_NOUSER | User inactive or not found in the Census |
| AS\_REVOKED | User's password is okay, but the user is disabled |
| AS\_INTRUDER | Intruder lockout enabled for this user |
| AS\_BADCLIENT | Local host is not authorized to query the Core Driver |
| AS\_NOAGENT | No Core Driver could be contacted |
| AS\_NOAUTHENV | No environment has been established |
| AS\_INVALIDREQ | Call rejected by the Core Driver as not valid or not supported |
| AS\_INVALIDARGS | Invalid arguments supplied to the function |
| AS\_KEYEXPIRED | Old key rejected by the Core Driver because the expiration date has passed |

If an AS\_OK return code is returned, the following fields in the ASCUSER structure contain additional information about the authenticated user:

| <ascu>.pass.expire | Number of seconds until the password expires (or -1 if the password does not expire) |
| <ascu>.pass.interval | Password change interval in seconds (or -1 if the password does not expire) |

If an AS\_REVOKED code is returned, the following field in the ASCUSER structure contains additional information about the user:

| <ascu>.login.disabled | User disabled flag |

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

main(int argc, char *argv[])
{
  ASCENV *asce;
  ASCUSER ascu;
  char *user, *pass;
  int rc;

  if (argc != 3) {
    fprintf(stderr, "usage: %s <user> <password>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  user = argv[1];
  pass = argv[2];

  /* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* check the user's password */
  rc = ASC_CHKPASSWD(asce, user, pass, &ascu);
  if (rc == AS_OK)
    printf("password ok\n");
  else if (rc == AS_NO)
    printf("password invalid\n");
  else
    printf("RC=%d, %s", rc, ASC_STRERROR(rc));

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
