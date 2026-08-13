# 4.1 Creating a Fanout Driver Object in Designer

Creating the driver includes installing the Fanout driver packages and then modifying the configuration to suit your environment.

* [Importing the Driver Packages](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9ihr)
* [Installing the Driver Packages](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9ihs)
* [Configuring the Driver Object](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9iht)
* [Configuring the Database Connections for the Driver](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9ihu)
* [Deploying the Driver Object](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9ihv)
* [Starting the Driver](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9j9g)
* [Managing the Connection Objects](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9j9f)

## 4.1.1 Importing the Driver Packages

You can update the driver packages at any time.The driver packages are stored in the Package Catalog. Packages are initially imported into the Package Catalog when you create, import, or convert a project. Ensure that you import the latest packages into the Package Catalog before installing the driver.

To verify the latest packages in the Package Catalog:

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Click OK to import the package updates.

   If prompted to restart Designer for the changes to take effect, click Yes, save your project, and then wait for the Designer to restart.

   or

   Click OK if there are no package updates.
4. Continue with [Installing the Driver Packages](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9ihs).

## 4.1.2 Installing the Driver Packages

1. In Designer, open your project.
2. In the Modeler, drag and drop a supported JDBC database from the Designer palette.

   For example, Oracle. For information about supported databases, see [Supported Databases](supported-jdbc-fanout-databases.html).
