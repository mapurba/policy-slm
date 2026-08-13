# 6.2 Configuration Parameters

* [Viewing Driver Parameters](jdbc-driver-parameters.html#b1mkcvu)
* [Deprecated Parameters](jdbc-driver-parameters.html#bvqzp4r)
* [Authentication Parameters](jdbc-driver-parameters.html#aaxz152)

## 6.2.1 Viewing Driver Parameters

1. In Identity Console, click the IDM Administration tile.
2. On the Driver Dashboard, locate the driver icon, then click the upper right corner of the driver icon to display the driver’s properties page.

## 6.2.2 Deprecated Parameters

The following parameters have been deprecated since version 1.6:

*Table 6-3* Deprecated Parameters

| Tag Name | Justification |
| connection-tester-class | The driver now dynamically creates a connection tester class at runtime, based upon information in XML descriptor files. This parameter is still operable, to ensure backwards compatibility. Its continued use, however, is discouraged. |
| connection-test-stmt | The driver now dynamically creates a connection tester class at runtime, based upon information in XML descriptor files. This parameter is still operable, to ensure backwards compatibility. Its continued use, however, is discouraged. |
| reconnect-interval | The reconnect interval is now fixed at 30 seconds on both channels. |

## 6.2.3 Authentication Parameters

After you import the driver, provide authentication information for the target database.

* [Authentication ID](jdbc-driver-parameters.html#bvqz2y8)
* [Authentication Context](jdbc-driver-parameters.html#bvqz35i)
* [Application Password](jdbc-driver-parameters.html#bvqz3f5)

### Authentication ID

An Authentication ID is the name of the driver’s database user/login account.The installation SQL script for each database provides information on the database privileges required for this account to authenticate to a supported database. The scripts are located in the install-dir\DirXMLUtilities\jdbc\sql\abbreviated-database-name\install directory.

This value can be referenced in the Connection Properties parameter value via the token {$username}. See [Connection Properties](configure-jdbc-driver-specific-parameters.html#b1pu3lk).

The default value for the sample configuration is idm.

### Authentication Context

The authentication context is the JDBC URL of the target database.

URL format and content are proprietary. They differ among third-party JDBC drivers. However, they have some similarities in content. Each URL, whatever the format, usually includes an IP address or DNS name, port number, and a database identifier. For the exact syntax and the content requirements of your driver, consult your third-party driver documentation.

For a list of JDBC URL syntaxes for supported third-party drivers, see [JDBC URL Syntaxes](supported-third-party-jdbc-drivers.html#bvx364n).

*IMPORTANT:*Changing anything in this value other than URL properties forces a resynchronization of all objects when triggerless publication is used.

### Application Password

An application password is the password for the driver’s database user/login account. The default value for the sample driver configuration is novell.

This value can be referenced in the Connection Properties parameter value via the token {$password}. See [Connection Properties](configure-jdbc-driver-specific-parameters.html#b1pu3lk).
