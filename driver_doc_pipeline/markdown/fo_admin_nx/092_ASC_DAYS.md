# ASC\_DAYS

Converts an integer number of seconds into an integer number of days.

## Syntax

```
#include <ascauth.h>
```

```
long ASC_DAYS(long secs);
```

## Parameters

| secs | A number of seconds. |

## Return Values

Returns the integer number of days corresponding to the given number of seconds.

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

printf("*** CHKPASWD expire days=%ld, expire interval days=%ld\n",
       ASC_DAYS(ascu.pass.expire), ASC_DAYS(ascu.pass.interval));
```
