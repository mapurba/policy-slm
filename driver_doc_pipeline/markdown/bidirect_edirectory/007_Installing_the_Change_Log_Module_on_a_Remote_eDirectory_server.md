# 3.2 Installing the Change-Log Module on a Remote eDirectory server

For the Bidirectional eDirectory driver to work, you must install the change-log module on the remote eDirectory server. The change-log enables the driver to recognize changes that require publication from the remote eDirectory to the Identity Vault. The change-log module is supported on the following eDirectory version 9.2.x and later.

NOTE:

* If the driver is running on an engine prior to Identity Manager 4.5.4, the driver will connect to Suite B enabled LDAP service on the connected eDirectory only if you enable Always Accept Server Certificate under the driver settings. For more information see, [Driver Settings](driver-configuration.html#bsdm0xp).
* When you configure eDirectory modules in a Suite B mode, they include support for ECDSA certificates and enforce the use of TLS 1.2 and Suite B ciphers as specified in RFC 6460. For more information on configuring eDirectory in Suite B modes, see [NetIQ eDirectory Administration Guide](https://www.netiq.com/documentation/edirectory-9/edir_admin/data/b1i4rmmx.html).
* When you upgrade to driver version 4.0.2 or later, ensure that there are no encrypted attribute events in the change cache.

The change-log module is provided on the Identity Manager media for 64-bit platforms. Copy the change-log module from /IDM/packages/Dirxml-Changelog directory of your installation folder and install it on the connected eDirectory server.

The following sections provide instructions to install the change-log module on Linux and Windows platforms:

* [Extending the Remote eDirectory Schema](installing-the-change-log-module-on-remote-edirectory-server.html#b1kbi2ln)
* [Installing and Upgrading the Change-Log Module on Linux](installing-the-change-log-module-on-remote-edirectory-server.html#cchefejh)
* [Installing and Upgrading the Change-Log Module on Windows](installing-the-change-log-module-on-remote-edirectory-server.html#cchjchhh)

## 3.2.1 Extending the Remote eDirectory Schema

Before installing or upgrading to change-log or driver version 402 or later, you need to manually extend the connected remote eDirectory schema to introduce a new attribute DirXMLServerKeys. You must perform an eDirectory health check to ensure that the tree is ready to accept the new schema.

To extend the clschema.sch schema file, use the [ice utility](https://www.netiq.com/documentation/edirectory-9/edir_admin/data/a5hgmnu.html).

For example:

ice -S SCH -f clschema.sch -D LDAP -s <remote eDirectory server> -d <Admin DN> -w <password>

## 3.2.2 Installing and Upgrading the Change-Log Module on Linux

On Open Enterprise Server 11 SP3, RHEL 7.x Server, and SUSE Linux Enterprise Server (SLES) 11 SP4 servers running eDirectory 8.8.8.8, the change-log 4.0.5 and later, the module requires libstdc++.so.6 package with GLIBCXX\_3.4.20.

To verify which libstdc++.so.6 version is installed on your server, run the strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX command. Ensure the GLIBCXX\_3.4.20 appears.

To install the latest libstdc++.so.6 RPM, use the SLES 11 SP4 update channel and then restart ndsd.

*IMPORTANT:*On SUSE Linux Enterprise Server (SLES) 12.x and Red Hat Enterprise Linux (RHEL) 7.x platforms, Identity Manager supports change-log module version 4.0.2 or later.

### Installing and Upgrading as a Root User

1. Create a remote eDirectory schema file (clschema.sch) with the following content:

   ```
   NDSSchemaExtensions DEFINITIONS ::=
   BEGIN

   "DirXML-ServerKeys" ATTRIBUTE ::=
   {
           Operation               ADD,
           Flags                   {DS_READ_ONLY_ATTR, DS_HIDDEN_ATTR},
           SyntaxID                SYN_OCTET_STRING,
           ASN1ObjID               {2 16 840 1 113719 1 14 4 1 65}
   }

   END
   ```
2. Extend clschema.sch schema. For more information on extending the remote eDirectory schema, see [Extending the Remote eDirectory Schema](installing-the-change-log-module-on-remote-edirectory-server.html#b1kbi2ln).
3. Stop eDirectory.
4. Navigate to the directory containing the change-log RPM and perform one of the following actions:
5. * To install the change-log RPM, run the following command:

     rpm -ivh <rpm name>.rpm

     Example: rpm -ivh ./novell-DXMLChlgx.rpm
   * To upgrade the change-log RPM, run the following command:

     rpm -Uvh --noscripts ./novell-DXMLChlgx.rpm
   * To upgrade the change-log version prior to 4.0.5 (4.0.2, 4.0.3, and 4.0.4) on OES 2018, run the following command:

     rpm -Uvh <rpm name>.rpm --force

     For example: rpm -Uvh /home/novell-DXMLChlgx\*.rpm --force
6. Start eDirectory.

### Installing as a Non-root User

If eDirectory is installed as a non-root user, you must install the Change-Log module as a non-root user. The Change-Log files are included in the driver RPM. To install the Change-Log module, install the driver RPM.

1. Set the root directory to non-root eDirectory location by entering the following command in the command prompt:

   ```
   ROOTDIR=<non-root eDirectory location>
   ```

   This will set the environmental variables to the directory where eDirectory is installed as a non-root user.

   For example, ROOTDIR="/local/home/nruser/base/bshappl/edir, where nruser is the non-root user.

   Note that this location is specified in the example script in Step 2.

   Alternatively, set the root directory by directly editing the script in a text editor before running the script in Step 2.
2. Install the Change-Log module by running the following script in a command prompt:

   ```
   ***************************************************************
   #!/bin/sh
   #set -x
   #Â© 2017 NetIQ Corporation and its affiliates. All Rights Reserved

   clear

   echo "======================================================================"
   echo " Installing packages... "
   echo "======================================================================"

   if [ "$1" == "" ] ; then
           exit
   fi

   pkgfile=$1
   ROOTDIR="/local/home/nruser/base/bshappl/edir"
   RPMDB=$ROOTDIR/rpm

   if [ ! -d "$RPMDB" ] ; then
           mkdir $RPMDB
   fi
           # create rpm database if it doesn't exist
           if [ ! -f $RPMDB/__db.000 ]
           then
   #                mkdir -p $RPMDB
                   rpm --dbpath "$RPMDB" --initdb
           fi

   RPM_FLAGS="--dbpath $RPMDB -Uvh --relocate=/etc=$ROOTDIR/etc --relocate=/opt=$ROOTDIR/opt --relocate=/opt/novell/eDirectory/lib64=$ROOTDIR/opt/novell/eDirectory/lib64 --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles --force"

   rpm $RPM_FLAGS $pkgfile
   ```

## 3.2.3 Installing and Upgrading the Change-Log Module on Windows

1. Create a remote eDirectory schema file (clschema.sch) with the following content:

   ```
   NDSSchemaExtensions DEFINITIONS ::=
   BEGIN

   "DirXML-ServerKeys" ATTRIBUTE ::=
   {
           Operation               ADD,
           Flags                   {DS_READ_ONLY_ATTR, DS_HIDDEN_ATTR},
           SyntaxID                SYN_OCTET_STRING,
           ASN1ObjID               {2 16 840 1 113719 1 14 4 1 65}
   }

   END
   ```
2. Extend clschema.sch schema. For more information on extending the remote eDirectory schema, see [Extending the Remote eDirectory Schema](installing-the-change-log-module-on-remote-edirectory-server.html#b1kbi2ln).
3. Shutdown the eDirectory service.
4. Navigate to the 64-bit folder containing the following DLLs and copy them to the eDirectory installation location. The default install location is C:\Novell\NDS.

   * dirxmllib.dll
   * dxevent.dll
   * xclldap.dll
5. Start the eDirectory service.
