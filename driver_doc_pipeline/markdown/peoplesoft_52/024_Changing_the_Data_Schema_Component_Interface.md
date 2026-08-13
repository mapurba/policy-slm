# 6.2 Changing the Data Schema Component Interface

The driver is preconfigured to use the Component Interfaces (CIs) defined in the PSA. The APIs for these CIs have been compiled and combined into the dirxmlcomps.jar file. At run time, the driver imports the interfaces required to interact with the appropriate CI.

If the driver is configured to use different data schema CIs, the Java APIs for these CIs also need to be built, compiled, and archived into a .jar file. The directions for building the CI APIs is documented in the PeopleBooks > PeopleSoft Component Interfaces > Programming Component Interfaces in Java > Building APIs in Java section of the PeopleTools documentation. (It is not necessary to rebuild all of the Java CI APIs, just those that are associated with your new schema CI.) The compiled and archived .jar file should be placed in the DirXML /lib subdirectory with the psoftshim.jar file.

* [Building the PeopleSoft Java Component Interface API](change-data-schema-interface.html#bt36j57)
* [Compiling the Java CI API](change-data-schema-interface.html#bt36nvd)
* [Building the CI API JAR File](change-data-schema-interface.html#bt36pzn)

## 6.2.1 Building the PeopleSoft Java Component Interface API

1. In the PeopleTools Application Designer, select the Schema CI you want to build.
2. Click Build > PeopleSoft APIs. In this example, the DirXML\_SCHEMA01 CI is used.

   ![Building the PeopleSoft Java CI API](../graphics/peoplesoft-api-build.jpg "Building the PeopleSoft Java CI API")
3. In the Build PeopleSoft API Bindings dialog box, select the build option for the Java classes.
4. Select a target directory for the Java CI APIs (For our example, C:\newci).
5. For the Select APIs to Build prompt, click None to deselect all CIs.
6. Using the scroll area, select the CIs for which you wish to generate an API. Make sure you select all CIs that begin with the name of the desired interface. This example uses CompIntfc.DIRXML\_SCHEMA01 and CompIntfc.DIRXML\_SCHEMA01Collection.

   *IMPORTANT:*In addition to your schema CIs, you must always select the CompIntfc.CompIntfcPropertyInfo and CompIntfc.CompIntfcPropertyInfoCollection APIs. They are required in order to compile the schema APIs.
7. Click OK to generate the CI APIs. You might be prompted to create the target directory you specified.

   ![Build PeopleSoft API Bindings](../graphics/peoplesoft-api-bindings.jpg "Build PeopleSoft API Bindings")

   The Application Designer status window should show a Generating API Wrappers message with the selected CIs, and then a Done message.

## 6.2.2 Compiling the Java CI API

After the APIs are generated, they must be compiled. The files are in C:\newci\PeopleSoft\Generated\CompIntfc. For our example, there should be eight Java files in this directory, including the four selected CI API files and four associated Java Interface files. Change directories to the file location and compile the Java files, using an appropriate JVM with a classpath argument specifying the PeopleTools psjoa.jar file.

An example command line is:

javac -classpath c:\psoft\pt84\class\psjoa.jar \*.java

After a successful compile, there is a .class file for each .java file in the directory.

## 6.2.3 Building the CI API JAR File

The final step of the build process is the generation of a .jar file containing the compiled .class files. It is important that the full class path be generated with the JAR file, so the process must begin at the root of the CI API directory, C:\newci. From this directory, use the following command line:

jar cvf0M newci.jar PeopleSoft/Generated/CompIntfc/\*.class

This command builds a JAR file called newci.jar that is comprised of the previously compiled .class files and contains the full class paths. The contents of the file can be verified by using WinZIP or another appropriate tool.

*Figure 6-1* Building a New .jar File

![](../graphics/ps50image6_a.png)

If the driver is currently running, it must be stopped. If you are using the Remote Loader, the driver must be shut down. If you are using a local driver, it is also necessary to shut down eDirectory.

Copy the new JAR file to the same lib location with the driver components psoftshim.jar, dirxmlcomps.jar, and psjoa.jar. Restart eDirectory (if required) and the driver and Remote Loader.
