# 1.1 Identity Manager GroupWise Driver

The NetIQ Identity Manager GroupWise driver is designed to work with GroupWise server. The GroupWise Identity Manager driver leverages the GroupWise REST services and provides the following benefits:

* It is architecture agnostic.
* It can run locally on the Identity Manager engine or in a Remote Loader configuration.
* It replaces the native JNDI communication layer by using the REST commands sent to the GroupWise Administration Service.
* It is enhanced and virtually eliminates the limitations of previously shipped GroupWise drivers. For example, on Linux, you no longer need to run the driver on the same server where GroupWise Domain is running. Also, you do not need to use ConsoleOne to access the GroupWise server.

## 1.1.1 Supported GroupWise Versions

GroupWise driver supports the following versions:

* GroupWise 2014 SP1 and later supported packs
* GroupWise 18

## 1.1.2 How the Driver Works

The GroupWise driver synchronizes data between the Identity Vault and GroupWise. It manages GroupWise accounts and account information. When a user or a group object is created, modified, renamed, or deleted in the Identity Vault, the driver synchronizes these changes with GroupWise.

When an event is generated in the Identity Vault, the driver processes the event and transforms the received XDS document by applying appropriate rules and policies. The transformed XDS document is passed to driver shim for further processing.
