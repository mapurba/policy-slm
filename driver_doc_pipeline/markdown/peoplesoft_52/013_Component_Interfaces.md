# 3.3 Component Interfaces

* [Accessing Transactions and Data through Component Interfaces](component-interfaces.html#ah6p4ij)
* [Configuring the Transaction Record SQL Date/Time Format](component-interfaces.html#bt35ere)
* [Configuring PeopleCode to Trigger Transactions](component-interfaces.html#ah4p176)
* [Testing Component Interfaces](component-interfaces.html#ajn78pl)

## 3.3.1 Accessing Transactions and Data through Component Interfaces

The driver accesses transactions waiting to be processed from the transaction table via the Component Interface (CI) object that is defined within PeopleTools. Each CI maps to a particular component. Components are built in order to access transaction tables and “schema” application object data. Schema objects represent all the necessary fields and methods that need to be exposed for data synchronization to the driver. These objects also enable the driver to update PeopleSoft data.

Each driver uses only one Transaction CI to access transactions. Every transaction is assigned to one default Schema CI. In the driver’s parameters, you must specify the Transaction CI object name as defined in PeopleSoft. This CI object maps to a predefined component that enables the driver to access transactions from one transaction table. The following represents the CI for a transaction table:

*Figure 3-2* Transaction Table Component Interface (CI)

![](../graphics/peoplesoft-table-component-infrastructre-3-2.jpg)

In addition to the Transaction CI name, the driver configuration contains a parameter that can specify a particular subset of the transactions that are available for processing. This allows a single Transaction CI to interface with multiple drivers, which might be synchronizing different sets of object data or different object types. This subset identifier is maintained in the DIRXML\_DRIVER field of the Transaction CI.

The following figure represents the CI for a Schema Component:

*Figure 3-3* Schema Component

![](../graphics/peoplesoft-schema-endpoint-3-3.jpg)

The PeopleSoft developer can specify these values when configuring the PeopleCode function calls to trigger a transaction online, or when creating transactions via a batch process. The PSA provides PeopleCode function DirXML\_Trans and is responsible for generating transaction events. The PSA contains several function calls which you may use to guide customization.

The PeopleCode DirXML\_Trans schema calls should always be placed in the SavePostChange PeopleCode on the record definitions. This ensures that the data is committed prior to the transaction being generated.

#### Changes to Field Names in PeopleSoft 8.41

With new releases of PeopleTools, changes are made to the policies regarding field names. With PeopleTools 8.41, there were two significant changes:

* Spaces are no longer allowed in CI field names.
* There are now case sensitivity issues in the CI API. Field names and field name values no longer align because of case-sensitive sorting. For example, a field named CN is sorted prior to a field named City. The result of trying to access the value of City returns the value for CN. The default schema of the CIs used by the driver now uses naming conventions that eliminate this unusual sorting error. This issue is particularly important for any field name modifications or additions customized for a prior implementation of the driver.
* Use the standard ALL-CAPS format to avoid any field name issues.

## 3.3.2 Configuring the Transaction Record SQL Date/Time Format

The proper functioning of the driver depends on the Date/Time strings in the Transaction View record to determine processing availability and relative event order of Transaction data rows. The Date/Time fields in the Transaction data rows are converted to formatted strings in the Transaction Views by using the PeopleCode Meta-SQL%DateTimeOut() function. The following image shows the default SQL View code for the DIRXML\_TRANS01V record:

*Figure 3-4* SQL View of Code for the DirXML\_TRANS01V Record

![](../graphics/peoplesoft-sql-records-3-4.jpg)

Unfortunately, the format of the strings presented by %DateTimeOut() might differ depending on the underlying DBMS software. To make sure a date and time string is generated in a consistently increasing lexicographic format, the following format is recommended:

* The date should be presented first in YYYY-MM-DD format.
* The time should be presented in 24-hour form with HH:MM:SS format (Additional information concatenated to this string, such as <milliseconds> is acceptable)
* These two strings should be placed together in “date-time” format.

The characters used to delimit the numerical values are not important as long as they are consistent. Examples of a well-formed, lexicographically ordered format are:

2004-08-26-14.44.33.000000 (ODBC Canonical style 121)

or

2004/08/26-14:44:33 (Generic)

The fields used by the driver are DIRXML\_DTTM\_ST and DIRXML\_CURRDTTM\_ST. These fields represent the date and time that the Transaction data row was created and the current processing date and time of the transaction.

If you are using a driver trace level of 2 or above, the driver traces the CurrDate and ActionDate of each Transaction row that it processes. If the format shown does not match the criteria specified, edit the SQL of the desired Transaction View record to perform the appropriate conversions on these fields. Make sure that you use the Build > Create Views option after making any modifications to the SQL definition of the View Record.

Because the configuration of the Date and Time format varies depending on the DBMS being utilized, changing this format should be done by the DBMS/PeopleSoft Database Administrator or other qualified personnel.

## 3.3.3 Configuring PeopleCode to Trigger Transactions

The PSA contains a number of PeopleTools objects that enable PeopleSoft to trap events into a transaction table. The driver then accesses the transaction tables through CI objects. The driver periodically requests transactions that need to be processed, based on their driver subtypes. It processes only those transactions that have a transaction date or time less than or equal to the current date or time value, along with an available status. Also, the driver processes transactions one at a time from the transaction table before getting a new transaction.

The driver then constructs an XML document from the data it retrieved and passes this to the Identity Manager engine for processing. It updates the transaction status and any applicable messages on the transaction table inside of PeopleSoft after processing is completed by the Identity Manager engine. When events occur within eDirectory, the driver connects to the appropriate CI and updates the PeopleSoft staging table as appropriate.

You trigger transactions using PeopleCode within the PeopleSoft application.This document assumes that you know how to write PeopleCode. If you need further assistance, refer to PeopleSoft documentation for more information.

The driver requires a Transaction CI and a Schema CI to process transactions. For more information on calling the PeopleSoft function that creates transaction records, please refer to [Customizing the PSA by Triggering Transactions](customize-psa-trigger-transactions.html).

* [Transaction Component](component-interfaces.html#ah4p1ql)
* [Schema Component](component-interfaces.html#ah4p1yx)

### Transaction Component

The Transaction Component interface enables the driver to request transactions by driver subtype, date and time, and event type. The driver requests a single transaction for processing and obtains the object ID for the record being processed.

When the driver selects the first transaction to process, it sets the status of the transaction to In Process. The driver then retrieves the Event Name (DIRXML\_EVENT), which it uses to create an Add, Modify, or Delete XML document. The driver uses the Schema ID (DIRXML\_SCHEMA) and the Associate ID (DIRXML\_ASSOC\_ID) values to access the appropriate CI Schema and appropriate record information associated with the object.

After the transaction has been processed by the Identity Manager engine, the driver updates the status of the transaction (DIRXML\_STATUS) and updates the Comment field (DIRXML\_DESCR) if an error or warning message is applicable.

*Figure 3-5* DirXML Transaction01

![](../graphics/ps81trans01_a.png)

### Schema Component

The Schema Component interface lets the driver retrieve data for a particular record and update the PeopleSoft staging table for that record. After the driver retrieves the Association ID (DIRXML\_ASSOC\_ID) and Schema name (DIRXML\_SCHEMA), it accesses the appropriate Schema object.

The driver also uses Schema CI as a Class identifier for object type matching. When the driver accesses the Schema CI, it uses the value it received in the Association ID (DIRXML\_ASSOC\_ID) as the key value to retrieve the data from the PeopleSoft environment. It also uses this CI to update PeopleSoft records.

For example, assume you want to process transactions for an employee with the DIRXML\_ASSOC\_ID field (key) value = P000001. The driver accesses the Schema CI with a key value of P000001. It retrieves all of the configured component elements that have been defined for that employee. The driver then converts the data collection into XML documents to be consumed by the Identity Manager engine. If there is a write-back command processed, or when data is written on the Subscriber channel, the driver uses this CI to update the staging table with the appropriate information into PeopleSoft for this particular employee.

## 3.3.4 Testing Component Interfaces

The Component Tester program (CITester.class) is included as part of the driver package. The program validates the proper installation, configuration, and revision of the PeopleSoft PeopleTools client software on the computer hosting the Identity Manager Driver for PeopleSoft. The program also validates a selected Transaction CI and Schema CI. Successful operation of the CITester helps ensure the proper client functionality for the driver.

The CITester completes the following checks during four phases:

* Phase I: Ensures that a PeopleSoft client session can be created.
* Phase II: Ensures that connection and authentication parameters to the PeopleSoft Application Server are correct.
* Phase III: Verifies that the Transaction CI required fields and keys are present.
* Phase IV: Verifies that the Schema CI required fields and keys are present.

If you are not using the default Schema CI, it is necessary to build the APIs for the desired CI. See [Changing the Data Schema Component Interface](change-data-schema-interface.html) for information on building custom CI API JAR files.

There might be variations of the error message data depending on the PeopleTools release. The CITester program runs all platforms supporting Java 1.3.1 or later and uses the Java PeopleSoft Component Interface (psjoa.jar) package from the PeopleTools distribution.

* [Important Considerations](component-interfaces.html#bgy2f3z)
* [Running the Test](component-interfaces.html#bgy2f9b)
* [Phase I: Creating a PeopleSoft Client Session](component-interfaces.html#bu07pm9)
* [Phase II: Authenticating to the PeopleSoft Client](component-interfaces.html#bu07w8s)
* [Phase III: Authenticating to the PeopleSoft Client](component-interfaces.html#bu085xl)
* [Phase IV: Retrieving the Schema Component Interface](component-interfaces.html#bu08no2)
* [Summary](component-interfaces.html#bu08t7k)

### Important Considerations

When you run the test, you must do one of the following:

* Set the CLASSPATH environment variable to include the path of the CITester.class, psjoa.jar and dirxmlcomps.jar files. If a custom CI API JAR file is required, include it in CLASSPATH.
* Set the -classpath option on the Java command line to include the CITester.class, psjoa.jar and dixmlcomps.jar files and any required custom CI API JAR files.

In addition, the java.exe for JRE/JDK version 1.3.1 or later must be installed and accessible via the PATH environment variable or be explicitly called out from the Java command line.

### Running the Test

From a command shell, execute the CITester.class test file. A sample CITester.bat file is provided as a reference that indicates the correct syntax and class files required to execute the test and the driver. To accept the test’s default values, press Enter. In Phase II, you are required to enter a value for the Application Server name.

The test writes output to the screen and to CITesterOutput.txt. The output file is written to the location where CITester.class resides.

### Phase I: Creating a PeopleSoft Client Session

If the test program establishes a session with the PeopleSoft client, you see the following message:

```
** PeopleSoft client session established successfully.
```

You might encounter the following errors during the test:

| Error Message | Solution |
| Exception in thread "main" java.lang.NoClassDefFoundError: psft/pt8/util/PSProperties. | You must add a path to the 8.1x or 8.4x psjoa.jar file to the environment CLASSPATH variable or set the path to the psjoa.jar file in the Java command line.  This error also occurs if an invalid version of the JVM (JRE/JDK) is being used. Refer to the [Important Considerations](component-interfaces.html#bgy2f3z) at the beginning of this section for more information. |

### Phase II: Authenticating to the PeopleSoft Client

1. Specify the Application Server name or IP address. Forward slashes are required when you enter the Application Server name (for example, //255.255.255.255).
2. Specify the Application Server Jolt port number.
3. Specify the PeopleSoft UserID
4. Specify the PeopleSoft UserID password.

If the test program verifies the connection and authentication parameters, you see the following message indicating success:

```
** The Connection and Authentication Parameters are verified to be correct.
```

You might encounter the following errors during the test:

| Error Message | Solution |
| ERROR: Failed Connection to the PeopleSoft Application Server. Please make sure you entered your authentication information correctly.  PeopleSoft Error/Warning Messages Pending. Number of Messages: 1 Message 1: Connect Failed: No additional information available (90, 01) | The target Application Server generates error and warning messages. This error indicates that you entered the wrong Application Server name or Application Server port number.  Ensure that the server name or address you entered contains a leading double slash (//) and that the address and name data is correct. Also, verify that you entered the Jolt port configured on the Application Server. |
| ERROR: Failed Connection to the PeopleSoft Application Server. Please make sure you entered your authentication information correctly.  PeopleSoft Error/Warning Messages Pending. Number of Messages: 1 Message 1: DOWNbea.jolt.ServiceException: Invalid Session | This message indicates an invalid Application Server name or port number. In some instances, if an invalid port number is specified, the CITester program hangs and requires a manual interrupt. |
| PeopleSoft Error/Warning Messages Pending Number of Messages: 2  Message 1: PeopleTools release (8.<num>) from web server '' is not the same as Application Server PeopleTools release (8.<num>) Access denied. | This message indicates that the PeopleTools version of the specified psjoa.jar does not match the version of the target PeopleSoft Application Server. PeopleTools requires a version match of the client and server. |
| PeopleSoft Error/Warning Messages Pending. Number of Messages: 3  Message 1: <UserID>@<Client computer> is an Invalid User ID, or you typed the wrong password. User ID and Password are required and case-sensitive. Make sure you're typing in the correct upper and lower case.  Message 2: Failed to execute GetCertificate request  Message 3: Invalid certificate for user <User ID> | The target Application Server generates the error and warning messages. Either the UserID or User ID password are incorrect or have been entered with the incorrect case. |

### Phase III: Authenticating to the PeopleSoft Client

The driver uses a Component Interface (CI) to access application modification transaction records from the Application Server. The field definitions of this interface must be identical to the DIRXML\_TRANS01 CI delivered with the driver. This test phase validates the field definitions of the named Transaction CI.

Enter the Transaction CI name or press Enter to validate DIRXML\_TRANS01.

If the test program retrieves and validates that all required fields and elements are present, you see the following message:

```
** Retrieval of Transaction Component Interface "DIRXML_TRANS01" succeeded.

- Property 'DIRXML_ASSOC_ID' is present.
- Property 'DIRXML_CURRDTTM' is present.
- Property 'DIRXML_DESCR' is present.
- Property 'DIRXML_DRIVER' is present and validated as key field.
- Property 'DIRXML_DTTM' is present.
- Property 'DIRXML_EVENT' is present.
- Property 'DIRXML_FIELDKEY' is present.
- Property 'DIRXML_FIELDNAME' is present.
- Property 'DIRXML_INST' is present and validated as key field.
- Property 'DIRXML_PROCESSED' is present.
- Property 'DIRXML_SCHEMA' is present.
- Property 'DIRXML_STATUS' is present.
- Property 'DIRXML_VALUE' is present.

** Transaction Component Interface element validation succeeded.
```

You might encounter the following errors during the test:

| Error Message | Solution |
| PeopleSoft Error/Warning Messages Pending. Number of Messages: 4Message 1: Cannot find Component Interface {<Transaction CI Name>} (91,2) Message 2: Initialization Failed (90,7) Message 3: Not Authorized (90,6) Message 4: Failed to execute PSSession request ERROR: Retrieval of Component Interface <Transaction CI Name> failed. | The target Application Server generates error and warning messages. This error indicates that the Transaction CI name specified does not exist or cannot be found by the Application Server. Ensure that you specified the correct name. |
| -Property '<property field name>' is not required. | This is an advisory message. It indicates that an additional field or fields that are not required by the driver have been defined in the specified Component Interface. |
| ERROR: Transaction Component Interface element validation failed. Required Fields are not all present. | The specified Transaction Component Interface does not contain all of the fields required by the driver. Verify that you entered the proper Transaction Component Interface name and validate that all fields contained in the default DIRXML\_TRANS01 Component Interface are present. |
| ERROR: Property '<Key field name>' is not defined as key field. | A field in the Transaction Component Interface is present, but is not properly configured as a key field. The Transaction Component Interface DIRXML\_DRIVER and DIRXML\_INST fields must be specified as key fields. |

### Phase IV: Retrieving the Schema Component Interface

The Schema CI defines the application data that is to be synchronized via the driver. The specified Schema CI must contain a primary key field that is specified via the Data Record ID field name.

To test the Schema CI, type the Schema CI name or press Enter to retrieve DIRXML\_SCHEMA01. Enter the Data Record ID field name. If the test program retrieves and validates that all required fields and elements are present, you see the following message:

```
** Retrieval of Schema Component Interface "DIRXML_SCHEMA01" succeeded.

- Property 'ASSOC_ID' is present and validated as key field.
- Property 'STATUS' is present.
- Property 'FULL_NAME' is present.
- Property 'FIRST_NAME' is present.
- Property 'MIDDLE_NAME' is present and validated as key field.
- Property 'LAST_NAME' is present.
- Property 'BIRTH_DATE' is present.
- Property 'DEPT_ID' is present.
- Property 'DEPT_LONG_DESCR' is present.
- Property 'DEPT_DN' is present.
- Property 'TITLE_ID' is present.
- Property 'TITLE_SHORT_DESCR' is present.
- Property 'TITLE_LONG_DESCR' is present.
- Property 'MANAGER_ID' is present.
- Property 'MAIL_DROP' is present.
- Property 'ADDRESS1' is present.
- Property 'CITY' is present.
- Property 'STATE' is present.
- Property 'POSTAL' is present.
- Property 'MANAGER' is present.
- Property 'COMMON_NAME' is present.
- Property 'DISTINGUISHED_NAME' is present.
- Property 'DESCRIPTION' is present.
- Property 'EMAIL_ID' is present.
- Property 'PHONE_BUSN' is present.
- Property 'PHONE_CELL' is present.
- Property 'PHONE_HOME' is present.
- Property 'PHONE_PGR' is present.
```

```
** Schema Component Interface element validation succeeded.
```

```
** All expected platform support is verified correct.
```

You might encounter the following errors during the test:

| Error Message | Solution |
| PeopleSoft Error/Warning Messages Pending. Number of Messages: 4 Message 1: Cannot find Component Interface {<Schema CI Name>} (91,2) Message 2: Initialization Failed (90,7) Message 3: Not Authorized (90,6) Message 4: Failed to execute PSSession request ERROR: Retrieval of Component Interface <Schema CI Name> failed. | The target Application Server generates error and Warning messages. This error indicates that the specified Schema CI name does not exist or cannot be found by the Application Server. Ensure that you specified the correct name. |
| ERROR: Specified Schema Component Interface Data Record ID Field '<Data Record ID Field Name>' not found. | The field name specified as the key field of the Schema Component Interface is not in the Component Interface definition. Verify that you entered the proper field name. |
| ERROR: Property '<Data Record ID Field Name>' is not defined as key field. | The field name specified as the key field of the Schema Component Interface is present but is not properly defined as the key field. Validate the Component Interface definition or verify that the proper field name was specified. |

### Summary

At the completion of the test, the program provides a summary containing the results of the test. The validated parameters are shown below in the summary.

```
Component Interface Test Summary
--------------------------------
Full Component Interface Functionality has been verified.
The following parameters may be used for PeopleSoft 5.0 Driver Configuration

Authentication ID            : PSADMIN
Authentication context     : //255.255.255.255:9000
Application Password      : PSADMIN
Schema CI Name             : DIRXML_SCHEMA01
Data Record ID Field       : ASSOC_ID
Transaction CI Name       : DIRXML_TRANS01
```
