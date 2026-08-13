# 2.4 Preparing the Entity Data Model Driver

This section helps you create, configure, and deploy the Entity Data Model driver. You perform these tasks in your project in Designer.

* [Updating the Base Package for the Entity Data Model Driver](b1fiyn6y.html#b1fixugi)
* [Configuring the Entity Data Model Driver](b1fiyn6y.html#b1eq64sa)
* [Adding the Driver Account to the Entity Data Model Driver](b1fiyn6y.html#b1fj1du0)
* [Deploying the Entity Data Model Driver and Supporting Objects](b1fiyn6y.html#b1eq64sd)

## 2.4.1 Updating the Base Package for the Entity Data Model Driver

NetIQ regularly provides updates to the Identity Manager drivers. You must have the latest content for the Entity Data Model driver, User Application driver, and notifications object. For more information about the packages, see [Installation Requirements](b1eqmb17.html#b1fjc5oz).

1. Open Designer.
2. Select Help > Check for Package Updates.
3. Select the updated packages that you want to update, including packages for the User Application driver and notification templates.
4. Click Yes.
5. When the update completes, restart Designer.

## 2.4.2 Configuring the Entity Data Model Driver

This section helps you configure the Entity Data Model driver and establish its basic settings.

The driver interacts with Entity Data Model through database views. It uses the Entity Data Model administrator account as well as an account in the Identity Manager identity applications. When configuring the driver, you need information about Entity Data Model and Identity Manager settings. For more information about required settings, see [Information Needed for Installation and Configuration](b1eqmb17.html#b1fiys8m).

*NOTE:*The Entity Data Model driver requires the driver set packages for common settings: NOVLACOMSET and NOVLCOMSET. Ensure that you import these packages before configuring the driver. For more information about the packages, see [Installation Requirements](b1eqmb17.html#b1fjc5oz).

1. In the Modeler view of Designer, select Developer.
2. (Conditional) If you have more than one driver set in the Identity Vault, select the driver set in the Modeler view to which you want to add the driver.
3. In the Palette view, expand Service.
4. Drag Entity Data Model to the Modeler view.

   This action opens the Driver Configuration Wizard.
5. For Select Driver Base Configuration, select Entity Data Model Base, then click Next.
6. For Optional Features, select the following items:

   * Default Configuration
   * Managed System Information
   * Password Synchronization
7. Click Next.
8. For Driver Name, specify a value. For example, Entity Data Model Driver.
9. Click Next.
10. (Conditional) Select Yes or No to determine if the driver will use the Remote Loader. If you select No, skip to [Step 11](b1fiyn6y.html#step11ar). If you select Yes, use the following information to complete the Remote Loader configuration, then click Next:

    * *Host Name:*
      Specify the hostname or IP address of the server where the driver’s Remote Loader service is running.
    * *Port:*
      Specify the port number where the Remote Loader is installed and running. The default port number is 8090.
    * *KMO:*
      Specify the Key Name of the Key Material Object (KMO) that contains the keys and certificate the Remote Loader uses for an SSL connection. This parameter is only used when you use SSL for connections between the Remote Loader and the Identity Manager engine.
    * *Other Parameters:*
      Specify any other parameters required to connect to the Remote Loader. Any parameters specified must use a key-value pair format, as follows: paraName1=paraValue1 paraName2=paraValue2.
    * *Remote Password:*
      Specify the Remote Loader’s password as defined on the Remote Loader. The Identity Manager server (or Remote Loader) requires this password to authenticate to the Remote Loader.
    * *Driver Password:*
      Specify the driver object password that is defined in the Remote Loader service. The Remote Loader requires this password to authenticate to the Identity Manager server.
11. Specify the following details to connect to the Entity Data Model database, then click Next:

    *Authentication ID:*
    Specify a user application ID. This ID is used to pass Identity Vault subscription information to the application.

    *Connection Information:*
    Specify the IP address or name of the server the application shim should communicate with.

    *Password:*
    Specify a password for the driver to communicate with the application.

    *Driver Options:*
    Select Show to display the driver options and specify the following parameters:

    * *Entity Data Model Database Connection URL:*
      Specify the JDBC connection URL. For example, jdbc:postgresql://(host):(port)/arops, where arops is the default operation table.
    * *JDBC Driver Class Name:*
      Specify the JDBC driver class name. For example, org.postgresql.Driver.

    *Publisher Options:*
    Select Show to display the publisher options and specify the following parameters:

    * *Entity Data Model Resources Base Container:*
      Specify the name for the base container for the Entity Data Model resources. For example, Identity\_Governance\_Resources.
    * *User Application Driver DN:*
      Specify the DN for User Application driver. For example, CN=User Application Driver,CN=driverset1,O=system.
    * *User Application Provisioning URL:*
      Specify the User Application provisioning URL. For example, http://<uahost>:<port>/IDMProv.
    * *User Application User Name:*
      Specify the user name for the User Application. For example, Admin.
    * *User Application User Password:*
      Specify the password for the user name of the User Application. For example, password.
    * *Provisioning Service Account Password:*
      Specify the password for the Provisioning Service Account. For example, pswd.

    *Allow IDM Account Creation and Migration?:*
    Click Adds and Migrate Allowed to allow Identity Manager to create new users based on the identities published from the Entity Data Model repository. Specify the following parameters and click Next.

    * *Entity Data Model Application URL:*
      Specify the URL of the server where Entity Data Model application is hosted. For example, http://arhost:8080.
    * *Entity Data Model Data Administrator User Name:*
      Specify the name for the Entity Data Model database administrator. For example, igadmin.
    * *Entity Data Model Data Administrator User Password:*
      Specify the password for the Entity Data Model database administrator. For example, igpassword.
    * *OSP Client Name:*
      Specify the user name for the User Application. For example, iac.
    * *OSP Client Password:*
      Specify the password for the user name of the User Application. For example, iacpswd.
12. (Conditional) On the Entity Data Model Default Configuration Information page, specify the container name where the new users from Entity Data Model will be created in the Publisher user Object Placement field. For example, data\users\igusers.
13. (Conditional) On the Entity Data Model Managed System Information page, fill in the following fields to define the ownership of Entity Data Model, then click Next:

    *General Information*

    * *Name:*
      Specify a descriptive name for the managed system.
    * *Description:*
      Specify a brief description of the managed system.
    * *Location:*
      Specify the physical location of the managed system.
    * *Vendor:*
      Specify the vendor of the managed system.
    * *Version:*
      Specify the version of the managed system.

    *System Ownership*

    * *Business Owner:*
      Select a user object in the Identity Vault that is the business owner of Entity Data Model. This can only be a user object, not a role, group, or container.
    * *Application Owner:*
      Select a user object in the Identity Vault that is the application owner of Entity Data Model. This can only be a user object, not a role, group, or container.

    *System Classification*

    * *Classification:*
      Select the classification of Entity Data Model. This information is displayed in the reports. The options are as follows:

      + Mission-Critical
      + Vital
      + Not-Critical
      + Other

        If you select Other, you must specify a custom classification for Entity Data Model.

    * *Environment:*
      Select the type of environment Entity Data Model provides. The options are asfollows:

      + Development
      + Test
      + Staging
      + Production
      + Other

        If you select Other, you must specify a custom environment for Entity Data Model.
14. Click Finish.

## 2.4.3 Adding the Driver Account to the Entity Data Model Driver

This section helps you apply the system account that you created for the driver in the identity applications to the driver. For more information about the account, see [Creating an Identity Manager Provisioning Service Account for the Driver](b1fdqy55.html).

*NOTE:*Identity Manager shares Global Configuration Values (GCVs) with the entire driver set, the Role and Resource driver, and the Entity Data Model driver. NetIQ recommends that you periodically review the GCVs to ensure that it does not get reset by installations of other drivers or changes to the Entity Data Model driver.

1. In the Outline view of Designer, right-click the Entity Data Model driver.
2. Select Properties.
3. In the navigation pane, select Driver Configuration and select Publisher Options tab.
4. Specify the DN and password of the service account created for User Application Provisioning Service Account DN.

   The Properties window displays the name of the service account based on the descriptive name that you created when you added the account to the GCVs for the driver set. For example, User Application Provisioning Service Account DN. For more information, see [Creating an Identity Manager Provisioning Service Account for the Driver](b1fdqy55.html).
5. Click OK.

## 2.4.4 Deploying the Entity Data Model Driver and Supporting Objects

After you create, configure, or modify the driver, you must deploy the Entity Data Model driver, User Application driver, and notifications object.

1. In the Modeler or Outline view of Designer, right-click Driver Set or the driver set where you installed the Entity Data Model driver.
2. Select Live > Deploy.
3. Select Deploy, then select OK.
4. Right-click the Entity Data Model driver, then repeat the two deployment steps.
5. Deploy the User Application driver.
6. Deploy the Default Notification Collection object.
7. (Conditional) If Identity Manager requests Security Equivalences values, set equivalence to the admin.sa.system user.
