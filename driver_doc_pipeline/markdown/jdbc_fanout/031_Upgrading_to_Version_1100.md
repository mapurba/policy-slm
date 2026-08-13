# 5.2 Upgrading to Version 1.1.0.0

In general, the Fanout driver upgrade process involves upgrading the installed driver packages and updating the existing Fanout agent and driver files.

This section provides general instructions for updating a driver. For information about updating the driver to a specific version, search for that driver patch in the [NetIQ Patch Finder Download Page](http://download.novell.com/patch/finder/#bu=novell&bu=netiq&bu=suse&familyId=7365&productId=45026&dateRange=&startDate=&endDate=&priority=&architecture=&keywords=&xf=7365) and follow the instructions from the Readme file accompanying the driver patch release.

* [Upgrading the Installed Packages](upgrade-to-jdbc-fan-out-1-1-0-0.html#t43fbqigvefe)
* [Updating the Fanout Agent and Driver](upgrade-to-jdbc-fan-out-1-1-0-0.html#t43fqsjy5a59)

## 5.2.1 Upgrading the Installed Packages

1. Download the latest available packages.

   To configure Designer to automatically read the package updates when a new version of a package is available, click Windows > Preferences > NetIQ > Package Manager > Online Updates in Designer. For more information about managing packages, see the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).
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

       For detailed information, see the [Upgrading Installed Packages](../../../identity-manager-48/designer_admin/data/packman.html#packmanupgrade) in the [NetIQ Designer for Identity Manager Administration Guide](../../../identity-manager-48/designer_admin/data/bookinfo.html#bookinfo).

## 5.2.2 Updating the Fanout Agent and Driver

* [Prerequisites](upgrade-to-jdbc-fan-out-1-1-0-0.html#t43fytrro6m9)
* [Updating the Fanout Agent](upgrade-to-jdbc-fan-out-1-1-0-0.html#t43fyuj7ts20)
* [Updating the Driver Files](upgrade-to-jdbc-fan-out-1-1-0-0.html#t43fbthql2xy)

### Prerequisites

1. Take a back-up of the current driver configuration.
2. Stop the driver instance.
3. Stop the Identity Vault.
4. In a browser, navigate to the [NetIQ Patch Finder Download Page](http://download.novell.com/patch/finder/#bu=novell&bu=netiq&bu=suse&familyId=7365&productId=45026&dateRange=&startDate=&endDate=&priority=&architecture=&keywords=&xf=7365).
5. Under Patches, click Search Patches.
6. Specify Identity Manager nn Fanout driver nn in the search box.
7. Download and unzip the contents of the patch file to a temporary location on your server.

   For example, IDM4.5\_FanoutAgent\_1110.zip.

### Updating the Fanout Agent

1. Stop the Fanout agent. For more information, see [Stopping the Fanout Agent](how-to-stop-jdbc-fan-out-agent.html).
2. Remove all the versions of the activemq-all-<Version>.jar file from your current <Fanout agent installation>\lib directory.
3. Update the Fanout agent files:

   * *Linux:*
     Depending on your Identity Manager installation type as root or non-root, log in to your server with appropriate rights and run the following command in a command prompt:

     rpm -Uvh <Fanout Agent Patch File Temporary Location>/linux/netiq-DXMfanout.rpm
   * *Windows:*
     Navigate to the <Extracted Fanout Agent Patch File Temporary Location>\windows\FanoutAgent\bin folder and copy the following files to <IdentityManager installation>\NDS\lib folder.

     + stopAgent.bat
     + FanoutAgent.jar
     + activemq-all-5.15.2.jar
4. Start the Fanout agent. For more information, see [Starting the Fanout Agent](how-to-start-jdbc-fan-out-agent.html).

### Updating the Driver Files

1. (Conditional) Stop the driver instance, then stop the Identity Vault if not already stopped:
2. Update the driver files:

   * *Linux:*
     To upgrade the existing RPM, log in as root and run the following command in a command prompt:

     rpm -Uvh <Driver Patch File Temporary Location>/linux/novell-DXMLfanoutdriver.rpm

     For example, rpm -Uvh <IDM4.5\_FanoutAgent\_1110.zip>/linux/novell-DXMLfanoutdriver.rpm
   * *Windows:*
     Perform the following actions:

     1. Navigate to the <Extracted Driver Patch File Temporary Location>\windows folder and copy the FanoutDriverShim.jar file to <IdentityManager installation>\NDS\lib folder.
     2. Copy the activemq-all-5.14.3.jar from <Extracted Driver Patch File Temporary Location>\windows\FanoutAgent\lib folder toÂ <C:\NetIQ\IdentityManager\NDS\lib folder.
3. Start the Identity Vault and the Fanout driver instance.
