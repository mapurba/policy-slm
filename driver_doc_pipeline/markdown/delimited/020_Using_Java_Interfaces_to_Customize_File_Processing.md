# 8.0 Using Java Interfaces to Customize File Processing

Java interfaces enable you to customize file processing by using Java classes that you write:

* InputSorter
* InputSource
* PreProcessor
* PostProcessor

These interfaces enable you to add extensions, which are optional. The driver continues to function as before without extensions. However, if you want to directly modify the behavior of the driver, but you have been unable to make these modifications from a style sheet or DirXML Script, extending the Delimited Text driver can be useful.

By using Java classes that you write, you can use the interfaces to customize the publish and subscribe processes in the following ways:

*Table 8-1* Customizing the Publish and Subscribe Processes

| Process | Interface | Description |
| Publish | InputSorter | Defines the processing order of multiple input files.  The system where your driver is installed determines the default processing order. For example, files on an NT system are processed in alphabetical order. You can use the InputSorter to impose the processing order that you require. |
| Publish | InputSource | Provides data other than the files in the default location for the driver to process.  For example, you can check an FTP server for input files and then transfer the files to the local file system for processing. |
| Publish | PreProcessor | Ties data manipulation required to prepare input files for driver processing directly to the driver.  Before this interface was available, preprocessing was independent of the driver. You could create a separate application that monitored another directory for input files, modify the files in some way, and then copy the files to the input directory of the driver. By creating a class that implements the PreProcessor, you can do this type of preprocessing more directly. |
| Subscribe | PostProcessor | Ties data manipulation required by the application, consuming Identity Vault output directly to the driver. |

These enhancements to the driver require Java programming. To implement this functionality, complete the following processes:

* [Creating a Java Class](create-java-class.html)
* [Creating a Java .jar File](create-java-jar-file.html)
* [Configuring the Driver to Use the New Class](configure-driver-new-class.html)
