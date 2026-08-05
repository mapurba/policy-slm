# A.2 Global Configuration Values

Global configuration values (GCVs) enable you to specify settings for the Identity Manager features such as password synchronization and driver heartbeat, as well as settings that are specific to the function of an individual driver configuration. Some GCVs are provided with the drivers, but you can also add your own.

In Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Locate the Delimited Text driver icon, then click the driver icon to display the driver’s properties page.
4. Click Global Config Values drop down to display the GCV page.

In Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select Properties > Global Configuration Values.

The Global Configuration Values are divided into the following categories:

* [Default Configuration](gcv-global-configuration-values.html#bry2spn)
* [Password Synchronization](gcv-global-configuration-values.html#bry2uzm)
* [Managed System Information](gcv-global-configuration-values.html#brnebcn)

## A.2.1 Default Configuration

The following GCVs control the configuration of the Delimited Text driver:

* *Field Delimiter:*
  Specifies the character that is used to delimit field values in the input files. It must be one character. You can also use the tab as the delimiter field value. Tab is represented as {tab}. The default is a comma.

  If the values of any of the input fields contain this character, enclose the entire value in quotes to prevent it from being seen as a delimiter. Changing this delimiter parameter to something other than a comma does not automatically change the delimiter character used in the output files when a Subscriber is used. To change the delimiter character in the output files, edit the Output Transform style sheet. The delimiter character is assigned to a variable at the beginning of that style sheet. For example, to change the delimiter, locate the <xsl:variable name="delimiter" select="','"/> line in the default style sheet and modify it appropriately.

  This option in the driver configuration synchronizes User, Group, Organization, Country, and Organizational Unit objects. It also mirrors the structure of a subtree in the other tree.
* *Field Names:*
  Specifies a comma-separated list of attribute names that can be referred to in the Schema Mapping rule. In the input files, the fields of the records must correspond to the order and positioning of the names in this list.

  For example, if you list eight field names in this parameter, each record of the input files should have eight fields separated by the field delimiter character. On Windows, see sample.csv in the delimitedtext/samples directory for an example. On Solaris and Linux, sample.csv is located in the /usr/lib/dirxml/rules/delim directory.

  The default values are LastName, FirstName, Title, Email, WorkPhone, Fax, WirelessPhone, and Description.
* *Association Attribute:*
  Specifies the attribute value used for association.
* *Suppress Encrypted Attribute in Trace:*
  This GCV is effective only when any of the attributes is set as Encrypted Attribute or only when Encrypted Attribute policy is active. When this attribute is set to Yes, the complete content of the csv file is suppressed. In case you wish to view the content, set the attribute to No.

  By default the GCV is set to Yes.

## A.2.2 Password Synchronization

The following GCVs control password synchronization for the Delimited Text driver. For more information, see the [NetIQ Identity Manager Password Management Guide](../../../identity-manager-48/password_management/data/netiq-idm-password-management.html#netiq-idm-password-management).

In Designer, you must click the ![](../graphics/designer_edit_pass_sync_n.png) icon next to a GCV to edit it. This displays the Password Synchronization Options dialog box for a better view of the relationship between the different GCVs.

In Identity Console, to edit the Password management options go to Configuration > Global Configuration Values, and then change it in your Password synchronization policy tab.

*Connected System Name or Driver Name:*
Specify the name of the driver. The e-mail notification template uses this value to identify the source of the notification message.

*Application accepts passwords from Identity Manager:*
If True, allows passwords to flow from the Identity Manager data store to the connected system.

*Identity Manager accepts passwords from application:*
If True, allows passwords to flow from the connected system to Identity Manager.

*Publish passwords to NDS password:*
Use the password from the connected system to set the non-reversible NDS password in eDirectory.

*Publish passwords to Distribution Password:*
Use the password from the connected system to set the NMAS Distribution Password used for Identity Manager password synchronization.

*Require password policy validation before publishing passwords:*
If True, applies NMAS password policies during publish password operations. The password is not written to the data store if it does not comply.

*Reset user’s external system password to the Identity Manager password on failure:*
If True, on a publish Distribution Password failure, attempt to reset the password in the connected system by using the Distribution Password from the Identity Manager data store.

*Notify the user of password synchronization failure via e-mail:*
If True, notify the user by e-mail of any password synchronization failures.

## A.2.3 Managed System Information

These settings help the Identity Reporting Module function to generate reports. There are different sections in the Managed System Information tab.

* [General Information](gcv-global-configuration-values.html#brnwucf)
* [System Ownership](gcv-global-configuration-values.html#brnwwph)
* [System Classification](gcv-global-configuration-values.html#brnwxtq)
* [Connection and Miscellaneous Information](gcv-global-configuration-values.html#brnx41r)

### General Information

*Name:*
Specifies a descriptive name for this Identity Vault.

*Description:*
Specifies a brief description of this Identity Vault.

*Location:*
Specifies the physical location of this Identity Vault.

*Vendor:*
Specifies the vendor of the Identity Vault.

*Version:*
Specifies the version of this Identity Vault.

### System Ownership

*Business Owner:*
Browse to and select the business owner in the Identity Vault for this Identity Vault. You must select a user object, not a role, group, or container.

*Application Owner:*
Browse to and select the application owner in the Identity Vault for this Identity Vault. You must select a user object, not a role, group, or container.

### System Classification

*Classification:*
Specifies the classification of the Identity Vault. This information is displayed in the reports. The options are:

* Mission-Critical
* Vital
* Not-Critical
* Other

  If you select Other, you must specify a custom classification for the Identity Vault.

*Environment:*
Specifies the type of environment the Identity Vault provides. The options are:

* Development
* Test
* Staging
* Production
* Other

  If you select Other, you must specify a custom classification for the Identity Vault.

### Connection and Miscellaneous Information

*Connection and miscellaneous information:*
This options is always set to hide, so that you don’t make changes to these options.
