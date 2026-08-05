# B.1 Using the ImageFile InputSource Extension

The ImageFile InputSource extension allows you to easily import GIF, JPG, and PNG images into eDirectory. The InputSource reads the image files from a specified directory, transforms them to a Base64-encoded string, and passes this string to the driver shim as if it were a normal delimited text string, together with additional information about the image, such as file size, file name, and modification date.

*Figure B-2* InputSource Extension

![](../graphics/accman_001_a.png)

Standard rules and style sheets, as used for other implementations of the Delimited Text driver, can be used to further process the image data. The image itself is meant to be stored in an attribute of syntax octet string or stream.

* [Installing the ImageFile InputSource Extension](b6f4txa.html#b6fwzdz)
* [Configuring the Driver for the ImageFile InputSource Extension](b6f4txa.html#bbtv5l0)

## B.1.1 Installing the ImageFile InputSource Extension

The ImageFile InputSource extensions are installed when you install Identity Manager and select the Delimited Text driver. The extensions are configured in the driver parameters. Each extension takes a parameter string that is specified in the driver parameters and passes it to the extension during initialization. Extensions define their own format for the parameter string.

The extensions are included in the DelimitedTextUtil.jar file.

## B.1.2 Configuring the Driver for the ImageFile InputSource Extension

Use the following table to customize your driver for the ImageFile extension.

*Table B-1* Delimited Text Driver Parameters

| Driver Parameter | XML Name | Sample Values | Purpose |
| Field Delimiter | field-delimiter | # | Indicates the character that is used to delineate field values in the input files. It must be one character.This must be set to the same character as the delim extension parameter or, if delim is not specified, set it to #. |
| Field Names (Field1, Field2, Field3…) | field-names | idx name prefix suffix size modified pic64 | A comma-separated list of attribute names that can be referred to in the Schema Mapping rule. In the input files, the fields of the records must correspond to the order and positioning of the names in this list. For example, if you list eight field names in this parameter, then each record of the input files should have eight fields separated by the field delimiter character.The extension defines which fields it supports. The fields as listed here are the ones delivered by the extension. Altering the fields can cause malfunctions. |
| InputSource Class | input-source | com.novell.nds.dirxml.driver.delimitedtext.imagefile.ImageFileInputSource | Class name of the input source. |
| InputSource init string | input-source-params | srcdir=c:\temp\dirxml;renameto=bak;delblacklist=false;renblacklistto=ignore;minsize=1000;debug=true | InputSource initialization parameters. For more information, see [Configuring the Driver for the ImageFile Extension](bbtw2zk.html#bbtw6xp). |
