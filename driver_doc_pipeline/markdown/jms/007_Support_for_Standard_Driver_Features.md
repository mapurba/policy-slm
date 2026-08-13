# 1.6 Support for Standard Driver Features

The following sections provide information about how the JMS driver supports these standard driver features:

* [Local Platforms](support-for-standard-driver-features.html#b8rfgy5)
* [Remote Platforms](support-for-standard-driver-features.html#blmlitc)
* [Entitlements](support-for-standard-driver-features.html#b8rflqk)
* [Password Synchronization Support](support-for-standard-driver-features.html#b8rflt6)
* [Information Synchronized](support-for-standard-driver-features.html#b8rflyd)

## 1.6.1 Local Platforms

A local installation is an installation of the driver on the same server as the Identity Manager engine, Identity Vault, and JMS vendor application. Both systems that the driver needs to communicate with (Identity Manager engine and JMS) are local to the driver.

The JMS driver can be installed on the same operating systems that are supported by the Identity Manager server. For information about the operating systems supported by the Identity Manager server, see "[Planning Your Installation](../../../identity-manager-48/setup_linux/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or "[Planning Your Installation](../../../identity-manager-48/setup_windows/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

## 1.6.2 Remote Platforms

The JMS driver can use the Remote Loader service. The Remote Loader service for the JMS driver can be installed on any of the Identity Manager supported platforms.

For more information about installing the Remote Loader services, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

## 1.6.3 Entitlements

The JMS driver does not have Entitlement functionality defined in its basic configuration files. The driver does support entitlements, if there are policies created for the driver to consume.

## 1.6.4 Password Synchronization Support

The basic configuration files for the JMS driver do not include policies for synchronizing passwords.

## 1.6.5 Information Synchronized

The JMS driver synchronizes any messaging format you want. By default, the driver is set up with a Loopback driver configuration.
