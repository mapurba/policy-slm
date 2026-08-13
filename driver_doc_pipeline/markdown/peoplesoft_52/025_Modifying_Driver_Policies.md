# 6.3 Modifying Driver Policies

The following sections contains information to help you understand how the driver’s policies are implemented, as well as information about how you can modify these objects:

* [Modifying the Driver Mapping Policy](modify-driver-policies.html#ablp2kz)
* [Using the Schema Query to Refresh the PeopleSoft Schema Component Interface](modify-driver-policies.html#ablpdda)
* [Publisher Channel Objects](modify-driver-policies.html#bqugfmr)
* [Understanding the Publisher Filter](modify-driver-policies.html#ablpmxh)
* [Publisher Filter Attributes](modify-driver-policies.html#ablprpc)
* [Securing the Data](modify-driver-policies.html#ablprej)
* [Publisher Object Policies](modify-driver-policies.html#bqugi72)
* [Subscriber Channel Objects](modify-driver-policies.html#bquglt1)
* [Understanding the Subscriber Filter](modify-driver-policies.html#ah6ywkb)
* [Securing the Data](modify-driver-policies.html#ah6ywxi)
* [Modifying the Filter](modify-driver-policies.html#ah6ywyr)
* [Subscriber Object Policies](modify-driver-policies.html#bquhbzb)

## 6.3.1 Modifying the Driver Mapping Policy

The Mapping policy is a NetIQ eDirectory object that defines the relationship between data fields defined in the PeopleSoft application and eDirectory attributes. The Mapping policy is located in the driver object container and is used by both the Publisher and Subscriber channels of the driver.

A preconfigured default Mapping policy is delivered with the driver product. The mappings defined in the Mapping policy are designed in coordination with the preconfigured PeopleSoft application Component Interface (CI) that is also delivered with the driver product.

The default Data Schema CI is called DIRXML\_SCHEMA01 and represents a set of employee data. The data fields in this CI are mapped to similar attributes of the eDirectory User object.

The following is a short sample of the delivered Mapping policy in .xml format. The nds-name represents the name of the class or attribute in eDirectory and the app-name represents the class or field name of the PeopleSoft CI.

```
<?xml version="1.0" encoding="UTF-8"?> <attr-name-map>
     <class-name>
          <nds-name>User</nds-name>
          <app-name>DIRXML_SCHEMA01</app-name>
     </class-name>      <attr-name classname="User">
          <nds-name>Given Name</nds-name>
          <app-name>FIRST_NAME</app-name>
     </attr-name>      ... </attr-name-map >
```

When you modify or create a Mapping policy, verify that the PeopleSoft field names appear identically (spelling and capitalization) in the Mapping policy and PeopleSoft CI definition. If you use the Identity Manager Mapping policy editor, correct mapping behavior is ensured. It is also important to note that if new attributes are included or removed from the Mapping policy, the new attribute set should be reflected in the respective Publisher and Subscriber filters. If mapped attributes are not included in the filters, they cannot be synchronized.

## 6.3.2 Using the Schema Query to Refresh the PeopleSoft Schema Component Interface

By default, the schema that the driver reads from PeopleSoft consists of the data fields defined on the DIRXML\_SCHEMA01 CI. If the data elements are modified, the CI is renamed, or additional Data Schema CIs are added to the driver configuration, it is necessary to refresh the PeopleSoft application schema definition and re-map affected attributes.

## 6.3.3 Publisher Channel Objects

The Publisher object contains a filter and a set of policies. Policies are necessary for converting data from the PeopleSoft CI into XDS format. The driver then submits the data to the Identity Manager engine. The engine applies the Publisher filter to the data and applies the business logic defined by the Publisher policies prior to submitting the data to Identity Vault.

## 6.3.4 Understanding the Publisher Filter

The Publisher filter is a logical component of the driver filter object. The filter specifies the object classes and accompanying attributes that are passed from the PeopleSoft CI to eDirectory. The filter is defined by using eDirectory attribute naming, so it is applied after schema mapping takes place.

For example, if the User class is specified in the Publisher filter with only the Surname and Given Name attributes, the Identity Manager engine allows changes to only these attributes to be passed to the Publisher policies from the PeopleSoft Driver. If a Telephone Number attribute is modified, the Publisher filter removes this data from the event document because the Telephone Number attribute is not in the filter. Other attribute values can be created by the Publisher policies according to the integration scenario.

You can configure the Publisher filter to include attributes required by your environment and allowable by eDirectory access controls. Configure it to include the following:

* Object classes that you want to synchronize.
* Attributes on those objects that you want to synchronize.
* Attributes that are required by your Publisher policies. These attributes are not synchronized, but are required to perform some defined business logic that is to be applied to the synchronized data. These are known as “notify” attributes.

The Publisher filter specifies a set of data to be considered as authoritative from the PeopleSoft database. Based on business logic, there might be multiple authoritative sources of specific data (such as another driver or eDirectory itself). The configuration of the filters in your environment determines data ownership and authority.

## 6.3.5 Publisher Filter Attributes

By default, PeopleSoft applications are considered to be highly authoritative. Therefore, most of the field names in the default DIRXML\_SCHEMA01 Component Interface are passed through the Publisher filter. As noted earlier, the names of attributes in the filter are eDirectory attribute names that have been mapped via the Mapping policies.

The Publisher channel attributes listed below are included in the default filter:

*Table 6-2* Publisher Channel Attributes

| departmentNumber | OU |
| employeeStatus | pager |
| Full Name | Physical Delivery Office Name |
| Given Name | Postal Code |
| homePhone | S |
| Initials | SA |
| isManager | Surname |
| jobCode | Telephone Number |
| mailstop | Title |
| managerWorkforceID | workforceID |
| mobile |  |

Most of the attributes in the Driver Filter are configured for bidirectional synchronization. This is done for sample purposes to allow the driver to perform add, modify, and delete operations on both the Subscriber and Publisher channels. In most installations, the driver policies and filter are configured to function in either a predominant Subscriber or Publisher mode.

## 6.3.6 Securing the Data

PeopleSoft applications, like many other applications, contain sensitive data that must be highly secured by organizations. There are two ways to ensure that secure data is not published from the PeopleSoft application:

* Remove it from the synchronized data CI definition.
* Remove it from the Publisher filter.

The first method guarantees that the data does not leave the PeopleSoft application. The second method guarantees that the data is not synchronized to Identity Vault via the driver.

## 6.3.7 Publisher Object Policies

Policies contain rules or templates that perform specific operations that can manipulate data, query either Identity Vault or PeopleSoft for additional data required for processing, create new attributes based on values of other attributes, or even discard entire data events. The following sections explain each policy and describe the operations of each policy or template. Because XML, DirXML Script, and XSLT allow for great flexibility, all policies can be modified to meet the individual needs of your organization. The Mapping policy has been previously described and is addressed in this section under [Modifying the Driver Mapping Policy](modify-driver-policies.html#ablp2kz).

The Publisher channel object, by default, contains or uses the following policies:

* [Input Transformation Policy](modify-driver-policies.html#cacjihjd)
* [Matching Policy](modify-driver-policies.html#abn61wg)
* [Create Policy](modify-driver-policies.html#cacjbjdd)
* [Placement Policy](modify-driver-policies.html#cacfhcaf)
* [Command Transformation Policy](modify-driver-policies.html#cacdbgbj)

### Input Transformation Policy

The Input Transformation policy is implemented as a default policy for the PeopleSoft Driver. Although the Input Transformation policy is not exclusively used by the Publisher channel, it performs a publishing role because it is used to transform the data format of any XDS document received from the PeopleSoft Driver shim, regardless of which channel generated the submission of the document. That is, the Subscriber channel can issue object queries to the driver shim. All data returned in the response is processed through the Input Transformation policy. An example of data transformation contained in this policy is the transformation of character attributes in PeopleSoft to Boolean attributes in eDirectory.

#### Manager Flag Data Transformation Template

This template, contained in the Input Transformation policy, converts the Y or N data values in the PeopleSoft Manager attribute into True or False Boolean values to reflect the data format of the Identity Vault’s Manager attribute.

### Matching Policy

The Matching policy is used by the Identity Manager engine to apply criteria to determine if a matching data object already exists in Identity Vault. The Matching policy is applied to all Add documents received from the PeopleSoft Driver shim. If a match is found by this policy, the Add event is automatically converted to a Modify event by the Identity Manager engine. If a matched object in eDirectory is not currently associated with the PeopleSoft application, an association is created.

The Matching policy should provide criteria that are guaranteed to produce a 0 or 1 match. More than one policy can exist, and the Identity Manager engine applies them in the order that they are defined. Any policy producing 0 or more matches is skipped and the next policy is applied. Processing finishes when one match is found or after the last policy has been processed.

The default Publisher Matching policy is a DirXML Script policy that attempts to match eDirectory User objects containing the same value in the workforceID attribute (mapped from the DIRXML\_SCHEMA01 attribute). A secondary policy attempts to match using the Surname and Given Name attribute.

### Create Policy

The Create policy is used to specify the criteria for creating a new object after the Matching policy has failed to find a match. This policy performs various tests and transformations based on the requirements for object creation in eDirectory and the business logic being applied.

The default PeopleSoft Create policy is an XML policy that asserts that the <add> document is for a User object and that it must contain a Surname and Given Name attribute. The Surname attribute is mandatory in eDirectory, and the business logic used for object naming requires the existence of the Given Name attribute. If this criteria is met, a secondary XSLT style sheet policy is called to create the eDirectory Name attribute. A final policy is provided to append a default password to new User objects.

### Placement Policy

The Placement policy defines where an object is placed in the eDirectory tree when the object is created. This placement can be determined based on the presence (or absence) of attributes, particular values of attributes, etc. Placement can also be determined by the Create policy and passed to the Placement policy.

In a typical PeopleSoft HR environment, an employee is hired within PeopleSoft, a notification is sent to the IS department, and an IS administrator determines the location of the new User object in the eDirectory tree. Before defining location policies in the Placement policy, analyze your organization's current business process.

The default PeopleSoft Placement policy is a DirXML Script policy that handles placement of User objects based on the employeeStatus attribute. It uses the following order of processing: If the employeeStatus value is A, the employee is placed in the Organizational Unit specified by the Active Users Container GCV value. If the employeeStatus is I, the employee’s User object is placed in the Organizational Unit as specified by the Inactive Users Container GCV value. If the employeeStatus attribute is not present, the employee’s User object is placed in the Organizational Unit as specified by the Inactive Users Container GCV value.

### Command Transformation Policy

The Command Transformation policy is the final transformation policy to be processed prior to submission of a Publisher document to Identity Vault. To demonstrate this functionality, the default PeopleSoft Driver configuration implements an unusual example of business logic that demonstrates the flexibility and power of Identity Manager.

The business logic scenario is a requirement to maintain the object CN attribute and full distinguished name DN of each User in the PeopleSoft application. The CN attribute is generated on new objects when they are created in eDirectory. The DN is not a true attribute, but a concatenation of the directory path and CN of a User. The DN changes based on the employeeStatus attribute of an object, so it is set on User Add events and Delete events that are transformed into Move events.

Because this data is known during the processing of the Command Transformation policy, the CN and DN data is placed into an <operation-data> element appended to the document, causing the object to be added or moved. After Identity Manager applies the data to Identity Vault, a status document is returned. The Output Transformation policy (documented in the Subscriber channel) monitors status documents that are returned and transforms successfully processed documents with attached <operation-data> elements into modification documents that are applied to the PeopleSoft application. This is known as write-back functionality.

As the final transformation policy, the Command Transformation policy provides an excellent location to define operations that must be applied without the risk of further event transformation, thus allowing complicated policy processing to be programmed in one location. The bulk of the business logic transformations in the Publisher channel are implemented in this policy.

The following templates exist in the default Command Transformation policy. In addition to the listed templates, all Identity Manager policies contain identity-transform templates that allow the copying of XML attributes and elements that are passed through unmodified. The default configuration only handles documents related to User objects.

* [match <add> element](modify-driver-policies.html#bgy38ma)
* [match <modify> element](modify-driver-policies.html#bgy39dt)
* [get-empl-status](modify-driver-policies.html#bgy39ke)
* [get-empl-isManager](modify-driver-policies.html#bgy39qc)
* [get-empl-CN](modify-driver-policies.html#bgy39w5)
* [get-empl-managerWorkforceID](modify-driver-policies.html#bgy3a3e)
* [get-empl-ID](modify-driver-policies.html#bgy3ai6)
* [set-manager-on-user](modify-driver-policies.html#bgy3amc)
* [set-manager-on-direct-reports](modify-driver-policies.html#bgy3arf)
* [clear-manager-on-direct-reports](modify-driver-policies.html#bgy3axk)
* [set-directReports-on-manager](modify-driver-policies.html#bgy3b2a)
* [clear-directReports-on-manager](modify-driver-policies.html#bgy3b8h)
* [set-directReports-on-user](modify-driver-policies.html#bgy3bdb)

#### match <add> element

This template does the following:

* Tries to find the User’s manager. If the manager is found and the manager’s employeeStatus attribute is set to A, the template sets the manager and managerWorkforceID attribute on the User.
* Sets the Login Disabled attribute based on employeeStatus. If the status is A, Login Disabled is set to False. If the status is I, then Login Disabled is set to True.
* Adds or removes the Group Membership value based on the employeeStatus attribute value. All active employees with the isManager attribute set to False are placed into an Employee Group. All active employees with the isManager attribute set to True are placed into a Manager Group. The Group Membership attribute and associated links on the group objects are cleared if the employeeStatus is set to I.
* Determines placement of an object based on the employeeStatus attribute value. Active User objects are placed in an Active Organizational Unit. Inactive User objects are placed in an InActive Organizational Unit.
* Adds the manager attribute to any other active User objects in the directory whose managerWorkforceID attribute specifies this new User.
* Adds the directReports attribute value to any active User object in the directory that is specified by this User's managerWorkforceID attribute.
* Generates a write-back <operation-data> element to facilitate the addition of the CN and DN attributes in PeopleSoft.

#### match <modify> element

This template does the following:

* Tries to find the User’s manager. If the manager is found and the manager’s employeeStatus attribute is set to A, the template sets the manager and managerWorkforceID attribute on the User.
* Sets the Login Disabled attribute based on employeeStatus. If the status is A, Login Disabled is set to False. If the status is I, then Login Disabled is set to True.
* Adds or removes the Group Membership value based on the employeeStatus attribute value. All active employees with the isManager attribute set to False are placed into an Employee Group. All active employees with the isManager attribute set to True are placed into a Manager Group. The Group Membership attribute and associated links on the group objects are cleared if the employeeStatus is set to I.
* Adds the manager attribute to any other active User objects in the directory whose managerWorkforceID attribute specifies this new User.
* Adds the directReports attribute value to any active User object in the directory that is specified by this User’s managerWorkforceID attribute.
* If the employeeStatus is changing from I to A, generates a Move event with a write-back event-id to facilitate the modification of the DN attribute in PeopleSoft. This event moves the User object from the InActive Organizational Unit to the Active Organizational Unit.

#### get-empl-status

This template requests the value of the employeeStatus attribute from a specified User object in eDirectory.

#### get-empl-isManager

This template requests the value of the isManager attribute from a specified User object in eDirectory.

#### get-empl-CN

This template requests the value of the CN attribute from a specified User object in eDirectory.

#### get-empl-managerWorkforceID

This template requests the value of the managerWorkforceID attribute from a specified User object in eDirectory.

#### get-empl-ID

This template requests the value of the Identity Manager WorkforceID attribute from a specified User object in eDirectory.

#### set-manager-on-user

This template queries Identity Vault to determine if the passed-in managerWorkforceID parameter references an active User object in eDirectory. The name of the manager-User object is set in the User's manager attribute if the manager is active.

#### set-manager-on-direct-reports

This template receives a manager-User object ID parameter. A query is sent to Identity Vault for a list of all active Users who have the specified manager-User object ID in the managerWorkforceID attribute. The manager attribute of all Users in the list is set with the name of the manager-User.

#### clear-manager-on-direct-reports

This template receives a manager-User object ID parameter. A query is sent to Identity Vault for a list of all active Users who have the specified manager-User object ID in the managerWorkforceID attribute. The manager attribute of all Users in the list is removed.

#### set-directReports-on-manager

This template receives a manager-User object ID parameter. A query is sent to Identity Vault to find an active User who has the specified manager-User object ID in the workforceID attribute. The directReports attribute of the manager-User object is modified to include the DN of the User object specified in the source document.

#### clear-directReports-on-manager

This template receives a manager-User object ID parameter. A query is sent to Identity Vault to find an active User who has the specified manager-User object ID in the workforceID attribute. The directReports attribute of the manager-User object is modified to remove the DN of the User object specified in the source document.

#### set-directReports-on-user

This template receives a User object ID parameter. A query is sent to Identity Vault to find a list of active Users who have the specified User object ID in the managerWorkforceID attribute. The directReports attribute of the User object is modified to include the DN of all User objects in the list.

## 6.3.8 Subscriber Channel Objects

The Subscriber object contains a filter and a set of policies. These policies are necessary for converting data from Identity Vault to the PeopleSoft Driver.

The Identity Vault sends filtered data modification events to PeopleSoft through the Identity Manager engine. The engine applies the business logic defined by the Subscriber policies prior to submitting the data to the PeopleSoft Driver, which converts the data from the Identity Manager XDS format into PeopleSoft Component Interface format. The PeopleSoft Driver then submits the data to the PeopleSoft application and updates the staging table.

## 6.3.9 Understanding the Subscriber Filter

The Subscriber filter is a logical component of the Driver Filter object. The filter specifies the object classes and accompanying attributes that are passed from eDirectory to the PeopleSoft Component Interface. The filter is defined by using eDirectory attribute naming, so it is applied before schema mapping takes place.

For example, if the User class is specified in the Subscriber filter with only the mobile and pager attributes, the filter allows changes to only these attributes to be passed to the Identity Manager engine. If a Telephone Number attribute is modified, the Subscriber filter removes this data because the Telephone Number attribute is not in the filter. Other attribute values can be created by the Subscriber policies according to the integration scenario.

You can configure the Subscriber filter to include attributes required by your environment and allowable by eDirectory access controls. Configure it to include the following:

* Object classes you want to synchronize.
* Attributes on those objects you want to synchronize.
* Attributes that are required by your Subscriber policies. These attributes cannot be synchronized, but are required to perform some defined business logic that is to be applied to the synchronized data. These are known as “notify” attributes.

The Subscriber filter specifies a set of data to be considered as authoritative from Identity Vault or any other authoritative application that might have written the data to Identity Vault. Based on business logic, there might be multiple authoritative sources of specific data (such as another driver or eDirectory itself). The configuration of the filters in your environment determines data ownership and authority.

### Subscriber Filter Attributes

Most of the attributes in the Subscriber filter are configured for bidirectional synchronization. This is done for sample purposes to allow the driver to perform add, modify, and delete operations on both the Subscriber and Publisher channels. In most installations the driver policies and filter are configured to function in either a predominant Subscriber or Publisher mode.

The attributes listed below are included in the default Subscriber filter.

*Table 6-3* The Subscriber Channel Attributes

| CN | managerWorkforceID |
| departmentNumber | mobile |
| Description | pager |
| employeeStatus | Physical Delivery Office Name |
| Given Name | Postal Code |
| homePhone | S |
| Initials | SA |
| Internet EMail Address | Surname |
| jobCode | Telephone Number |
| mailstop | workforceID |

As mentioned previously, the Subscriber synchronization attributes in the Driver filter are present for demonstration purposes. It is very important to note that Subscriber filter and policies should be set to match the requirements of the PeopleSoft CI being utilized. If you want the ability to add objects on the Subscriber channel, make sure all required attributes in the CI are allowed to pass through the filter. Also make note of which fields in the CI are related display fields or translate values that cannot be synchronized, such as, Title, OU, and Full Name. By implementing and enforcing the CI application restrictions in your filter and policies, you encounter fewer synchronization errors and achieve higher throughput.

## 6.3.10 Securing the Data

If there is sensitive data that should not be shared with the PeopleSoft application, it should be removed from the Subscriber filter.

## 6.3.11 Modifying the Filter

A properly configured Subscriber filter promotes a secure environment and secures data sharing from Identity Vault to PeopleSoft. Make sure that attributes that are required for Subscriber policies processing (such as workforceID) are present in the filter even if they won't be synchronized to the PeopleSoft application.

## 6.3.12 Subscriber Object Policies

Policies contain templates that perform specific operations that can manipulate data, query either Identity Vault or PeopleSoft for additional data required for processing, create new attributes based on values of other attributes, or even discard entire data events. The following section explains each policy and provides a description of the operations each policy performs. Because XML, DirXML Script, and XSLT allow for great flexibility, all policies can be modified to meet the individual needs of your organization. The Schema Mapping policy has been previously described and is not addressed in this section. For information on the Schema Mapping policy, refer to [Modifying the Driver Mapping Policy](modify-driver-policies.html#ablp2kz).

The Subscriber object, by default, contains or uses the following policies:

* [Event Transformation Policy](modify-driver-policies.html#bt3744g)
* [Matching Policy](modify-driver-policies.html#ah6yx2b)
* [Create Policy](modify-driver-policies.html#ah6yydx)
* [Output Transformation Policy](modify-driver-policies.html#ah6z0sm)

### Event Transformation Policy

The Event Transformation Policy is used to remove or change received event types into different events. The following templates exist in the default Event Transformation Policy:

* [Match <rename> Element](modify-driver-policies.html#bgy3cya)
* [Match <move> Element](modify-driver-policies.html#bgy3d56)
* [Match <delete> Element](modify-driver-policies.html#bgy3db2)

#### Match <rename> Element

PeopleSoft does not allow the rename or modification of primary key values. This policy transforms a User Rename event into a Modify event that resets the CN and DISTINGUISHED\_NAME fields in the CI.

#### Match <move> Element

PeopleSoft does not support object containment or hierarchy. This policy transforms User Move events into Modify events that reset the DISTINGUISHED\_NAME field in the CI.

#### Match <delete> Element

This template is commented out by default to allow delete events to be passed to the driver. This policy remains for reference for non-delete scenarios. Previous versions of the driver did not support Delete events, so this template transforms them into Modify events that remove only Subscriber channel fields in the CI (CN, DISTINGUISHED\_NAME, Internet Email Address, and Description).

### Matching Policy

The Matching policy is used by the Identity Manager engine to apply criteria to determine if a matching data object already exists in the PeopleSoft application. The Matching policy is applied to all documents received from Identity Vault that contain User objects that are not currently associated with PeopleSoft objects. If a match is found by this policy, the Add event is converted into an object merge operation. This merge queries PeopleSoft for all attributes in the Publisher filter and applies them to Identity Vault, and queries Identity Vault for all attributes in the Subscriber filter and applies them to the PeopleSoft application. The process is finalized when an association value is written on the eDirectory User object.

The Matching policy should provide criteria that are guaranteed to produce a 0 or 1 match. More than one policy can exist, and the Identity Manager engine applies them in the order that they are defined. Any policy producing 0 or more than one match is skipped and the next policy is applied. Processing finishes when one match is found or after the last policy has been processed.

The default Subscriber Matching policy is an XML policy that attempts to find a PeopleSoft DIRXML\_SCHEMA01 object that contains an ASSOC\_ID attribute that matches the eDirectory User object’s workforceID attribute. If that policy fails, the driver uses another policy to locate a PeopleSoft DIRXML\_SCHEMA01 secondary object with a matching Given Name and Surname. The policy is defined in eDirectory class and attribute names because schema mapping has not yet been applied.

### Create Policy

The Create policy specifies the criteria for creating a new object after the Matching policy has failed to find a match. This policy performs various tests and transformations based on the requirements for object creation in the DIRXML\_SCHEMA01 CI in PeopleSoft and the business logic being applied.

The default Subscriber Create policy is a DirXML Script policy that asserts that the Add document is for a User object and that it must contain a value for Given Name, Surname, employeeStatus, departmentNumber, and jobCode. These fields are required because the default PSA has defined these fields as required in the DIRXML\_SCHEMA01 CI. (Additional required fields, such as BirthDate and Manager, have defined default values in the CI and are thus not required here.) By making sure all required fields are present before submitting the Add event to the driver, synchronization performance and integrity is enhanced.

This default policy does not assert particular values that are required for employeeStatus, departmentNumber, and jobCode in the PSA, but such assertions can be added to the Subscriber policies if desired.

### Output Transformation Policy

The Output Transformation policy is implemented as both a DirXML Script and an XSLT policy by default for the PeopleSoft Driver. Although the Output Transformation policy is not exclusively used by the Subscriber channel, it performs a subscribing role because it is used to transform the data format of any XDS document received from Identity Vault, regardless of which channel generated the submission of the document. An example of data transformation contained in this policy is the transformation of single-value eDirectory attributes into structured, multivalue scroll elements in PeopleSoft.

The following templates exist in the default Output Transformation policy. In addition to the listed templates, all Identity Manager policies contain identity-transform templates that allow the copying of XML attributes and elements that are passed through unmodified. Multiple instances of each listed template exist for each type of document or data element that can be received by the policy.

* [Write-back](modify-driver-policies.html#bgy3duc)
* [From-merge Write-back](modify-driver-policies.html#bgy3e0d)
* [Manager Flag Data Transformation](modify-driver-policies.html#bgy3e67)
* [Add DN Value to Subscribe Adds](modify-driver-policies.html#bgy3ea5)

#### Write-back

As documented in the Publisher channel Command Transformation policy, this template monitors all status document responses from Identity Vault. If a status document with a Success value is received and it contains <operation-data> with peoplesoft-cn and peoplesoft-dn values, the template holds the status document and issues a Modify document with the CN and DN values to the PeopleSoft application. When the write-back command completes, the original status document is returned to the Publisher channel.

#### From-merge Write-back

This policy behaves similarly to the [Write-back](modify-driver-policies.html#bgy3duc) policy, but it is applied to modify documents that are generated when the Identity Manager engine merges data on matched or resynchronized objects.

#### Manager Flag Data Transformation

This template converts the Boolean True and False values of the Identity Vault isManager attribute into character Y and N values of the PeopleSoft Manager field.

#### Add DN Value to Subscribe Adds

When objects are added to PeopleSoft, this policy adds the DN of the IDV object to the event attributes.
