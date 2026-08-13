# 5.3 Upgrading the Driver

The driver upgrade process involves upgrading the installed driver packages and updating the driver files.

This section provides general instructions for updating a driver. For information about updating the driver to a specific version, search for that driver patch in the [NetIQ Patch Finder Download Page](http://download.novell.com/patch/finder/#bu=novell&bu=netiq&bu=suse&familyId=7365&productId=45026&dateRange=&startDate=&endDate=&priority=&architecture=&keywords=&xf=7365) and follow the instructions from the Readme file accompanying the driver patch release.

* [Upgrading the Installed Packages](bf9dg6g.html#t43fbqigvefe)
* [Applying the Driver Patch](bf9dg6g.html#t43fbthql2xy)

## 5.3.1 Upgrading the Installed Packages

1. Download the latest available packages.

   To configure Designer to automatically read the package updates when a new version of a package is available, click Windows > Preferences > NetIQ > Package Manager > Online Updates in Designer. However, if you need to add a custom package to the Package Catalog, you can import the package .jar file. For detailed information, see the [Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade) in [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).
2. Upgrade the installed packages.

   1. Open the project containing the driver.
   2. Right-click the driver for which you want to upgrade an installed package, then click Driver > Properties.
   3. Click Packages.

      If there is a newer version of a package, there is check mark displayed in the Upgrades column.
   4. Click Select Operation for the package that indicates there is an upgrade available.
   5. From the drop-down list, click Upgrade.
   6. Select the version that you want to upgrade to, then click OK.

      *NOTE:*Designer lists all versions available for upgrade.
   7. Click Apply.
   8. (Conditional) Fill in the fields with appropriate information to upgrade the package, then click Next.

      Depending on which package you selected to upgrade, you must fill in the required information to upgrade the package.
   9. Read the summary of the packages that will be installed, then click Finish.
   10. Review the upgraded package, then click OK to close the Package Management page.

       For detailed information, see the [Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade) in [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

## 5.3.2 Applying the Driver Patch

The driver patch updates the driver files. You can install the patch as a root or non-root user.

### Prerequisites

Before installing the patch, complete the following steps:

1. Take a back-up of the current driver configuration.
2. (Conditional) If the driver is running with the Identity Manager engine, stop the Identity Vault and the driver instance.
3. (Conditional) If the driver is running with a Remote Loader instance, stop the Remote Loader instance and the driver instance.
4. In a browser, navigate to the [NetIQ Patch Finder Download Page](http://download.novell.com/patch/finder/#bu=novell&bu=netiq&bu=suse&familyId=7365&productId=45026&dateRange=&startDate=&endDate=&priority=&architecture=&keywords=&xf=7365).
5. Under Patches, click Search Patches.
6. Specify Identity Manager nn Workorder Driver nn in the search box.
7. Download and unzip the contents of the patch file to a temporary location on your server.

   For example, IDM45\_Workorder\_4000.zip.

### Applying the Patch as a Root User

In a root installation, the driver patch installs the driver files RPMs in the default locations on Linux. On Windows, you need to manually copy the files to the default locations.

1. Update the driver files:

   * *Linux:*
     Log in to your server as root and run the following command in a command prompt:

     rpm -Uvh <Driver Patch File Temporary Location>/linux/novell-DXMLwkodr.rpm

     For example, rpm -Uvh <IDM45\_Workorder\_4000.zip>/linux/novell-DXMLwkodr.rpm
   * *Windows:*
     Navigate to the <Extracted Driver Patch File Temporary Location>\windows folder and copy the WorkOrder.jar file to <IdentityManager installation>\NDS\lib or <IdentityManager installation>\RemoteLoader\<architecture>\lib folder.
2. (Conditional) If the driver is running locally, start the Identity Vault and the driver instance.
3. (Conditional) If the driver is running with a Remote Loader instance, start the Remote Loader instance and the driver instance.

### Applying the Patch as a Non-Root User

1. Verify that <non-root eDirectory location>/rpm directory exists and contains the file, \_db.000.

   The \_db.000 file is created during a non-root installation of the Identity Manager engine. Absence of this file might indicate that Identity Manager is not properly installed. Reinstall Identity Manager to correctly place the file in the directory.
2. To set the root directory to non-root eDirectory location, enter the following command in the command prompt:

   ```
   ROOTDIR=<non-root eDirectory location>
   ```

   This will set the environmental variables to the directory where eDirectory is installed as a non-root user.
3. Download the patch and untar or unzip the downloaded file.
4. To install the driver files, enter the following command:

   ```
   rpm --dbpath $ROOTDIR/rpm -Uvh --relocate=/usr=$ROOTDIR/opt/novell/eDirectory --relocate=/etc=$ROOTDIR/etc --relocate=/opt/novell/eDirectory=$ROOTDIR/opt/novell/eDirectory --relocate=/opt/novell/dirxml=$ROOTDIR/opt/novell/dirxml --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles <rpm-location>
   ```

   For example, to install the WorkOrder driver RPM, use this command:

   ```
   rpm --dbpath $ROOTDIR/rpm -Uvh --relocate=/usr=$ROOTDIR/opt/novell/eDirectory --relocate=/etc=$ROOTDIR/etc --relocate=/opt/novell/eDirectory=$ROOTDIR/opt/novell/eDirectory --relocate=/opt/novell/dirxml=$ROOTDIR/opt/novell/dirxml --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles /home/user/novell-DXMLwkodr.rpm
   ```
