# 4.2 Upgrading from the Java-Based RACF Driver

*IMPORTANT:*Please read carefully all points in this section regarding changes that need to be considered on systems running previous versions of the Identity Manager bidirectional driver for RACF.

The RACF driver for Identity Manager 4.8 introduces significant architectural changes over previous releases. The RACF driver that was provided with Identity Manager 3.6.1 and earlier releases employed a Java-based architecture, which leveraged the TELNET/TSO interface to interact with the RACF system.

The new RACF driver provides the same functionality through an improved design that is more efficient and easier to configure. To learn more about the new architecture, see [Section 1.0, Overview](b3r8p5u.html).

Given these changes, systems using previous versions of the driver require several adjustments before the new driver can be fully implemented. Some key components require removal and others will need to be migrated. Be sure to review and consider all points in this section as you decide on appropriate changes to both the Identity Vault and your RACF system.

## 4.2.1 Upgrading the RACF Event Subsystem

Your current RACF Event Subsystem is a collection of tasks, JCLs and TSO commands that were packaged as TRANSMIT archives named idmload.xmt and samplib.xmt. In past installations, the contents of these archives were added to the z/OS RACF system to provide the RACF driver with hooks into the RACF database for both Subscribing and Publishing events.

To use the new release of the driver, you will need to ensure that all of these components are replaced with their latest versions, including any that bear the same file names.

