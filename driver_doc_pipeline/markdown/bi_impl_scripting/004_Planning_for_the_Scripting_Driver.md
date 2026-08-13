# 2.0 Planning for the Scripting Driver

The planning process for the NetIQÂ® Identity Manager Driver for Scripting begins by determining whether you develop your own scripts and policies for use with your external account management system or you obtain them from a third party.

If you are customizing the scripts, the process continues by installing the Scripting driver to a development system. The first decision to make is whether you run the driver shim on Windows or a Linux/UNIX system. (The driver engine component hosted by NetIQ Identity Manager can run on any operating system that supports Identity Manager.) The driver shim should be installed on a system that hosts, or is remotely connected to, the external account management system. The operating system of this system is the operating system of the driver shim.

Your operating system choice determines what scripting language to use. On Linux and UNIX, pre-written libraries are included for Bourne shell, Perl and Python\*. On Windows, libraries are included for Microsoft VBScript and PowerShell\*. Also, with additional development work, you can port these libraries to another scripting language.

Continue the development process by reading [Section 5.0, Customizing the Scripting Driver](b8n5bw5.html) and following its instructions.

If you have obtained custom scripts from a third party, you should follow their instructions for installing the Scripting driver and their custom components.You should install and test the driver on a test system first and then on production systems.

This section reviews some of the issues to consider before you install the Scripting driver. Major topics include

* [Prerequisites for Linux and UNIX Scripting](b8mno8l.html)
* [Prerequisites for Windows Scripting](b8mns15.html)
* [Establishing a Security-Equivalent User](b8mo9gg.html)

For general information about planning for identity management, see the Identity Manager 3.6.1 Installation Guide.
