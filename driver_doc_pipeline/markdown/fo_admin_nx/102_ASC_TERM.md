# ASC\_TERM

Terminates and frees the environment that was created by a call to ASC\_INIT() or ASC\_INIT\_EXT(). After the environment is terminated, no more calls to the Core Driver can be made without first issuing another ASC\_INIT() or ASC\_INIT\_EXT() call.

## Syntax

```
#include <ascauth.h>
```

```
void ASC_TERM(ASCENV *asce);
```

## Parameters

| asce | The environment item returned from the call to ASC\_INIT() or ASC\_INIT\_EXT(). |

## Return Values

No value is returned from this function.

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

[ASC\_INIT](babbgdde.html)

[ASC\_INIT\_EXT](babiiiag.html)
