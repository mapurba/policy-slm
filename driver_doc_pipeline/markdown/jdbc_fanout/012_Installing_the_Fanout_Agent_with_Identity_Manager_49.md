# 2.2 Installing the Fanout Agent with Identity Manager 4.9

You can install the Fanout agent with the Identity Manager engine and select the Fanout Agent option during the installation.

The driver files are automatically installed on the Identity Manager server at the same time as the Identity Manager engine. For installing the Fanout agent, you must select the Fanout Agent option during the installation.

## 2.2.1 Linux

1. Log in as root or administrator on the computer where you want to install the Identity Manager engine.
2. Download the Identity\_Manager\_4.9.0\_Linux.iso file from the NetIQ Downloads website.
3. Mount the downloaded.iso.
4. From the root directory of the .iso file, run the following command:
5. Read through the license agreement.
6. Enter y to accept the license agreement.
7. Decide the Identity Manager server edition you want to install. Enter y for Advanced Edition and n for Standard Edition.
8. Select Identity Manager Engine and complete the installation.

## 2.2.2 Windows

1. Log in as root or administrator on the computer where you want to install the Identity Manager engine.
2. From the directory that contains the installation files, run idm\_install.exe.
3. Accept the license agreement, and then click Next.
4. In the Select Components window on Windows, select Fanout Agent.

   When you select this option, the installer creates a FanoutAgent directory under /opt/novell/dirxml/ on Linux and C:\NetIQ\IdentityManager\ on Windows. The FanoutAgent directory includes the bin and lib directories.

   For more information about the options, see "[Planning to Install Identity Manager](../../../identity-manager-48/setup_windows/data/planning-to-install-identity-manager.html#planning-to-install-identity-manager)" in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).
5. (Optional) To select specific drivers for the individual components, complete the following steps:

   1. Click Customize the selected components, and then click Next.
   2. Expand Drivers under the component that you want to install.
   3. Select the drivers that you want to install.
6. Click Next.
7. In the Activation Notice window, click OK.
8. For Authentication, specify a user account and its password with sufficient rights in eDirectory to extend the schema. Specify the user name in the LDAP format. For example, cn=admin,o=company.
9. For Pre-Installation Summary, verify the settings.
10. Click Install.
11. Activate Identity Manager.
12. Copy your existing Fanout configuration to the new configuration file. For more information, see [Migrating the Fanout Agent Configuration](how-to-migrate-the-fan-out-agent-configuration.html).
13. To create and configure your driver objects, consult the specific guide for that driver. For more information, see [Identity Manager Drivers documentation website.](https://www.netiq.com/documentation/identity-manager-47-drivers)
14. (Optional) For the default installation locations, see /tmp/idmInstall.log.
