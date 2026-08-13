# 2.0 Installing the Driver Files

By default, the JMS driver files are installed on the Identity Manager server at the same time as the Identity Manager engine. The installation program extends the Identity Vault’s schema and installs both the driver shim and the driver configuration files. It does not create the driver in the Identity Vault (see [Section 3.0, Creating a New Driver Object](creating-a-new-driver-object.html)) or upgrade an existing driver’s configuration (see [Section 5.0, Upgrading an Existing Driver](upgrading-an-existing-driver.html)).

You don’t need to install the Identity Manager engine on this same machine. Using a Remote Loader, you can separate the engine and the driver shim, allowing you to balance the load on different machines or accommodate corporate directives.

The installation scenario you select determines how the driver shim is installed. If you choose to install the driver shim on the same machine as Identity Manager (where Identity Manager engine and Identity Vault are located), Identity Manager calls the driver shim directly. If you choose to install the driver shim on another machine, you must use the Remote Loader.

You can install the driver in one of the following ways:

* On a local machine: Install the JMS driver files on the Identity Manager server and connect to the JMS server by using the JMS PROVIDER URL (Connection Properties). See [Installing Identity Manager](../../../identity-manager-48/setup_linux/data/install-identity-manager-linux.html#install-identity-manager-linux) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Installing the Identity Vault](../../../identity-manager-48/setup_windows/data/windows-install-identity-vault.html#windows-install-identity-vault) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).
* On a remote machine, you can install in one of the following ways:

  + You can install the Identity Vault, the Identity Manager engine, and the driver on a separate computer from the JMS domain controller. This configuration leaves the domain controller free of any Identity Manager software.
  + Alternatively, you can install the Remote Loader and driver shim on the JMS domain controller, but install the Identity Vault and the Identity Manager engine on a separate server.

  See the instructions [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_linux/data/configuring-remote-loader-and-drivers.html#configuring-remote-loader-and-drivers) in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Configuring the Remote Loader and Drivers](../../../identity-manager-48/setup_windows/data/b18xta1v.html#b18xta1v) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).
