# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

* [Driver Module](driver-configuration.html#b94psgk)
* [Driver Object Password](driver-configuration.html#b94psgy)
* [Authentication](driver-configuration.html#b94psh9)
* [Startup Option](driver-configuration.html#b94pshp)
* [Driver Parameters](driver-configuration.html#b94psi3)
* [ECMAScript (Designer Only)](driver-configuration.html#b94sjyt)
* [Global Configurations](driver-configuration.html#brxo3h7)

## A.1.1 Driver Module

The Driver Module section lets you change the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The name of the Java class is:

com.novell.nds.dirxml.driver.delimitedtext.DelimitedTextDriver

*Native:*
Used to specify the name of the .dll file that is instantiated for the application shim component of the driver. If this option is selected, the driver is running locally.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* Remote Loader Client Configuration for Documentation: Includes information on the Remote Loader client configuration when Designer generates documentation for the Delimited Text driver.
* Driver Object Password: Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

## A.1.2 Driver Object Password

*Driver Object Password:*
Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The Authentication section stores the information required to authenticate to the connected system.

*Authentication information for server:*
Displays or specifies the server that the driver is associated with.

*Authentication ID:*
Specify a user application ID. This ID is used to pass Identity Vault subscription information to the application.

Example: Administrator

*Authentication Context:*
Specify the IP address or name of the server that the application shim should communicate with.

*Remote Loader Connection Parameter:*
Used only if the driver is connecting to the application through the Remote Loader.

In Identity Console, the parameter to enter is hostname=xxx.xxx.xxx.xxx port=xxxx kmo=certificatename, where the host name is the IP address of the Remote Loader server and the port is the port the Remote Loader is listening on. The default port for the Remote Loader is 8090.

The kmo entry is optional. It is used only when an SSL connection exists between the Remote Loader and the Identity Manager engine.

Example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Application Password:*
Specify the password for the user object listed in the Authentication ID field.

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited.

Click Unlimited to set the file size to unlimited in Designer.

## A.1.4 Startup Option

The Startup Option section enables you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option applies only if the driver is deployed and was previously disabled. If this is not selected, the driver re-synchronizes the next time it is started.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment. For example, you might find the default Publisher polling interval to be shorter than your synchronization requires. Making the interval longer could improve network performance while still maintaining appropriate synchronization.

The driver parameters are presented by categories:

* [Driver Options](driver-configuration.html#brxo445)
* [Subscriber Options](driver-configuration.html#brxo525)
* [Publish Options](driver-configuration.html#brxo63c)

### Driver Options

*Driver parameters for server:*
Displays or specifies the server name or IP address of the server whose driver parameters you want to modify.

*Edit XML:*
Opens an editor so that you can edit the driver’s configuration file.

*Field Delimiter:*
Specifies the character that is used to delimit field values in the input files. It must be one character. You can also use the tab as the delimiter field value. Tab is represented as {tab}. The default is a comma.

If the values of any of the input fields contain this character, enclose the entire value in quotes to prevent it from being seen as a delimiter.

Changing this delimiter parameter to something other than a comma does not automatically change the delimiter character used in the output files when a Subscriber is used. To change the delimiter character in the output files, edit the Output Transform style sheet. The delimiter character is assigned to a variable at the beginning of that style sheet. For example, to change the delimiter, locate the <xsl:variable name="delimiter" select="','"/> line in the default style sheet and modify it appropriately.

*Field Names:*
Specifies a comma-separated list of attribute names that can be referred to in the Schema Mapping rule. In the input files, the fields of the records must correspond to the order and positioning of the names in this list.

For example, if you list eight field names in this parameter, each record of the input files should have eight fields separated by the field delimiter character. On Windows, see sample.csv in the delimitedtext/samples directory for an example. On Solaris and Linux, sample.csv is located in the /usr/lib/dirxml/rules/delim directory.

The default values are LastName, FirstName, Title, Email, WorkPhone, Fax, WirelessPhone, and Description.

*Object Class Name:*
Specifies the NetIQ eDirectory class name that should be used when creating new objects to correspond to input files.

*Allow Driver to Consume Its Own Output:*
Prevents you from inadvertently creating a situation in which the driver writes output files that are immediately read in again as input of the same driver.

The default is No. By default, the driver won't load if all the following conditions occur:

* You have both a Subscriber channel and a Publisher channel.
* The input and output directories are the same.
* The input and output file extensions are the same.

If you want to feed the output of the Subscriber channel into the input of the Subscriber channel as a way to detect Identity Vault events to trigger other changes in the Identity Vault, set this parameter to Yes. For example, to update the Full Name attribute when the Given Name, Surname, or Initials attributes are updated, set this parameter to Yes.

### Subscriber Options

*Output File Path:*
Specifies the directory on the local file system where output files will be created. An error occurs if this directory doesn’t exist. The default values are:

Windows: c:\csvsample\output

Solaris or Linux: /csvsample/output

*Output File Extension:*
When this parameter contains no value, the default Java character encoding for your locale is used.

Output files have a unique name that ends with the characters in the Output File Extension parameter. If the output files from a Subscriber channel are used as input files for the Publisher channel of another Delimited Text driver, the destination file extension must match the source file extension parameter of the second driver.

*Destination File Character Encoding (leave blank for default):*
To use an encoding other than the default for your locale, enter one of the canonical names from the [Supported Encoding table](http://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html).

The Publisher and Subscriber channels can use different character encodings.

*Maximum Number of Transactions per Output File:*
Specifies the maximum number of transactions that are written to a single output file. When the file transaction limit is reached, the file closes, and a new file is created for subsequent transactions. If you do not want to limit the number of transactions that can be written to a single file, leave this parameter blank or set it to zero.

For more information, see the next item, [Maximum Time in Seconds before Flushing All Transactions:](driver-configuration.html#brxnuj0).

*Enable/Disable Duplicate Records:*
To allow duplicate records to be written into the output files, change this parameter to Yes. By default, the parameter is set to No.

*Maximum Time in Seconds before Flushing All Transactions:*
If no new transactions have been written to the output file in the amount of time specified in this parameter, the file is closed. When new transactions need to be written, a new output file is created. If you do not want to limit the time that can pass before the output file is closed, leave this parameter blank or set it to zero.

*Time of Day (Local Time) to Flush All Transactions:*
If a value is supplied for this parameter, the current output file is closed at the specified time each day. Subsequent transactions are written to a new file. This parameter does not prevent the Maximum Number of Transactions per Output File or the Maximum Time in Seconds before Flushing All Transactions parameters from also acting as output file thresholds. If you use this parameter and only want one file per day, set the other two parameters to zero.

The format of this parameter can be HH:MM:SS (using the 24-hour clock) or H:MM:SS AM/PM. An hour is required, but the minutes and seconds are optional. Because the parameter assumes local time, any time zone information included in the value is ignored.

The previous three parameters (Maximum Number of Transactions per Output File, Maximum Time in Seconds before Flushing All Transactions, and Time of Day to Flush All Transactions) are all capable of acting as a threshold for the transaction size a file is able to grow to, or for the time that it remains open to accept new transactions.

As long as an output file is still open for writing by the Delimited Text driver, it should not be considered as finalized. Avoid opening the file in any other process until the driver closes the file. For this reason, one of the three previous parameters must be set to assure that output files don’t remain open indefinitely. To avoid this condition, if the driver detects that all three parameters are blank (or zero), it automatically sets the Maximum Number of Transactions per Output File to the value of 1.

### Publish Options

*Input File Path:*
The Publisher channel looks for new input files in the Input File Path, which is a directory on the local file system. Example paths:

* On Windows: c:\csvsample\input
* On Solaris and Linux: /usr/lib/dirxml/rules/delim

*Input File Extension:*
The extension used to designate input files (for example, csv).

*Source File Character Encoding (leave blank for default):*
When this parameter contains no value, the default Java character encoding for your locale is used.

To use an encoding other than the default for your locale, enter one of the canonical names from the [Supported Encoding table](http://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html).

If the Input File Extension parameter is .xml, the Source File Character Encoding can be indicated in one of two ways.

* If a value is indicated in the Source File Character Encoding parameter, it is used.
* If the parameter is blank, and if the XML document specifies an Encoding Declaration as described in the [W3C XML Recommendation](http://www.w3.org/TR/REC-xml#charencoding) in paragraph 4.3.3, the Encoding Declaration is handled by the XML parser in the Identity Manager engine.

  The Identity Manager XML parser handles the following character encodings:

  + UTF-8
  + UTF-16
  + ISO-8859-1
  + US-ASCII

*Rename File Extension:*
The Publisher channel uses only files that have the extension specified in the parameter. After the files have been processed, the value of the Rename File Extension parameter is appended to the filename, so the Publisher channel won’t try to process the same file again. If the value of the Rename File Extension parameter is left blank, the source file is deleted after it is processed.

*IMPORTANT:*If you change the default, use only characters that are valid in filenames on your platform. Invalid characters cause the rename to fail and the driver to reprocess the same file repeatedly.

*Polling Rate (in Seconds):*
When the Publisher channel has finished processing all source files, it waits the number of seconds specified in this parameter before checking for new source files to process.

*Publisher heartbeat interval:*
Configures the driver shim to send a periodic status message on the Publisher channel when there has been no Publisher traffic for the given number of minutes.

## A.1.6 ECMAScript (Designer Only)

Enables you to add ECMAScript resource files. The resources extend the driver’s functionality when Identity Manager starts the driver.

## A.1.7 Global Configurations

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
