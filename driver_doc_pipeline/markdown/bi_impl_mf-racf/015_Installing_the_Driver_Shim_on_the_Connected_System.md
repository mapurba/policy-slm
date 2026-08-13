# 3.6 Installing the Driver Shim on the Connected System

The driver shim and its files are installed into data sets that you specify, and into files created by the installation process in the HFS.

The driver uses an embedded Remote Loader. It is not necessary to install Java on the connected system.

For all procedures in this section that are performed using the target RACF system, you must use a privileged user with both TSO and OMVS segments.

Topics in this section include

* [Setting Up the Libraries on Your z/OS System](b3xehpq.html#b686w3q)
* [Authorizing the Driver TSO Commands](b3xehpq.html#b6gg0a2)
* [Securing the Driver Shim with SSL](b3xehpq.html#b6a6dt2)
* [Configuring the Remote Loader and Driver Object Passwords](b3xehpq.html#b6a6fy0)
* [Allocating and Initializing the Change Log Data Set](b3xehpq.html#b689r3r)
* [Setting Up the Started Tasks](b3xehpq.html#b6gwofm)
* [Testing before Installing the Security System Exit](b3xehpq.html#b689zih)
* [Installing the Driver Security System Exits](b3xehpq.html#cegbjdbc)
* [Testing the Completed Connected System Installation](b3xehpq.html#b68a0hn)

## 3.6.1 Setting Up the Libraries on Your z/OS System

The driver shim is packaged as z/OS partitioned data sets (PDS) unloaded with the TRANSMIT command.

* *Driver Samples Library:*
  samplib.xmt contains sample cataloged procedures, other JCL, and sample configuration-related files.
* *Driver Load Library:*
  idmload.xmt contains executable programs for the driver shim.
* *Driver REXX Exec Library:*
  racfexec.xmt contains the REXX execs for the scriptable framework and to perform configuration tasks.

To upload these files to the target system and extract them:

1. Use FTP to upload the files to the target system from the workstation where you placed them in [Step 2](b3xd1sq.html#b6a682m).

   ```
     c:\> ftp Your-z/OS-Host
     User: Your-User-ID
     Password:
     ftp> quote site lrecl=80 recfm=fb
     ftp> binary
     ftp> put samplib.xmt
     ftp> put racfexec.xmt
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
     receive indataset(racfexec.xmt)
     INMR901I Dataset IDM.RACFEXEC from ADMIN on SYSB
     INMR906A Enter restore parameters or 'DELETE' or 'END' +
     dsname('sys3.racf.racfexec') volume(work0a)
     . . . many IEBCOPY messages . . .
     INMR001I Restore successful to dataset 'SYS3.RACF.RACFEXEC'
     READY
   ```
4. Add the driver load library to the APF list.

   Use the PARMLIB IEAAPFxx or PROGxx member as appropriate. If you use the dynamic APF facility, you can use the SET PROG command to activate your changes. Otherwise, you must IPL for the change to take effect.
5. Restrict access to the driver load library.

   *WARNING:*Do not put the driver load library in the linklist unless you use program protection to secure its contents against unauthorized use. Failure to protect the driver load library introduces security exposures.
6. Customize the JOB card and run the job in the samples library member HFSINST.

   This creates the HFS file system structure for the driver.

## 3.6.2 Authorizing the Driver TSO Commands

LDXSERV and SAFQUERY require APF authorization. They reside in the driver load library, which you added to the APF list in [Step 4](b3xehpq.html#b689pdv). You must also add them to the list of authorized TSO commands.

1. Add LDXSERV and SAFQUERY to the AUTHCMD NAMES(...) statement in member IKJTSOxx of SYS1.PARMLIB or its equivalent.

   *Example 3-1* Example:

   ```
     AUTHCMD NAMES( +
       . . . other commands . . . +
       LDXSERV SAFQUERY)
   ```
2. Use the PARMLIB TSO command to activate your changes.

   *Example 3-2* Example:

   ```
     PARMLIB CHECK(00)
     PARMLIB UPDATE(00)
   ```

   For more information about the PARMLIB command, see the TSO/E System Programming Command Reference for your system.

## 3.6.3 Securing the Driver Shim with SSL

1. Run the REXX exec in the REXX exec library member SETCERT.
2. When prompted, enter the Metadirectory server host name or IP address and secure LDAP port number (default is 636).
3. When prompted, enter Y to accept the certificate authority presented.

   ```
     You are about to connect to the eDirectory LDAP server to retrieve
     the eDirectory Tree Trusted Root public certificate.

     Enter the LDAP Server Host Address [localhost]: sr.digitalairlines.com
     Enter the LDAP Server Port [636]:

     Certificate Authority:
        Subject:       ou=Organizational CA,o=TREENAME
        Not Before:    20160821144845Z
        Not After:     20260821144845Z
     Do you accept the Certificate Authority? (Y/N) y
   ```

## 3.6.4 Configuring the Remote Loader and Driver Object Passwords

Run the REXX exec in the driver REXX exec library member SETPWDS, and respond to the prompts.

Use the same passwords that you used in [Step 11](b1bybgrg.html#b1bxqts4) when setting up the driver on the Metadirectory server.

## 3.6.5 Allocating and Initializing the Change Log Data Set

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

## 3.6.6 Setting Up the Started Tasks

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

   For information about starting and stopping the change log started task, see [Starting and Stopping the Change Log Started Task](b432wif.html).

   The change log started task should be started during your system startup procedure before user processing begins. Any events of interest that occur are stored in the memory queue until the change log started task has initialized.

   The change log started task should be stopped during your system shutdown procedure after all user processing has ended. Any events of interest that occur after the change log started task shuts down remain in the memory queue and are lost when the system is shut down.
4. Review your Workload Manager definitions to ensure that the change log started task is assigned to a Service Class appropriate for its role.

### Setting Up the Driver Shim Started Task

Install and run the driver shim started task on only one system that shares the security system database.

To install the driver shim started task:

1. Copy member RACFDRV from the samples library to your started task procedure library (SYS1.PROCLIB or its equivalent). You can give the driver shim started task a different name if necessary.
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
5. Assign a restricted user ID to the RACFDRV started task, which has OMVS and TSO segments. This user ID must have read/write permissions to the opt/novell/racfdrv directory and subdirectories to run properly.

   ```
     ADDUSER RACFDRV OMVS(UID(0)) TSO RESTRICTED SPECIAL AUDITOR NOPASSWORD NOOIDCARD
     SETROPTS GENERIC(STARTED)
     RDEFINE STARTED RACFDRV.* STDATA(USER(RACFDRV) GROUP(SYS1) TRUSTED(YES))
     SETROPTS CLASSACT(STARTED)
     SETROPTS RACLIST(STARTED)
     SETROPTS RACLIST(STARTED) REFRESH
   ```

   In this example, adding the SPECIAL and AUDITOR attributes allows the driver shim (RACFDRV) to enter any valid RACF command. NOPASSWORD and NOIDCARD “protects” the RACF ID against being used to enter system by any means that requires a password. You will also need to change the SYS1 placeholder to the value of a GROUP profile on your RACF system that can be assigned to started tasks.

   If you wish to assign RACFDRV a UNIX user ID other than “0”, you must then ensure the owner of the /opt/novell/racfdrv directory reflects this new user ID:

   ```
     oshell chown -R RACFDRV /opt/novell/racfdrv
   ```

## 3.6.7 Testing before Installing the Security System Exit

You can use the LDXSERV command to test your installation before you install the exit.

1. If it is not already running, start the change log started task.

   For details about starting the change log started task, see [Starting and Stopping the Change Log Started Task](b432wif.html).
2. Issue the following command from a TSO session that has the driver load library included in its STEPLIB concatenation:

   ```
     LDXSERV STATUS
   ```

   Examine the output of the command. You should see information about the memory queue, information about the change log started task, and a valid, empty change log data set.

## 3.6.8 Installing the Driver Security System Exits

Follow your normal procedure for applying such changes to your z/OS system. We recommend that you

* Install and test the exits on a test system or partition first.
* Make a copy of your system volumes before applying any changes.
* Consider packaging the exits as SMP/E user modifications.

To install the RACF exits:

1. Install LDXEVX01, the Common Command exit, using the Dynamic Exit Facility.

   For testing, we recommend that you set up two PROGxx members in SYS1.PARMLIB (or equivalent), to allow for easy removal of the exit if desired.

   1. Edit SAMPLIB members PROGAD and PROGDL. Change <LDX load library> to your LDX load library name.
   2. Copy these two members to your system PARMLIB data set. If you already have a PROGAD or PROGDL member, rename the LDX members to a PROGxx name that's not in use.
   3. When ready, use the console command SET PROG=AD to activate LDXEVX01 as an IRREVX01 exit point.
   4. To uninstall the LDX exit, issue SET PROG=DL as a console command.

   For permanent installation, do one of the following:

   * Add the EXIT ADD statement in PROGAD to your production PROG xx PARMLIB member.
   * Add a SET PROG=AD command to CONSOL00 or an automation script, so that it is issued during your IPL procedure.
2. Install ICHRIX02, the RACROUTE REQUEST=VERIFY(X) (RACINIT) postprocessing exit.

   * If you do not have an existing ICHRIX02 exit, run the job in the samples library member RIX0A. This job uses SMP/E to linkedit LDXRIX02 into SYS1.LPALIB as exit ICHRIX02.
   * If you have an existing ICHRIX02 exit, update samples library member RIX0B as appropriate. RIX0B installs a router that calls the driver postprocessing exit and your existing exit.

   *NOTE:*To uninstall this exit, use the SMP/E RESTORE function and then IPL with the CLPA option.
3. After you have installed these two exits, IPL the z/OS system with the CLPA option.

## 3.6.9 Testing the Completed Connected System Installation

1. If it is not already running, start the change log started task.

   For details about starting the change log started task, see [Starting and Stopping the Change Log Started Task](b432wif.html).
2. Perform some actions to exercise the security system exit routines and create some sample events.

   1. Change a password using the logon screen.
   2. Create new user ID.
3. Issue the following command from a TSO session that has the driver load library included in its STEPLIB concatenation:

   ```
   LDXSERV STATUS
   ```

   Examine the output of the command. You should see the exit routines loaded, information about the memory queue, information about the change log started task, and a valid, non-empty change log data set.
