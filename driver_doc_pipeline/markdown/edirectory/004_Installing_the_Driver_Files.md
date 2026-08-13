# 2.0 Installing the Driver Files

If you are synchronizing information between TreeA and TreeB, you must install the Metadirectory engine and eDirectory driver on eDirectory servers in both trees. Therefore, the installation must be completed twice—once for the Metadirectory engine and eDirectory driver in TreeA and once in TreeB.

The eDirectory servers where you install the driver must hold master or read/write replicas of the objects you want synchronized between the two trees.

The installation program extends the Identity Vault (eDirectory) schema and installs the driver shim. It does not create the driver in the Identity Vault (see [Section 3.0, Creating a New Driver Object](creating-a-new-driver-object.html)) or upgrade an existing driver’s configuration (see [Section 4.0, Upgrading an Existing Driver](upgrading-an-existing-driver.html)).

The eDirectory driver does not use the Remote Loader because the driver in one tree communicates directly with the driver in the other tree.

The eDirectory driver requires the following:

* NetIQ Certificate Server running on each server that hosts the driver.
* A certificate authority (CA) to support SSL encryption between drivers.

NetIQ Certificate Server and the certificate authority are discussed more in [Section 5.0, Securing Driver Communication](securing-driver-communication.html).
