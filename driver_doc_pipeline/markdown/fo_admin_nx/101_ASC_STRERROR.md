# ASC\_STRERROR

Returns the error string for the specified ASC function error code.

## Syntax

```
#include <ascauth.h>
```

```
const char *ASC_STRERROR(int errnum);
```

## Parameters

| errnum | The error return value from a call to an ASC\_ function. |

## Return Values

Returns a static character string corresponding to the integer errnum value as defined in ascauth.h for ASC function error codes.

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

rc = ASC_CHKPASSWD(asce, userid, password, &ascu);
strcpy(status, ASC_STRERROR(rc));
printf("\n*** CHKPASSWD return code = %d (%s)\n", rc,status);
```
