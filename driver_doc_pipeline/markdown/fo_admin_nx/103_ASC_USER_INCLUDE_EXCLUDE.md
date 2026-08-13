# ASC\_USER\_INCLUDE\_EXCLUDE

Determines if a given user matches an AS.USER.INCLUDE or AS.USER.EXCLUDE statement in the platform configuration file.

## Syntax

```
#include <ascauth.h>
```

```
int ASC_USER_INCLUDE_EXCLUDE(ASCENV *asce, char *user);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |
| user | The Enterprise User ID of the user to be checked. |

## Return Values

Returns one of the following integer values defined in ascauth.h:

| AS\_NOMATCH | The user does not match any INCLUDE/EXCLUDE statement. Because“AS.USER.INCLUDE \* is implicit in the absence of AS.USER.EXCLUDE \*, the user is included. |
| AS\_INCLUDED | User matches an AS.USER.INCLUDE statement. |
| AS\_EXCLUDED | User matches an AS.USER.EXCLUDE statement or an entry in the built-in standard exclude list. |
| AS\_NOAUTHENV | No environment has been established. |

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

rc = ASC_USER_INCLUDE_EXCLUDE(asce, userid);
if (rc == AS_NOMATCH)
  printf("%s does not match an Include or Exclude statement\n", userid);
else if (rc == AS_INCLUDED)
  printf("%s matches an Include statement\n", userid);
else if (rc == AS_EXCLUDED)
  printf("%s matches an Exclude statement\n", userid);
else
  printf("RC=%d, %s", rc, ASC_STRERROR(rc));
```

## See Also

[ASC\_INIT](babbgdde.html)

[ASC\_INIT\_EXT](babiiiag.html)
