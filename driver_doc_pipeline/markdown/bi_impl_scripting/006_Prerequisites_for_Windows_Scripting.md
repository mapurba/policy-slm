# 2.2 Prerequisites for Windows Scripting

* [Identity Vault Server](b8mns15.html#b8mnsiz)
* [Windows PowerShell](b8mns15.html#bfcuzub)
* [Microsoft .NET Framework](b8mns15.html#b1a818rh)
* [Other Software](b8mns15.html#b8mntk1)

## 2.2.1 Identity Vault Server

The following software is required on the Identity Vault Server:

* NetIQ Identity Manager 4.8 or higher
* NetIQ eDirectory (level supported by Identity Manager and higher)

## 2.2.2 Windows PowerShell

Windows PowerShell is installed by default for Windows Server 2008 R2 and later for servers and Windows 7 and later for workstations. If you are using an older version of Windows, see [Microsoft芒聙聶s website](http://www.microsoft.com) for information on installing PowerShell.

Also be aware of the following:

* Windows PowerShell versions up to 5.x are supported; the latest 5.x version of PowerShell supported by your Windows edition is recommended. Note that the cross-platform versions of PowerShell, i.e. 6.x and higher, are not supported.
* You must use the x86 or x64 version of PowerShell that corresponds with the version of the Scripting Driver you intend to use.
* Before using the Scripting Driver, you must change PowerShell芒聙聶s default script execution policy as follows:

  1. Right-click Windows Powershell (in the Windows PowerShell folder) on the Windows Start Menu and select 芒聙聹Run as Administrator芒聙聺.

     *NOTE:*You must have administrative privileges to run this command.
  2. Enter the following command:

     ```
     Set-ExecutionPolicy Unrestricted
     ```

     The setting is saved automatically.

     *NOTE:*You must have administration privileges to run this command.
  3. Close PowerShell.

## 2.2.3 Microsoft .NET Framework

* If you are running the Script Service for Windows PowerShell ([Running the Script Service for PowerShell (default mode)](b8mow8v.html#brh2if1)), the Microsoft .NET Framework is required.
* By default, the Microsoft .NET Framework 4.0 or higher is required to use the Script Service--the version installed by default on your Windows system is recommended. Additionally, you will need to install the .NET Framework 3.5 Feature--the steps to do so are detailed in the installation instructions (section TODO). Alternatively, if you need to support PowerShell version 2.0, you can use the legacy Script Service by following these instructions:
* + 1. Stop the Script Service if it is running.

  + 2. Backup the following files in the WSDriver\bin directory:
  + - ScriptService.exe
    - ScriptClient.exe
    - SSLogger.dll
    - SSConfFile.dll
  + 3. From the source media, extract the contents of the Win\win\_all\_scriptservice\_ps20.zip file to the WSDriver\bin directory. This will overwrite the files above.
  + 4. Start the Script Service.
* NOTE: the highest version of PowerShell that the legacy Script Service will run is version 2.0, even if later versions are installed on the system.

## 2.2.4 Other Software

* If you use the Script Service for Windows PowerShell, the Microsoft Web Services Enhancement module must be installed from the installation media--see the installation instructions for more information.
* The latest version of NetIQ iManager can be installed on the Identity Vault Server or a separate system.
* NetIQ Designer 3 or 4 (optional; for development).
