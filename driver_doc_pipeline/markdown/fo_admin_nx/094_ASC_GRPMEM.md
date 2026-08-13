# ASC\_GRPMEM

Obtains a list of all members of the given group and places it in the buffer supplied by the caller.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_GRPMEM(ASCENV *asce, char *object, char *buf, u_int size);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| object | The fully distinguished group name whose membership list is to be returned. |
| buf | The buffer in which the membership list is to be returned. Member names are separated by a new line ‘\n' character. The list is truncated and the call returns AS\_TOOSMALL if the buffer size cannot hold the entire list. |
| size | The size of the buffer you provided. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | Member list successfully returned |
| AS\_BADCLIENT | Local host not authorized to query the Core Driver |
| AS\_NOAGENT | No Core Driver could be contacted |
| AS\_NOAUTHENV | No environment has been established |
| AS\_INVALIDREQ | Call rejected by the Core Driver as not valid or not supported |
| AS\_INVALIDARGS | Invalid arguments supplied to the function |
| AS\_TOOSMALL | Size of the pre-allocated buffer is too small-list truncated |
| AS\_INVALIDOBJ | Specified object does not exist |
| AS\_KEYEXPIRED | Old key rejected by the Core Driver because the expiration date has passed |

## Remarks

The list is truncated, and the call returns AS\_TOOSMALL if the buffer size cannot hold the entire list. You can retry with a larger buffer.

You can use ASC\_SECEQUAL to see if an individual user is a member of a given group.

The groups a given user is a member of are included in the list returned by ASC\_LISTSEQV.

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

main(int argc, char *argv[])
{
  ASCENV *asce;
  char *group, buffer[2000];
  int rc;

  if (argc != 2) {
    fprintf(stderr, "usage: %s <group>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  group = argv[1];

/* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* Get group membership info */
  rc = ASC_GRPMEM(asce, group, buffer, sizeof(buffer));
  if (rc == AS_OK)
    printf("Members of group %s:\n%s\n", group, buffer);
  else if (rc == AS_TOOSMALL) {
    printf("Members of group %s:\n%s\n", group, buffer);
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

[ASC\_LISTSEQV](chdgfafi.html)

[ASC\_SECEQUAL](chdcaaic.html)

[ASC\_TERM](babeeidi.html)

[ASC\_STRERROR](babgiddd.html)
