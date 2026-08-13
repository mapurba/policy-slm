# ASC\_RIGHTS

Checks the specified effective rights of one object over another for a specific attribute.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_RIGHTS(ASCENV *asce, char *obj1, char *obj2,
                char *attribute, char *rights);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| obj1 | The Enterprise User ID or fully distinguished object name whose effective rights are to be tested. |
| obj2 | The Enterprise User ID or fully distinguished object name for which access by obj1 is to be tested. |
| attribute | The name of an attribute of obj2 for which the effective rights of obj1 are requested. The special attribute names All Attributes Rights, Entry Rights, and SMS Rights can also be specified. |
| rights | The rights to test. The characters specified must be in the following set: [S,C,R,W,A]. These correspond to Supervisor, Compare, Read, Write, and Add Self. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_OK | User or object has the specified rights to the specified object attribute |
| AS\_NO | User or object does not have the specified rights to the specified object attribute |
| AS\_ATTRNOTFOUND | Specified attribute could not be found |
| AS\_INVALIDOBJ | Specified user not found in the Census or the specified object does not exist |
| AS\_INVALIDOBJLEN | Specified object exceeds maximum length |
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
  char *obj1, *obj2, *attr, *rights;
  int rc;

  if (argc != 5) {
    fprintf(stderr, "usage: %s <obj1> <obj2> \
            <attribute> <rights>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  obj1   = argv[1];
  obj2   = argv[2];
  attr   = argv[3];
  rights = argv[4];

/* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* check for rights */
  rc = ASC_RIGHTS(asce, obj1, obj2, attr, rights);
  if (rc == AS_OK)
    printf("User has rights\n");
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
