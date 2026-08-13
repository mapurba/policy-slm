# 3.6 Installing the Driver Shim on the Connected System

The driver shim and its files are installed into data sets that you specify, and into files created by the installation process in the HFS.

The driver uses an embedded Remote Loader. It is not necessary to install Java on the connected system.

For all procedures in this section that are performed using the target system, use a user ID with administrative rights.

* [Setting Up the Libraries on Your z/OS System](b3xehpq.html#b686w3q)
* [Authorizing the Driver TSO Commands](b3xehpq.html#b6gg0a2)
* [Securing the Driver Shim with SSL](b3xehpq.html#b6a6dt2)
* [Configuring the Remote Loader and Driver Object Passwords](b3xehpq.html#b6a6fy0)
* [Allocating and Initializing the Change Log Data Set](b3xehpq.html#b689r3r)
* [Setting Up the Started Tasks](b3xehpq.html#b6gwofm)
* [Testing before Installing the Security System Exit](b3xehpq.html#b689zih)
* [Installing the Driver Security System Exit IDMTSSIX](b3xehpq.html#b689zsr)
* [Testing the Completed Connected System Installation](b3xehpq.html#b68a0hn)

## 3.6.1 Setting Up the Libraries on Your z/OS System

The driver shim is packaged as z/OS partitioned data sets (PDS) unloaded with the TRANSMIT command.

* *Driver Samples Library:*
  samplib.xmt contains sample cataloged procedures, other JCL, and sample configuration-related files.
* *Driver Load Library:*
  idmload.xmt contains executable programs for the driver shim.
* *Driver REXX Exec Library:*
  tssexec.xmt contains the REXX execs for the scriptable framework and to perform configuration tasks.

To upload these files to the target system and extract them:

1. Use FTP to upload the files to the target system from the workstation where you placed them in [Step 2](b3xd1sq.html#b6a682m).

   ```
   c:\> ftp Your-z/OS-Host
   User: Your-User-ID
   Password:
   ftp> quote site lrecl=80 recfm=fb
   ftp> binary
   ftp> put samplib.xmt
   ftp> put tssexec.xmt
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
   dsname('sys3.ts.samplib') volume(work0a)
   . . . many IEBCOPY messages . . .
   INMR001I Restore successful to dataset 'SYS3.TS.SAMPLIB'
   READY
   receive indataset(idmload.xmt)
   INMR901I Dataset IDM.LOAD from ADMIN on SYSB
   INMR906A Enter restore parameters or 'DELETE' or 'END' +
   dsname('sys3.ts.load') volume(work0a)
   . . . many IEBCOPY messages . . .
   INMR001I Restore successful to dataset 'SYS3.TS.LOAD'
   READY
   receive indataset(tssexec.xmt)
   INMR901I Dataset IDM.EXECLIB from ADMIN on SYSB
   INMR906A Enter restore parameters or 'DELETE' or 'END' +
   dsname('sys3.ts.execlib') volume(work0a)
   . . . many IEBCOPY messages . . .
   INMR001I Restore successful to dataset 'SYS3.TS.EXECLIB'
   READY
   ```
4. Add the driver load library to the APF list.

   Use the PARMLIB IEAAPFxx or PROGxx member as appropriate. If you use the dynamic APF facility, you can use the SET PROG command to activate your changes. Otherwise, you must IPL for the change to take effect.
5. Restrict access to the driver load library.

   *WARNING:*Do not put the driver load library in the linklist unless you use program protection to secure its contents against unauthorized use. Failure to protect the driver load library introduces security exposures.
6. Customize the JOB card and run the job in the samples library member HFSINST.

   This creates the HFS file system structure for the driver.

## 3.6.2 Authorizing the Driver TSO Commands

LDXSERV, SAFQUERY and TSSLPBK require APF authorization. They reside in the driver load library, which you added to the APF list in [Step 4](b3xehpq.html#b689pdv). You must also add them to the list of authorized TSO commands.

1. Add LDXSERV, SAFQUERY and TSSLPBK to the AUTHCMD NAMES(...) statement in member IKJTSOxx of SYS1.PARMLIB or its equivalent.

   *Example 3-1* Example:

   ```
   AUTHCMD NAMES(...
     other commands...
     LDXSERV SAFQUERY TSSLPBK)
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

Use the same passwords that you used in [Step 11](b1byr9qs.html#b1byr9re) when setting up the driver on the Metadirectory server.

## 3.6.5 Allocating and Initializing the Change Log Data Set

The change log data set is a standard z/OS direct access data set. The change log data set must reside on a shared device unless it is used by only a single system.

Create one change log data set. It is shared by each z/OS system that shares the security system database. The log file utility LDXUTIL is used to initialize the change log data set. The change log data set must be initialized before you start the driver shim started task for the first time.

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

* [Preparing User IDs for the Started Tasks](b3xehpq.html#b6gwp0h)
* [Setting Up the Change Log Started Task](b3xehpq.html#b689vol)
* [Setting Up the Driver Shim Started Task](b3xehpq.html#b6b9x41)

### Preparing User IDs for the Started Tasks

You can use any name for the user IDs.

1. Create the administrative user ID for the change log started task by entering the following single command line:

   ```
   TSS CREATE(LDXLOGR) TYPE(USER) NAME('CHANGE LOG ACID')
     DEPARTMENT(deptname)
     PASSWORD(NOPW,0) FACILITY(STC)
   ```

   Using NOPW creates the user ID without a password. If you assign a password, you will be prompted for it upon starting the change log started task.

   The above example uses the ACID TYPE(USER) for managing ACIDs in a specific Department. Use an appropriate type based on your intended management scope. For example, use TYPE(SCA) to manage ACIDs for any Department or Division.
2. Create the user for the driver shim started task by entering the following single command line:

   ```
   TSS CREATE(TSDRV) TYPE(DCA) NAME('DRIVER SHIM ACID')
     DEPARTMENT(deptname)
     PASSWORD(NOPW,0) FACILITY(STC)
   ```

   In the above example, a Top Secret type DCA is assigned to the user ID, so it can be an administrator type capable of managing ACIDs within a department.

   Using NOPW creates the user ID without a password. If you assign a password, you will be prompted for it upon starting the change log started task.
3. Assign OMVS attributes to the driver shim ACID, which is required to run the driver shim started task, by entering the following command lines:

   ```
   TSS ADDTO(TSDRV) ID(0) HOME(/) OMVSPGM(/bin/sh) DFLTGRP(OMVSGRP)

   TSS MODIFY(OMVSTABS)
   ```

   In this example, UID(0)and DFLTGRP(OMVSGRP) are used. Any UNIX user ID and group may be assigned here, provided they have read/write access to the HFS directories created in [Securing the Driver Shim with SSL](b3xehpq.html#b6a6dt2) and [Configuring the Remote Loader and Driver Object Passwords](b3xehpq.html#b6a6fy0).
4. Assign necessary administrator privileges to the driver shim ACID by entering the following single command:

   ```
   TSS ADMIN(TSDRV) ACID(ALL) MISC1(ALL) MISC2(ALL) MISC9(ALL)
     DATA(RESOURCE, XAUTH, INSTDATA, CICS, PROFILE, ADMIN, NAMES, ACID,
     PASSWORD, ALL)
   ```

   In the above example, administrator privileges are assigned to LIST/CREATE/DELETE/MODIFY ACIDs and all the data within their scope.
5. Add the user ACIDs to the STC table to assign them to the started tasks by entering the following command lines:

   ```
   TSS ADDTO(STC) PROCNAME(LDXLOGR) ACID(LDXLOGR)

   TSS ADDTO(STC) PROCNAME(TSDRV) ACID(TSDRV)
   ```
6. Use the include/exclude file to exclude these users from provisioning.

   *Example 3-3* Example Include/Exclude File Fragment:

   ```
   EXCLUDE
      ...
      LDXLOGR
      TSDRV
      ...
   ENDEXCLUDE
   ```

   For details about the include/exclude file, see [The Connected System Include/Exclude File](b3xxit1.html).

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

1. Copy member TSDRV from the samples library to your started task procedure library (SYS1.PROCLIB or its equivalent). You can give the driver shim started task a different name if necessary.
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

## 3.6.7 Testing before Installing the Security System Exit

You can use the LDXSERV command to test your installation before you install the exit.

1. If it is not already running, start the change log started task.

   For details about starting the change log started task, see [Starting and Stopping the Change Log Started Task](b432wif.html).
2. Issue the following command from a TSO session that has the driver load library included in its STEPLIB concatenation:

   ```
   LDXSERV STATUS
   ```

   Examine the output of the command. You should see information about the memory queue, information about the change log started task, and a valid, empty change log data set.

## 3.6.8 Installing the Driver Security System Exit IDMTSSIX

Follow your normal procedure for applying system-level changes to your z/OS system. We recommend that you do the following:

* Install and test the exit on a test system or partition first.
* Make a copy of applicable libraries before applying any changes.
* Plan a back off procedure.

This exit uses the Top Secret Recovery File Exit to capture TSS commands. There are three different procedures for installing the driver exit module IDMTSSIX into the Top Secret installation exit TSSINSTX. Use the following table to select the procedure to use based on your Top Secret version and your current use of TSSINSTX.

*Table 3-1* Exit Installation Procedure Choices

| Top Secret Version | Your Use of TSSINSTX | Installation Procedure to Use |
| Version 12 | Not used | [Exit Installation Procedure 1](b3xehpq.html#b6cqm28) |
| Version 12 | Using TSSINSTX, but not using either the security file change or password functions | [Exit Installation Procedure 2](b3xehpq.html#b6cqnyt) |
| Any version supported by the driver other than version 12 | Not using TSSINSTX, or using TSSINSTX but not using either the security file change or password functions | [Exit Installation Procedure 2](b3xehpq.html#b6cqnyt) |
| Any version supported by the driver | Already using the security file change or password functions of TSSINSTX | [Exit Installation Procedure 3](b3xehpq.html#b6cqnz2) |

### Exit Installation Procedure 1

1. Allocate and reformat a Recovery File for Top Secret, using TSSMAINT. It will be used in a later step.
2. Use IEBCOPY to copy member TSSINSTX from the driver load library to your TSS load library.

   This member was built based on the sample provided in the TSSOPMAT library for CA Top Secret version 12.
3. If your TSS load library is in the z/OS linklist, refresh LLA with the following operator command:

   ```
   F LLA,REFRESH
   ```
4. Activate the exit using the following operator command:

   ```
   F TSS,EXIT(ON)
   ```
5. Add the following statements to your Top Secret control options parameter file if they are not already used or specified on the TSS JCL:

   ```
   EXIT(ON)
   RECOVER(ON)
   RECFILE(dataset-name)
   ```

### Exit Installation Procedure 2

1. If you are not already using a Top Secret Recovery File, allocate and format a Recovery File for Top Secret, using TSSMAINT.
2. Add the following statements to your modified TSSINSTX source at both the CHANGE and PASSWORD labels:

   ```
            GETMAIN R,LV=72            Get standard savearea
            LR    R11,R13              Save original R13
            LR    R13,R1               New savearea addr into R13
            LR    R1,R9                Copy parmlist base to R1
            L     R15,=V(IDMTSSIX)     Get addr of IDM module
            BALR  R14,R15              Call it
            LR    R1,R13               Copy temp savearea ptr to R1
            LR    R13,R11              Restore R13
            FREEMAIN R,LV=72,A=(1)     Get rid of savearea
            B     EXIT0
   ```

   These statements are in the driver samples library member TSSINSTX.
3. In the TSSINSTX function matrix (label MATRIX near the beginning of the source module), set the following two entries to #####YES:

   ```
   (32) New Password Verification
   (48) Security File Change
   ```

   You can use the MATRIX table in driver samples library member TSSINSTX as an example.
4. Assemble and link TSSINSTX to replace your existing TSSINSTX module. Add the following statements to the link step:

   ```
   //SYSLIB  DD  DISP=SHR,DSN=<driver load library>
   //SYSLIN  DD  DISP=OLD,DSN=<TSSINSTX object from ASM step>
   //        DD  *
     INCLUDE SYSLIB(IDMTSSIX)
     ENTRY TSSINSTX
     NAME TSSINSTX(R)
   ```
5. If your TSS load library is in the z/OS linklist, refresh LLA with the following operator command:

   ```
   F LLA,REFRESH
   ```
6. Activate the exit using the following operator command:

   ```
   F TSS,EXIT(ON)
   ```
7. Add the following statements to your Top Secret control options parameter file if they are not already used or specified on the TSS JCL:

   ```
   EXIT(ON)
   RECOVER(ON)
   RECFILE(dataset-name)
   ```

### Exit Installation Procedure 3

1. If you are not already using a Top Secret Recovery File, allocate and reformat a Recovery File for Top Secret, using TSSMAINT. It will be used in a later step.
2. Determine the calling sequence for your functions and the driver module IDMTSSIX.

   * The driver exit functions never fail a request, and they expect the current request to succeed.
   * If your functions might reject a request, call them before IDMTSSIX.
   * Do not call IDMTSSIX for a request that your exit functions reject.
   * If your exit functions never reject a request, it does not matter whether IDMTSSIX is called before or after your functions.
3. Add the following statements to your modified TSSINSTX source in both the CHANGE and PASSWORD functions:

   ```
            GETMAIN R,LV=72            Get standard savearea
            LR    R11,R13              Save original R13
            LR    R13,R1               New savearea addr into R13
            LR    R1,R9                Copy parmlist base to R1
            L     R15,=V(IDMTSSIX)     Get addr of IDM module
            BALR  R14,R15              Call it
            LR    R1,R13               Copy temp savearea ptr to R1
            LR    R13,R11              Restore R13
            FREEMAIN R,LV=72,A=(1)     Get rid of savearea
            B     EXIT0
   ```

   These statements are in the driver samples library member TSSINSTX.
4. In the TSSINSTX function matrix (label MATRIX near the beginning of the source module), set the following two entries to #####YES:

   ```
   (32) New Password Verification
   (48) Security File Change
   ```

   You can use the MATRIX table in driver samples library member TSSINSTX as an example.
5. Assemble and link TSSINSTX to replace your existing TSSINSTX module. Add the following statements to the link step:

   ```
   //SYSLIB  DD  DISP=SHR,DSN=<driver load library>
   //SYSLIN  DD  DISP=OLD,DSN=<TSSINSTX object from ASM step>
   //        DD  *
     INCLUDE SYSLIB(IDMTSSIX)
     ENTRY TSSINSTX
     NAME TSSINSTX(R)
   ```
6. If your TSS load library is in the z/OS linklist, refresh LLA with the following operator command:

   ```
   F LLA,REFRESH
   ```
7. Activate the exit using the following operator command:

   ```
   F TSS,EXIT(ON)
   ```
8. Add the following statements to your Top Secret control options parameter file, if they are not already used or specified on the TSS JCL:

   ```
   EXIT(ON)
   RECOVER(ON)
   RECFILE(dataset-name)
   ```

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
