# 6.4 Managing Additional Attributes

You can add additional attributes to the driver for both the Publisher and Subscriber channels. These attributes can be accessed by the REXX execs for all event types.

To publish or subscribe to additional attributes, you must add them to the filter and add support for them into the REXX execs.

* [Modifying the Filter](b3xywb2.html#b45fdpp)
* [Modifying the Rexx Execs for New Attributes](b3xywb2.html#b45fsjx)
* [Modifying the Publisher Channel for Additional Top Secret Fields](b3xywb2.html#b6acpv9)

## 6.4.1 Modifying the Filter

1. On the iManager Driver Overview page for the driver, click the Filter icon on either the Publisher or Subscriber channel. It is the same object.
2. In the Filter Edit dialog box, click the class containing the attribute to be added.
3. Click Add Attribute, then select the attribute from the list.
4. Select the flow of this attribute for the Publisher and Subscriber channels.

   * *Synchronize:*
     Changes to this object are reported and automatically synchronized.
   * *Ignore:*
     Changes to this object are not reported and not automatically synchronized.
   * *Notify:*
     Changes to this object are reported, but not automatically synchronized.
   * *Reset:*
     Resets the object value to the value specified by the opposite channel. (You can set this value on either the Publisher or Subscriber channel, but not both.)
5. Click Apply.

If you want to map this attribute to an existing attribute in the connected system schema file, modify the Schema Mapping policy for the driver.

For complete details about managing filters and Schema Mapping policies, see the policy documentation on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## 6.4.2 Modifying the Rexx Execs for New Attributes

In the Subscriber channel, a specific REXX exec is called to take the appropriate action for each type of event. For example, if the additional attribute is required for adds and modifies of users, modify IDMADDU and IDMMODU to process the additional attribute.

Publishing additional attributes requires that you act on changes made in the source application.

## 6.4.3 Modifying the Publisher Channel for Additional Top Secret Fields

New field names can be added to the Top Secret Field Descriptor Table (FDT). This table also allows installations to remap existing fields to additional data, supplied by the customer. For more information about the FDT, see your Top Secret documentation.

The Publisher channel makes use of Java classes and XSLT to help you publish new field names for a customized Top Secret installation.

TSO commands, such as TSS, are sent from the change log to the Identity Manager Input Transformation Policies as the original command that was entered by the user, including all keywords and operand values that were supplied. A set of helper functions, written in Java, helps you to parse these keywords appropriately with XSLT, through the use of XSLT Java extension calls.

The default Input Transformation is named TSO (TSS) Input Transformation, and is the first policy to act on data for the Publisher channel. This policy is implemented as an XSLT script. When invoked by the processor, the script retrieves a parser that is created once per lifetime of the Identity Manager JVM\* instance and is unique to this particular driver instance and command instance. The parser registers known keywords, and you can register custom keywords. After being registered, the parser is invoked to parse the command image and produces a node set containing a single XML document that represents the command image. This document can then be transformed into XDS documents for event types processed by the Metadirectory engine.

The following table describes the Java classes and methods.

*Table 6-3* Java Classes and Methods

| Java Class | Java Method | Description |
| TSOCommandParser | static TSOCommandParser registerParser(String name, String driver) | Static method that creates a new TSOCommandParser object with a uniquely specified name and driver string |
| TSOCommandParser | static boolean hasParser(String name, String driver) | Static method that returns true if a parser is available or false if one is not |
| TSOCommandParser | static TSOCommandParser getParser(String name, String driver) | Static method that returns the parser that has been registered previously |
| TSOCommandParser | void registerCommand(String cmd) | Registers a TSO command with this parser instance |
| TSOCommandParser | NodeSet parse(String cmd) | Parses the TSO command and returns a NodeSet that can be used for XSLT processing |
| TSOCommand | TSOCommand(String name) | Constructor method to create a new TSO command with a case-insensitive command string prefix |
| TSOCommand | void registerKeyword(TSOKeyword keyword) | Registers a keyword to be associated with this TSOCommand instance |
| TSOCommand | void registerPositional(TSOPositional pos) | Registers a positional parameter to be associated with this TSOCommand instance |
| TSOKeyword | TSOKeyword(String name) | Constructor method to create a new TSO keyword instance with a case-insensitive keyword string value |
| TSOKeyword | void registerKeyword(TSOKeyword keyword) | Registers a sub-keyword for this TSOKeyword instance |
| TSOKeyword | void registerPositional(TSOPositional pos) | Registers a positional parameter to be associated with this TSOCommand instance |
| TSOKeyword | void setDefaultValue(String v) | Assigns a default value for a keyword that contains a value during parsing |
| TSOKeyword | void setImpliedName(String n) | Assigns a name to be used to describe the keyword in lieu of its string name |
| TSOKeyword | void mapValue(String key, String value) | Assigns a mapped value to the key string when found during parsing |
| TSOKeyword | void sensitive() | Sets this keyword to be case sensitive by using the XML attribute is-sensitive=true |
