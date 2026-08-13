# ASC\_SECEQUAL

Checks to see if a user has security equivalence to the specified object.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_SECEQUAL(ASCENV *asce, char *user, char *object);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| user | The Enterprise User ID to be tested. |
| Object | The fully distinguished object name to test the user for security equivalence. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | User has security equivalence to the specified object |
| AS\_NO | User does not have security equivalence to the object |
| AS\_NOUSER | User inactive or not found in the Census |
| AS\_BADCLIENT | Local host not authorized to query the Core Driver |
| AS\_NOAGENT | No Core Driver could be contacted |
| AS\_NOAUTHENV | No environment has been established |
| AS\_INVALIDREQ | Call rejected by the Core Driver as not valid or not supported |
| AS\_INVALIDARGS | Invalid arguments supplied to the function |
| AS\_INVALIDOBJ | Specified object does not exist |
| AS\_KEYEXPIRED | Old key rejected by the Core Driver because the expiration date has passed |

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

main(int argc, char *argv[])
{
  ASCENV *asce;
  char *user, *object;
  int rc;

  if (argc != 3) {
    fprintf(stderr, "usage: %s <user> <object>\n", argv[0]);
    exit(EXIT_FAILURE);
  }
  user   = argv[1];
  object = argv[2];

/* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* check for security equivalence */
  rc = ASC_SECEQUAL(asce, user, object);
  if (rc == AS_OK)
    printf("User has security equivalence\n");
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
