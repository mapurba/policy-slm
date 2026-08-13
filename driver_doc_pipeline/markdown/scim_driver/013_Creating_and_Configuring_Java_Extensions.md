# 3.1 Creating and Configuring Java Extensions

In some cases, the connected application could implement the SCIM interface to exchange information in a method that might deviate from the RFC standards. To create Java extensions, the modifier class file, for example <SFDocModifier.jar> must be available in the path /opt/novell/eDirectory/lib/dirxml/classes.

You can modify the following requests and responses using Java extensions:

* Subscriber request document to the connected application.
* Subscriber response document for Identity Manager.
* Publisher request document sent through the Publisher channel to the connected application.
* Publisher response document received through the publisher channel to Identity Manager.

You should name your modifier class using any Java package and a class name that is convenient for your environment.

For example, if you are writing your own class that implements the DocumentModifiers interface, and you named your class as MyDocumentModifiers within a package called com.microfocus.idm, then you perform the following steps to compile .jar, and deploy your class:

1. Prepare your environment.

   Make sure that you have a current Java Development Kit (JDK) installed on your computer. Visit the [Java Web Site](https://www.oracle.com/java/technologies/) if you need to download one.
2. Gather your source code in the proper directory structure as defined by your package naming.

   In the above example, navigate to com > microfocus > idm > MyDocumentModifiers.java to find the source code file.
3. Make sure you have the jar files you need to compile your class.

   At a minimum, you need SCIMUtils.jar, available in:

   * Linux path: /opt/novell/eDirectory/lib/dirxml/classes
   * Windows path: C:\NetIQ\IDM\NDS\lib

   Also, if you are using XML documents within your class, you also need nxsl.jar, that is available in /opt/novell/eDirectory/lib/dirxml/classes.
4. Place the .jar file in the root directory. For example, out of the com directory.
5. Execute the command prompt or shell prompt with the above path.
6. Compile your class by entering one of the following commands:

   * *For Windows:*
     javac -classpath SCIMUtils.jar;nxsl.jar com\novell\idm\\*.java
   * *For Linux or UNIX:*
     javac -classpath SCIMUtils.jar:nxsl.jar com/novell/idm/\*.java
7. Create a Java archive file containing your class by entering one of the following commands:

   * *For Windows:*
     jar cvf mydriverextensions.jar com\microfocus\idm\\*.class
   * *For Linux:*
     jar cvf mydriverextensions.jar com/microfocus/idm/\*.class
8. Place the jar file you created in [Step 7](create-configure-java-extensions.html#bw1la3n) into the same directory that contains the SCIMShim.jar.

   * In Windows: C:\NetIQ\IDM\NDS\lib.
   * In Linux: /opt/novell/eDirectory/lib/dirxml/classes
9. In Identity Console, edit the driver settings:

   1. Select Custom Java Extension to Show.
   2. Select Document Handling to Implemented.
   3. Specify com.microfocus.idm.MyDocumentModifiers as the value for Class and a relevant string value for Init Parameter.

      *NOTE:*The init parameter is the string that is passed to the init method of your class. You can add all the required information for class initialization in this file.
10. Restart the driver. You can now use your custom class.
