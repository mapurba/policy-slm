# 3.2 Creating the Driver in Designer

You create the Blackboard driver in Designer by importing its basic configuration file and then modifying the configuration to suit your environment. After creating and configuring the driver, you need to deploy it to the Identity Vault and start it.

* [Importing the Current Driver Packages](btvlznh.html#bubilzl)
* [Installing the Driver Packages](btvlznh.html#btvm0ef)
* [Configuring the Driver](btvlznh.html#btvm5dq)
* [Deploying the Driver](btvlznh.html#btvm5dv)
* [The Driver Shim Configuration File](btvlznh.html#fsdfds)
* [Starting the Driver](btvlznh.html#btvm5dw)

## 3.2.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer and can be updated after they are initially installed. You must have the most current version of the packages in the Package Catalog before you can create a new driver object.

To verify you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to update the packages

   or

   click OK if the packages are up-to-date.
4. In the Outline view, right-click the Package Catalog.

   Click Import Package.

   ![](../graphics/import_pkg.png)
5. Select any BlackboardREST driver packages

   or

   Click Select All to import all of the packages displayed.

   *NOTE:*By default, only the base packages are displayed. Deselect Show Base Packages Only to display all packages.
6. Click OK to import the selected packages, then click OK in the successfully imported packages message.
7. After the current packages are imported, continue with [Installing the Driver Packages](btvlznh.html#btvm0ef)

## 3.2.2 Installing the Driver Packages

1. In Designer, open your project.
2. In the Modeler, right-click the driver set where you want to create the driver, then select New > Driver.
3. Select BlackboardREST Base, then click Next.
4. Select the optional features to install the Blackboard driver. All options are selected by default. The options are:

   *BlackboardREST Default Configuration:*
   This package contains the default configuration information for the Blackboard driver. Always leave this option selected.

   *BlackboardREST Group Based Enrollments:*
   This package contains the policies required if you want to use Group attributes for Blackboard Enrollments.

   *BlackboardREST User Entitlements:*
   This package contains the policies and entitlements required to enable the driver to account creation and management with entitlements. For more information, see the Identity Manager 4.8 Entitlements Guide on the [Identity Manager 4.8 Documentation Site](https://www.netiq.com/documentation/identity-manager-47/).
5. Click Next.
6. On the Driver Information page, fill in the following field:

   *Driver Name:*
   The name that identifies the driver in Designer and eDirectory®.
7. Click Next.
8. On the Remote Loader page, fill in the following fields:

   *Host Name:*
   Enter the Host Name or IP Address where the bbdrv service has been installed and is running for this driver.

   *Port:*
   Enter the Port Number where the bbdrv service has been installed and is running for this driver. The Default Port is 8090.

   *Remote Password:*
   The Remote Loader password is used to control access to the Remote Loader instance. It must be the same password during the bbdrv configuration.

   *Driver Password:*
   The Driver Object Password is used by the bbdrv service to authenticate itself to the Identity Manager server. It must be the same password that is specified as the Driver Object Password on the Identity Manager Remote Loader.

   *Key Material Object (KMO):*
   Enter the Key Material Object to be used for the SSL connection to the bbdrv service.
9. Click Next.
10. On the next page fill in the following fields:

    *Blackboard Server Hostname:*
    Example: bb.myschool.edu

    *Blackboard Server Port:*
    This must be the SSL encrypted port. Example: 443

    *Blackboard Server Url:*
    This is the base URL for the REST API. Example: /learn/api/public/v1/

    *Blackboard Server API Key:*
    Enter the Blackboard Learn API Key acquired when Configuring the REST API on your Blackboard Learn Instance.

    *Blackboard Server API Secret:*
    Enter the Blackboard Learn API Secret acquired when Configuring the REST API on your Blackboard Learn Instance.
11. (Conditional) This page displays only if you selected to install the Blackboard Group Based Enrollments package. Fill in the following field:

    *Choose the roles that should be used for users who are added to the following group attributes:*
    This setting holds mappings from Group attributes to Blackboard Enrollment Roles. The default map contains mappings that map members of the Member attribute to Student enrollment object and members of the Owner attribute to Instructor enrollment objects. Additional roles can be supported by extending the schema and mapping the desired group attribute to a Blackboard role. Values should be in the format <attribute>:<bb role>.

    *NOTE:*These values are case-sensitive and eDirectory attributes usually start with a capital letter.

    *NOTE:*You must remember to add the additional attributes to the filter.
12. Click Next.
13. (Conditional) This page displays only if you selected to install the Blackboard User Entitlements package. Fill in the following field:

    *If a user loses the bbAccount Entitlement take the following action:*
    Choose the desired action if a user loses the bbAccount Entitlement.
14. Click Next.
15. (Conditional) This page displays only if you selected to install the Blackboard Default Configuration package. (This package should always be selected.) Fill in the following fields:

    *Limit the driver to a base container in the Identity Vault for synchronization:*
    Limit events the driver processes to a base container in eDirectory.

    *Specify the base container in the Identity Vault for User synchronization:*
    This container is used in the Subscriber channel Event Transformation policies to limit the Identity Vault objects being synchronized. Example: users.myorg.

    *Specify the base container in the Identity Vault for Group synchronization:*
    This container is used in the Subscriber channel Event Transformation policies to limit the Identity Vault objects being synchronized. Example: groups.myorg

    *What action should be taken on an enrollment when a Person is removed from a Group:*
    If set to Delete enrollments dropped from a Group will result in the Person being removed from the Course or Organization. If set to Disable the Person's enrollment will be disabled in the Course or Organization.

    *Automatically set the required ID attribute for new Person, Course, and Organization objects to the source name of the object:*
    If true then the required id attribute for Person, Course, and Organization types in Blackboard will be automatically set to Source Name if the id attribute is not already set. The attributes are DirXML-BB-p-id for Person, DirXML-BB-c-id for Course, and DirXML-BB-o-id for Organization.

    *Automatically set the required title attribute for new Course, and Organization objects to the source name of the Group:*
    Automatically set required attribute DirXML-bb-c-course-title to the source name for Course objects if it is not already set. Automatically set required attribute DirXML-bb-o-title to source name for Organization objects.

    *Automatically set the required user roles attributes for Person objects:*
    If true the default roles chosen below will be set for a user if they are not present on the user object.

    *Default System Role for new users:*
    The default system role to use for new users. See Blackboard Documentation for more information about System Roles.

    *Default Institutional Role for new users. [ex. Student, Staff, Alumni, Guest, Faculty, Observer, or any custom defined roles]:*
    Default Institutional Role. See Blackboard documentation for more information about Institutional Roles.

    *Group objects in this subtree will be synchronized as Courses in Blackboard:*
    All group objects in this subtree will be synchronized as Courses in Blackboard. Group objects in eDirectory can represent a Course or Organization object in Blackboard.

    *Group objects in this subtree will be synchronized as Organizations in Blackboard:*
    All group objects in this subtree will be synchronized as Organizations in Blackboard. Group objects in eDirectory can represent a Course or Organization object in Blackboard.

    *Automatically set required Person attribute DirXML-BB-p-email if it is not set:*
    Email address is a required attribute for User creation in Blackboard. If true then the following setting will be used to create the user’s email address in Blackboard.

    *Domain name to use for default email address:*
    Email address is a required attribute for a Person in Blackboard. This value will be used to set the email address attribute in Blackboard for users who do not have an email address specified in their eDirectory User object. The CN of the user will be used with the value provided to create the email address.
16. Click Next.
17. Review the summary of tasks that will be completed to create the driver, then click Finish.
18. After you have installed the driver, you must change the configuration for your environment. Proceed to [Configuring the Driver](btvlznh.html#btvm5dq).

## 3.2.3 Configuring the Driver

After importing the driver configuration file, you need to configure the driver before it can run. Complete the following tasks to configure the driver:

* *Configure the driver parameters:*
  There are many settings that can help you customize and optimize the driver. The settings are divided into categories such as Driver Configuration, Engine Control Values, and Global Configuration Values (GCVs). Although it is important for you to understand all of the settings, your first priority should be to configure the driver parameters located on the Global Configuration Values page.
* *Configure the driver filter:*
  Modify the driver filter to include the object classes and attributes you want synchronized between the Identity Vault and Blackboard.
* *Configure Policies:*
  Modify the policies as needed.

  *IMPORTANT:*Policies should only be modified using Designer or changes could be lost when a package is upgraded or the driver is run in “factory mode.”

  For information about the default configuration policies, see [Section A.0, Policies](btyjlp4.html).
* *Configure password synchronization:*
  The basic driver configuration is set up to support password synchronization through Universal Password. If you don’t want this setup, see “Configuring Password Flow ” in the Identity Manager 4.8 Password Management Guide.

After completing the configuration tasks, continue with the next section, [Deploying the Driver](btvlznh.html#btvm5dv).

## 3.2.4 Deploying the Driver

After a driver is created in Designer, it must be deployed into the Identity Vault.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon or the driver line, then select Live > Deploy.
3. If you are authenticated to the Identity Vault, skip to Step 5; otherwise, specify the following information:

   * *Host:*
     Specify the IP address or DNS name of the server hosting the Identity Vault.
   * *Username:*
     Specify the DN of the user object used to authenticate to the Identity Vault.
   * *Password:*
     Specify the user’s password.
4. Click OK.
5. Read the deployment summary, then click Deploy.
6. Read the message, then click OK.
7. Click Define Security Equivalence to assign rights to the driver.

   The driver requires rights to objects within the Identity Vault. The Admin user object is most often used to supply these rights. However, you might want to create a DriversUser (for example) and assign security equivalence to that user. Whatever rights that the driver needs to have on the server, the DriversUser object must have the same security rights.

   1. Click Add, then browse to and select the object with the correct rights.
   2. Click OK twice.
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.

   You should exclude any administrative User objects (for example, Admin and DriversUser) from synchronization.

   1. Click Add, then browse to and select the user object you want to exclude.
   2. Click OK.
   3. Repeat Step 8a and 8b for each object you want to exclude.
   4. Click OK.

## 3.2.5 The Driver Shim Configuration File

The driver shim configuration file controls operation of the driver shim. This file is located at /etc/bbdrv.conf on the Linux server hosting the driver shim.

A default configuration file is created at installation time.

You can specify the configuration options listed in Table 4-5, one per line. You can also specify these options on the driver shim command line. For details about driver shim command line options, see Section D.2, Driver Shim Command Line Options.

*Table 3-2*

| Option (Short and Long Forms) | Description |
| -conn connString  -connection connString | A string with connection options. Enclose the string in double quotes (“). If you specify more than one option, separate the options with spaces.  port=driverShimPort  ca=”Certificate Authority Key File” |
| -hp httpPort  -httpport httpPort | Specifies the HTTP services port number. The default HTTP services port number is 8091.  You can connect to this port to view log files. For details, see Section A.1, Driver Status and Diagnostic Files. |
| -path driverPath | Specifies the path for driver files. The default path is /opt/novell/bbdrv. |
| -t traceLevel  -trace traceLevel | Sets the level of debug tracing. 0 is no tracing, and 10 is all tracing. For details, see Section A.1, Driver Status and Diagnostic Files. |
| -tf fileName  -tracefile fileName | Sets the trace file location.  Default file: /opt/novell/bbdrv/logs/trace.log |
| -tfm size  -tracefilemax size | Specifies the limit to the size of the trace file for this instance. Specify the value in kilobytes, megabytes, or gigabytes, using the abbreviation for the byte type. The minimum value is 100K. For example:  * -tracefilemax 1000K * -tracefilemax 100M * -tracefilemax 10G  *NOTE:*  * When you add this option to the configuration file, the application uses the specified name for the tracefile and includes up to 9 “roll-over” files. Each file size is 1/10th of the total size specified. The roll-over files are named using the base of the main trace filename plus \_n, where n is 1 through 9. * If the trace file data is larger than the specified maximum when the Driver Shim is started, the trace file data remains larger than the specified maximum until roll-over is completed through all 10 files. |

Example Configuration File

```
-tracefile /opt/novell/bbdrv/logs/trace.log
-trace 0
-tracefilemax 100M
-connection "ca=/opt/novell/bbdrv/keys/ca.pem port=8090"
-httpport 8091
-path /opt/novell/bbdrv/
```

## 3.2.6 Starting the Driver

When a driver is created, it is stopped by default. To make the driver work, you must start the driver and cause events to occur. Identity Manager is an event-driven system, so after the driver is started, it won’t do anything until an event occurs.

To start the driver:

1. Make sure the Remote Loader driver instance is running:

   * ```
      At the Linux server command line, enter:

      /etc/init.d/bbdrvd start
     ```
2. In Designer, open your project.
3. In the Modeler, right-click the driver icon or the driver line, then select Live > Start Driver.
