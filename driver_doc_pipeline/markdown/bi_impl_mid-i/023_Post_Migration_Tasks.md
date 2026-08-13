# 4.3 Post-Migration Tasks

Perform the steps listed in [Post-Installation Tasks](b3xfpxf.html). After the new driver is operating properly, you can remove the Fan-Out driver components as follows:

1. Delete the Platform object from the Fan-Out driver configuration.
2. Remove Platform Services from the connected system:

   1. Remove ASAMPWD from the QPWDVLDPGM system value.
   2. Remove the ASAM library from your library list.
   3. Remove the ASAM library and /usr/local/ASAM directory created by Platform Services installation.
3. If this is the last platform being served by the Fan-Out driver, you can uninstall the core driver:

   1. Remove the ASAM directory from the file system.
   2. Remove the ASAM System container object and all of its subordinates from the tree.
   3. Uninstall the Fan-Out driver plug-ins.
