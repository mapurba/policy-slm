# 3.8 Uninstalling the Driver

* [Uninstalling the Security System Exits](b3xfu1c.html#b6m29nd)
* [Uninstalling the Driver Shim](b3xfu1c.html#b6m2adc)
* [Uninstalling the Driver Object from the Identity Vault](b3xfu1c.html#b6m2a11)

## 3.8.1 Uninstalling the Security System Exits

The procedure you use for uninstalling the security exits depends on how you set them up.

If you linked the LDXNPXIT exit with exits of your own:

1. Reinstall your original exits, then IPL with CLPA to load the relinked exits in the active LPA.
2. If you change the exit names as you relinked them, be sure to also update the GSO EXITS record with the changed exit names.
3. Delete the exit modules from the LPA library containing them. Then IPL with CLPA at a convenient time.

If you are using LDXNPXIT, LDXNPHXT or LDXPOST alone:

1. Update the GSO EXITS record to remove the exit names.

   1. Enter the following TSO commands:

      ```
       READY
      acf
        ACF
      set control(gso) sysid(system)
        CONTROL
      insert sysid(system) exits lidpost() newpxit() npwpexit()
      ```
   2. Install the new values. From an z/OS console, enter:

      ```
       MODIFY ACF2,REFRESH
      ```
2. Delete the exit modules from the LPA library containing them. Then IPL with CLPA at a convenient time.

## 3.8.2 Uninstalling the Driver Shim

1. Remove the change log started task (LDXLOGR) and driver shim (ACF2DRV) started task from your system startup and shutdown procedures.
2. Stop both started tasks (LDXLOGR and ACF2DRV).

   For details, see [Starting and Stopping the Change Log Started Task](b432wif.html) and [Starting and Stopping the Driver Shim Started Task](b6ba6cj.html).
3. Remove members LDXLOGR and ACF2DRV from your started task procedure library.
4. Remove the driver load library from your APF list by modifying PARMLIB IEAAPFxx or PROGxx member as appropriate.

   *NOTE:*If you use the dynamic APF facility, you can use the SET PROG command to activate your changes. Otherwise, you must IPL for the change to take affect.
5. Remove the LDXSERV and ACFQUERY TSO commands from IKJTSOxx.
6. Remove the driver files from the HFS:

   ```
     oshell rm -rf /opt/novell
   ```
7. Delete the SAMPLIB, LOAD and EXEC driver data sets.
8. Delete the change log data set that you created in [Allocating and Initializing the Change Log Data Set](b3xehpq.html#b689r3r).

## 3.8.3 Uninstalling the Driver Object from the Identity Vault

1. In iManager, select Identity Manager Administration from the top menu icons.
2. Under Administration tasks, select Identity Manager Overview.
3. Click Driver Sets and navigate to your driver set by clicking on its name.
4. Click Drivers, then click Delete Driver on the Driver Set Overview page.
5. Select the driver object to be deleted, then click OK.
