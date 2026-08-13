# 5.3 JDBC Driver Settings

You can change the driver options to align with your connected database. [Table 5-1](modify-jdbc-driver-settings.html#b965dak) summarizes the JDBC driver settings.

*Table 5-1* JDBC Driver Settings

| Setting | Description |
| Driver name | The name of the driver that you want to display in the driver set. |
| Target database | The database that the driver connects to. |
| Driver is local/remote | Whether the driver runs locally or remotely on a Remote Loader. |
| Synchronization model | Whether the driver uses views to synchronize directly to existing tables of arbitrary structure or synchronize to intermediate staging tables of a particular structure. |
| Third-party JDBC implementation | The class of the third-party JDBC file specific to the database being synchronized with Identity Manager. For more information, see [JDBC Driver Class Names](supported-third-party-jdbc-drivers.html#bvx38mr). |
| Data flow | Whether the authoritative source of data is the database, Identity Manager, or bidirectional (both the database and Identity Manager). |
| Database host IP address | The IP address of the database host. |
| Database port | The port that the driver shim uses to communicate with the database. If you don’t provide a port number, the Driver Configuration Wizard provides a default port number for the database that you selected at install time. |
| User container DN | The distinguished name (complete context) of the container where the database users are published. For example: data\company\users. |
| Group container DN | The distinguished name (complete context) of the container where the database groups are published. For example: data\company\groups. |
| Publication mode | Whether publication is triggered (default) or triggerless. |
