# 11.2 Step-by-Step Installation Instructions

This section presents step-by-step tasks that can be used in various Platform Services installation scenarios.

Before beginning installation, be sure to complete the following:

* Verify that your platform meets minimum system requirements. For information about required systems and software, as well as supported platforms and operating environments, see the [Identity Manager 4.8 Drivers Documentation Web site](https://www.netiq.com/documentation/identity-manager-47-drivers). From this index page, you can select a Readme file associated with the platform(s) for which you need Fan-Out Driver support.
* To improve your readiness, complete the planning suggestions detailed in [Section 9.0, Planning for Platform Services](brfhf59.html) before you begin.
* Install, setup and configure the Fan-Out Core Driver (see [Section 5.0, Installing the Core Driver](bcgicacb.html))
* Follow the steps in [Configuring Platforms](br3n4tb.html#bfijtk0).
* Obtain the Platform Services distribution package for your target operating system from the [NetIQ downloads site](http://download.novell.com).
* Always check the [NetIQ Support Web Site](http://support.netiq.com) for the latest support pack and product update information. Check the Release Notes and Readme files for the version you are installing for any special actions that might be required.

When you are ready to begin installation, refer to the following tasks, depending on your scenario:

* [Installing Platform Services](bbcdjghj.html#bfmrexb)
* [Upgrading Platform Services](bbcdjghj.html#bfmrh03)
* [Executing Commands for Unattended Installation](bbcdjghj.html#bfmrh04)
* [Customizing Installation](bbcdjghj.html#bfmrh05)

## 11.2.1 Installing Platform Services

To install Platform Services:

1. From your installation media, locate and execute the appropriate self-extracting installer:

   ```
   sh aix_platformservices.bin
   sh freebsd_x86_platformservices.bin
   sh hpux_platformservices.bin
   sh hpux_ia64_platformservices.bin
   sh linux_x86_platformservices.bin
   sh linux_x86_64_platformservices.bin
   sh debian_x86_platformservices.bin
   sh linux_s390x_platformservices.bin
   sh solaris_sparc_platformservices.bin
   sh solaris_x86_platformservices.bin
   sh tru64_platformservices.bin
   ```
2. Select a language, read and accept the License Agreement.
3. Enter a path for installation or press the Enter key for the default, /usr/local.
4. Enter the address of the primary Core Driver.

   This represents the hostname or IP address of the system running the Core Driver Shim.
5. Enter the TCP port of the primary Core Driver or enter the default, 3451.
6. If you wish to enter secondary drivers, select y and repeat steps 4-5 of this task for each. Otherwise, select n.
7. Enter the name of the platform.

   *NOTE:*The name you enter needs to have already been setup and specified when the Core Driver was configured for a new connected system, prior to Platform Services installation.
8. Enter an eDirectory administrative user.

   This identity will authenticate to eDirectory and must have read and write privileges to the ASAM System container subtree.
9. Enter the password for the eDirectory administrative user.
10. Choose a provisioning option to configure this platform:

    * Select a to provision users and groups to /etc/passwd and /etc/group.
    * Select b to setup the system’s Name Service Switch (NSS) for virtual provisioning.
    * Select c to configure this platform for API use only (no provisioning).

    *NOTE:*For more information about these options, see [Provisioning](bfqqm8v.html).
11. Choose an option for user password authentication:

    * Select a to redirect authentication requests to the Metadirectory.
    * Select b to authenticate users locally from /etc/shadow.
    * Select c to redirect authentication requests to the Metadirectory but synchronize passwords to provide local failover.

    *NOTE:*For more information about these options, see [Authentication](bfqqmfq.html).
12. If you selected b or c in the previous step, now select whether users can change their eDirectory passwords from this Linux/UNIX platform.

## 11.2.2 Upgrading Platform Services

To upgrade an existing installation of Platform Services:

1. If any Platform Services daemons are running, be sure to stop them before proceeding. For more information, see [Stopping Platform Services](bfmrhmm.html#bfmrj2b).
2. From your installation media, locate and execute the appropriate self-extracting installer:

   ```
   sh aix_platformservices.bin
   sh freebsd_x86_platformservices.bin
   sh hpux_platformservices.bin
   sh hpux_ia64_platformservices.bin
   sh linux_x86_platformservices.bin
   sh linux_x86_64_platformservices.bin
   sh debian_x86_platformservices.bin
   sh linux_s390x_platformservices.bin
   sh solaris_sparc_platformservices.bin
   sh solaris_x86_platformservices.bin
   sh tru64_platformservices.bin
   ```
3. Select a language, read and accept the License Agreement.
4. When prompted to Update Package, select y.
5. Restart your Platform Services daemon. For more information, see [Starting Platform Services](bfmrhmm.html#bfmrj2a)

## 11.2.3 Executing Commands for Unattended Installation

Since the release of Identity Manager 3.6, the Fan-Out Platform Services installer supports command-line non-interactive installations and configurations. Using this feature you can install Platform Services with a single command line, allowing the entire process to be scripted for a mass deployment. To use the unattended installation feature, you must specify the -non-interactive parameter with one or more of the following parameter options.

* To specify the DNS or IP hostname(s) and TCP port(s) of the Fan-Out Core Driver Shim:

  ```
  -corehost hostname:port[,hostname:port]
  ```

  For example, if you had three hosts, the command line would be similar to the following:

  ```
  -corehost host10:3451,host20:3451,host30:3451
  ```
* To specify the eDirectory administrative user:

  ```
  -admin admin-dn
  ```
* To specify the password for the eDirectory administrative user:

  ```
  -password password
  ```
* To specify the name of the platform object to configure this host with:

  ```
  -platname name
  ```
* To specify the name of the platform set under which to auto-create the platform object, use all of the following options:

  ```
  -platformset name
  -permit-pass-sync <yes | no | ifAvailable>
  ```

  When you specify a platform set and a permit password sync option, the platform will be automatically created within the specified platform set with the corresponding password sync options. The IP or DNS information will also be automatically populated by the Core Driver. If a platform with this name already exists, the installation will fail.
* To specify the platform’s provisioning configuration, use one of these options:

  ```
  -local-prov | -nss-prov | -no-prov
  ```

  Respectively these options represent: local provisioning, NSS (virtual) provisioning, and API only (no provisioning).
* To specify the platform’s authentication configuration, use one of the following options:

  ```
  -auth-redir | -auth-local | -auth-local-failover
  ```

  Respectively these options represent: redirect authentication, authenticate locally, and authentication redirection with local failover.
* To specify whether PAM should be auto-configured for password publishing, use one of the following options:

  ```
  -pam-pass | -no-pam-pass
  ```
* To specify the installation path:

  ```
  -path path
  ```
* To specify the default run mode (operation mode) of the Platform Receiver:

  ```
  -runmode <persistent | polling>
  ```

### Example of Unattended Installation Command

The following command will automatically install Platform Services on Linux for local authentication and provisioning:

```
sh linux_x86_platformservices.bin -non-interactive
    -corehost 10.0.0.1:3451 -admin admin.acme -password novell
    -platname linux123 -local-prov -auth-local -pam-pass
    -path /usr/local -runmode persistent
```

## 11.2.4 Customizing Installation

If you have a custom process for deploying installations, upgrades or updates, you may prefer to extract the installation content manually for integration into your process. The self-extracting .bin installers use platform-specific packages to deploy the distribution files. These packages can be recovered by executing the appropriate installer with the -extract parameter.

For example, if linux\_x86\_64 were the operating system architecture of your target platform, you would execute the following command:

```
  sh linux_x86_64_platformservices.bin -extract
```

This resulting extraction would produce the following temporary directory structure:

```
  linux_86_64
  linux_86_64/setup
  linux_86_64/setup/admin.fanplat
  linux_86_64/setup/install
  linux_86_64/license-C.txt
  linux_86_64/license-zh_cn.txt
  linux_86_64/license-de.txt
  linux_86_64/license-cs.txt
  linux_86_64/package
  linux_86_64/package/novell-DXMLfanplat-4.8.rpm
  linux_86_64/license-es.txt
  linux_86_64/license-fr.txt
  linux_86_64/license-it.txt
  linux_86_64/license.txt
  linux_86_64/license-jp.txt
  linux_86_64/license-zh_tw.txt
  linux_86_64/license-nl.txt
  linux_86_64/license-pl.txt
  linux_86_64/license-pt.txt
  linux_86_64/license-ru.txt
  linux_86_64/license-sv.txt
```

The installation script is located under the setup directory. The native package file, which is located inside the package directory, will vary in name depending on the operating system used by your target platform. To determine the name of your native package file, see [Table 11-2](bbcdjghj.html#bfn59no).

*Table 11-2* Native Package Names by Platform.

| Platform | Native Package Name |
| Linux | novell-DXMLfanplat-4.8.rpm |
| Solaris | DXMLfanplat-4.8.pkg |
| AIX | novell-DXMLfanplat-4.8.rpm |
| HP-UX | novell-DXMLfanplat-4.8.depot |
| FreeBSD | novell-DXMLfanplat-4.8.tgz |
| Debian | novell-DXMLfanplat-4.8.deb |

Once you have extracted the contents from the .bin archive, you may choose to modify the configuration script, <os>/setup/install, and wish to rebundle the contents into a new .bin installer. To do so, first extract the header file:

```
  head -n 76 <os>_platformservices.bin > header
```

Then, edit the files as necessary inside the <os> directory. Finally, recreate the .bin:

```
  tar cf <os>_platformservices.tar <os>
  cat header <os>_platformservices.tar > <os>_platformservices.bin
```
