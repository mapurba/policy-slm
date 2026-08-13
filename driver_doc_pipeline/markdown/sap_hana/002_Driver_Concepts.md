# 1.1 Driver Concepts

## 1.1.1 How the Driver Works

The following diagram illustrates the bi-directional relationship between Identity Manager and the connected application.

*Figure 1-1* SAP HANA Driver Architecture

![](../graphics/sap-hana-architecture-diag.png)

The SAP HANA driver supports User, User Group and Roles. It uses JDBC and SSL connection to create and configure for secured communication. Subscriber channel supports all the CRUD (create, read, update, and delete) operations for Users. User Group and Roles operations are supported using Entitlements. Publisher Channel supports all the CRUD operations for Users, User Groups and Roles.

Since SAP HANA does not provide any delta changes, we use our own generic delta computation module. Also we build a wrapper to calculate these delta changes. SAP HANA supports offset pagination as well.
