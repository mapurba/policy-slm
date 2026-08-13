# 1.2 Support for Standard Driver Features

The following sections provide information about how the Salesforce.com driver supports these standard driver features:

* [Local Platforms](salesforce-support-standard-driver-features.html#b8rfgy5)
* [Remote Platforms](salesforce-support-standard-driver-features.html#b8rfh3h)
* [Supported Operations](salesforce-support-standard-driver-features.html#boxbqdy)

## 1.2.1 Local Platforms

A local installation is an installation of the driver on the Identity Manager server. You can install the Salesforce.com driver on the operating systems supported for Identity Manager server.

For information about the operating systems supported for Metadirectory server, see the [NetIQ Identity Manager Technical Information website](https://www.netiq.com/products/identity-manager/advanced/technical-information/).

## 1.2.2 Remote Platforms

The Salesforce.com driver can use the Remote Loader service to run on a server other than the Identity Manager server. You can install the Salesforce.com driver on the operating systems supported for the Remote Loader.

For information about the supported operating systems for Remote Loader, see the [NetIQ Identity Manager Technical Information website](https://www.netiq.com/products/identity-manager/advanced/technical-information/).

## 1.2.3 Supported Operations

The Salesforce.com driver supports the following operations on the Subscriber channel:

* Add users

  When a user is added to your database, the user is created in the Salesforce.com.
* Update users

  When a user is updated in your database, the updated user information is synchronized with the Salesforce.com.
* Delete users

  When a user is deleted from your database, the user state is made inactive in the Salesforce.com.
* Password synchronization

  The basic configuration files for the Salesforce.com driver are capable of synchronizing passwords.

  When a user is newly created and provided with a password, the password is synchronized with Salesforce.com. If the password is not provided, a random password is generated for the user. You can use the command transformation policies to change the random password generation feature.

  *NOTE:*Salesforce.com driver does not support the following:

  + dn-type attributes
  + Multivalued attributes. If multivalued attributes are added to the Identity Vault, only one of the values is synchronized with the Salesforce.com driver.

The following operations are supported on the Publisher channel:

* Add users
* Modify users

  If the IsActive attribute is set to False, the user is disabled in the Identity Vault.
