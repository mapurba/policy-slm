# 3.2 Installing the PSA Sample Project

Complete the following tasks to install the sample project for testing and configuration purposes:

* [Installing the PSA Files](install-psa-sample-project.html#bt34zfm)
* [Importing the PSA Project into the PeopleSoft Database](install-psa-sample-project.html#ah6n9o5)
* [Building Project Record Definitions](install-psa-sample-project.html#ah3mpzf)
* [Applying Security to the PSA](install-psa-sample-project.html#amfhvou)
* [Understanding the Architecture of the PSA Sample Project](install-psa-sample-project.html#bt352p7)
* [Testing Sample PeopleSoft Applications](install-psa-sample-project.html#ah3mqoy)

## 3.2.1 Installing the PSA Files

If you did not install the PSA during the initial driver installation, locate the product CD or download, go to the PeopleSoft application server, and run install.exe. You should see the following PSA files on your target server:

* DIRXML\_PSA50\_TOOLS84.exe for PeopleTools 8.5x

  *NOTE:*For installing PeopleSoft 8.5 version, use the DIRXML\_PSA50\_TOOLS84.exe file. There is no change in the installation procedure for PeopleSoft 8.5x from PeopleSoft 8.4x version.

These files are self-extracting zip files that contain the PSA project folder and files for the different versions of PeopleTools. Extract the appropriate file onto the file system of your PeopleSoft Application Designer host (c:\psa).

To ensure that the PSA can be imported into the PeopleSoft Application server, make sure that the PSA files have write access enabled. For example, in Windows, you should turn off read-only file properties.

## 3.2.2 Importing the PSA Project into the PeopleSoft Database

After the PSA files have been installed in an accessible file system location, they must be imported into the PeopleSoft Database via the PeopleSoft Application Designer tool.

* [PeopleSoft 8.5x](install-psa-sample-project.html#bgy286y)

### PeopleSoft 8.5x

1. Connect to the PeopleSoft database as administrator in two tier mode.
2. In the Application Designer, select Tools > Copy Project> From File.
3. Click Browse and select the PSA project directory: c:\psa\DIRXML\_PSA50\_TOOLS84.
4. Click Open.
5. Select all object types, then click Copy to copy all project components into the PeopleSoft database.

## 3.2.3 Building Project Record Definitions

After you have imported the project into the PeopleSoft database, you should build project record definitions and project views.

1. Log in to the PeopleSoft Application Designer by using an administrator username that has administrative and development rights.
2. In the Application Designer, select Build > Project.
3. In Build Options, click Create Tables and Execute SQL Now. After the project tables are created, click Close to close the Build Progress window.
4. Click Build to create sample project tables.

   You must create project tables before creating the views. Views are created with information from table fields.
5. In the Application Designer, select Build > Project.
6. In Build Options, click Create Views and Execute SQL Now.
7. Click Build to create the sample project views. After views are created, click Close to close the Build Progress window.

## 3.2.4 Applying Security to the PSA

In order for the driver to access PeopleSoft transaction tables, you need to apply security to the PSA. You accomplish this by creating the DirXML Administrator role and then assigning it to the administrative user. You can assign the role to an existing account or create a new account specifically for PSA security.

* [PeopleSoft 8.5](install-psa-sample-project.html#bgy290f)

### PeopleSoft 8.5

1. Log in to the PeopleSoft portal.
2. Click PeopleTools > Security > Permissions & Roles > Roles.
3. Click Add a New Value, then specify a role name (for example, DirXML Administrator).
4. Type a description for the role.
5. (Optional) Type a long description for the role.
6. Click the Permissions List tab.
7. Search for and select the DirXML permissions list, then click Save.
8. Assign DirXML Administrator role to your administrative user by clicking PeopleTools > Security > User Profiles > User Profiles.
9. Click Search to locate the User Profile that you want to add the DirXML Administrator role to, then click the User ID.
10. Click the Roles tab, then click one of the + buttons to add a new role.
11. Search and select the role, click DirXML Administrator to add it, then click Save.

## 3.2.5 Understanding the Architecture of the PSA Sample Project

The PSA Sample project is intended to provide recommended PeopleSoft integration scenarios through the use of very comprehensive instructions and examples. The various elements of the PSA are completely independent of any existing PeopleSoft application software, so there is no risk of data table corruption, extension, or modification.

The objects of the PSA include:

* Field definitions
* Record definitions
* Page definitions
* Component definitions
* Component Interface definitions
* Menu definitions
* SQL code

All of these objects are named with a prefix of DIRXML\_ so that they cannot be confused with existing objects.

* [Sample Application](install-psa-sample-project.html#bgy2a1j)
* [Staging Table](install-psa-sample-project.html#bgy2a6m)
* [Transaction Table](install-psa-sample-project.html#bgy2ads)
* [PSA Best Practices](install-psa-sample-project.html#bt358u5)

### Sample Application

This application is intended to simulate the data and functions of an HR or other type of Person provisioning application. The base Record definitions for the application are:

* DIRXML\_S\_PERS: Provides basic HR field data
* DIRXML\_S\_DEPT: Sample Department codes table
* DIRXML\_S\_PHONES: Phone Numbers table

The data is accessed through the DIRXML\_ADMINISTRATOR menu options. The menu provides access to a DirXML Sample People component and a DirXML Sample Department component. These applications simulate the standard methods for adding and updating Department and Person data into the PeopleSoft database. The driver default configuration does not directly access any of these tables or components. Additionally, the data provided by this application is not passed directly to the driver from these components. The actual transfer of data takes place through staging table components.

### Staging Table

The staging table interface is designed to insulate the PeopleSoft Application data from direct manipulation by the driver. This allows an interface to be designed to:

* Combine access to the data from multiple data tables and applications through a single interface.
* Prevent the driver from viewing or modifying sensitive application data.
* Provide storage for external data that does not easily fit into standard PeopleSoft applications.

The Record definition that represents all of the data that can be published or subscribed by the driver is called DIRXML\_STAGE01. This record aggregates most of the data fields from the three Application data records into a single access point. There are also additional fields not in the Application records that are used to contain references to the synchronized eDirectory objects.

For PeopleSoft users, the data in the staging table can be accessed via the DirXML Schema 01 component of the DIRXML\_ADMINISTRATOR menu. The driver accesses the data via the DIRXML\_SCHEMA01 Component Interface.

### Transaction Table

Every time a modification is made to the Application Data Records, transaction records are placed in the DIRXML\_TRANS01 table. The PSA places identifiers indicating the key of the data row being modified, the time of the event, the type of event, and various other pieces of transaction related data. Any change made to a data row via the DIRXML\_ADMINISTRATOR application interfaces is recorded with an NPSDriver1P identifier that shows the data is being published by a PeopleSoft administrator. Changes made via the Component Interface API are recorded with an NPSDriver1S identifier that shows the data was subscribed into the application tables programmatically.

In addition to providing an audit trail of database modifications, the transaction table is utilized by the driver to facilitate Publisher channel activities. The driver polls the transaction table for records in the Available state, reads the related application data record, and processes the data through the Publisher channel. The transaction records are then updated with the processing status.

In addition to the transaction tables and interfaces, the PSA includes utilities to monitor, maintain, archive, and remove transaction records.

### PSA Best Practices

Data moves between the various PeopleSoft components and tables through PeopleCode. Each of the application data records in the PSA contains PeopleCode that performs the basic functions of moving data between the Staging table and Application tables, ensuring the integrity of the data and data transfers, and generating Transaction table records at the appropriate time and with the appropriate data. PeopleCode is very powerful and is capable of performing a wide variety of tasks, some of which are potentially destructive to your data.

*IMPORTANT:*Only personnel who have completed PeopleTools and PeopleCode training should modify the elements of the PSA.

These guidelines might prove helpful when implementing changes to the PSA.

* Whenever possible, always provide a Component Interface (CI) to affected data tables. In the PSA, the DIRXML\_S\_PERS data rows are created and updated with PeopleCode via the DIRXML\_TST\_PERS CI. The CI guarantees the integrity of the data as defined by the designer of the application. It ensures that valid Translate values, proper data format, and required fields are present. Most importantly, the CI can restrict the data fields that can be accessed on a particular record or record set. This is a very important aspect of data security.
* The DIRXML\_SCHEMA01 CI has been extended with a Delete method that enables removal of data schema records via the driver’s Subscriber channel. Using this functionality is not required. The method can be removed from the CI or the driver can be configured to not use it.
* Make sure that the staging table record contains the same required fields that exist on the target Application records. This helps ensure successful record data synchronization.
* It is important to generate transactions whenever the application data table records are created or updated, even if the changes are made by the driver. Although data loopback can occur, the generation process ensures that Translate table values and related field values generated by the changes are properly synchronized.
* If you are using SQLExec() statements to update tables or create records, use great care to ensure that you are not violating the logic and rules of the applications overlying the tables. SQL is the easiest and most powerful, and therefore most destructive, method for updating data, but it is also the most potentially destructive.
* Do not generate Transaction records until after you have successfully updated the application tables.
* You can completely bypass the staging table interface in your synchronization scenario. The driver can be directed to interact with any CI. Make sure that the PeopleCode generating the transaction records is updated to specify the new Application data CI and is triggered appropriately. Also ensure that the same CI methods are implemented and enabled.
* The driver is delivered with a Java archive (JAR) file that contains the compiled Java interfaces for all of the CI defined in the PSA. If the driver is to be configured to use different application CIs, it is necessary to build and JAR those interfaces. For more information, refer to [Changing the Data Schema Component Interface](change-data-schema-interface.html).
* Test everything thoroughly.

## 3.2.6 Testing Sample PeopleSoft Applications

You can test to ensure that transactions are created and to validate that the application works. The following information explains how to create a Department and add a new person to test your sample application.

* [PeopleSoft 8.5x](install-psa-sample-project.html#bgy2c3g)

### PeopleSoft 8.5x

1. Log in to the PeopleSoft portal.
2. Click DirXML Administrator from the left menu.

   If the DirXML Administrator menu doesn’t appear, you should delete the Application Server cache and reboot the Application Server.
3. Click DirXML Sample Department.

   ![](../graphics/peoplesoft-add-dept-new.jpg)
4. Specify a sample department, then click Save.
5. Click DirXML Sample People.
6. Specify values for a sample user, then click Save and verify that the user's data appears in the Transaction01 table. You do this by searching in the DirXML Transaction01 application.
7. Verify that other delivered applications work by selecting them from the DirXML Administrator menu.
