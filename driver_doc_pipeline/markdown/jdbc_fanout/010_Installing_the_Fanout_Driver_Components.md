# 2.0 Installing the Fanout Driver Components

The Fanout driver and the Fanout agent files are included in the Identity Manager 4.9 installation media. The driver files are automatically installed on the Identity Manager server at the same time as the Identity Manager engine. The installation program extends the Identity Vault’s schema and installs the driver shim. The installation program provides an option to install the Fanout agent. For more information, see [Installing the Fanout Agent with Identity Manager 4.9](how-to-install-fan-out-agent-with-identity-manager-4-7.html).

After the agent is installed, configure the agent to suit your requirement and then create the driver. For more information, see [Section 3.0, Configuring the Fanout Agent](how-to-configure-fan-out-agent.html).

If you are upgrading your existing driver, perform the following tasks:

* Update the current driver packages in Designer. For more information, see [Creating a Fanout Driver Object in Designer](how-to-create-jdbc-fan-out-driver-object-in-designer.html).
* Migrate your existing Fanout agent configuration to the new Fanout agent installed with Identity Manager 4.6. For more information, see [Migrating the Fanout Agent Configuration](how-to-migrate-the-fan-out-agent-configuration.html).
