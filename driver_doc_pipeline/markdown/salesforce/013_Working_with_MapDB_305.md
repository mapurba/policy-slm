# 5.3 Working with MapDB 3.0.5

NetIQ recommends that you review the following sections before upgrading your driver to work with Identity Manager 4.8 engine:

* [Understanding Identity Manager 4.8 Engine Support for Driver Versions](working-with-mapdb.html#t45xdplm7bes)
* [Manually Removing the MapDB Cache Files](working-with-mapdb.html#t45xh79ev1l7)

## 5.3.1 Understanding Identity Manager 4.8 Engine Support for Driver Versions

* Drivers shipped with Identity Manager 4.8 are compatible with Identity Manager 4.8 Engine or Remote Loader. You must perform the following actions to complete the driver upgrade:

  1. Upgrade the Identity Manager Engine.
  2. (Conditional) Upgrade the Remote Loader.
  3. Upgrade the driver.
  4. Manually remove the MapDB state cache files from the Identity Vault’s DIB directory. For more information, see [Manually Removing the MapDB Cache Files](working-with-mapdb.html#t45xh79ev1l7).
* Drivers shipped before Identity Manager 4.8 are not compatible with Identity Manager 4.8 Engine or Remote Loader.
* Drivers shipped with Identity Manager 4.8 are not backward compatible with Identity Manager 4.7.x Engine or Remote Loader.
* Drivers shipped with Identity Manager 4.8 are not backward compatible with Identity Manager 4.6.x Engine or Remote Loader.

## 5.3.2 Manually Removing the MapDB Cache Files

The Identity Manager engine upgrade process removes the existing MapDB driver work cache files (dx\*) from the Identity Vault’s DIB directory (/var/opt/novell/eDirectory/data/dib or C:\Novell\NDS\DIBFiles). You must manually remove the existing MapDB state cache files for the driver after upgrading the driver. The MapDB state cache files for the JDBC driver are represented in the following formats:

* <Salesforce Driver Name>.\*
* <Salesforce Driver Name>

For example, <Salesforce Driver>.p, <Salesforce Driver>.t, or Salesforce Driver1

This action ensures that your driver works correctly with Identity Manager 4.8 engine.
