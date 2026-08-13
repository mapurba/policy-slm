# 5.1 Upgrading the Driver

There is no separate procedure for upgrading an Entitlements Service driver shim. The driver shim is upgraded with a new version of Identity Manager engine.

To upgrade the installed packages for the driver, perform the following actions in Designer:

1. Download the latest available packages.

   To configure Designer to automatically read the package updates when a new version of a package is available, click Windows > Preferences > NetIQ > Package Manager > Online Updates in Designer. However, if you need to add a custom package to the Package Catalog, you can import the package .jar file. For more information about creating custom packages, see [Developing Packages](../../../identity-manager-48/designer_admin/data/packmandevelop.html#packmandevelop) in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).
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

       For detailed information, see the [Upgrading Installed Packages](../../../identity-manager-49/designer_admin/data/packman.html#packmanupgrade) in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-49/designer_admin/data/bookinfo.html#bookinfo).
