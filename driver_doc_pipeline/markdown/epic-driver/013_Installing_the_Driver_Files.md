# 2.8 Installing the Driver Files

To install the driver files you must perform one of the following actions based on your platform:

* Linux:

  1. Navigate to the extracted driver zip folder > linux.
  2. Install the netiq-DXMLEpic.rpm in your driver installation directory by running the following command in a terminal window.

     rpm -Ivh <rpm file path>/netiq-DXMLEpic.rpm
  3. Restart Identity Vault.
* Windows:

  1. Navigate to the extracted driver zip folder > windows.
  2. Copy the EpicDriverShim.jar file into the /opt/ novell/eDirectory/lib/dirxml/classes directory, or \Novell\RemoteLoader\lib if the driver is installed with the Remote Loader.
  3. Restart Identity Vault.

When creating the Designer driver object, set the name of the Java class to com.pds.epicdriver.EpicDriverShim, as shown in the following image:

![](../graphics/img03.png)
