# 4.1 Upgrading an Existing Driver to GroupWise Driver

To upgrade an existing driver to the supported GroupWise driver, you need to upgrade the following driver components:

* Driver shim
* Driver packages

* [Upgrading the Driver Shim](t42hyptk7vr6.html#b199w80j)
* [Upgrading the Existing Driver Packages](t42hyptk7vr6.html#b1cyleg3)

## 4.1.1 Upgrading the Driver Shim

To upgrade the driver shim, perform the following actions:

1. Stop the driver instance by using Identity Console, Designer, or dxcmd by performing one of the following actions:

   * If the driver is running locally, stop the driver instance and the Identity Vault.
   * If the driver is running with a Remote Loader instance, stop the driver and the Remote Loader instance.

   For example, go to a command prompt on Linux and run ndsmanage stopall
2. Download the driver patch file to a temporary folder on your server.
3. Extract the contents of the driver patch file.
4. Update the driver files:

   * Linux: Open a command prompt and run the following command to upgrade the existing RPM:

     rpm -U (image-path)/novell-DXMLGWRest.rpm
   * Windows: Navigate to the <Extracted Driver Patch File Temporary Location>\windows folder and copy the GWRestShim.jar file to <IdentityManager installation>\RemoteLoader\lib folder.
5. (Conditional) If the driver is running locally, start the Identity Vault and the driver instance.

   For example, open a command prompt on Linux and run ndsmanage startall
6. (Conditional) If the driver is running with a Remote Loader, start the Remote Loader and the driver instance.

## 4.1.2 Upgrading the Existing Driver Packages

You must upgrade the existing GroupWise driver packages to GroupWise 2.5 packages.

1. Download all GroupWise 2.5 or 2.6 packages from the [Package Update site](http://cdn.novell.com/cached/designer/packages/idm/customupdatesite2_0_0/).

   Ensure that the package version is 2.5 or 2.6. For more information about the packages needed for the driver upgrade, see [Driver Packages](key-features.html#b1d4ygp2).
2. Right-click the driver, then click Properties.
3. Click Packages, and select the packages to upgrade.

   *IMPORTANT:*Performing a partial upgrade of the packages might break the existing driver functionality.

   If you want to install the legacy GroupWise driver after installing the upgraded packages, you need to manually select 2.0.x packages during package installation because 2.5 packages will become the default packages for the GroupWise driver. You must ignore 2.5 packages for creating a legacy GroupWise driver.
4. Follow the driver configuration steps from [Installing the Driver Packages](create-driver-object-designer.html#brn9cu1).
5. Click Next.
6. In the driver configuration page, update the GroupWise Driver Class name to com.novell.gw.dirxml.driver.rest.shim.GWdriverShim.

   *NOTE:*Change the name of the driver module if you are running the driver locally. If you are running the driver remotely, modify the Remote Loader instance configuration with the new class name before starting the driver instance.
7. Deploy the driver.
8. Start the driver.

*IMPORTANT:*GroupWise does not support Distribution List and External Entities objects. However, the upgraded driver supports the Modify operation for them. For a list of GCVs applicable for the upgraded driver, see [GCVs Applicable for the Upgraded Driver](gcv-upgraded-driver.html).
