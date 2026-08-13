# 11.1 About Platform Services for Linux and UNIX

Platform Services for Linux/UNIX consists of four major components:

* *Platform Services Process:*
  The Platform Services Process receives requests from other processes and manages communications with one or more Core Drivers for Authentication Services.
* *System Intercept:*
  The System Intercept is implemented in most Linux/UNIX systems using a Pluggable Authentication Module (PAM). The Platform Services PAM module communicates with the Platform Services Process for password verification and password changes. In AIX the System Intercept may be implemented either by PAM or LAM (Loadable Authentication Modules), which is IBM’s proprietary predecessor to the PAM standard.
* *Platform Receiver:*
  The Platform Receiver requests provisioning events from Event Journal Services and runs a Receiver script to carry out the appropriate action for each event as it is received.
* *Platform Services Cache Daemon:*
  The Platform Services Cache Daemon requests provisioning events from Event Journal Services and stores the information locally in a memory cache pool. Requests by the local system for account information, such as the Fan-Out Name Services Switch, can access this information efficiently.

## 11.1.1 Secure Sockets Layer Entropy Requirements

Secure Sockets Layer (SSL), used by Platform Services for communication with Core Drivers, requires a source of entropy. Some Linux/UNIX implementations provide a /dev/random device for entropy. If your Linux/UNIX implementation does not include a /dev/random device, you must install an entropy daemon. You must also include an ENTROPY statement in your platform configuration file to specify the source of entropy. For information about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).

## 11.1.2 The Platform Services Process

The Platform Services Process provides an interface for the System Intercept and the AS Client API to one or more Core Drivers for Authentication Services.

The Platform Services Process is called whenever a user attempts to enter the system using a user ID and password or when a user attempts to change the password. Such a request is passed from the system intercept to the Platform Services Process, which then communicates with a Core Driver and returns a response.

The Platform Services Process performs the following tasks:

* Handles password check and password change requests from users
* Communicates with Core Drivers for Authentication Services
* Redirects Authentication Services requests to another Core Driver if a Core Driver is unreachable or returns an unexpected error
* Gathers and logs performance statistics

The Platform Services Process communicates with Core Drivers using Secure Sockets Layer (SSL).

Start the Platform Services Process during system startup and stop it during system shutdown.

The Platform Services Process reads its configuration information from ASAM/data/asamplat.conf, the platform configuration file. The Platform Services Process logs messages to the SYSLOG facility specified by the SYSLOGFACILITY statement in the platform configuration file. For details about the platform configuration file, see. [Section 10.0, The Platform Configuration File](beibfiae.html).

## 11.1.3 The System Intercept

The Platform Services System Intercept communicates with the Platform Services Process for password verification and password changes.

The System Intercept is implemented in most Linux/UNIX systems using a Pluggable Authentication Module (PAM). Platform Services for AIX uses the Loadable Authentication Module (LAM) system provided by AIX. AIX 5.3 and later also supports PAM.

## 11.1.4 The Platform Receiver

The Platform Receiver processes provisioning events received from the Event Journal Services component of the Core Driver.

The Platform Receiver communicates with Event Journal Services using Secure Sockets Layer (SSL). Data is encoded using UTF-8. You can use the CODEPAGE statement in the platform configuration file to configure the Platform Receiver to convert data using a specified code page. For details about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).

Run the Platform Receiver on a schedule that is appropriate for your requirements. For details about Platform Receiver operation, see [The Platform Receiver](babdcabj.html).

The Platform Receiver reads its configuration information from ASAM/data/asamplat.conf, the platform configuration file. It logs messages to the SYSLOG facility specified by the SYSLOGFACILITY statement in the platform configuration file.

When the Platform Receiver successfully updates a password in the local security system or Samba password file, it logs a message to SYSLOG.

## 11.1.5 Receiver Scripts

Receiver scripts for Linux/UNIX platforms are implemented as shell scripts. The Platform Receiver (asamrcvr) runs the scripts from ASAM/bin/PlatformServices/PlatformReceiver/scripts.

Provisioning events are received as groupings of name-value pairs as shown in the following example:

