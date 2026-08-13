# B.2 Creating and Configuring Java Extensions

Using the sample code and SOAP Driver Javadoc found at the [NetIQ Developer Downloads Web site](http://www.novell.com/documentation/dirxmldrivers/javadoc/api/index.html) as a guide, write the Java code for your class. In the A-Z listing, search for SOAP Driver. You should name your class by using any Java package and class name that is convenient for your environment and your organization.

For example, if you were writing your own class that implemented the DocumentModifiers interface, and you named your class MyDocumentModifiers within a package called com.novell.idm, then you would perform the following steps to compile, jar, and deploy your class:

1. Prepare your environment.

   Make sure you have a current Java Development Kit (JDK) installed on your computer. Visit the [Java Web Site](http://java.sun.com/) if you need to download one.
2. Gather your source code in the proper directory structure as defined by your package naming.

   In the example given above, you would have a com directory that contained a novell directory that contained an idm directory. Within the idm directory, you would have a source file named MyDocumentModifiers.java.
3. Make sure you have the jar files you need to compile your class.

   At a minimum, you need SOAPUtil.jar. If you are using XML documents within your class, you also need nxsl.jar.
4. Put a copy of the required jar files in a convenient location like the root of your compile directory just outside the com directory, then access a system command prompt or shell prompt with that location as the current directory.
5. Compile your class by entering one of the following commands:

   * *For Windows:*
     javac -classpath SOAPUtil.jar;nxsl.jar com\novell\idm\\*.java
   * *For Linux or UNIX:*
     javac -classpath SOAPUtil.jar:nxsl.jar com/novell/idm/\*.java
6. Create a Java archive file containing your class by entering one of the following commands:

   * *For Windows:*
     jar cvf mydriverextensions.jar com\novell\idm\\*.class
   * *For Linux:*
     jar cvf mydriverextensions.jar com/novell/idm/\*.class
7. Place the jar file you created in [Step 6](create-configure-extensions.html#bw1la3n) into the same directory that contains the SOAPShim.jar.

   In Windows, this is often C:\Novell\NDS\lib.
8. In Identity Console, edit the driver properties under Driver Parameters.

   1. Next to Custom Java Extension, select Show.
   2. Next to Document Handling, select Implemented.
   3. Specify com.novell.idm.MyDocumentModifiers as the value for Class and any string as the value for Init Parameter.

      The init parameter is the string that is passed to the init method of your class, so you can put any information here that you want to use during your class initialization.
9. Restart the driver.

You can now use your custom class.
