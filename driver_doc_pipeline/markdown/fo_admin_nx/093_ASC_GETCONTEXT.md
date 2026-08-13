# ASC\_GETCONTEXT

Obtains a user's fully distinguished object name from the Census and copies it into the buffer supplied by the caller.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_GETCONTEXT(ASCENV *asce, char *user, char *buffer, u_int size);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| user | The Enterprise User ID. |
| buffer | The buffer that is to receive the context. The result is truncated and the call returns AS\_TOOSMALL if the buffer size cannot hold the entire result. |
| size | The length in bytes of the buffer. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | Context was found |
| AS\_NOUSER | User inactive or not found in the Census |
| AS\_BADCLIENT | Local host not authorized to query the Core Driver |
| AS\_NOAGENT | No Core Driver could be contacted |
| AS\_NOAUTHENV | No environment has been established |
| AS\_INVALIDREQ | Call rejected by the Core Driver as not valid or not supported |
| AS\_INVALIDARGS | Invalid arguments supplied to the function |
| AS\_TOOSMALL | Size of the pre-allocated buffer is too small-result truncated |
| AS\_KEYEXPIRED | Old key rejected by the Core Driver because the expiration date has passed |

## Remarks

The buffer is padded with nulls if needed.

The format of the returned login context is the simple dot form. For example: .jondoe.j.myorg

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

#define MAX_CONTEXT 512

main(int argc, char *argv[])
{
  ASCENV *asce;
  char *user, *context;
  int rc;

  if (argc != 2) {
    fprintf(stderr, "usage: %s <user>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  user    = argv[1];

  /* allocate buffer */
  context = (char *) malloc(MAX_CONTEXT);

  /* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* get the user's context */
  rc = ASC_GETCONTEXT(asce, user, context, MAX_CONTEXT);
  if (rc == AS_OK)
    printf("context is %s\n", context);
  else
    printf("RC=%d, %s", rc, ASC_STRERROR(rc));

  free(context);

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
