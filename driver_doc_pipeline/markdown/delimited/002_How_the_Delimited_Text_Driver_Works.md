# 1.1 How the Delimited Text Driver Works

The Delimited Text driver uses the Publisher channel, the Subscriber channel, and policies to control data flow between the Identity Vault and the delimited text files, as explained in the following sections:

* [Publisher and Subscriber Channels](beyzsyq.html#b94b9il)
* [Policies](beyzsyq.html#b94b9in)
* [Supported File Types](beyzsyq.html#bez0eol)

## 1.1.1 Publisher and Subscriber Channels

The Delimited Text driver provides data flow along the Publisher and Subscriber channels as shown in [Figure 1-1](beyzsyq.html#b94b9im).

*Figure 1-1* Data Flow

![Delimited Text Driver data flow](../graphics/es004_a.png "Delimited Text Driver data flow")

The example configuration that ships with this driver includes both Subscriber and Publisher channels. However, in many configurations, only one-way data flow is required. In those configurations, only a Publisher or Subscriber channel is used. The other channel is disabled. For more information, see [Section 5.0, Setting Up One-Way Synchronization](delimited-one-way-synchronization.html).

### Publisher Channel

The Publisher channel reads information from input text files on your local file system and submits that information to the Identity Vault via the Identity Manager engine.

By default, the Publisher channel does the following:

* Checks the input directory every 10 seconds.
* Processes any files that have a .csv extension.
* Changes .csv extensions of processed files to .bak.
* Cycles through this process until you stop the driver.

### Subscriber Channel

The Subscriber channel watches for additions and modifications to Identity Vault objects and creates output files on your local file system that reflect those changes.

By default, the Subscriber channel keeps an output file open until either 200 transactions have been logged or 30 seconds have elapsed. When either of these thresholds is reached, the output file is saved with a number.csv filename and a new output file is opened.

## 1.1.2 Policies

Policies control data synchronization between the driver and the Identity Vault. The following table provides information on the set of pre-configured policies that come with the Delimited Text driver. For information about modifying policies, see [NetIQ Identity Manager - Using Designer to Create Policies](../../../identity-manager-48/policy_designer/data/using-designer-to-create-policies.html#using-designer-to-create-policies).

*Table 1-1* Preconfigured Policies

| Policy | Description |
| Schema Map | Configured on the driver object.  Maps Identity Vault User properties to application attributes as follows:   * Surname > LastName * Given Name > FirstName * Title > Title * Internet EMail Address > Email * Telephone Number > WorkPhone * Facsimile Telephone Number > Fax * mobile > WirelessPhone * Description > Description   The application attributes correspond to the sequence of values in the file or, if present, to the attributes associated with unnamed Â XDS <field> elements. |
| Input Transform | Configured on the driver object.  If the input document is an XML document, no transformations are made. If the document is a delimited text file, each record is transformed into an XDS Add element for User objects with attributes defined by the schema map.  Associations are defined by the value of user's e-mail attribute. |
| Output Transform | Configured on the driver object.  Specifies that a comma is used as the delimiter character for output files and that the file format is comma-separated value (CSV) format. It transforms the XDS document into CSV format and submits it to the driver shim. |
| Create | Configured on the Publisher channel.  Specifies that in order for a User to be created in an Identity Vault, the Given Name and Internet EMail Address attributes must be defined.  The user CN is formed by concatenating the values of first name and last name. |
| Matching | Configured on the Publisher channel.  Specifies that a user in an Identity Vault is the same user specified in the input file when the value of Internet Email Address is the same in both places.  If there is a match, only changed attributes are updated in the Identity Vault. |
| Placement | Configured on the Publisher channel.  Specifies that a new user is placed in the Users or Active container and named with the CN created by the Input Transform rule.  You need to create a Users\Active container at the root of your tree before you start the driver. |
| Event Transform | Configured on the Subscriber channel.  If an Identity Vault reports a Modify or Sync event, those events are changed to an instance element that can be used to create a complete output record. |

## 1.1.3 Supported File Types

The driver currently supports two types of files:

* [Comma-Separated Values Files](beyzsyq.html#bez0eom)
* [XML Files in XDS Format](beyzsyq.html#bez0eon)

### Comma-Separated Values Files

Comma-separated value (CSV) files are text files that contain data divided into fields and records. Fields are delimited by commas, and records are delimited by a hard return.

If you need a comma or hard return within the value of a particular field, the entire field value should be enclosed in quotes.

Because the meaning of each field in a CSV file is derived from its position, each record in a CSV file should have the same number of fields. Field values can be left blank, but each record should have the same number of delimiter characters.

### XML Files in XDS Format

The XDS format is the defined NetIQ subset of possible XML formats. This is the initial format for data coming from an Identity Vault. By modifying default rules and changing the style sheets, the Delimited Text driver can be configured to work with any XML format.

For detailed information on the XDS format, refer to [NDS DTD Commands and Events](http://developer.novell.com/ndk/doc/dirxml/index.html?dirxmlbk/data/a5323rs.html).

For information on configuring the driver to use XML files in the XDS format, see [Section 6.0, Configuring for XDS XML Files](delimited-configure-xds-xml-file.html).
