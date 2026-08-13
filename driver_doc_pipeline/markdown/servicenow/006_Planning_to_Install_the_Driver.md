# 1.5 Planning to Install the Driver

This section provides information for planning the installation and configuration process for the driver.

* [Installation Requirements](b1i9dwls.html#b1i9e7qe)
* [Options for Installing the Driver Shim](b1i9dwls.html#b1i9e888)

## 1.5.1 Installation Requirements

The ServiceNow driver requires the following applications and files:

* Identity Manager 4.5 Service Pack 2, particularly the following components:

  + Designer
  + Remote Loader (if you want to connect through the Remote Loader)
  + Role and Resource Service driver
  + User Application driver
  + Driver Set packages

    - Advanced Java Class
    - Common Settings
    - Identity Manager Default Universal Password Policy
* ServiceNow driver files

  + ServicenowShim.jar
* ServiceNow driver packages

  + ServiceNow Base
  + ServiceNow Default Configuration
  + ServiceNow Entitlements
  + ServiceNow Password Synchronization

## 1.5.2 Options for Installing the Driver Shim

You can install the driver shim on the Identity Manager server. Alternatively, you can use the Remote Loader service to run the driver on a server other than the Identity Manager server. In this case, the driver and the Remote Loader service run on the same server. The Remote Loader loads drivers and communicates with the Identity Manager engine on behalf of drivers installed on remote servers.

For more information about supported platforms for installing Identity Manager or the Remote Loader, see “[Planning to Install Identity Manager](../../../identity-manager-48/setup_linux/data/planning-to-install-identity-manager.html#planning-to-install-identity-manager)” in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or “[Planning to Install Identity Manager](../../../identity-manager-48/setup_windows/data/planning-to-install-identity-manager.html#planning-to-install-identity-manager)” in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

For information about configuring the Identity Manager drivers with the Remote Loader, see [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).
