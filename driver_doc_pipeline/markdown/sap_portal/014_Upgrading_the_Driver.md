# 4.2 Upgrading the Driver

The driver upgrade process involves upgrading the installed driver packages and updating the existing driver files. These are independent tasks and can be separately planned for a driver. For example, you can update the driver packages and choose not to update the driver files at the same time. However, you are recommended to complete all the update steps within a short amount of time to ensure that the driver has the latest updates.

* [Upgrading the Installed Packages](identity-manager-sap-portal-driver-upgrade-procedure.html#upgrading-installed-packages-for-identity-manager-sap-portal-driver)
* [Updating the Driver Files](identity-manager-sap-portal-driver-upgrade-procedure.html#updating-driver-files-for-identity-manager-sap-portal-driver)

Before starting the upgrade process, ensure that you have taken a back-up of the current driver configuration.

## 4.2.1 Upgrading the Installed Packages

1. Download the latest available packages.

   To configure Designer to automatically read the package updates when a new version of a package is available, click Windows > Preferences > NetIQ > Package Manager > Online Updates in Designer. However, if you need to add a custom package to the Package Catalog, you can import the package .jar file. For more information about creating custom packages, see [Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade) in [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).
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

## 4.2.2 Updating the Driver Files

This section provides general instructions for updating the driver files. For information about updating the driver files to a specific version, search for that driver patch in the [Patch Finder Download Page](http://download.novell.com/patch/finder/#bu=novell&bu=netiq&bu=suse&familyId=7365&productId=45026&dateRange=&startDate=&endDate=&priority=&architecture=&keywords=&xf=7365) and follow the instructions from the Readme file that accompanies the driver patch release.

To update the driver files:

1. Stop the driver instance by using Identity Console, Designer, or dxcmd by performing one of the following actions:

   * If the driver is running locally, stop the driver instance and the Identity Vault.
   * If the driver is running with Remote Loader, stop the driver and the Remote Loader instance.

   For example, go to a command prompt on Linux and run ndsmanage stopall
2. Download the driver patch file to a temporary folder on your server.
3. Extract the contents of the driver patch file.
4. Update the driver files:

   * *Linux:*
     Perform the following actions:

     1. Log in as root on the server where you want to update the driver files.
     2. Open a command prompt and run the following command to upgrade the existing RPM:

        rpm -Uvh <Driver Patch File Temporary Location>/linux/novell-DXMLsappt.rpm

        For example, rpm -Uvh <SAPPortal\_4010.zip>/linux/novell-DXMLsappt.rpm
   * *Windows:*
     Navigate to the <Extracted Driver Patch File Temporary Location>\windows folder and copy the SAPPortalShim.jar file to <IdentityManager installation>\NDS\lib or <IdentityManager installation>\RemoteLoader\<architecture>\lib folder.

     For example, copy SAPPortalShim.jar file from <Extracted IDM45\_ SAPPortal\_4010.zip>\windows directory to <IdentityManager installation>\RemoteLoader\64bit\lib folder.
5. (Conditional) If the driver is running locally, start the Identity Vault and the driver instance.

   For example, open a command prompt on Linux and run ndsmanage startall
6. (Conditional) If the driver is running with Remote Loader, start the Remote Loader and the driver instance.
