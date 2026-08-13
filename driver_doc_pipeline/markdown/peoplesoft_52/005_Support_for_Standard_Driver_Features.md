# 1.4 Support for Standard Driver Features

The following sections provide information about how the PeopleSoft driver supports these standard driver features:

* [Local Platforms](supported-driver-features.html#b8rfgy5)
* [Remote Platforms](supported-driver-features.html#b8rfh3h)
* [Entitlements](supported-driver-features.html#b8rflqk)

## 1.4.1 Local Platforms

A local installation is an installation of the driver on the Identity Manager server. The PeopleSoft driver can be installed on the operating systems supported for the Identity Manager server.

For information about the operating systems supported for the Identity Manager server, see "[Planning Your Installation](../../../identity-manager-48/setup_linux/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or "[Planning Your Installation](../../../identity-manager-48/setup_windows/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

*NOTE:*Support for the local and remote platforms depends on the supported platforms of the PeopleTools Client (PSJOA) software.

## 1.4.2 Remote Platforms

The PeopleSoft driver can use the Remote Loader service to run on a server other than Identity Manager server. The PeopleSoft driver can be installed on the operating systems supported for the Remote Loader.

For information about the supported operating systems, see "[Planning Your Installation](../../../identity-manager-48/setup_linux/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or "[Planning Your Installation](../../../identity-manager-48/setup_windows/data/planning-an-identity-manager-installation.html#planning-an-identity-manager-installation)" in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

*NOTE:*The support for the local and remote platforms depends on the supported platforms of the PeopleTools Client (PSJOA) software.

## 1.4.3 Entitlements

The PeopleSoft driver does not have entitlement functionality defined within the default driver packages. The driver does support entitlements, if there are policies created for the driver to consume.
