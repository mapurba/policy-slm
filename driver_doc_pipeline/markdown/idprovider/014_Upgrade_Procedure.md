# 4.2 Upgrade Procedure

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
