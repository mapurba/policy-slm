# B.2 Customizing ImageFile InputSource

You can fine-tune the behavior of the ImageFile InputSource by setting the parameters that are discussed in this section. Parameters are passed to the InputSource as a string.

The string must be in the following format:

<name1>=<value1>;<name2>=<value2>;<name n>=<value n>

Sample:

srcdir=c:\temp\dirxml;renameto=bak;delblacklist=false;renblacklistto=ignore;minsize=1000;debug=true

Use the following values to configure the ImageFile properties:

*Table B-2* ImageFile InputSource Parameters

| Parameter | Required | Default | Purpose |
| srcdir | yes |  | Directory where the image files are stored. |
| minsize | no | -1 | Minimum size of the file to be processed. Number is the number of bytes. Set the value to -1 to disable the filter. |
| maxsize | no | -1 | Maximum size of the file to be processed, in bytes. Set the value to -1 to disable the filter. |
| minwidth | no | -1 | Minimum width of the image to be processed (number of pixels). Set the value to -1 to disable the filter. |
| maxwidth | no | -1 | Maximum width of the image to be processed (number of pixels). Set the value to -1 to disable the filter. |
| minheight | no | -1 | Minimum height of the image to be processed (number of pixels). Set the value to -1 to disable the filter. |
| delim | no | # | Delimiter to be used in the created input files. The same delimiter must be configured in the driver parameters for the Delimited Text driver. |
| consolidate | no | true | Set consolidate to True to produce only one input file for all images. Set consolidate to False to produce an input file for each image. |
| renameto | no |  | Specify the suffix you want to be appended to the image files after processing. By default, the renameto parameter is not set and the files are deleted after processing. |
| debug | no | false | Set to True to turn on debug messages. Debugging is turned off by default. |
| delblacklist | no | true | Set to False to prevent deletion of the blacklist. The blacklist consists of all the image files that have been filtered out. By default, the blacklist is deleted. |
| renblacklistto | no |  | Specify any file suffix you want blacklist image files to be renamed to. By default the renameto parameter is not set and the processed files are handled according to the delblacklist parameter. |
