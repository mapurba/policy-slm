# ASC\_INIT\_EXT

Reads the platform configuration file and initializes the environment so that calls can be made to a Core Driver. This function or ASC\_INIT() must be called before any other API function. ASC\_INIT\_EXT() differs from ASC\_INIT() in that you can provide a buffer into which the API places error messages if the API environment cannot be initialized.

## Syntax

```
#include <ascauth.h>
```

```
ASCENV *ASC_INIT_EXT(char *filename, char *error_msg, size_t size);
```

## Parameters

| filename | The name of the platform configuration file.  If you call ASC\_INIT\_EXT() with a NULL in place of the filename parameter as in ASC\_INIT\_EXT(NULL, buffer, BUFSIZE), the default is  /usr/local/ASAM/data/asamplat.conf |
| error\_msg | A buffer you provide into which an error message can be placed if the environment cannot be initialized. |
| size | The size of the error\_msg buffer you have provided. |

## Return Values

Returns a pointer to the environment item created upon success. If an error has occurred, NULL is returned, and a descriptive error message is placed into the error\_msg buffer.

## Example

```
#include <stdio.h>
#include <stdlib.h>
#include <ascauth.h>

#define BUFSIZE 256

main()
{
  ASCENV *asce;

  /* initialize the authentication environment */
  /*   allocate buffer */
  buffer = (char *) malloc(BUFSIZE);
  asce = ASC_INIT_EXT(NULL, buffer, BUFSIZE);
  if (asce == NULL) {
    fprintf(stderr, "Error: cannot initialize authentication environment\n");
    fprintf(stderr, "  %s \n", buffer);
    exit(EXIT_FAILURE);
  }

  /* now you can make additional authentication calls  here */

  /* now terminate the authentication environment */
  ASC_TERM(asce);
  return 0;
}
```

## See Also

[ASC\_INIT](babbgdde.html)

[ASC\_TERM](babeeidi.html)
