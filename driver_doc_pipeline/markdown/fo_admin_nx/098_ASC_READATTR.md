# ASC\_READATTR

Returns the value of the specified single-valued attribute for the specified object.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_READATTR(ASCENV *asce, char *object, char *attribute,
                   char *buffer, u_int bufsize);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| object | The Enterprise User ID or fully distinguished object name of the object whose attribute value is to be returned. |
| attribute | The single-valued attribute whose value is to be returned for the object. Only the Home Directory attribute of a User object is supported at this time. |
| buffer | The buffer in which the object's attribute value is to be returned. The results are truncated and the call returns AS\_TOOSMALL if the buffer size cannot hold the entire attribute value. |
| bufsize | The size of the buffer you provided. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | Attribute value has been placed in the buffer successfully |
| AS\_BADCLIENT | Local host not authorized to query the Core Driver |
| AS\_ATTRNOTFOUND | Attribute does not exist for the specified object |
| AS\_NOAGENT | No Core Driver could be contacted |
| AS\_NOAUTHENV | No environment has been established |
| AS\_INVALIDREQ | Call rejected by the Core Driver as not valid or not supported |
| AS\_INVALIDARGS | Invalid arguments supplied to the function |
| AS\_TOOSMALL | Size of the pre-allocated buffer is too small-results are truncated |
| AS\_INVALIDOBJ | Specified object does not exist |
| AS\_KEYEXPIRED | Old key rejected by the Core Driver because the expiration date has passed |

## Remarks

The results are truncated, and the call returns AS\_TOOSMALL if the buffer size cannot hold the entire attribute value. You can retry with a larger buffer.

## Limitations

Only the Home Directory attribute of a User object is supported at this time.

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

main(int argc, char *argv[])
{
  ASCENV *asce;
  char *user, buffer[2000];
  int rc;

  if (argc != 2) {
    fprintf(stderr, "usage: %s <UserObjectFDN>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  user = argv[1];

/* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* Get User object's home directory info */
  rc = ASC_READATTR(asce, user, "HOME DIRECTORY", buffer, sizeof(buffer));
  if (rc == AS_OK)
    printf("Home Directory for User object %s:\n%s\n", user, buffer);
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
