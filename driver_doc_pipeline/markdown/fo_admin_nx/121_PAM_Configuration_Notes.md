# B.1 PAM Configuration Notes

Identity Manager Fan-Out Driver platforms for most Linux/UNIX implementations make use of the Pluggable Authentication Modules (PAM) framework for system-entry services, such as login. PAM is defined by OSF RFC 86.0.

When a service (login, ftp, user written application, etc.) makes a call to the PAM API, the request is forwarded to the appropriate authentication module based on the specifications you have made in the PAM configuration file, normally /etc/pam.conf. (Most Linux implementations separate the PAM parameters for various services into files in the /etc/pam.d/ directory.) A sample pam.conf file for Platform Services is included in each Linux/UNIX platform distribution.

Topics in this section include:

* [Using the Sample PAM Configuration Files](chdibedb.html#bk44mt1)
* [Beyond Default Configuration for PAM](chdibedb.html#bk45pwp)

## B.1.1 Using the Sample PAM Configuration Files

The simple presence of Platform Services on a Linux or UNIX system is not enough to make PAM work with Identity Manager. This functionality must be activated by adding the appropriate line-entries to your PAM configuration file(s).In most cases, you can determine the necessary line entries by using a set of sample PAM configuration file templates that are part of the Platform Services installation. Using these templates will enable the default PAM support for Platform Services, which is to redirect three of the most common sign-on applications to Identity Manager: ssh, passwd, and su. These templates are located as follows:

| Operating System | PAM Configuration File Templates Location |
| AIX | /usr/local/ASAM/bin/PlatformServices/pam.conf.sample |
| FreeBSD | /usr/local/ASAM/bin/PlatformServices/pam.d |
| HP-UX | /usr/local/ASAM/bin/PlatformServices/pam.conf.sample |
| Linux | /usr/local/ASAM/bin/PlatformServices/pam.d |
| Solaris | /usr/local/ASAM/bin/PlatformServices/pam.conf.sample |

There are two basic methods for using the templates to update PAM on each of your systems based on your current setup, as summarized in the following table.

*Table B-1* Two methods for using the sample PAM configuration files.

| Method | Description | When to use this method | Applications redirected to Identity Manager |
| Replace current configuration file(s) with provided sample(s). | Select from the pre-configured sample files supplied with Platform Services for your version of Linux or UNIX. Use it/them in place of your current PAM configuration file(s). | If you have never modified the default PAM configuration file(s) that came with your implementation of Linux or UNIX, then this easiest method should work for you. | ssh, passwd, su  (default configuration) |
| Use sample(s) as a guide. | Manually modify your current PAM configuration files, using the supplied sample(s) as a guide. | When it is not appropriate to replace your current PAM configuration file(s) with one or more of the supplied samples.  Examples: You have already modified your PAM configuration from the vendor default, or you have an OS version that does not match the samples. | Any you choose. |

## B.1.2 Beyond Default Configuration for PAM

If you want Identity Manager to work with more system-entry applications than those included in the sample file templates included with Platform Services, then you will need to be more familiar with how PAM works. The remainder of this section offers information and examples to use when your needs for PAM surpass the Platform Services default configuration.

* [Stacking Multiple Schemes](chdibedb.html#bk45sl4)
* [Where to Find More Detailed Information about PAM](chdibedb.html#bk45std)
* [Overview of pam.conf](chdibedb.html#bk45szs)
* [Example pam.conf File Fragment](chdibedb.html#bk45tfg)
* [Examples](chdibedb.html#bk45tr8)
* [Using Options with the Platform Services PAM Module](chdibedb.html#bk46632)

### Stacking Multiple Schemes

The PAM architecture enables authentication by multiple authentication services through stacking. Stacking service modules can force users to authenticate to several authentication services, possibly using different passwords, or it can allow users the opportunity to authenticate using any one of several methods or some combination of methods.

It is very important to understand certain return codes returned by services in the stack, because these return codes are used in conjunction with the control flag to determine the behavior of the authentication flow within the stack.

Always test the logical flow of your configuration. Some configurations could allow users to log in without passwords, while others could prevent login by anyone, including root. Many service modules, including the Platform Services service module, treat root differently from other users.

### Where to Find More Detailed Information about PAM

* For detailed information about PAM, see RFC 86.0, included in each Linux/UNIX Platform Services distribution package.
* For PAM configuration file information specific to your Linux/UNIX implementation, see the man pages, typically man pam.conf.
* For Linux-PAM documentation on the Web, see the [Linux Kernel site](http://www.kernel.org/pub).

### Overview of pam.conf

An entry in pam.conf has the form:

```
service   module-type   control-flag   module-path   option
```

* *service*
  The name of a service, such as login and ftp. The specification other indicates the module to be used by all other applications not specified in the file.
* *module-type*
  The type of PAM function.

  + *auth*
    User authentication
  + *account*
    Account access, such as expiration and time of day restrictions
  + *session*
    Session management accounting
  + *password*
    Password change
* *control-flag*
  Determines continuation or failure behavior of the module. This is especially important if stacking is used.

  + *required*
    This module must return success in order to have the overall result be successful. If this module fails, stack processing continues.
  + *requisite*
    Like required, except stack processing fails immediately if this module fails. Requisite is not used in all versions of PAM.
  + *sufficient*
    If this module is successful, skip the remaining modules in the stack, even if their control flags indicate they are required. If this module fails, the overall result might be determined by other modules in this stack.
  + *optional*
    If this module fails, the overall result can be successful if another module in this stack returns success. If this module succeeds, the overall result might be determined by other modules in this stack. If no other modules are required, then a success by an optional module causes success for the stack.
* *module-path*
  The pathname of the module to be invoked for the function. The PAM service module for Platform Services, pam\_ascauth, checks the user ID to see if it is in the Exclude list or is the user ID root (unless the root\_nds PAM parameter is specified). If either condition is met, then pam\_ascauth returns PAM\_IGNORE, which has the same effect as the Platform Services authentication service not being included in the stack.
* *option*
  Command line parameters to be passed to the module. The developer of a module can use these any way desired, but the PAM framework recommends that several parameters always be supported. Among these are use\_first\_pass (use the same password as that used by the first module that asked for one) and try\_first\_pass (like use\_first\_pass, but prompt if it is not valid).

  The Platform Services PAM module supports several other parameters. For details about these parameters, see [Using Options with the Platform Services PAM Module](chdibedb.html#bk46632).

### Example pam.conf File Fragment

The following is a fragment from the sample pam.conf file that is provided with Platform Services for Solaris 8.

```
login auth sufficient /usr/lib/security/pam_ascauth.so.1 stats
login auth required   /usr/lib/security/pam_unix.so.1 try_first_pass
```

This fragment deals with authenticating users of the login service.

The first line specifies the Platform Services PAM module, pam\_ascauth.so.1, passing it a parameter of stats, which causes it to write additional statistics records about its processing to syslog. If pam\_ascauth.so.1 returns success, the user is granted access to the system. If pam\_ascauth.so.1 returns failure, the next module is called.

The second line calls the native Solaris PAM module. It is invoked only if the Platform Services PAM module returns failure. This module first tries the password that was entered by the user and rejected by the driver. If the password is not valid, the user is prompted for the local Linux or UNIX system password. If that password is rejected, the user is not granted access to the system. Even if this module returns success, the next module in the stack, if any, is called.

*WARNING:*You must be familiar with PAM configuration for your particular Linux/UNIX implementation before attempting to create your own PAM configuration files. Take extreme care in configuring PAM on your systems. Mistakes here can result in major security exposures.

### Examples

The examples in the following sections demonstrate possible PAM configurations.

The first section in the [Solaris 2.9 Example PAM Configuration File Fragment](chdibedb.html#bk45ua3) represents the auth configuration for service-name OTHER in a generic Solaris 2.10 /etc/pam.conf file. The first module (pam\_authtok\_get) prompts for a user ID and password. The second module (pam\_dhkeys) does a keylogin (if needed). The third module (pam\_unix\_cred) establishes credentials for Solaris projects (see the project man page). Finally, pam\_unix\_auth is called to do an authentication based on the default repository as listed in nsswitch.conf.

The second section in this example, which would replace the first section, authenticates using the Identity Manager Fan-Out Driver. If the driver authentication fails, an attempt is made to authenticate the user against the local repository, using the password from the driver prompt. Note that pam\_unix\_cred is placed before pam\_ascauth, in case project credentials are needed. There are no known negative side effects to placing the pam\_unix\_cred before pam\_ascauth, even in environments where Solaris projects are not used.

#### Solaris 2.9 Example PAM Configuration File Fragment

```
#vendor supplied
OTHER  auth requisite    pam_authtok_get.so.1
OTHER  auth required     pam_dhkeys.so.1
OTHER  auth required     pam_unix_cred.so.1
OTHER  auth required     pam_unix_auth.so.1

#Identity Manager Fan-Out Driver variation
OTHER  auth required     pam_unix_cred.so.1
OTHER  auth sufficient   pam_ascauth.so.1 stats
OTHER  auth requisite    pam_unix_authtok_get.so.1
OTHER  auth required     pam_dhkeys.so.1
OTHER  auth required     pam_unix_auth.so.1
```

#### FreeBSD 5.5 Example PAM Configuration File Fragment

The following example represents a possible auth configuration for service-name sshd on a FreeBSD\* 5.5 platform. FreeBSD 5.5 uses /etc/pam.d, so this example’s auth fragment comes from /etc/pam.d/sshd and the service-name is reflected in the file name, not the first column in the file.

```
# vendor supplied
auth   required        pam_nologin.so       no_warn
auth   sufficient      pam_opie.so          no_warn no_fake_prompts
auth   requisite       pam_opieaccess.so    no_warn allow_local
#auth   sufficient      pam_krb5.so          no_warn try_first_pass
#auth   sufficient      pam_ssh.so           no_warn try_first_pass
auth   required        pam_unix.so          no_warn try_first_pass

# Identity Manager Fan-Out Driver variation
auth   required        pam_nologin.so       no_warn
auth   sufficient      pam_opie.so          no_warn no_fake_prompts
auth   requisite       pam_opieaccess.so    no_warn allow_local
#auth   sufficient      pam_krb5.so          no_warn try_first_pass
#auth   sufficient      pam_ssh.so           no_warn try_first_pass
auth   sufficient      pam_ascauth.so       stats
auth   required        pam_unix.so          no_warn try_first_pass
```

In the above example, pam\_nologin and pam\_opie\* are placed above pam\_ascauth in the stack so that the features they support remain enabled for all users. Then authentication is attempted via the Fan-Out driver. If the user can not be authenticated with the Fan-Out driver, the local authentication methods are attempted.

#### SUSE® Linux Enterprise Server (versions 10 and 12) Configuration File Fragment

The following example represents a possible auth configuration for service-name sshd on a SUSE 10 and 11 platforms. SUSE, versions 10 and 11 (as with most distributions of Linux), uses /etc/pam.d, so this example’s auth fragment comes from /etc/pam.d/sshd and the service-name is reflected in the file name, not the first column in the file. The various configuration files for many distributions of Linux include a common file for each module type. The following example shows how to add the Fan-Out driver PAM module to a particular service without modifying the common file.

```
# vendor supplied
auth   include        common-auth
auth   required       pam_nologin.so

# Identity Manager Fan-Out Driver variation
auth   sufficient     pam_ascauth.so
auth   include        common-auth
auth   required       pam_nologin.so
```

### Using Options with the Platform Services PAM Module

You can specify the following parameters to the Platform Services PAM module to control its operation:

*Table B-2* Options available for the Platform Services PAM Module

| option | Description |
| always\_fail | Instructs PAM module to always return PAM\_AUTH\_ERR (used for testing). |
| always\_ignore | Instructs PAM module to always return PAM\_IGNORE (used for testing). |
| conf | Specifies where the platform configuration file is located. The default location is /usr/local/ASAM/data/asamplat.conf. Example: conf=/usr/local/ASAM/data/myplat.conf |
| debug | Instructs the PAM module to write debugging records to syslog. |
| ignore\_no\_user | Instructs PAM module to return PAM\_IGNORE when an authentication request returns “No user.” |
| must\_prompt | Instructs PAM module to prompts all users for current password during a password change, even excluded users. |
| no\_warn | Instructs PAM module not to pass any warnings to a system-entry application that is requesting authentication. |
| root\_nds | Forces the root user to be authenticated and managed by the Identity Manager Fan-Out Driver. This is not normally desirable. If this option is not specified, the root user is managed by the local security mechanism. |
| stats | Instructs the PAM module to write syslog records containing authentication statistics. The records contain information on what type of request was made, the result, and the elapsed time to complete the request. |
| succeed\_no\_user | Instructs the PAM module to return PAM\_SUCCESS when an authentication request returns “No user.” |
| try\_first\_pass | Instructs the PAM module to try the password that was provided by the previous PAM module in the stack. If this does not work, the user is prompted to enter a password. |
| use\_first\_pass | Instructs the PAM module to use the password that was provided by the previous PAM module in the stack. If this does not work, the module fails. |

For more information about PAM module configuration, see [Overview of pam.conf](chdibedb.html#bk45szs).
