# ASC\_INIT

Reads the platform configuration file and initializes the environment so that calls can be made to a Core Driver. This function or ASC\_INIT\_EXT() must be called before any other API function.

## Syntax

```
#include <ascauth.h>
```

```
ASCENV *ASC_INIT(char *filename);
```

## Parameters

| filename | The name of the platform configuration file.  If you call ASC\_INIT() with a NULL in place of the filename parameter as in ASC\_INIT(NULL), the default is as follows:  *z/OS:* Always uses the ASCLIENT started task active configuration.  *IBM i:* /usr/local/ASAM/data/asamplat.conf  *Linux/UNIX:* /usr/local/ASAM/data/asamplat.conf |

## Return Values

Returns a pointer to the API environment item created upon success. If an error has occurred, NULL is returned.

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

main()
{
  ASCENV *asce;

  /* initialize the authentication environment */
  asce = ASC_INIT(NULL);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    exit(EXIT_FAILURE);
  }

  /* now you can make additional authentication calls  here */

  /* now terminate the authentication environment */
  ASC_TERM(asce);
  return 0;
}
```

## See Also

[ASC\_INIT\_EXT](babiiiag.html)

[ASC\_TERM](babeeidi.html)