Copy and unpack the new archives, idmload.xmt, samplib.xmt and racfexec.xmt, to your RACF system, using the instructions provided in [Setting Up the Libraries on Your z/OS System](b3xehpq.html#b686w3q).

Although you might replace your existing LOAD and SAMPLIB libraries with the updated versions, NetIQ recommends that you unpack the archives to new physical locations to avoid name and version confusion. Then, once the new driver is setup and running, you can remove the older LOAD and SAMPLIB data sets from your system.

### HFS File System Structure

To use this release of the RACF driver, you need to prepare a location in the HFS file system. To assist you in this task, the SAMPLIB data set includes a Job Card named HFSINST.

Edit the paths in this file as appropriate to your local environment and submit it as a Job Card to create your default HFS path, located at /opt/novell/racfdrv. If you decide to change this path, you will also need to change the DRVCONF member to reflect the install path.

### New Password Exit

*NOTE:*If you do not wish to synchronize RACF password phrases, you can skip this step.

The new RACF driver’s password exit routine, LDXRIX02, supports the ability to capture changes in RACF password phrases, which is new to z/OS 1.10.

To install the ICHRIX02 exit, follow step 2 in [Installing the Driver Security System Exits](b3xehpq.html#cegbjdbc).

### Remote Loader Task

The Remote Loader from the previous RACF driver is a job named LDXDRVRP that runs Java in the Open Edition environment. Since it is no longer needed you will need to stop LDXDRVRP and remove it from your system’s startup routines.

The new embedded remote loader is included in the new RACF Driver Shim, RACFDRV, which runs as a native z/OS started task.

To install this new Driver Shim, follow the instructions in [Setting Up the Started Tasks](b3xehpq.html#b6gwofm). You will need to customize the RACFDRV JCL to include

* The DSN to locate the LOAD, SAMPLIB, and EXEC data sets, specified by RACFDSN
* The location of your existing change log data set, specified by LOGFILE
* The appropriate cod page, if necessary; see [International Considerations](bmn95bn.html)

Next, you will need to configure the Driver Shim started task with an SSL certificate for secure communication between the Identity Vault and RACF systems. Even if you have completed this once for the previous release of the RACF driver, you will need to repeat the task due to a difference in certificate formats. For instructions, see [Securing the Driver Shim with SSL](b3xehpq.html#b6a6dt2).

Finally, you will need to set passwords for the Remote Loader and the RACF driver. If you have done this with the previous version of the RACF driver, you can migrate those passwords to the new location by copying the lpwd1f40 and dpwd1f40 files to /opt/novell/racfdrv/keys directory. If you have not, you will need to customize and run the SETPWDS script, included in the SAMPLIB data set. Ensure the file permissions on these two files are protected. By default, these permissions are set to owner(0) with read permissions only by owner (600). To assign a user ID to the RACFDRV started task with these UNIX permissions, see step 5 in [Setting Up the Started Tasks](b3xehpq.html#b6gwofm).

### TSO Administrative RACF ID

This RACF ID was used in the previous version to log on to the RACF system and issue commands. In this release, the Remote Loader directly executes commands using the IKJEFTSR service routine interface. Therefore, this ID is no longer needed and can be removed from the RACF system.

### Change Log Started Task

The change log started task, LDXLOGR, has not changed from the previous release, however it is recommended that you use the version that shipped with the updated LOAD library. Customize the LDXLOGRP JCL to include the latest LOAD library in its STEPLIB.

### Publisher Change Log

The RACF driver now supports a new data event type for RACF password phrases. However, all of your existing events that might be queued in the change log will be processed, as is, by the new driver. You do not need to do anything to your existing change log.

However, please do not run the LOGINIT job, as this will clear all events in your existing change log data set.

### APF Authorization

The new LOAD library location, which includes LDXSERV and SAFQUERY, will need to be added to your APF list.

Use the PARMLIB IEAAPFxx or PROGxx member as appropriate. If you use the dynamic APF facility, you can use the SET PROG command to activate your changes. Otherwise, you must IPL for the change to take effect.

## 4.2.2 Upgrading the Identity Vault Components

*NOTE:*Before starting the upgrade, stop the existing RACF driver using iManager.

### Java Utility Library

Previous versions of the RACF driver used methods contained in RACF.jar to convert XDS to RACF commands and RACF commands to XDS documents. This Java archive also provided Telnet routines for connecting to the RACF system and executing commands through the TSO interface. This archive needs to be removed from your Identity Vault’s system path and replaced with the latest version, now named zOS.jar.

Depending on your operating system, remove the old RACF driver Java code as follows:

* If you are running Linux or AIX, enter

  ```
    rpm -e novell-DXMLracf
  ```
* If you are running Windows, locate and remove RACF.jar from

  ```
    \novell\nds\lib
  ```

Depending on your operating system, install the updated version as follows:

* If you are running Linux, enter

  ```
    rpm -ivh novell-DXMLracf-4.8-3.rpm
  ```
* If you are running windows, copy zOS.jar to

  ```
    \novell\nds\lib
  ```

Verify that RACF.jar has been removed and a later copy of zOS.jar has been installed.

*IMPORTANT:*Please be certain you have installed the latest version of zOS.jar,especially if you have ever used the CA-Top Secret\* driver for Identity Manager. This driver includes an older version of zOS.jar that is not compatible with the RACF Driver.

Once you have replaced RACF.jar with the new zOS.jar, you will need to restart eDirectory to refresh the Metadirectory engine’s Java classes.

### RACF Driver Configuration Import

The RACF driver configuration file is an XML file containing policies and installation options for the Driver object that is deployed in the Identity Vault. The new XML configuration file contains some new options for configuring TSO and OMVS segments, as well as options for using RACF password phrases. Neither of these new options are required, however, there are new policies that must be installed into your existing RACF driver instance to properly convert data to and from the new RACF driver.

#### New Required Policies

Three new polices were added to the Publisher Input Policies:

* TSO (RACF) Input Transform
* RACF Back Patch Transform
* Final TSO Input Transform

Each of these XSLT policies is required for the Publisher channel to properly convert the RACF change log event data into XDS-formatted events that the Publisher channel can operate on.

One new policy was added to the Subscriber Output Transformation Policies:

* Subscriber Append RACFCMD

This new policy is required to convert the XDS document into a RACF command, which can then be processed by the new REXX scripts framework.

#### Importing as a New Driver

You can import the new XML configuration to create a brand new RACF Driver object and avoid having to update individual policies. However, if you choose this method, you will need to copy policies from your old driver that are needed for your provisioning guidelines. Furthermore, all associations made through the old driver object will now be invalid. NetIQ recommends you import and update your existing RACF driver.

#### Importing and Updating the Existing RACF Driver

*IMPORTANT:*Some policies in the new RACF driver have been updated. If you have customized any of the default policies that came with previous versions of the RACF driver, be sure to rename your policies so the upgrade process does not replace them.

When you import the new XML configuration, it will prompt you for a new driver name or allow you to select an existing driver to update. Follow these steps:

1. Select your existing RACF driver from the Existing drivers drop-down box.

   *NOTE:*The new RACF driver requires a Remote Loader configuration—even if you are not using the Remote Loader task with your existing RACF driver. Importing the new driver initiates a series of prompts.
2. When prompted for a remote host and port, enter the IP or DNS host address for the RACF system where the driver shim started task will be running. The default port is 8090.
3. Enter the driver object password when prompted.
4. Enter the Remote Loader password when prompted.
5. Respond to any remaining prompts according to how you intend to use the new rules and policies provided with the new RACF driver.
6. Once you have finished responding to these prompts, click Next.

   You will be prompted to choose any policies you wish to update.
7. Select, at least, the following new and required policies:

   * TSO (RACF) Input Transform
   * RACF Back Patch Transform
   * Final TSO Input Transform
   * Subscriber Append RACFCMD
8. Click Next.

   *NOTE:*At this point, you might receive a -613 error from the iManager plug-ins. If this occurs, you can ignore the message and proceed.
9. Click Finish to complete the upgrade.

You also will need to restore any custom RACF driver policies you have written. To do this:

1. Return to the Driver Overview page.
2. Select the Policy Set from which you wish to restore custom policies.
3. Click Insert > Use an existing policy to browse for the name of the custom policy.
4. Repeat steps 2-4 for each custom policy you wish to restore.

If you received a -613 error in Step 8 above, you will need to link the required policies manually. To do this:

1. Return to the Driver Overview page.
2. Select the Input Transform policies.
3. Select Publisher Input Transformation and click Insert to insert the new required input transformation policies.
4. Select Use an existing policy option, then select Final TSO Input Transform.
5. Repeat Step 4 for RACF Back Patch Transform and TSO (RACF) Input Transform.
6. Select, then remove, Input Transformation and Input Transformation Script.

   The remaining Input Transform policies should display as follows:

   * TSO (RACF) Input Transform
   * RACF Back Patch Transform
   * Final TSO Input Transform
7. Update Subscriber Output Transformation Policies and follow the same steps to insert Subscriber Append RACFCMD as the first policy in the list.
