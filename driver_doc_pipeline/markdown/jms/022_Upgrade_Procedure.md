# 5.3 Upgrade Procedure

The driver upgrade process involves updating the driver files and upgrading the installed driver packages. However, there is no separate procedure for updating the driver shim. The driver shim is updated with a new version of Identity Manager engine.

To upgrade the installed packages for the driver, perform the following actions in Designer:

1. Download the latest available packages.

   To configure Designer to automatically read the package updates when a new version of a package is available, click Windows > Preferences > NetIQ > Package Manager > Online Updates in Designer. However, if you need to add a custom package to the Package Catalog, you can import the package .jar file. For more information about creating custom packages, see [Developing Packages](../../../identity-manager-48/designer_admin/data/packmandevelop.html#packmandevelop) in [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).
2. Upgrade the installed packages.

   1. Open the project containing the driver.
   2. Right-click the driver for which you want to upgrade an installed package, then click Driver > Properties.
   3. Click Packages.

      If there is a newer version of a package, there is check mark displayed in the Upgrades column.
   4. Click Select Operation for the package that indicates there is an upgrade available.
   5. From the drop-down list, click Upgrade.
   6. Select the version that you want to upgrade to, then click OK.
   7. Click Apply.
   8. (Conditional) Fill in the fields with appropriate information to upgrade the package, then clickNext.
   9. Read the summary of the packages that will be installed, then click Finish.
   10. Review the upgraded package, then click OK to close the Package Management page.

       For detailed information, see "[Upgrading the Identity Manager Drivers](../../../identity-manager-48/setup_linux/data/upgrading-drivers.html#upgrading-drivers)" in the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or "[Upgrading the Identity Manager Drivers](../../../identity-manager-48/setup_windows/data/upgrade-drivers.html#upgrade-drivers)" in the [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

## 5.3.1 Applying the Driver Patch

The driver patch updates the driver files. You can install the patch as a root or non-root user.

### Prerequisites

Before installing the patch, complete the following steps:

1. Take a back-up of the current driver configuration.
2. Stop the driver instance.
3. Stop the Identity Vault.
4. In a browser, navigate to the [NetIQ Patch Finder Download Page](http://download.novell.com/patch/finder/#bu=novell&bu=netiq&bu=suse&familyId=7365&productId=45026&dateRange=&startDate=&endDate=&priority=&architecture=&keywords=&xf=7365).
5. Under Patches, click Search Patches.
6. Specify Identity Manager nn Bidirectional eDirectory Driver nn in the search box.
7. Download and unzip the contents of the patch file to a temporary location on your server.

### Applying the Patch as a Root User

In a root installation, the driver patch installs the driver files in the default locations on Linux. On Windows, you need to manually copy the files to the default locations.

1. Delete or move the existing files that match the files being copied.
2. Update the driver files:

   * *Linux:*
     Open a command prompt and run the following command to upgrade the existing RPM:

     rpm -Uvh <Driver Patch File Temporary Location>/linux/novell-DXMLjms.rpm
   * *Windows:*
     Navigate to the <Driver Patch File Temporary Location>\windows folder and copy the JMSShim.jar file to <IdentityManager installation>\NDS\lib or <IdentityManager installation>\RemoteLoader\<architecture>\lib folder.
3. (Conditional) If the driver is running locally, start the Identity Vault and the driver instance.

   For example, open a command prompt and run ndsmanage startall
4. (Conditional) If the driver is running with a Remote Loader instance, start the Remote Loader instance and the driver instance.

### Applying the Patch as a Non-Root User

1. Verify that <non-root eDirectory location>/rpm directory exists and contains the file, \_db.000.

   The \_db.000 file is created during a non-root installation of the Identity Manager engine. Absence of this file in the directory might indicate that Identity Manager is not properly installed and it might be necessary to re-install it to place the file in the directory.
2. To set the root directory to non-root eDirectory location, enter the following command in the command prompt:

   ```
   ROOTDIR=<non-root eDirectory location>
   ```

   This will set the environmental variables to the directory where eDirectory is installed as a non-root user.
3. To install the driver files, enter the following command:

   ```
   rpm --dbpath $ROOTDIR/rpm -Uvh --relocate=/usr=$ROOTDIR/opt/novell/eDirectory --relocate=/etc=$ROOTDIR/etc --relocate=/opt/novell/eDirectory=$ROOTDIR/opt/novell/eDirectory --relocate=/opt/novell/dirxml=$ROOTDIR/opt/novell/dirxml --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles <rpm-location>
   ```

   For example, to install the JMS driver RPM, use this command:

   ```
   rpm --dbpath $ROOTDIR/rpm -Uvh --relocate=/usr=$ROOTDIR/opt/novell/eDirectory --relocate=/etc=$ROOTDIR/etc --relocate=/opt/novell/eDirectory=$ROOTDIR/opt/novell/eDirectory --relocate=/opt/novell/dirxml=$ROOTDIR/opt/novell/dirxml --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles /home/user/novell-DXMLjms.rpm
   ```
