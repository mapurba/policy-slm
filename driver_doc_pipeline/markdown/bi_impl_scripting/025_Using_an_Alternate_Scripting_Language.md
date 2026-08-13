# 5.10 Using an Alternate Scripting Language

An alternative scripting language can be used by porting the globals, IDMLib, and other scripts to the alternative language. Porting requires a solid understanding of one of the provided languages (Bourne Shell, Perl and Microsoft VBScript and PowerShell) and the target language. The language should have facilities for executing programs and reading/writing to their standard input and output. The script language program must be able to be run from the command prompt.

To change the program the driver executes when running a script, modify the Script Command driver parameter. After the name of the program, you can include any needed command line parameters. To this string, the driver appends a space and the name of the Subscriber, Polling or Heartbeat script. For the Subscriber script, the full path to the event file and the full path to the Driver Parameter file are the next two parameters. For the Polling and Heartbeat scripts, the Driver Parameter file is the next parameter.

The event file contains the event document in XML format. On Windows, you must use the EventReader.exe program included with the Scripting driver to process this file. Running EventReader with the nvpairs option retrieves the event document as name/value pairs (the default). Using the xds option retrieves the event in its original XDS/XML format. On Linux and UNIX, events are submitted to scripts using shared memory. You must use the Shared Memory Helper, ussmh, to process these events. Running ussmh with the -xml option retrieves the XML document in its original XDS/XML format.

The Driver Parameter file contains name/value pairs for the driver parameters. See [UNIX Shell Developer Guide](b8n6ps6.html), [Perl Developer Guide](b8n7oqz.html), and [Microsoft VBScript Developer Guide](b8nlv23.html) for more information.

On the Publisher channel, you must use the Change Log tool (idmevent.exe on Windows and usclh on Linux/UNIX), to submit events to the driver.

The names of the Subscriber, Polling and Heartbeat scripts can be altered in the driver parameters.
