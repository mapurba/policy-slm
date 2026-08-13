# 6.7 Configuring Third-Party JDBC Drivers

The following guidelines help you configure third-party drivers. For specific configuration instructions, refer to your third-party driver’s documentation.

* Use the latest version of the driver.
* Third-party driver behavior might be configurable.

  In many cases, incompatibility issues can be resolved by adjusting the driver’s JDBC URL properties.
* When you work with international characters, you often must explicitly specify to third-party drivers the character encoding that the database uses.

  Do this by appending a property string to the end of the driver’s JDBC URL.

  Properties usually consist of a property keyword and character encoding value (for example, jdbc:odbc:mssql;charSet=Big5). The property keyword might vary among third-party drivers.

  The possible character encoding values are defined by Sun. For more information, refer to [Sun’s Supported Encoding Web site](http://java.sun.com/j2se/1.5.0/docs/guide/intl/encoding.doc.html).

The following table lists the recommended settings for maximum driver compatibility. These settings are useful when you use an unsupported third-party driver during initial configuration.

*Table 6-64* Recommended Settings for Third-Party JDBC Drivers

| Parameter Name | Compatibility Value |
| Synchronization filter | empty |
| Reuse statements? | 0 (no) |
| Use manual transactions? | 0 (no) |
| Use minimal number of connections? | yes |
| Retrieve minimal metadata? | 1 (yes) |
| Number of returned result sets | one |
