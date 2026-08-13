# 6.0 SCIM Schema Utility

The SCIM schema utility is used to fetch the connected application’s schema. Using the schema mapping policy, the resource attributes of connected application are mapped with the respective resource attributes of Identity Manager.

You can fetch schema of the connected application using one of the following methods:

* SCIM 2.0: The default schema for Users and Groups as defined in [RFC 7643](https://www.rfc-editor.org/info/rfc7643), which holds core users and group along with extended user schema definition.
* Application URL: This utility fetches the schema by querying an application URL. For example, <https://ap17.salesforce.com/services/scim/v2/Schemas>
* Import JSON: If the schema endpoint of a connected application is not available, you can provide a user defined schema file from your local file system. For example, <NIdM\_Driver\_SCIM\schema\scim\_default\_schemas>

After the schema is fetched successfully, the connected application’s resources and its attributes are available in the schema mapping policy. You can now use the new schema for mapping the resources and its attributes accordingly.