3. Select the Fanout Base from the list of available base packages, then click Next.
4. Select the Synchronization Mode. For more information, see [Data Synchronization](supported-jdbc-fan-out-operations.html#b1ijodhb).
5. Select the optional features to install for the Fanout driver, then click Next.

   All options are selected by default. The options are:

   * *Entitlements Support:*
     These packages contain the policies that provision the user accounts on the connected database. For more information, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-48/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).
   * *Data Collection:*
     These packages contain the policies that enable the driver to collect data for reports. If you are using Identity Reporting, ensure that this option is selected. For more information, see [NetIQ Identity Reporting: User’s Guide to Running Reports](../../../identity-manager-48/report_descriptions/data/bookinfo.html#bookinfo).
   * *Account Tracking:*
     These packages contain the policies that enable account tracking information for reports. If you are using Identity Reporting, ensure that this option is selected. For more information, see [NetIQ Identity Reporting: User’s Guide to Running Reports](../../../identity-manager-48/report_descriptions/data/bookinfo.html#bookinfo).
6. (Conditional) If there are package dependencies for the packages you selected to install for this driver, you must install them to install the selected package. Click OK to install the package dependency listed.
7. (Conditional) If more than one type of package dependency is installed, Designer displays separate configuration pages for each package. Click OK to install any additional package dependencies.
8. (Conditional) The Common Settings page is displayed only when the Common Settings package is installed as a dependency. On the Install Common Settings page, specify the common settings for User and Group containers:

   * *User Container:*
     Select the Identity Vault container where the user accounts will be added in the Identity Vault. This value becomes the default for all drivers in the driver set.
   * *Group Container:*
     Select the Identity Vault container where the groups will be added in the Identity Vault. This value becomes the default for all drivers in the driver set.
9. Click Next.

   When all dependencies are installed, you must configure the components.
10. On the Driver Information page, specify a name for the driver that is unique within the driver set, and then click Next.
11. On the Application Authentication page, fill in the following information:

    * *Connection Information:*
      Specify the URL of the ActiveMQ instance to which this driver connects to. For example, tcp://111.1.1.1:61616.
    * *Synchronization Filter:*
      Select the synchronization filter. For more information, see [Database Scoping Parameters](../../jdbc/data/configure-jdbc-driver-specific-parameters.html#b1pu3k1) from the [NetIQ Identity Manager Driver for JDBC Implementation Guide](../../jdbc/data/netiq-identity-manager-driver-for-jdbc.html#netiq-identity-manager-driver-for-jdbc).
    * *Synchronization Model:*
      Select the synchronization model based on the synchronization mode specified in Step 4.
12. Do not change the default values of the remaining parameters on this page, then click Next.
13. On the Entitlements Information page, specify a name for the Account Entitlement Value field, then click Next.
14. (Conditional) This page is displayed only if you selected to install the Data Collection and Account Tracking groups of packages. On the Managed System Information page, fill in the following fields to define your connected database application:

    * *Name:*
      Specify a descriptive name for the connected database application. The name is displayed in reports.
    * *Description:*
      Specify a brief description for the connected database application. The description is displayed in reports.
    * *Location:*
      Specify the physical location of the connected database application. The location is displayed in reports.
    * *Vendor:*
      Specify the vendor of the connected database application. This information is displayed in reports.
    * *Version:*
      Specify the version of the connected database application. The version is displayed in reports.
15. Click Next.
16. (Conditional) This page is displayed only if you selected to install the Managed System packages and the Account Tracking packages. On the Install Managed System Information page, fill in the following fields to define the classification of the connected database application. This information is displayed in the reports. The options are:

    * *Classification:*
      Select the classification of the connected database application. This information is displayed in the reports. Your options are:

      + Mission-Critical
      + Vital
      + Not-Critical
      + Other

        If you select Other, you must specify a custom classification for the JDBC system.
    * *Environment:*
      Select the type of the connected database application environment. The options are:

      + Development
      + Test
      + Staging
      + Production
      + Other

        If you select Other, you must specify a custom classification for the database application.

      Click Next.
17. (Conditional) This page is displayed only if you selected to install the Data Collection and Account Tracking groups of packages. Fill in the following fields to define the ownership of the connected database application:

    * *Business Owner:*
      Select a user object in the Identity Vault that is the business owner of the database application. This can only be a user object, not a role, group, or container.
    * *Application Owner:*
      Select a user object in the Identity Vault that is the application owner of the database application. This can only be a user object, not a role, group, or container.

    Click Next.
18. (Conditional) This page is displayed only if you selected to install the Account Tracking groups of packages. On the Account Tracking Initial Configuration page, fill in the following fields:

    * *Fanout Database Type:*
      Select the required database. The Fanout supports databases such as, MySQL, SQL Server, Sybase, and Oracle.
    * *Synchronization Model:*
      Specify the mode of data synchronization.
    * *User Table:*
      This field is populated based on your selection in the Synchronization Model. Specify the table or view in the connected database for which account tracking is enabled. By default, the value is usr.
    * *Realm:*
      Specify the name of the realm that uniquely identifies the location of user accounts in the connected database. For example, mysql.indirect.usr, where mysql is the database name with the indirect data synchronization model, and user is the table or view in the connected database for which account tracking is enabled.

      Click Next.
19. Review the summary of tasks that will be completed to create the driver, then click Finish.

The driver is now created. To modify the configuration settings, proceed to the [Configuring the Driver Object](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9iht).

## 4.1.3 Configuring the Driver Object

After importing the packages and creating the driver object, configure the driver to make it operational. Many settings are available to help you customize and optimize the driver. However, you should first configure the driver parameters located on the Driver Configuration page.

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon or the driver line, then select Properties.
3. Click Driver Configuration and select the Driver Parameters tab.
4. In the Driver Options tab, specify the queue names in the Transport parameters. The different queues are:

   * *Subscriber Event Queues (SEND/RECV/DELAYED):*
     The driver uses these queues to send the Subscriber events to the Fanout agent and receive the status of these events.
   * *Configuration Queues (SEND/RECV):*
     The driver uses these queues for sending the driver initialization documents and exchanging the handshake documents with the Fanout agent.
   * *Query-In Queues (SEND/RECV):*
     The driver uses these queues to receive the queries from the Fanout agent and sends the response of the queries to the Fanout agent.
   * *Query-Out Queues (SEND/RECV):*
     The driver uses these queues to send the queries to the Fanout agent and receive the response of the queries from the Fanout agent.

   *NOTE:*If you specified a different name for the queues in these parameters, ensure that the same queue name is used during Fanout agent configuration.
5. In the Fanout Agent Configuration Parameters, fill in the following information:

   * *Fanout Shim Password:*
     Click Set Password to specify the Fanout shim password.
   * *Fanout Agent Password:*
     Click Set Password to specify the Fanout agent password.

     The Fanout driver uses these passwords for performing handshake with the Fanout agent.
   * *Encryption Key:*
     Click Set Password to specify the key to encrypt or decrypt the sensitive data before sending the data to the message queues.

   *NOTE:*Ensure that you provide the same value for the Fanout agent and shim passwords and the encryption key. The default passwords are netiq.
6. To enable the SSL communication between the Fanout driver and ActiveMQ, specify the following information:

   * *AMQ Keystore Path:*
     The full path to the keystore file. For example, /root/amq-clients.ks.
   * *AMQ Keystore Password:*
     The password used by the keystore.
   * *AMQ Truststore Path for SSL Certs:*
     The full path to the truststore file. For example, /root/amq-clients.ts.
   * *AMQ Truststore Password:*
     The password used by the truststore.
   * *Secure Protocol Version:*
     Specifies the version of the TLS protocol that the driver uses to connect to the Identity Manager engine. Identity Manager supports TLSv1, TLSv1\_1, and TLSv1\_2.

     *NOTE:*This parameter is included in Fanout driver 1.1.
   * *Enforce Suite B:*
     Specifies whether the driver should use Suite B for establishing communication with ActiveMQ. When Suite B is enabled, the communication is authenticated with Suite B cryptographic algorithms. This communication is supported only on TLS 1.2 protocol.

     *NOTE:*This parameter is included in Fanout driver 1.1.

   For more information about securing communication, see [Section 6.0, Securing Fanout Driver Communication](how-to-establish-ssl-communication-between-identity-manager-and-jdbc-fan-out-driver.html).
7. Do not change the default value of Fanout Shim classname.
8. Do not change the default value of Matching Attributes.

   The Fanout agent uses Matching Attributes to match the objects in the delayed add events. This parameter must be schema-mapped equivalent of the attributes that are used in the object matching policy. If you are using different attributes, specify the attribute names according to the connected system schema.
9. The Normal JDBC Driver settings section for the Fanout driver is similar to the JDBC driver. For more information about these parameters, see [Driver Parameters](../../jdbc/data/how-to-configure-jdbc-driver.html#b4m4h9a) in the [NetIQ Identity Manager Driver for JDBC Implementation Guide](../../jdbc/data/netiq-identity-manager-driver-for-jdbc.html#netiq-identity-manager-driver-for-jdbc).

After completing the configuration tasks, continue with [Configuring the Database Connections for the Driver](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1ij9ihu).

## 4.1.4 Configuring the Database Connections for the Driver

Designer lets you configure multiple database connections for the Fanout driver. Each JDBC driver instance loaded by the Fanout agent uses this information to connect to the database and for tracing purposes.

Alternatively, you can run the createConnLDIF script to create an LDIF file that includes the connection objects for the Fanout driver. However, you can run the script only after deploying the driver. For more information, see [Configuring the Database Connections by Using the createConnLDIF Script](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1imqqix).

The advantage of using Designer is that it allows you to manage the connections after they are configured. If you use the createConnLDIF script for creating the connections, the script does not provide this flexibility.

* [Configuring the Database Connections in Designer](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1iog05u)
* [Configuring the Database Connections by Using the createConnLDIF Script](how-to-create-jdbc-fan-out-driver-object-in-designer.html#b1imqqix)

### Configuring the Database Connections in Designer

1. Open your project in Designer.
2. In the Modeler, right-click the driver icon and select Fanout Configuration.
3. Click ![](../graphics/icon_plus_green_n.png) icon to create a Fanout connection.
4. Specify the Fanout connection details:

   * *Name:*
     Specify the name for the new connection.

     *NOTE:*NetIQ restricts the connection object name to15 characters.
   * *User:*
     Specify the user name with which the JDBC driver instance will authenticate to the database.
   * *Connection Password:*
     Specify the password with which the JDBC driver instance will authenticate to the database
   * *Server:*
     Specify the server with which the JDBC driver instance will connect to. For more information, see [JDBC URL Syntaxes](../../jdbc/data/supported-third-party-jdbc-drivers.html#bvx364n) in the [NetIQ Identity Manager Driver for JDBC Implementation Guide](../../jdbc/data/netiq-identity-manager-driver-for-jdbc.html#netiq-identity-manager-driver-for-jdbc).
   * *Trace Level:*
     Specify the trace level for the JDBC driver instance. This defines the level for logging the trace messages.
   * *Trace File:*
     Specify the name of the trace file. This file includes the trace and debugging messages for the JDBC driver instance.

     *NOTE:*In order to have a single trace file for both database connection and the Fanout agent, configure them with the same trace file name.
   * *Trace File Size:*
     Specify the trace file size. This defines the limit for the trace file.

     This parameter is not currently supported with the driver.
5. Click ![](../graphics/enable_disable_n.png) icon to enable or disable the selected connection. By default, the connection is disabled.
6. Click Save on the Designer toolbar.
7. (Conditional) To create multiple database connections for the Fanout configuration, repeat Step 3 through Step 6.

### Configuring the Database Connections by Using the createConnLDIF Script

After deploying the driver, you can run the createConnLDIF script to create an LDIF file that allows you to create multiple database connection objects. The createConnLDIF file is located in default installation path of the Fanout agent.

To create a database connection:

1. Create a CSV file with the required database connection information. A sample CSV file is located in the default installation directory of the Fanout agent.
2. Run the createConnLDIF script as follows:

   ```
   createConnLDIF [DriverDN in LDAP format] [input csv absolute file path] [output ldif absolute file path]
   ```

   This script creates the LDIF file in the specified location.
3. Import the LDIF file into eDirectory using any LDAP tool.

## 4.1.5 Deploying the Driver Object

After you create the driver in Designer, you can deploy the driver into the Identity Vault.

To deploy the driver:

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
5. Read through the deployment summary, and then click Deploy.
6. Read the success message, and then click OK.
7. Click Define Security Equivalence to assign rights to the driver.
8. Click Exclude Administrative Roles to exclude users that should not be synchronized.
9. Click OK.

## 4.1.6 Starting the Driver

After creating a driver, you must start it. Identity Manager is an event-driven system and starts caching the events once the driver is deployed. These events are processed when you start the driver.

*NOTE:*NetIQ recommends that you complete the Fanout agent configuration before starting the driver. For more information, see [Section 3.0, Configuring the Fanout Agent](how-to-configure-fan-out-agent.html).

To start the driver:

1. In Designer, open your project.
2. In the Modeler, right-click the driver icon ![](../graphics/driver_icon_n.png) or the driver line, then select Live > Start Driver.

## 4.1.7 Managing the Connection Objects

When you make changes to the connection objects and deploy the Fanout driver, you need not restart the driver. Depending on the connection object changes, the Fanout driver starts, stops, or restarts the JDBC driver instances.

When you add, modify, or delete a connection object, the Fanout driver sends the configuration update to the Fanout agent. Based on the changes made, the Fanout agent starts, stops, or restarts the corresponding JDBC driver instance.

*NOTE:*To detect the changes to the connection objects, Identity Manager provides two additional filter classes namely DirXML-Resource and DirXML-Driver in the default filter of the Fanout driver.

Ensure that you review the following notes before redeploying the Fanout driver:

* When you deploy the Fanout driver, all the connection objects are also deployed. If you perform any dynamic updates to the connection objects or if you create the connection object dynamically using Designer, NetIQ recommends that you deploy those connection objects separately to avoid the entire driver restart.
* If you change the password for a connection object, the connection object must be deployed again. In this case, NetIQ recommends that you do not separately deploy or reconcile the named-passwords for the connection objects.
* When you use Designer to delete an existing Fanout connection, the connection object is deleted only from Designer and it is not updated in the Identity Vault. To delete an existing Fanout connection object from the Identity Vault, use Identity Console to manually remove the connection object.
