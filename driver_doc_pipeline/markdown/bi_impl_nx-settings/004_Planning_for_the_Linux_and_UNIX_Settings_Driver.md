# 2.0 Planning for the Linux and UNIX Settings Driver

When you install the Identity Manager driver for Linux and UNIX Settings you are prompted to supply certain information. The prompts are self-explanatory, but you should consider the following questions before installing the driver:

* What range of numbers do you want the driver to use when assigning UID numbers?
* What range of numbers do you want the driver to use when assigning GID numbers?
* Will you be using LUM?
* Will you be using NetIQ® Samba?
* Do you want the driver to assign UID and GID numbers based on the driver’s Identity Manager Stylesheet object or based on the LUM Linux/UNIX Config object?

  *IMPORTANT:*If you use the LUM Linux/UNIX Config object, do not use iManager to enable users for LUM. That could result in duplicate UID assignments.
* Do you need to import some UIDs and GIDs from platforms before running the driver? If so, how will you do the import?
