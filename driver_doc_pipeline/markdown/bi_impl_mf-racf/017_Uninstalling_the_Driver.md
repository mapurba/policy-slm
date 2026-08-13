# 3.8 Uninstalling the Driver

* [Uninstalling the Security System Exits](b3xfu1c.html#b6m29nd)
* [Uninstalling the Driver Shim](b3xfu1c.html#b6m2adc)
* [Uninstalling the Driver Object from eDirectory](b3xfu1c.html#b6m2a11)

## 3.8.1 Uninstalling the Security System Exits

To uninstall exit LDXEVX01, the Common Command exit, issue SET PROG=DL from the console.

To uninstall exit LDXRIX02, use the SMP/E RESTORE function and then IPL with the CLPA option.

## 3.8.2 Uninstalling the Driver Shim

1. Remove the change log started task and driver shim started task from your system startup and shutdown procedures.
2. Stop the change log started task and driver shim started task.

   For details, see [Starting and Stopping the Change Log Started Task](b432wif.html) and [Starting and Stopping the Driver Shim Started Task](b6ba6cj.html).
3. Remove members LDXLOGR and RACFDRV from your started task procedure library.
4. Remove the driver load library from your APF list.

   Reverse the action you took in [Step 4](b3xehpq.html#b689pdv).
5. Remove the LDXSERV and SAFQUERY commands from IKJTSOxx.

   Reverse the actions you took in [Authorizing the Driver TSO Commands](b3xehpq.html#b6gg0a2).
6. Remove the driver files from the HFS. They were created in [Step 6](b3xehpq.html#b6a6aw2).

   ```
   rm -rf /opt/novell
   ```
7. Delete the driver samples library, load library, and REXX exec library that you created in [Step 3](b3xehpq.html#b689ggk).
8. Delete the change log data set that you created in [Allocating and Initializing the Change Log Data Set](b3xehpq.html#b689r3r).

## 3.8.3 Uninstalling the Driver Object from eDirectory

1. In iManager, select Identity Manager Overview from the Identity Manager task list on the left side of the window.
2. Navigate to your driver set by searching the tree or by entering its name.
3. Click Delete Driver on the Identity Manager Overview page.
4. Select the Driver object to be deleted, then click OK.
