# 2.4 Creating the Driver Object

To create a SAP HANA driver object you must install the driver packages and then modify the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start the driver.

* [Importing the Current Driver Packages](t4avmq79xc47.html#t4avmq79xju0)
* [Installing and Configuring the Driver Object](t4avmq79xc47.html#t4avmq79xz9m)

## 2.4.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer and can be updated after they are initially installed.

To verify that you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the Outline view, right-click the Package Catalog.
3. Click Import Package.
4. Browse to the location where you downloaded the SAP HANA packages.
5. Select the required packages for SAP HANA. Alternately, you can click Select All to import all of the packages displayed. For the available SAP HANA packages, see [SAP HANA Driver Packages](t4fles1fxjl7.html).
6. Click OK to import the selected packages, then click OK in the successfully imported packages message.
7. After the current packages are imported, continue with [Installing and Configuring the Driver Object](t4avmq79xc47.html#t4avmq79xz9m).

## 2.4.2 Installing and Configuring the Driver Object

1. In Designer, open your project.
2. From the Palette, drag-and-drop the SAP HANA driver to the desired driver set in the Modeler.

   The SAP HANA driver is under the Enterprise category in the Palette.
3. Select the required packages that you want to install for the SAP HANA driver, then click Next. For more information, see [SAP HANA Driver Packages](t4fles1fxjl7.html).
4. Click OK on the Package Dependencies screen.
5. Fill the Driver Name field, then click Next.
6. In the Driver Parameters page, the following sections and fields are displayed. Enter the values in the corresponding fields as shown below and click Next.

   * Driver Options: The Driver Options field defaults to Show Authentication Parameters.

     + SAP HANA Driver Database Configuration:Select the authentication type as required. The available options are:

       - Username: This option requires the user name of the SAP HANA database to establish connection.
       - Password: Specify the database password.
       - SQL Endpoint: Specify the destination SAP HANA SQL Endpoint details to establish the connection.

         For example:

         * <server>:<port>. Ex: myServer:30015
         * <endpoint>:<port>. Ex: 1234568-abcd-12ab-34cd-1234abcd.hana.hanacloud.ondemand.com:443
       - Use SSL Connection: By default this value is set to False. You can switch it to True if SSL Connection is required. If it is set to True, provide Truststore Path and Truststore Password. If Truststore > Path and Truststore Password are not provided, the driver looks for the certificate in the default Java keystore. For more information on secured connection, see .
     + Cache Parameters: It reads the default cache path or user defined path. Specify the Cache Directory Path to store the temporary files.
     + Advanced Parameters: By default the value is set to Hide. When it is set to Show, under Paging Parameters specify the number of pages to be processed at a time by the driver in Page Size.
7. Fill in the Subscriber Options as shown below and click OK.

   * Assign User to a default UserGroup: By default the value is set to Yes to assign the user to default user group. Else the user is not assigned to any user group.

     + Default usergroup name: This field is enabled if Assign User to a default UserGroup value is set to Yes. By default, DEFAULT is the UserGroup name and is editable.
8. Fill in the Publisher Options as shown below and click Next.

   * Publisher Options:

     + Enable Publisher Channel: Yes
     + Users: Specify the values in the fields as shown below:

       - Migrate Users on Driver Startup: These parameters are valid only at driver startup. Driver will continue with regular polling after the task at startup is completed. If driver shuts down unexpectedly during migration, just restart the driver and migration will continue. If it’s is set to True, migration is initiated for users, on driver startup. When it’s set to False, regular polling for users is initiated.
       - Poll Users: It polls the users from SAP HANA application during migration. By default this value is set to True.
       - Exclude Users: This field excludes the system generated users while polling. You can add/delete/ edit the user prefixes. All the Users with UserName starting with any of the strings listed will not be migrated or polled.
     + User Groups:

       - Migrate User Groups on Driver Startup: These parameters are valid only at driver startup. Driver will continue with regular polling after the task at startup is completed. If driver shuts down unexpectedly during migration, just restart the driver and migration will continue. If it’s is set to True, migration is initiated for user groups on driver startup. When it’s set to False, regular polling for user groups is initiated.
       - Poll User Groups: It polls the user groups from SAP HANA application during migration. By default this value is set to False.
       - Exclude User Groups: This field excludes the system generated users groups while polling. You can add/delete/ edit the user group prefixes. All the user groups starting with any of the strings listed will not be migrated or polled.
     + Roles:

       - Migrate Roles on Driver Startup: These parameters are valid only at driver startup. Driver will continue with regular polling after the task at startup is completed. If driver shuts down unexpectedly during migration, just restart the driver and migration will continue. If it’s is set to True, migration is initiated for roles on driver startup. When it’s set to False, regular polling for roles is initiated.

       - Poll Roles: It polls the roles from SAP HANA application during migration. By default this value is set to False.
       - Exclude Roles: This field excludes the system generated roles while polling. You can add/delete/ edit the role prefixes. All the roles with the name starting with any of the strings listed will not be migrated or polled.
     + Polling Interval: It is the number of minutes between the polling cycles.
     + Heartbeat Interval: This option is used to configure the driver shim to send a periodic status message on the Publisher channel, when there is no Publisher traffic for a specified number of minutes. By default, this is set to 10 minutes.
9. Fill in the following fields for the Remote Loader information, then click Next:

   *Connect To Remote Loader:*
   Select Yes or No to determine if the driver will use the Remote Loader. For more information, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

   If you select No, skip to Step 8. If you select Yes, use the following information to complete the configuration of the Remote Loader:

   *Host Name:*
   Specify the IP address or DNS name of the server where the Remote Loader is installed and running.

   *Port:*
   Specify the port number for this driver. Each driver connects to the Remote Loader on a separate port. The default value is 8090.

   *KMO:*
   Specify the Key Name (for example, kmo=remotecert) of the Key Material Object (KMO) containing the keys and certificate to be used for SSL.

   If you used spaces in the certificate name, you need to enclose the KMO object nickname in single quotation marks.

   *Remote Loader Password:*
   Specify a password to control access to the Remote Loader. It must be the same password that is specified as the Remote Loader password on the Remote Loader.

   *Driver Password:*
   Specify a password for the driver to authenticate to the Identity Manager server. It must be the same password that is specified as the Driver Object Password on the Remote Loader.
10. Click Next. Review the summary of tasks that will be completed to create the driver, then click Finish.
11. After you have installed the driver, you can change the configuration for your environment. or more information, see [Creating the Driver Object](t4avmq79xc47.html).
