# 2.6 Creating the Driver Object

To create a Workday driver object you must install the driver packages and then modify the configuration to suit your environment. After you create and configure the driver object, you need to deploy it to the Identity Vault and start the driver.

* [Importing the Current Driver Packages](t4avmq79xc47.html#t4avmq79xju0)
* [Installing and Configuring the Driver Object](t4avmq79xc47.html#t4avmq79xz9m)

## 2.6.1 Importing the Current Driver Packages

The driver packages contain the items required to create a driver, such as policies, entitlements, filters, and Schema Mapping policies. These packages are only available in Designer and can be updated after they are initially installed.

To verify that you have the most recent version of the driver packages in the Package Catalog:

1. Open Designer.
2. In the Outline view, right-click the Package Catalog.
3. Click Import Package.
4. Browse to the location where you downloaded the Workday packages.
5. Select the required packages for Workday. Alternately, you can click Select All to import all of the packages displayed. For the available Workday packages, see [Workday Driver Packages](t4fles1fxjl7.html).
6. Click OK to import the selected packages, then click OK in the successfully imported packages message.
7. After the current packages are imported, continue with [Installing and Configuring the Driver Object](t4avmq79xc47.html#t4avmq79xz9m).

## 2.6.2 Installing and Configuring the Driver Object

1. In Designer, open your project.
2. From the Palette, drag-and-drop the Workday driver to the desired driver set in the Modeler.

   The Workday driver is under the Enterprise category in the Palette.
3. Select the required packages that you want to install for the Workday driver, then click Next. For more information, see [Workday Driver Packages](t4fles1fxjl7.html).
4. Click OK on the Package Dependencies screen.
5. Fill the Driver Name field, then click Next.
6. In the Driver Parameters page, the following sections and fields are displayed. Enter the values in the corresponding fields as shown below and click Next.

   * Driver Parameters: The Driver Options field defaults to show and the following sections are displayed:

     + Authentication Parameters: Select the authentication type required as shown in the following [Authentication Parameters](t4avmq79xc47.html#auth_params) table. The available options are:

       - Basic: This option requires the user ID and password to authenticate and establish connection with Workday.
       - OAuth 2.0: This an open authentication protocol. This authentication method enables a third-party application to access and share data from a HTTP service across connected applications (for example, Workday).

       *Table 2-1* Authentication Parameters

       | Field/Description | Sample Field Value |
       | If you select Basic, the following fields appear:  - Workday Login ID: Specify the user ID that is used to login to Workday. Ensure that the user has required permission to fetch and modify data from Workday. Perform the following steps to find the tenant name:  1. Log in to the Workday sandbox.   2. On the first page, find the tenant details appearing in the upper left corner of the page. - Workday Login Password: Specify the password that is used to login to Workday. | - Workday Login ID: <IntegrationUsername@tenantName> - Workday Login Password: <workday password> |
       | If you select OAuth2.0, the following fields appear:  - Access token URL: Specify the URL of the server used for requesting token access. For more information to generate the URL, see [Generating Client ID and Token Endpoint](t4eie9te8d7c.html#t4f4helql9pu). - Client ID: Specify the Workday Client ID for OAuth 2.0 authentication. For more information to generate the Client ID, see [Generating Client ID and Token Endpoint](t4eie9te8d7c.html#t4f4helql9pu). - User Name: Specify the Workday Integration User Name for OAuth 2.0. - Keystore File: Specify the path of the keystore file. For more information, see [Creating x509 Public Key Certificate](t4eie9te8d7c.html#t4f4hedopy5q). - Alias: Specify the Alias name for secret (private) key in the keystore file. This is the alias name that was provided when creating the keystore certificate. For more information, see [Creating x509 Public Key Certificate](t4eie9te8d7c.html#t4f4hedopy5q). - Keystore Password: Enter the password of the Keystore. This is the password that was provided when creating the keystore certificate. For more information, see [Creating x509 Public Key Certificate](t4eie9te8d7c.html#t4f4hedopy5q).  *NOTE:*Ensure the file password and the private key passwords are same when creating the keystore. | - Access token URL: <https://wd2-impl-services1.workday.com/ccx/oauth2/tenantname/token> - Client ID: <AjkwZTU5GUtOWIopb00MWrnmkkzODYtZjU0MjNkNDIfgykl> - User Name: <name of the user> - Keystore File: <C:\keystore> - Alias: <keystore alias name> - Keystore Password: <password for the keystore file> |
     + Connection Parameters: Specify the [Connection Parameters](t4avmq79xc47.html#connec_params) as explained in the following table:

       *Table 2-2* Connection Parameters

       | Field/Description | Sample Field Value |
       | Workday Login URL: Specify the login URL of Workday.  Perform the following steps to find the Host Name:  1. Log in to the Workday sandbox or production instance. 2. Search for Public Web Services in the search box. 3. Select Public Web Services from the search results. 4. Scroll down to Human Resources (Public)and click on the ellipsis (3 dots). Then click the Web Services list and select View WSDL. 5. Scroll down to the end to find the soapbind:address location value assigned to the location element in the WSDL file. 6. Copy and save the Workday soapbind:address location part of the value. For example, location="https://wd5-impl-services9.workday.com/...." | <https://hostName/ccx/service/tenantName/Human\_Resources/v32.0> |
       | Workday API Version | v32.0 onwards  *NOTE:*This value should not be changed. |
       | Proxy Authentication: Proxy authentication enables you enhance the security of your environment by placing a middle ware layer between the Workday driver and the Identity Vault. | If you decide to use a proxy authentication, then specify the following fields:  - Proxy hostname and port: Specify the host address and the host port. Choose an unused port number on your server. - User name: Enter the proxy user ID. - User Password: Set the proxy user password. |
     + General Parameters: Specify the [General Parameters](t4avmq79xc47.html#general_params) as shown in the following table:

       *Table 2-3* General Parameters

       | Field/Description | Sample Field Value |
       | Cache Files Directory: Specify the absolute path of the directory where the driver has to create cache files which is required for its operations. As cache files can be large in size, it is recommended to provide the directory with no size limit. | /var/opt/novell/eDirectory/data/dib or C:/NetlQ/IDM/NDS/DIBFiles/ |
     + SSL Parameters: Specify the [SSL Parameters](t4avmq79xc47.html#ssl_params) values as explained in the following table:

       *Table 2-4* SSL Parameters

       | Field/Description | Sample Field Value |
       | Workday Keystore File: Specify the path and the name of the keystore file that contains the trusted certificates for the remote server to provide server authentication. | For example:  - In Windows: <C:\security\keystore> - In Linux: </var/opt/novell/eDirectory/workday/idmworkday.jks>  To obtain a Workday tenant root CA certificate and import it to the Java keystore. see [Section 7.0, Securing Communication](t4avmq7ea8tv.html). |
       | Workday Keystore Password | Specify the password for the keystore file. |
     + Advanced Parameters: Select Show to configure the Advanced Parameters.

       - Paging Parameters: Specify the [Paging Parameters](t4avmq79xc47.html#paging_params) as explained in the following table:

         *Table 2-5* Paging Parameters

         | Field/Description | Sample Field Value |
         | Page size: Specify the number of pages to be processed at a time by the driver. This value is used for both the recurring and scheduled polling cycle and should be set as per the Java heap available to the driver. | Specify the page size in this field. By default, the paging size is set to 50.  For more information on setting paging size value see, [Setting Paging Size Parameter Value](t4ckji9y7x6h.html). |
         | Query-Ex timeout in seconds: Specify the timeout in seconds for Query Ex. | <120> |
       - Transformation Parameters: Specify the [Transformation Parameters](t4avmq79xc47.html#transform_params) as shown in the following table:

         *Table 2-6* Transformation Parameters

         | Field/Description | Sample Field Values |
         | Transformation Parameters: Set the following parameters on the Publisher channel and select the required values for each of them from the list of default values or you can create custom values by clicking on the ![](../graphics/icon_plus_green_n.png) icon.  The default Parameter Names configured are:  * Parameter Name: wdOrgList  Custom values for this parameter can also be added by clicking on the ![](../graphics/icon_plus_green_n.png) icon. You can collect such Organization values from the Workday implementation team. * Parameter Name: wdIntFieldAttrList * Parameter Name: wdAutoCompleteBP * Parameter Name: wdCustomIdList * Parameter Name: wdFetchPrivatePhoneInformation * Parameter Name: wdTransactionLimit | The descriptions for the default Parameter Name and their associated Parameter Value are shown below:  * wdOrgList: The values here indicate the types of Organizational data that will be returned from a call of the Get\_Worker SOAP API.  Parameter Values:  + Supervisory   + Cost\_Center   + Company   + Cost\_Center\_Hierarchy   + Matrix   + Region * wdIntFieldAttrList: Add the names of any custom, override fields created in Workday for Workers and that should be synchronized to the Identity Vault. This option can be used to synchronize data to the Identity Vault that is not currently synchronized by the shim. * wdAutoCompleteBP: Set this to true to mark the business process for the modification as complete and immediately commit the update to the Worker. * wdCustomIdList: Add the names of any Other/Custom IDs that the driver should synchronize to the Identity Vault and/or which should have data from the Identity Vault written back to Workday using the Change\_Other\_IDs API. * wdFetchPrivatePhoneInformation: When set to true, the driver will retrieve phone information if that number has been marked private in Workday. By default this is set to false which means meaning only the phone numbers marked public will be published. * wdTransactionLimit: This parameter indicates maximum number of transactions that the wd-TransactionLog attribute can hold. The following values are available to select:  + 3   + 5   + 10   + 15   + 30  *NOTE:*The wd-TransactionLog attribute is a multi-valued attribute, and is capable of storing multiple transactions. |
7. Fill in the Subscriber Options as shown below and click Next.

   IMPORTANT:

   * To place the imported custom stylesheet in the required folder, you must have the required modify folder permissions.
   * When you are importing the custom stylesheets and placing it in the required folder, you must ensure that the folder modify rights must be available only for the system administrator or the user running the Identity Vault process.

   * Subscriber Options

     + Worker Settings

       - Import Worker Stylesheet: Specify the absolute path to import the custom stylesheet for a worker. Leave this field empty to operate with default stylesheet. If stylesheet is configured, the data in the custom stylesheet will be considered.

         For example:

         * Linux: /home/NOVLSPML2-its-XDSInputTransform\_worker.xml
         * Windows: C:\NOVLSPML2-its-XDSInputTransform\_worker.xml
     + Worker Photo Settings

       - Import Worker Photo Stylesheet: Specify the absolute path to import the custom stylesheet for worker's photo. Leave this field empty to operate with default stylesheet. If stylesheet is configured, the data in the custom stylesheet will be considered.

         For example:

         * Linux: /home/NOVLSPML2-its-XDSInputTransform\_workerphoto.xml
         * Windows: C:\ NOVLSPML2-its-XDSInputTransform\_workerphoto.xml
8. Fill in the Publisher Options as shown below and click Next.

   *IMPORTANT:*When you are importing the custom stylesheets, you must ensure that it can be modified only by the system administrator or the user running the Identity Vault process.

   * Publisher Options:

     + Enable Publisher Channel: Yes
     + Heartbeat Interval: This option is used to configure the driver shim to send a periodic status message on the Publisher channel, when there is no Publisher traffic for a specified number of minutes. By default, this is set to 10 minutes.
     + Recurring API: Specify the values in the fields as shown below:

       - Polling interval in minutes: Number of minutes between the polling cycles. This is applicable for both worker and job profile. By default, the polling interval is set to 10 minutes.
       - Migrate on Startup: These parameters are valid only at driver startup. Driver will continue with regular polling after the task at startup is completed. If driver shuts down unexpectedly during migration, just restart the driver and migration will continue from where it stopped.

         If you select the value as:

         * True: Migration is initiated for the Recurring APIs (i.e Worker and Job Profile) that are enabled in the configuration, on driver startup. After migration is completed, the driver continues with regular polling cycle.
         * False: Regular polling for Recurring APIs that are enabled in the configuration is initiated. This parameter can force the migration by clearing cache files.

         *IMPORTANT:*You must ensure not restart the driver with this parameter set to true for a completed migration, unless re-migration is required.
       - Enable Delta and Future Object Creation on initial Migration: Set the vale as true to enable the Delta and Future Object Creation upon the initial migration of objects from Workday.

         *IMPORTANT:*To enable this feature, it is mandatory to set the Migrate on Startup value as True.

         * Number of days of Prior Transactions to be considered for Future Object creation: The number of past days for which the delta object should be created as a part of migration.
       - Effective Poll Time: Set the time interval for the effective polling. This polling is applicable for Worker and Job Profile. The effective polling can be performed once in a day at a selected time slot.
     + Worker:

       - Poll Worker: Select Enable to poll worker objects from Workday.

         * Worker Poll Settings: Select Show to view worker poll settings and specify the values as shown in the following table:
         * Worker Poll Offset in seconds: By default the value is set to 0. The poll overlaps for the number of seconds specified in the offset. It subtracts given seconds from the last poll timestamp.
         * Response Group Element List: Specify the elements to be included as part of the response received from Workday. Worker\_Response\_Group section in Workday Get\_Workers API displays the list of all the elements that can be included. This list has the following default values:

           + Include\_Reference
           + Include\_Additional\_Jobs
           + Include\_User\_Account
           + Include\_Personal\_Information
           + Include\_Employment\_Information
           + Include\_Organizations
           + Exclude\_Company\_Hierarchies
           + Exclude\_Matrix\_Organizations
           + Include\_Transaction\_Log\_Data
           + Include\_Management\_Chain\_Data
         * Field and Parameter Criteria Provider Reference List: The integration system IDs will be placed in the Field\_And\_Parameter\_Criteria\_Data section of the GET SOAP API request.
         * *Transaction Log Criteria Reference List:*
           Enter the transaction type references to be checked for changes during normal polling. For more information on Additional transaction type references, see [Configuring the Driver to Include Additional Transaction Type References](t4finmpwdw5m.html). These are primarily Business\_Process\_Type transaction type references. To see changes for additional business processes, add the Business\_Process\_Type to this list. A few of the Business\_Process\_Type references configured by default are shown below:

           + Hire Employee
           + Add Additional Job
           + Add Retiree Status
           + Assign Matrix Organization
           + Assign Workers
           + Change Job
           + Change Business Title
           + Change Legal Name
           + Change Organization Assignments for Worker
           + Change Organization Assignments for Workers by Organization
           + Change Preferred Name
           + Change Personal Information
           + Contact Information Event
           + Demote Employee
           + Promote Employee
           + Edit ID Information
           + Change Personal Information
           + Edit Other IDs for Worker
           + Contact Information Event
           + Terminate Employee
           + Contract Contingent Worker
           + End Contingent Worker Contract
           + Transfer Employee
           + Transfer Contingent Worker
           + Request Leave of Absence
           + Request Return from Leave of Absence
           + Change Photo
           + Home Contact Information Event
           + Work Contact Information Event
         * Import Worker Stylesheet: Specify the absolute path to import custom stylesheet for worker. Leave this field empty to operate with default stylesheet. If stylesheet is configured, the data in the custom stylesheet will be merged with the default one.

           For example:

           + Linux: /home/NOVLSPML2-its-XDSInputTransform\_worker.xml
           + Windows: C:\NOVLSPML2-its-XDSInputTransform\_worker.xml
     + Job Profile:

       - Poll JobProfile: Select Enable to poll JobProfile objects from Workday.

         * Job Profile Poll Settings: Select Show to view JobProfile poll settings.

           + Response Group Elements List: Specify the elements to be included as part of the response received from Workday. The Job\_Profile\_Response\_Group section in Get\_Job\_Profiles API displays the list of elements that can be included.

             This list has the following default values:

             - Include\_Reference
             - Include\_Job\_Profile\_Compensation\_Data
             - Include\_Job\_Profile\_Basic\_Data
           + Field and Parameter Criteria Provider Reference List: Specify the integration system IDs for the override fields created in Workday. The integration system IDs will appear in the Field\_And\_Parameter\_Criteria\_Data section of the GET request criteria.
           + Import Job Profile Stylesheet: Specify the absolute path to import custom stylesheet for job profile. Leave this field empty to operate with default stylesheet. If stylesheet is configured, the data in the custom stylesheet will be merged with the default one.

             For example:

             - Linux: /home/NOVLSPML2-its-XDSInputTransform\_jobprofile.xml
             - Windows: C:\NOVLSPML2-its-XDSInputTransform\_jobprofile.xml
     + Scheduled API:

       - Scheduler: Specify the time of the day to poll objects from Workday. This is applicable to objects such as, Terminated Workers, Location, Organization job Family, and Worker Photo.
     + Terminated Workers:

       - Poll Terminated Workers: Select Enable to poll JobProfile objects from Workday.

         * Terminated Workers Poll Settings: Select Show to view JobProfile poll settings.
         * Termination Business types to poll: Specify the list of worker business termination types to poll. For example, Terminate Employee, End Contingent Worker Contract.
         * Number of days to fetch: Specify the number of days to be queried for terminated workers.
     + Location:

       - Poll Location: Select Enable to poll Location objects from Workday.

         * Location Poll Settings: Select Show to view Location poll settings.
         * Location Types to Poll: Specify the list of location types to poll. The Location\_Type\_Reference section in Workday Get\_Locations API displays the list of elements that can be included.
         * Location Usage Types to Poll: Specify the list of location usage types to poll. The Location\_Usage\_Reference section in Workday Get\_Locations API displays the list of elements that can be included.
         * Response Group Elements List: Specify the elements to be included as part of the response received from Workday. The Location\_Response\_Group section in Workday Get\_Locations API displays the list of elements that can be included.
         * Field and Parameter Criteria Provider Reference List: Specify the integration system IDs for the override fields created in Workday. The integration system IDs will appear in the Field\_And\_Parameter\_Criteria\_Data section of the GET request criteria.
         * Import Location Stylesheet: Specify the absolute path to import custom stylesheet for location. Leave this field empty to operate with default stylesheet. If stylesheet is configured, the data in the custom stylesheet will be merged with the default one.

           For example:

           + Linux: /home/NOVLSPML2-its-XDSInputTransformJocation.xml
           + Windows: C:\ NOVLSPML2-its-XDSInputTransform\_location.xml
     + Worker Photo:

       - Poll Worker Photo: Select Enable to poll worker’s photo from Workday.

         * Worker Photo Poll Settings: Select Show to view worker’s photo poll settings.
         * Resize Worker Photo: Select Yes to resize the worker’s photo.

           + Maximum Photo Height: It is recommended to specify the maximum photo height as 200.
           + Maximum Photo Width: It is recommended to specify the maximum photo width as 140.
           + Worker Photo Attribute Settings:

             - Compress Worker’s Photo: Resize worker’s photo to the specified height and width and stores it in Identity Vault’s photo attribute. The Identity Vault’s photo attribute will store only those photos which are less than 64KB in size.
             - Compress Worker’s Photo and Retain the Original Photo File: Resize the worker’s photo to the specified dimensions and stores it in Identity Vault’s photo attribute. Also, stores a copy of the original photo in the wd-originalPhoto photo stream attribute.
         * Photo Update Report URL: Specify the URL for Workday Photo Update Report.
         * Photo Update Calculated Field: Specify the Calculated Field created on Workday. This field records the DateTime value for last photo update event for the workers.
         * Photo Report Namespace: Specify the namespace of the custom report under Web Services Options.
         * Import Worker Photo Stylesheet: Specify the absolute path to import the custom stylesheet for Worker Photo. Leave this field empty to operate with default stylesheet. If stylesheet is configured, the data in the custom stylesheet will be merged with the default one.

           For example:

           + Linux: /home/NOVLSPML2-its-XDSInputTransform\_workerphoto.xml
           + Windows: C:\ NOVLSPML2-its-XDSInputTransform workerphoto.xml
     + Job Family:

       - Poll JobFamily: Select Enable to poll job family objects from Workday.

         * Job Family Poll Settings: Select Show to view Job Family poll settings.
         * Response Group Elements List: Specify the elements to be included as part of the response received from workday. Job\_Family\_Response\_Group section in Workday Get\_Job\_Families API displays the list of elements that can be included.
         * Field and Parameter Criteria Provider Reference List: Specify the integration system IDs for the override fields created in Workday. The integration system IDs appear in the Field\_And\_Parameter\_Criteria\_Data section of the GET request criteria.
         * Import Job Family Stylesheet: Specify the absolute path to import custom stylesheet for job family. Leave this field empty to operate with default stylesheet. If stylesheet is configured, the data in the custom stylesheet will be merged with the default one.

           For example:

           + Linux: /home/NOVLSPML2-its-XDSInputTransformjobfamily.xml
           + Windows: C:\NOVLSPML2-its-XDSInputTransformjobfamily.xml
     + Organization:

       - Poll Organization: Select Enable to poll organization objects from Workday.

         * Organization Poll Settings: Select Show to view organization poll settings.
         * Response Group Elements List: Specify the elements to be included as part of the response received from workday. Organization\_Response\_Group section in Workday Get\_Organizations API displays the list of elements that can be included.
         * Field and Parameter Criteria Provider Reference List: Specify the integration system IDs for the override fields created in Workday. The integration system IDs appear in the Field\_And\_Parameter\_Criteria\_Data section of the GET request criteria.
         * Import Organization Stylesheet: Specify the absolute path to import custom stylesheet for organization. Leave this field empty to operate with default stylesheet. If stylesheet is configured, the data in the custom stylesheet will be merged with the default one.

           For example:

           + Linux: /home/NOVLSPML2-its-XDSInputTransform\_organization.xml
           + Windows: C:\NOVLSPML2-its-XDSInputTransform\_organization.xml
     + Advanced Entitlement Settings:

       - Advanced Entitlement Settings: Select the value as Show to configure the entitlement settings.

         * Staffing Web Service URL: Enter the URL of the staffing web service specific to your tenant. The procedure to obtain the staffing web service URL is similar to obtaining the Workday login URL (as shown in the [Connection Parameters](t4avmq79xc47.html#connec_params) table), except that you must perform a search for Staffing (Public) instead of HR Services (Public).
         * Organization Types ID Values List: The list of values of Organization\_Type\_IDs for the organizations that you want to collect the role entitlements for. If you specify any values here, only then the filter is applied. Else, by default IDV considers all the Organization Type ID values defined in Workday.

           For example, some the standard Organization Type ID values are:

           + Supervisory
           + Cost\_Center
           + Company
           + Cost\_Center\_Hierarchy
           + Matrix
           + Region, etc.

   *NOTE:*Identity Console does not support full migration of objects from Workday Identity Vault if you select the Migrate into IDVault option. To migrate all objects, you must set the values in Migration on Startup or Scheduled Polling fields accordingly in the Driver Parameters in Designer.
9. Fill in the following fields for the Remote Loader information, then click Next:

   *Connect To Remote Loader:*
   Select Yes or No to determine if the driver will use the Remote Loader. For more information, see [Configuring the Remote Loader and Drivers](../../../identity-manager-49/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Install and Upgrade Guide for Linux](../../../identity-manager-49/setup_linux/data/front.html#front).

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
10. On the Install Workday Default Configuration page, fill in the following fields for User - Publisher settings and Advanced Settings, then click Next:

    *Merge Employee and Contingent workers:*
    Select true to merge Employee and Contingent workers in Identity vault. Selecting the value as true will maintain a single user object in Identity vault for converting an employee to contingent worker, or vice-versa.

    *User Placement Container:*
    This global configuration value is used to get a reference to the container IDV where new users will be created. It may be different than user search container. The DN is expected in slash-format such as data\workday\users. If you want to configure a custom container, specify custom as the value and define a custom placement policy.

    *User Search Container in:*
    This global configuration value is used to get a reference to the container where Workday users are stored. This value is used for all workers (both Employee and Contingent workers). If you want separate containers for different type of users, then use custom option in matching/creation/placementpolicy. The DN provided here should in slash-format, such as data\workday\users.

    *Default Password Policy:*
    Specify the path for the default password policy to be used while creating random password for new Users, for example Security\Password Policies\Sample Password Policy. A sample policy NETQWDDCFG-pub-cp-user-default-password is added in the default configuration package. This policy adds a random password to new users created in Identity Vault. The password generated confirms to the password policy configured in the GCV (default.password.policy). This policy has to be added to the creation policy set to get executed.

    *User Advanced Settings:*
    If this option is set to show, fill the following fields:

    * Creation Settings: If this option is set to show, fill the following fields:

      + *Mandatory Attributes for User creation:*
        Lists all the required attributes for creating a new user object. Each of the specified attributes must be included in the Publisher filter. By default, the following attribute are available to select. You can add any custom attribute by clicking on the ![](../graphics/icon_plus_green_n.png) icon:

        - Given Name
        - Surname
        - WorkforceID
        - wd-WorkerIDType
        - wd-UserName
      + *User CN Attribute:*
        Specify the name of an attribute to be used for creating CN of user. If custom policy is defined to create CN, mention the value as Custom.
    * Match Settings: If this option is set to show, fill the following fields:

      + *Matching Attributes for User:*
        Select a method for matching the users in IDV. Select Custom, if you want to add a customized policy. The system provide following options to match the user under publisher matching policy:

        - Match WorkforceID
        - Match CN
        - Match all above in order
        - Match Custom-Define yourself
    * Contact Settings: If this option is set to show, fill the following fields

      + *Default Country ISO Code:*
        Specify the default country ISO Code for modifying the contact data.
      + *Work Contact Usage Type:*
        Specify the value of communication usage type as configured in Workday for work contact information.
      + *Home Contact Usage Type:*
        Specify the value of communication usage type as configured in Workday for home contact information.
      + *Work Phone Contact Details:*
        Specify the mapping attributes for different types of contact devices used at work.

        - *Device Type:*
          Specify the ID of the contact type as configured in Workday. For example, Landline, Mobile etc.
        - *Attribute Name:*
          Specify the name of an attribute, which holds the contact values for the given device type. If there is only a single value for th given device type, you can specify a single-value or a multi-value type. In case, there are multiple values for the given device type, you must only specify multi-value attribute.
      + *Home Phone Contact Details:*
        Specify the mapping attributes for different types of contact devices used at home.

        - *Device Type:*
          Specify the ID of the contact type as configured in Workday. For example, Landline, Mobile etc.
        - *Attribute Name:*
          Specify the name of an attribute, which holds the contact values for the given device type. If there is only a single value for th given device type, you can specify a single-value or a multi-value type. In case, there are multiple values for the given device type, you must only specify multi-value attribute.
      + *Country Phone Codes:*
        Select the country phone code of the user. You can add a country phone code that are available in Workday. For the procedure to fetch a country phone code from Workday, see [Fetching Country Phone Code ID and Phone Type ID from Workday](t4finm0426n2.html#t4finohor8km).
11. On the subsequent installation pages, fill the following fields as shown in the respective <Object> - Publisher Settings pages, then click Next:

    *<Object> Placement Container:*
    This global configuration value is used to get a reference to the container in IDV where new objects will be created. It may be different than object search container. The DN is expected in slash-format such as Data\Workday\relation. If you want to configure a custom container, specify custom as the value and define a custom placement policy. The following containers are created by default:

    * Relation Objects: data\workday\relation
    * Job Family Objects: data\workday\jobfamily
    * Location Objects: data\workday\location
    * Photo Objects: data\workday\photo
    * Job Profile Objects: data\workday\jobprofile
    * Organization Objects: data\workday\organization

    *<Object> Search Container:*
    This global configuration value is used to search the container in IDV. The DN is expected in slash-format such as Data\Workday\relation.

    *NOTE:*The field values for the search containers are the same as placement containers.

    *Advanced Settings:*
    Defaults to Hide, set as Show to configure advanced settings for the object. The associated fields to configure the advanced settings appear.

    * Advanced Settings

      + <Object> Advanced Settings: Defaults to Hide, set as Show to configure advanced settings.

        - Creation Settings

          * Mandatory Attributes for <Object> creation: Specify the list of required attributes for creating a new Photo object. Each of the attributes specified must be included in the Publisher filter.

            For example, wd-RelationID.
          * <Object> CN Attribute: Specify the attribute name used for CN creation of Photo.

            For example, wd-RelationID.
        - Match Settings

          * Matching Attribute for <Object>: Specify the Identity Vault attribute name mapped to the application attribute. This attribute must be part of Mandatory Attributes list in creation settings.

            For example, wd-relationID
12. In the Retry Attributes page, specify a comma separated list of attribute modifications to retry when the user is activated in the Attributes to modify when the user is activated.

    For example, wd-HomePrimaryPhone, wd-WorkPrimaryPhone, Internet EMail Address, homeEmailAddress
13. Review the summary of tasks that will be completed to create the driver, then click Finish.
14. After you have installed the driver, you can change the configuration for your environment. or more information, see [Creating the Driver Object](t4avmq79xc47.html).
