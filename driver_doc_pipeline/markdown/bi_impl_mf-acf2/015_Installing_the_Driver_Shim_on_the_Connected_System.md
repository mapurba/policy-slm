# 3.6 Installing the Driver Shim on the Connected System

The driver shim and its files are installed into data sets that you specify, and into files created by the installation process in the HFS.

The driver uses an embedded Remote Loader. It is not necessary to install Java on the connected system.

For all procedures in this section that are performed using the target ACF2 system, you must use a privileged user with both TSO and OMVS segments.

Topics in this section include

* [Setting Up the Libraries on Your z/OS System](b3xehpq.html#b686w3q)
* [Securing the Driver Shim with SSL](b3xehpq.html#b6a6dt2)
* [Configuring the Remote Loader and Driver Object Passwords](b3xehpq.html#b6a6fy0)
* [Allocating and Initializing the Change Log Data Set](b3xehpq.html#b689r3r)
* [Setting Up the Started Tasks](b3xehpq.html#b6gwofm)
* [Authorizing the Driver TSO Commands](b3xehpq.html#b6gg0a2)
* [Testing Before Installing the Security System Exit](b3xehpq.html#b689zih)
* [Installing the Driver Security System Exits](b3xehpq.html#cegbjdbc)
* [Testing the Completed Connected System Installation](b3xehpq.html#b68a0hn)

## 3.6.1 Setting Up the Libraries on Your z/OS System

The driver shim is packaged as z/OS partitioned data sets (PDS) unloaded with the TRANSMIT command.

* *Driver Samples Library:*
  SAMPLIB.XMT contains sample cataloged procedures, other JCL, and sample configuration-related files.
* *Driver Load Library:*
  IDMLOAD.XMT contains executable programs for the driver shim.
* *Driver REXX Exec Library:*
  ACF2EXEC.XMT contains the REXX execs for the scriptable framework and to perform configuration tasks.

To upload these files to the target system and extract them:

1. Use FTP to upload the files to the target system from the workstation where you placed them in [Step 2](b3xd1sq.html#b6a682m).

   ```
     c:\> ftp Your-z/OS-Host
     User: Your-User-ID
     Password:
     ftp> quote site lrecl=80 recfm=fb
     ftp> binary
     ftp> put samplib.xmt
     ftp> put acf2exec.xmt
     ftp> quote site pri=30 sec=5 cyl
     ftp> put idmload.xmt
     ftp> quit
   ```
2. Log on to z/OS using the same user ID that you used for the FTP session.
3. Use the TSO RECEIVE command to extract the data sets. When RECEIVE prompts you for parameters, specify the appropriate data set names and volumes according to your standards.

   Place these data sets on a disk volume that is shared by the systems that share the security system database.

   ```
     READY
     receive indataset(samplib.xmt)
     INMR901I Dataset IDM.SAMPLIB from ADMIN on SYSB
     INMR906A Enter restore parameters or 'DELETE' or 'END' +
     dsname('sys3.idm.samplib') volume(work0a)
     . . . many IEBCOPY messages . . .
     INMR001I Restore successful to dataset 'SYS3.IDM.SAMPLIB'
     READY
     receive indataset(idmload.xmt)
     INMR901I Dataset IDM.LOAD from ADMIN on SYSB
     INMR906A Enter restore parameters or 'DELETE' or 'END' +
     dsname('sys3.idm.load') volume(work0a)
     . . . many IEBCOPY messages . . .
     INMR001I Restore successful to dataset 'SYS3.IDM.LOAD'
     READY
     receive indataset(acf2exec.xmt)
     INMR901I Dataset IDM.ACF2EXEC from ADMIN on SYSB
     INMR906A Enter restore parameters or 'DELETE' or 'END' +
     dsname('sys3.acf2.acf2exec') volume(work0a)
     . . . many IEBCOPY messages . . .
     INMR001I Restore successful to dataset 'SYS3.ACF2.ACF2EXEC'
     READY
   ```
4. Add the driver load library to the APF list.

   Use the PARMLIB IEAAPFxx or PROGxx member as appropriate. If you use the dynamic APF facility, you can use the SET PROG command to activate your changes. Otherwise, you must IPL for the change to take effect.
5. Restrict access to the driver load library.

   *WARNING:*Do not put the driver load library in the linklist unless you use program protection to secure its contents against unauthorized use. Failure to protect the driver load library introduces security exposures.
6. Customize and run the JOB card samples library member SAMPLIB(HFSINST).

   This creates the HFS file system structure for the driver.
7. Verify the Unix file structure was created:

   ```
     /opt/novell/acf2drv/
     /opt/novell/acf2drv/keys
     /opt/novell/acf2drv/logs
   ```

## 3.6.2 Securing the Driver Shim with SSL

1. Customize the REXX exec member EXEC(SETCERT) to specify the LOAD library and DRVCONF locations for your installation.
2. Run the REXX member EXEC(SETCERT).
3. When prompted, enter the Metadirectory server host name or IP address and secure LDAP port number (default is 636).
4. When prompted, enter Y to accept the certificate authority presented.

   ```
     You are about to connect to the eDirectory LDAP server to retrieve
     the eDirectory Tree Trusted Root public certificate.

     Enter the LDAP Server Host Address [localhost]: sr.digitalairlines.com
     Enter the LDAP Server Port [636]:

     Certificate Authority:
        Subject:       ou=Organizational CA,o=TREENAME
        Not Before:    20060821144845Z
        Not After:     20160821144845Z
     Do you accept the Certificate Authority? (Y/N) y
   ```
5. Verify the following file was created:

   ```
     /opt/novell/acf2drv/keys/ca.pem
   ```

   *NOTE:*If you are unable to contact the LDAP server using these steps, see [Driver Certificate Setup Failure](b3yee7z.html#b3ygrta).

## 3.6.3 Configuring the Remote Loader and Driver Object Passwords

1. Customize the REXX EXEC(SETPWDS)member to specify the LOAD library and DRVCONF location for your installation.
2. Run the REXX member EXEC(SETPWDS) and respond to the prompts.
3. Verify the following files were created:

   ```
     /opt/novell/acf2drv/keys/lpwd1f40
     /opt/novell/acf2drv/keys/dpwdlf40
   ```

## 3.6.4 Allocating and Initializing the Change Log Data Set

The change log data set is a standard z/OS direct access data set. The change log data set must reside on a shared device unless it is used by only a single system.

Create one change log data set. It is shared by each z/OS system that shares the security system database.Use the log file utility LDXUTIL to initialize the change log data set. The change log data set must be initialized before you start the driver shim started task for the first time.

To allocate and initialize the change log data set:

1. Customize the samples library member LOGINIT.

   Update the JCL to conform to your local installation requirements, and specify the following:

   * The name of your driver load library.
   * A name for your change log data set.
   * The shared disk volume where the change log is to be allocated. Specify a different unit name if appropriate.
2. Run the LOGINIT job.

   An IEC031I D37 message is normal and should be ignored.
3. Ensure that your change log data set is protected appropriately for the sensitive nature of its contents.

*WARNING:*If you initialize a change log data set that contains data, the data is lost.

## 3.6.5 Setting Up the Started Tasks

* [Setting Up the Change Log Started Task](b3xehpq.html#b689vol)
* [Setting Up the Driver Shim Started Task](b3xehpq.html#b6b9x41)

### Setting Up the Change Log Started Task

You must install and run the change log started task on each system that shares the security system database.

To install the change log started task:

1. Copy member LDXLOGR from the samples library to your started task procedure library (SYS1.PROCLIB or its equivalent). You can give the change log started task a different name if necessary.
2. Update the JCL to specify the following:

   * The name of your driver load library
   * The name of your change log data set
3. Add the change log started task to your system startup and shutdown procedures.

   For more information, see [Starting and Stopping the Change Log Started Task](b432wif.html).

   The change log started task should be started during your system startup procedure before user processing begins. Any events of interest that occur are stored in the memory queue until the change log started task has initialized.

   The change log started task should be stopped during your system shutdown procedure after all user processing has ended. Any events of interest that occur after the change log started task shuts down remain in the memory queue and are lost when the system is shut down.
4. Review your Workload Manager definitions to ensure that the change log started task is assigned to a Service Class appropriate for its role.

### Setting Up the Driver Shim Started Task

Install and run the driver shim started task on only one system that shares the security system database.

To install the driver shim started task:

1. Copy member ACF2DRV from the samples library to your started task procedure library (SYS1.PROCLIB or its equivalent). You can give the driver shim started task a different name if necessary.
2. Update the JCL to specify the following:

   * The name of your driver load library
   * The name of your driver shim configuration file

     You can use your driver samples library member DRVCONF as a model. For details, see [The Driver Shim Configuration File](b4baik6.html).
   * The name of your connected system schema file

     You can use your driver samples library member SCHEMDEF as a model. For details, see [The Connected System Schema File](b3xxapt.html).
   * The name of your include/exclude file

     You can use your driver samples library member INCEXC as a model. For details, see [The Connected System Include/Exclude File](b3xxit1.html).
   * The name of your change log data set
   * The name of your driver REXX exec library
3. Add the driver shim started task to your system startup and shutdown procedures.

   For information about starting and stopping the driver shim started task, see [Starting and Stopping the Driver Shim Started Task](b6ba6cj.html).

   The driver shim started task should be started during your system startup procedure before user processing begins. The driver shim started task should be stopped during your system shutdown procedure after all user processing has ended.
4. Review your Workload Manager definitions to ensure that the driver shim started task is assigned to a Service Class appropriate for its role.
5. Assign a restricted user ID to the ACF2DRV started task, which has been authorized for OMVS and TSO.

   ```
     acf
     set lid
     insert acf2drv account audit job security stc tso group(omvsgrp)
     set profile(user) div(omvs)
     insert acf2drv uid(0) home(/) omvspgm(/bin/sh)
   ```

   This user ID must have read/write permissions to the /opt/novell/acf2drv/ directory and subdirectories to run properly. In the example above, these permissions are given to ACF2DRV by uid(0) and group(omvsgrp).

## 3.6.6 Authorizing the Driver TSO Commands

The ACF2 driver uses two TSO commands, LDXSERV and ACFQUERY, to interact with the ACF2 system. These two commands need to be APF-authorized and configured as TSO commands on the ACF2 system:

1. Add LDXSERV and ACFQUERY to the AUTHCMD NAMES(...) statement in member IKJTSOxx of SYS1.PARMLIB or its equivalent.

   *Example 3-1* Example:

   ```
     AUTHCMD NAMES( +
       . . . other commands . . . +
       LDXSERV ACFQUERY)
   ```
2. Use the PARMLIB TSO command to activate your changes.

   *Example 3-2* Example:

   ```
     PARMLIB CHECK(00)
     PARMLIB UPDATE(00)
   ```

## 3.6.7 Testing Before Installing the Security System Exit

You can use the LDXSERV command to test your installation before you install the exit.

1. If it is not already running, start the change log started task.

   For details about starting the change log started task, see [Starting and Stopping the Change Log Started Task](b432wif.html).
2. Issue the following command from a TSO session that has the driver load library included in its STEPLIB concatenation:

   ```
     LDXSERV STATUS
   ```
3. Examine the output of the command. As in the following example, you should see information about the memory queue and the change log started task, as well as a valid, empty change log data set:

   ```
     READY
     ldxserv status

     <ldx>
       <source>
         <product build="20210103" instance="ldxserv" version="4.83">
           NetIQ IDM ACF2 Driver Version 4.8.3.0
         </product>
         <contact>NetIQ Corporation</contact>
       </source>
       <output>
         <status level="success">
           <queue version="4.83" state="active" created-by="" entries="0"/>
           <logger version="4.83" state="active" taskid="LDXLOGR"
              logfilename="SYSTEMS.LDXACF.V4810103.LOGFILE"/>
           <logfile name="SYSTEMS.LDXACF.V4810103.LOGFILE" state="empty"/>
         </status>
       </output>
     </ldx>
   ```
4. Also in this output, check for the following information:

   * The <logfile> element describes the change log data set created earlier (see [Allocating and Initializing the Change Log Data Set](b3xehpq.html#b689r3r)). The name attribute describes the data set location and the state attribute describes how full the change log is, expressed either as a percentage or with the keyword empty.
   * The <logger> element displays the status of the change log started task, including attributes for its version, assigned taskid and logfilename if the change log data set is configured for writing.
   * The <queue> element displays the properties of the cross-memory queue, including attributes for version, number of entries currently queued, and created-by (which module created the queue). Before the Exits are installed, the entries attribute will be 0 and the created-by attribute should be empty.

## 3.6.8 Installing the Driver Security System Exits

The ACF2 driver uses three ACF2 exits for capturing changes in ACF2 and publishing them to the Identity Vault.

* LDXPOST is the ACF2 Logonid exit, invoked by the LIDPOST exit point, which captures and queues changes to the Logonid record database.
* LDXNPXIT is the ACF2 exit, invoked by the NEWPXIT exit point, which captures and queues password changes from terminal logon.

  *NOTE:*The LDXNPXIT exit does not capture administrative password changes from the ACF2 menus or the interactive ACF command.
* LDXNPHXT is the ACF2 exit, invoked by the NPWPEXIT exit point, which captures and queues password phrase changes from terminal logon.

All three exits are optional for capturing changes to ACF2. If you do not intend to capture changes to the Logonid records, then you do not need to install LDXPOST. If you do not intend to capture user password changes at logon time, then you do not need to install LDXNPXIT. If you do not intend to capture password phrases at logon time, then you do not need to install LDXNPHXT.

To install LDXPOST, the Logonid database exit:

1. Copy the LOAD library member LDXPOST into a library specified by SYS1.PARMLIB member LPALSTxx. If you add an additional load library to LPA, you will also need to IPL your system to apply these changes.
2. Update the ACF2 GSO option to add the exits. From TSO Ready:

   ```
     ACF
     SET CONTROL(GSO) SYSID(NAME)
     INSERT SYSID(NAME) EXITS LIDPOST(LDXPOST)
     QUIT
   ```
3. Refresh the GSO record.

   ```
     MODIFY ACF2,REFESH(EXITS)
   ```
4. IPL the system if LPA has been modified.

To install LDXNPXIT, the password change exit:

1. Copy the LOAD library member LDXNPXIT into a library specified by SYS1.PARMLIB member LPALSTxx. If you add an additional load library to LPA, you will also need to IPL your system to apply these changes.
2. Update the ACF2 GSO option to add the exit. From TSO Ready:

   ```
     ACF
     SET CONTROL(GSO) SYSID(NAME)
     INSERT SYSID(NAME) EXITS NEWPXIT(LDXNPXIT)
     QUIT
   ```
3. Refresh the GSO record.

   ```
     MODIFY ACF2,REFESH(EXITS)
   ```
4. IPL the system if LPA has been modified.

To install LDXNPHXT, the password phrase change exit:

1. Copy the LOAD library member LDXNPHXT into a library specified by SYS1.PARMLIB member LPALSTxx. If you add an additional load library to LPA, you will also need to IPL your system to apply these changes.
2. Update the ACF2 GSO option to add the exit. From TSO Ready:

   ```
     ACF
     SET CONTROL(GSO) SYSID(NAME)
     INSERT SYSID(NAME) EXITS NPWPEXIT(LDXNPHXT)
     QUIT
   ```
3. Refresh the GSO record.

   ```
     MODIFY ACF2,REFESH(EXITS)
   ```
4. IPL the system if LPA has been modified.

## 3.6.9 Testing the Completed Connected System Installation

You can, again, use the LDXSERV command to test your installation after installing the ACF2 security exit(s). Issue the following command from a TSO session that has the driver load library included in its STEPLIB concatenation:

```
  LDXSERV STATUS
```

Examine the output of the command. As in the following example, you should see information about the exits, LDXNPXIT and LDXPOST:

```
  READY
  ldxserv status

  <ldx>
    <source>
      <product build="20210103" instance="ldxserv" version="4.83">
        Novell IDM ACF2 Driver Version 4.8.3.0
      </product>
      <contact>NetIQ Corporation</contact>
    </source>
    <output>
      <status level="success">
        <exit name="LDXNPXIT" state="enabled" version="4.83"
          build-date="20210103" times-called="0" events-queued="1" info="OK"/>,
        <exit name="LDXPOST " state="enabled" version="4.83"
          build-date="20210103" times-called="0" events-queued="1" info="ok"/>
      </status>
    </output>
  </ldx>
```

The output will show two <exit> elements that describe the state of each ACF2 exit. Each exit will include:

* A version attribute to describe the version level
* A build-date attribute to describe the exact date of assembly
* A times-called attribute describing how many times the exit has been invoked
* An events-queued attribute to show how many events this particular exit has queued an event into memory
