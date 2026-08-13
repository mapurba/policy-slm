# 7.2 Working with MapDB 3.0.5

NetIQ recommends that you review the following sections before upgrading your driver to work with Identity Manager 4.7 engine:

* [Understanding Identity Manager 4.7 Engine Support for Driver Versions](working-with-mapdb305.html#t45xdplm7bes)
* [Manually Removing the MapDB Cache Files](working-with-mapdb305.html#t45xh79ev1l7)

## 7.2.1 Understanding Identity Manager 4.7 Engine Support for Driver Versions

* Drivers shipped with Identity Manager 4.7 are compatible with Identity Manager 4.7 Engine or Remote Loader. You must perform the following actions to complete the driver upgrade:

  1. Upgrade the Identity Manager Engine.
  2. (Conditional) Upgrade the Remote Loader.
  3. Upgrade the driver.
  4. Manually remove the MapDB state cache files from the Identity Vault’s DIB directory. For more information, see [Manually Removing the MapDB Cache Files](working-with-mapdb305.html#t45xh79ev1l7).
* Drivers shipped before Identity Manager 4.7 are not compatible with Identity Manager 4.7 Engine or Remote Loader.
* Drivers shipped with Identity Manager 4.7 are not backward compatible with Identity Manager 4.6.x Engine or Remote Loader.
* Drivers shipped with Identity Manager 4.7 are not backward compatible with Identity Manager 4.5.x Engine or Remote Loader.

## 7.2.2 Manually Removing the MapDB Cache Files

The Identity Manager engine upgrade process removes the existing MapDB driver work cache files (dx\*) from the Identity Vault’s DIB directory (/var/opt/novell/eDirectory/data/dib or C:\Novell\NDS\DIBFiles). You must manually remove the existing MapDB state cache files for the driver after upgrading the driver. The MapDB state cache files for the JDBC driver are represented in the following format:

jdbc\_<driver instance guid>\_\*

where \* is the name of the state cache file. For example, jdbc\_<driver instance guid>\_0 or jdbc\_<driver instance guid>\_1.t

This action ensures that your driver works correctly with Identity Manager 4.7 engine.
