# 1.2 Support for Standard Driver Features

The following sections provide information about how the SOAP driver supports these standard driver features:

* [Local Platforms](support-standard-driver-features.html#b8rfgy5)
* [Remote Platforms](support-standard-driver-features.html#b8rfh3h)
* [Password Synchronization Support](support-standard-driver-features.html#b8rflt6)
* [Information Synchronized](support-standard-driver-features.html#b8rflyd)

## 1.2.1 Local Platforms

A local installation is an installation of the driver on the Identity Manager server. The SOAP driver can be installed on the operating systems supported for the Identity Manager server.

For information about the operating systems supported for the Identity Manager server, see the [NetIQ Identity Manager Technical Information website](https://www.netiq.com/products/identity-manager/advanced/technical-information/).

## 1.2.2 Remote Platforms

The SOAP driver can use the Remote Loader service to run on a server other than the Identity Manager server. The SOAP driver can be installed on the operating systems supported for the Remote Loader.

For information about the operating systems supported for the Identity Manager server, see the [NetIQ Identity Manager Technical Information website](https://www.netiq.com/products/identity-manager/advanced/technical-information/).

## 1.2.3 Password Synchronization Support

The SOAP driver is capable of synchronizing passwords.

## 1.2.4 Information Synchronized

Unlike most other drivers, the SOAP driver synchronizes protocols instead of objects. It synchronizes the SPML 1.0 and DSML 2.0 protocols. The driver contains the following features:

* HTTP transport of data between the Identity Vault and a Web service
* Example configurations for SPML and DSML
* Customization of HTTP Request-Header fields

  By default, a basic authorization request header with an ID and password is provided for the Subscriber channel.
* SSL connections using the HTTPS protocol
* Subscriber HTTP and HTTPS proxy servers
* Definition and selection of multiple Subscriber connections in the policy at runtime
* Potential to act as an HTTP or HTTPS listener for incoming connections on the publisher channel
* Potential extensibility through customized Java code

  For more information, see [Section B.0, Using Java Extensions](using-java-extensions.html).
