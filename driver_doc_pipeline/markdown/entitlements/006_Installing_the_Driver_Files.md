# 3.0 Installing the Driver Files

By default, the Entitlements Service driver files are installed on the Identity Manager server at the same time as the Identity Manager engine. No other installation configurations are supported; you cannot use the Remote Loader to run the Entitlements Service driver.

The installation program extends the Identity Vault’s schema and installs the driver shim. It does not create the driver in the Identity Vault (see [Section 4.0, Creating a New Driver Object](b94c4u0.html)) or upgrade an existing driver’s configuration (see [Section 5.0, Upgrading an Existing Driver](upgrade-existing-driver.html)).
