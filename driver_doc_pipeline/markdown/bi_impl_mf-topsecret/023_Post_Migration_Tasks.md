# 4.4 Post-Migration Tasks

Perform the steps listed in [Post-Installation Tasks](b3xfpxf.html).

After the new driver is operating properly, you can remove the Fan-Out driver components.

1. Delete the Platform object from the Fan-Out driver configuration.
2. On the connected system, uninstall Platform Services.
3. If this is the last platform being served by the Fan-Out driver, you can uninstall the Fan-Out core driver.

   1. Remove the ASAM directory from the file system.
   2. Remove the ASAM System container object and all of its subordinates from the tree.
   3. Uninstall the Fan-Out driver plug-ins.
