# 6.1 Smart Configuration

The JDBC driver can recognize the supported set of third-party JDBC drivers and databases. Also, the driver can dynamically and automatically configure the majority of driver compatibility parameters so you don’t need to understand and explicitly set such parameters.

These features are implemented via the following four types of XML descriptor files, which describe a third-party JDBC driver or database to the JDBC driver.

* Third-party JDBC driver
* Third-party JDBC driver import
* Database
* Database import

In addition to predefined descriptor files, you can create custom descriptor files for a database or third-party JDBC driver.

* [Specifying Custom Descriptor Files](auto-configure-jdbc-driver-parameters.html#bgyzc99)
* [Reserved Filenames for Descriptor Files](auto-configure-jdbc-driver-parameters.html#bgyzcjc)
* [Import Descriptor Files](auto-configure-jdbc-driver-parameters.html#bgyzcp8)
* [Descriptor File Locations](auto-configure-jdbc-driver-parameters.html#bgyzcv6)
* [Precedence](auto-configure-jdbc-driver-parameters.html#bgyzd12)
* [Custom Descriptor Best Practices](auto-configure-jdbc-driver-parameters.html#bgyzd7v)
* [Descriptor File DTDs](auto-configure-jdbc-driver-parameters.html#bgyzdda)

## 6.1.1 Specifying Custom Descriptor Files

You can force the driver to use a custom descriptor file for a database or third-party JDBC driver. To specify a custom database descriptor file, see [Database Descriptor Filename](configure-jdbc-driver-specific-parameters.html#b1pu3m0). To specify a custom third-party driver descriptor file, see [JDBC Driver Descriptor Filename](configure-jdbc-driver-specific-parameters.html#b1pu3lt). This is useful when multiple descriptor files exist for the same database or third-party JDBC driver. For the custom descriptor file to take effect, set the driver parameter as the jdbc-driver-descriptor.

## 6.1.2 Reserved Filenames for Descriptor Files

Descriptor filenames that ship with the driver begin with the underscore character ( \_ ). Such filenames are reserved to ensure that descriptor files that ship with the driver do not conflict with custom descriptor files. Obviously, custom descriptor filenames must not begin with the underscore character.

## 6.1.3 Import Descriptor Files

Import descriptor files allow multiple, nonimport descriptor files to share content. This functionality reduces the size of nonimport descriptor files, minimizes the need for repetition of content, and increases maintainability. Import files cannot be imported across major types. That is, JDBC driver descriptors cannot import database imports, and database descriptors cannot import JDBC driver imports.

Furthermore, custom nonimport descriptors cannot import reserved descriptor imports. For example, if a custom third-party JDBC driver descriptor file named custom.xml tries to import a reserved third-party JDBC driver descriptor named \_reserved.xml, an error is issued. These limitations accomplish the following:

* Ensure that no dependencies exist between reserved and custom import files
* Allow extension of existing reserved descriptor files in later versions of the driver

## 6.1.4 Descriptor File Locations

Descriptor files must be located in a .jar file whose name begins with the prefix “jdbc” (case-insensitive) and resides in the runtime classpath.

The following table identifies where to place descriptors within a descriptor .jar file:

*Table 6-1* Where to Place Descriptors

| Descriptor Type | Directory Path |
| Third-party JDBC driver | com/novell/nds/dirxml/driver/jdbc/db/descriptor/driver |
| Third-party JDBC driver import | com/novell/nds/dirxml/driver/jdbc/db/descriptor/driver/import |
| Database | com/novell/nds/dirxml/driver/jdbc/db/descriptor/db |
| Database import | com/novell/nds/dirxml/driver/jdbc/db/descriptor/db/import |

Reserved descriptor files are located in the JDBCConfig.jar file. To ensure that these reserved files are not overwritten when the JDBC driver is updated, place custom descriptors in a different .jar file.

## 6.1.5 Precedence

Parameters explicitly specified through a management console, such as Identity Console, always have precedence over parameters specified through descriptor files. Descriptor file parameters only take effect when a parameter is not set through the management console.

Parameters and other information specified in a nonimportable descriptor file always have precedence over information specified in descriptor import files. If a parameter or other information is duplicated within a descriptor file, the first instance of the parameter or information takes precedence over subsequent instances.

Among import files, precedence is determined by import order. Import files declared earlier in the import list take precedence over those that follow.

## 6.1.6 Custom Descriptor Best Practices

* Do not begin custom descriptor files name with the underscore ( \_ ) character.
* Place custom descriptor files in a jar file other than JDBCConfig.jar, and begin the filename with the prefix “jdbc” (case-insensitive).
* Do not use custom descriptors to import reserved import files (filenames that begin with the underscore character).

## 6.1.7 Descriptor File DTDs

The following sections contain DTDs for all descriptor file types. These DTDs can help you construct custom descriptor files.

*Table 6-2* Where to Find Descriptor DTDs

| Descriptor Type | Appendix |
| Third-party JDBC driver | [Section H.0, Third-Party JDBC Driver Descriptor DTD](third-party-jdbc-driver-descriptor-dtd.html) |
| Third-party JDBC driver import | [Section I.0, Third-Party JDBC Driver Descriptor Import DTD](third-party-jdbc-driver-descriptor-import-dtd.html) |
| Database | [Section J.0, Database Descriptor DTD](database-descriptor-dtd.html) |
| Database import | [Section K.0, Database Descriptor Import DTD](database-descriptor-dtd-import.html) |
