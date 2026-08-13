# 2.3 Migrating the Fanout Agent Configuration

As part of upgrading your existing driver, you must copy your current Fanout configuration to the new configuration file after the Fanout agent is installed in the following default locations:

* *Linux:*
  /opt/novell/dirxml/fanoutagent
* *Windows:*
  C:\NetIQ\IdentityManager\FanoutAgent

Identity Manager provides a migration utility to help you copy the existing configuration to the newly installed Fanout agent directory. The utility is located in the bin directory of the new Fanout agent installation directory on both Linux and Windows platforms.

To copy the existing configuration, perform the following steps:

1. Stop the Fanout agent.
2. Copy the required third party jar files to the lib directory in the new Fanout agent directory.
3. Copy the existing configuration.

   1. Navigate to bin in the installation directory of the new Fanout agent and locate the migration script for your platform.

      * *Linux:*
        fanoutMigration
      * *Windows:*
        fanoutMigration.bat
   2. Run the migration script using the following syntax:

      fanoutMigration <existing location of the Fanout agent>

      For example, ./fanoutmigration /root/NIdM\_Driver\_4.5\_JDBCFanout

      where /root/NIdM\_Driver\_4.5\_JDBCFanout is the location of the existing Fanout agent.

      *NOTE:*In addition to copying the configuration information, the command appends two new attributes to the configuration file. These attributes are required for setting the secure protocol version for SSL communication and for enabling the SuiteB communication. For more information, see [Generating the Default Configuration File](how-to-generate-the-default-configuration-file.html).
   3. (Optional) If the configuration is successfully copied to the new location, delete the existing directory.
4. Start the Fanout agent by specifying the absolute path of the new Fanout agent configuration file in the command.

   The Fanout agent configuration is located in /opt/novell/dirxml/fanout/config on Linux and C:\NetIQ\IdentityManager\FanoutAgent\config on Windows.
