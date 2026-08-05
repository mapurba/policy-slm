# B.4 Customizing the ImageFile Extension

You can fine-tune the behavior of the ImageFile extension by setting parameters. Parameters are passed to the PostProcessor as a string.

The string must be in the following format:

<name1>=<value1>;<name2>=<value2>;<name n>=<value n>

Sample:

destdir=/var/novell/idm/users/output/images;format=png;debug=true

Use the following table to customize the ImageFile extension.

*Table B-4* ImageFile Custom Parameters

| Parameter | Required | Default Value | Purpose |
| destdir | yes |  | Directory where the image files are stored. |
| delim | no | # | Used when parsing the output files. The same delimiter should be configured in the Delimited Text driver parameters. |
| format | no | png | Image format. |
| debug | no | false | Set the value to True to turn on debugging. Debugging is off by default. |
