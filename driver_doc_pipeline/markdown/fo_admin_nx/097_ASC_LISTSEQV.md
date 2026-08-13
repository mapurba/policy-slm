# ASC\_LISTSEQV

Obtains a user's Security Equals attribute list and places it in the buffer supplied by the caller.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_LISTSEQV(ASCENV *asce, char *user, char *buf, u_int size);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| user | The Enterprise User ID whose Security Equals list is to be returned. |
| buf | The buffer in which the security equivalence list is to be returned. Object names are separated by a new line ‘\n' character. The list is truncated and the call returns AS\_TOOSMALL if the buffer size cannot hold the entire list. |
| size | The size of the buffer you provided. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | Security equivalence list successfully returned |
| AS\_NOUSER | User inactive or not found in the Census |
| AS\_BADCLIENT | Local host is not authorized to query the Core Driver |
| AS\_NOAGENT | No Core Driver could be contacted |
| AS\_NOAUTHENV | No environment has been established |
| AS\_INVALIDREQ | Call rejected by the Core Driver as not valid or not supported |
| AS\_INVALIDARGS | Invalid arguments supplied to the function |
| AS\_TOOSMALL | Size of pre-allocated buffer is too small-the list is truncated |
| AS\_INVALIDOBJ | Specified object does not exist |
| AS\_KEYEXPIRED | Old key rejected by the Core Driver because the expiration date has passed |

## Remarks

The list is truncated, and the call returns AS\_TOOSMALL if the buffer size cannot hold the entire list. You can retry with a larger buffer.

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

main(int argc, char *argv[])
{
  ASCENV *asce;
  char *object, buffer[2000];
  int rc;

  if (argc != 2) {
    fprintf(stderr, "usage: %s <object>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  object = argv[1];

/* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* Get security equivalence info */
  rc = ASC_LISTSEQV(asce, object, buffer, sizeof(buffer));
  if (rc == AS_OK)
    printf("Security equivalences of object %s:\n%s\n", object, buffer);
  else if (rc == AS_TOOSMALL) {
    printf("Security equivalences of object %s:\n%s\n", object, buffer);
    printf("** list was truncated because of lack of buffer space **\n");
  }
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