```
enterpriseUserName  bob
```

The Platform Receiver calls a Receiver script whenever it is necessary to obtain information about users or groups on the platform and whenever it is appropriate to take an action for a user or group on the platform.

### Processing Summary

1. When the Platform Receiver calls a Receiver script, it maps the name-value pairs in environment variables as shown in the following example:

   ```
   ENTERPRISEUSERNAME=bob
   ```

   User names and group names are checked for validity before they are mapped to environment variables. A utility Receiver script is called to perform the validity checking.
2. Receiver scripts are called as appropriate to determine group affiliations for user events and group membership for group events.
3. Receiver scripts are called to take the necessary actions.

### Execution Sequence

When the Platform Receiver responds to events by calling the appropriate scripts, the sequence in which those scripts are called is not always consistent. This is because the Platform Receiver’s responses can be influenced by many variables, including:

* Other events received prior to the current event
* The latest synchronization between eDirectory and the connected system

[Table 11-1](bbcjcgif.html#bftd4ri) provides examples of typical script execution order and demonstrates how that order can vary.

*Table 11-1* Script Execution Order Examples

| Event | Script Execution Order |
| Add a user to eDirectory | ``` platformverifyandmapname.sh does_user_exist.sh adduser.sh addusertogroup.sh enableuser.sh disableuser.sh ``` |
| Add a group to eDirectory | ``` platformverifyandmapname.sh doesgroupexist.sh adduser.sh addgroup.sh populategroup.sh ``` |
| Add a user to an eDirectory group (causing the Platform Receiver | (Group event response:)   ``` platformgetgrnam.sh platformgetpwnam.sh doesgroupexist.sh platformverifyandmapname.sh doesgroupexist.sh platformgroupmem.sh ```   *NOTE:*The above scripts provide reason-checking before continuing with the remaining scripts.   ``` modgroup.sh populategroup.sh ```   (User event response:)   ``` platformgetgrnam.sh platformgetpwnam.sh does_user_exist.sh platformverifyandmapname.sh does_user_exist.sh platformgroupaff.sh enableuser.sh disableuser.sh moduser.sh addusertogroup.sh removeuserfromgroup.sh ``` |

## 11.1.6 The Name Service Switch

The Name Service Switch communicates with the Platform Services Cache Daemon for account information defined by the RFC 2307 Posix Profile attributes. This library module may be installed on any Linux or UNIX system for complete account redirection, providing an alternative to storing user and group accounts and passwords locally. This information is delivered from eDirectory™ and updated live through Identity Management event mechanisms.

## 11.1.7 The Platform Services Cache Daemon

The Platform Services Cache Daemon processes provisioning events received from the Event Journal Services component of the Core Driver. These events are stored in local memory for quick access and the cache is updated live when new events are processed. The daemon communicates with Event Journal Services using Secure Sockets Layer (SSL). Data is encoded using UTF-8. You can use the CODEPAGE statement in the platform configuration file to configure the Platform Services Cache Daemon to convert data using a specified code page. For details about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html). Run the daemon on system startup. For details about the daemon's operation, see [The Platform Services Cache Daemon](b15d6zwe.html).

The daemon reads its configuration information from ASAM/data/asamplat.conf, the platform configuration file. The daemon logs messages to the SYSLOG facility specified by the SYSLOGFACILITY statement in the platform configuration file.

## 11.1.8 Authentication Services

Authentication Services for Linux/UNIX redirects authentication requests to eDirectory and can replicate passwords from eDirectory.

When a password for a user associated with a Linux/UNIX system that uses password replication is changed in eDirectory, a provisioning event is generated by the Core Driver and given to the Platform Receiver for processing. By default, the Core Driver converts passwords to lowercase before sending them to the Platform Receiver. For more information about password case, see [Lower Password Case](br3n4tb.html#bfprpgq).

Because password replication information travels in both directions, it is affected by the Include/Exclude lists of both Authentication Services and Identity Provisioning. It is important therefore, to configure the Include/Exclude lists for both the Platform Services Process and the Platform Receiver symmetrically if the platform uses password replication.
