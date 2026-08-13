# 1.0 Overview

The Identity Manager 4.8 driver for Scripting synchronizes data between the Identity Vault and a connected system using a scripting environment suitable for the target application. Languages such as Shell, Perl\* and Microsoft\* VBScript\* can be used to extend the base set of sample scripts to update and retrieve information from the target application. Traditional driver development is accomplished with Java\* and the Policy Builder. With the Scripting environment, driver development can be done in alternate languages, which provide a large set of packages and complex language syntax. In addition, your target application might already provide management tools, commands, or APIs written or easily accessible in Perl, Shell Script or VBScript.

The Scripting driver runs on a large number of Linux and UNIX platforms, including Linux, Solaris\*, AIX\* and HP-UX\*. In addition, a Microsoft Windows\* service is available for applications that run on the Windows platform. The driver also uses embedded Remote Loader technology to communicate with the Identity Vault, bidirectionally synchronizing changes between the Identity Vault and the connected system. The embedded Remote Loader component, also called the driver shim, runs as a native process on the connected Linux or UNIX system or a Windows service on a Windows system. There is no requirement to install Java on the connected system. The simplicity of installation, configuration and security provides an excellent environment for the development of new drivers.

Major topics in this section include

* [Driver Architecture](b8mn84s.html)
* [Configuration Overview](b8mncmk.html)
