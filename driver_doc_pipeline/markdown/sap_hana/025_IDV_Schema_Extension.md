# C.0 IDV Schema Extension

As part of solution, we need to extend the schema of eDirectory so that the SAP HANA driver can create these additional objects in the IDV. The proposed schema extension in sch formats are available for download. The following classes are added in IDV.

* The schema file should only be extended with the ndssch utility. Using any other method for importing the schema file fails for certain attributes. A sample syntax for importing the schema file has been provided below:

  For Windows:

  Syntax: /opt/novell/eDirectory/bin/ndssch -h IP:PORT -t WIN-TREE-NAME admin-FDN SchemaFilePath/schemaFile.sch -p password

  Example: /opt/novell/eDirectory/bin/ndssch -h WINDOWS\_IP:524 -t WIN\_TREE admin.sa.system /home/sapHana-schema.sch -p password

  For Linux:

  Syntax: ndssch -t LINUX-TREE-NAME admin-FDN SchemaFilePath/schemaFile.sch

  Example: ndssch -t TREE-NAME admin.sa.system /home/sapHana-schema.sch
* Effective Class for UserGroup: sapHanaUserGroup
* Effective Class for Role: sapHanaRole
