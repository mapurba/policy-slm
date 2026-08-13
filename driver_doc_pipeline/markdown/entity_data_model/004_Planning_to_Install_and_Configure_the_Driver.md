# 1.3 Planning to Install and Configure the Driver

This section provides useful information for planning the installation and configuration process.

## 1.3.1 Installation Requirements

The Entity Data Model driver requires the following applications and files, at a minimum. When you installed Identity Manager, you might also have chosen to install the files for the Entity Data Model driver.

* Access Review 1.1 or Entity Data Model 2.5
* Identity Manager 4.5 Service Pack 1 at a minimum, particularly the following components:

  + Identity applications
  + Designer
  + Remote Loader
  + Role and Resource Service driver

    NOVLRSERVB - Role and Resource Service Driver Base, package version 4.5.0.20140925170245, at a minimum
  + User Application driver

    NOVLUABASE - User Application Base, version 4.5.1.20150602213315, at a minimum

    NOVLPROVNOTF - Provisioning Notification Templates, version 2.0.1.20150528174045, at a minimum
  + Drive Set packages

    NOVLACOMSET - Driver Set package for Common Settings Advanced Edition

    NOVLCOMSET - Driver Set package for Common Settings
* Database JDBC file

  + Third-party JDBC driver for connecting to the Entity Data Model database
* Entity Data Model driver file

  + arshim.jar - Entity Data Model driver shim
* Entity Data Model driver packages

  + NOVLARBASE - Entity Data Model Base
  + NOVLARDCFG - Entity Data Model Default Configuration
  + NOVLARMSINFO - Entity Data Model Managed System Information
  + NOVLARWDSYN - Entity Data Model Password Sync

## 1.3.2 Information Needed for Installation and Configuration

Ensure that you have the information that you need to install and configure the Entity Data Model driver. For more information about the process, see [Checklist for Installing and Configuring the Driver](b1fdqnrb.html).

Entity Data Model settings
:   * Host and port of the Entity Data Model server
    * URL for the Entity Data Model application
    * (Conditional) For https connectivity, security certificate for the Entity Data Model application
    * Account and password for a global or data administrator in Entity Data Model
    * Account and password for the administrator of the Entity Data Model databases
    * Name of the Operations table in the Entity Data Model database, by default igops
    * OSP client name and password for Entity Data Model in the Roles Based Provisioning Module configuration utility

Identity Manager settings
:   * Host and port for the Remote Loader running on the Entity Data Model server
    * DN for the User Application driver
    * URL for the User Application where an administrator creates user accounts

      By default, the URL contains IDMProv.
    * (Conditional) For https connectivity, security certificate for the User Application
    * Account and password for an administrator of the User Application
