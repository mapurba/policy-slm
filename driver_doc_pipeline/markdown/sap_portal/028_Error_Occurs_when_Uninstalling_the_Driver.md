# 9.5 Error Occurs when Uninstalling the Driver

If you have installed the SAP Portal driver on a server that does not have a Java Virtual Machine (JVM) installed on it, you receive the following error when trying to uninstall the driver:

```
No Java virtual machine could be found from your PATH
environment variable. You must install a VM prior to
running this program.
```

The problem only occurs if you install the SAP Portal driver on a server that does not have Identity Manager or the Remote Loader installed on it.

The workaround is to install the driver on a server with Identity Manager or the Remote Loader, or install the JVM and add the installation location to the PATH variable.

*Linux/UNIX:*
To add the JVM to the PATH variable:

1. From a command line, enter export PATH=<JAVA-HOME-PATH>/bin/:$PATH.
2. Run the uninstall script for the Sentinel driver, where the JAVA-HOME-PATH is the Java or JRE installation location.

*Windows:*
To add the JVM to the PATH variables, use the following command:

```
"Uninstall NetIQ Identity Manager Drivers for SAP.exe" LAX_VM "<JAVA-HOME-PATH>\bin\java.exe"
```

For information about uninstalling the driver, see "[Uninstalling the Identity Manager Engine](../../../identity-manager-48/setup_linux/data/uninstalling-idm-engine.html#uninstalling-idm-engine)" in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [Uninstalling the Identity Manager Engine](../../../identity-manager-48/setup_windows/data/uninstalling-identity-manager-engine.html#uninstalling-identity-manager-engine) in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).
