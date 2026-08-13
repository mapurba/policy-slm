# 2.5 Configuring Entity Data Model

Entity Data Model uses the Entity Data Model driver to integrate collected permissions and permission assignment tasks with the role and resource catalog in Identity Manager. To do so, you must modify the Entity Data Model configuration settings.

* [Integrating the Driver with Entity Data Model](b1fiz4wa.html#b1fiz4wb)
* [Integrating Entity Data Model Data with Identity Manager](b1fiz4wa.html#b1i1jg28)

## 2.5.1 Integrating the Driver with Entity Data Model

You must configure Entity Data Model to support integration with the Entity Data Model driver. NetIQ provides the Identity Governance Configuration utility, which allows you to modify settings for Entity Data Model. For more information about using the utility, see “ [Running the Identity Governance Configuration Ultility](https://www.netiq.com/documentation/identity-governance-35/admin-guide/data/t471a0i3umhe.html)” in the [NetIQ Identity Governance Administrator Guide](https://www.netiq.com/documentation/identity-governance-35/admin-guide/data/front.html).

1. Log in to the server that hosts Entity Data Model.
2. Navigate to the installation directory for Entity Data Model. For example, opt/netiq/idm/apps/idgov.
3. To run the utility, enter the following command:

   ```
   ./bin/configutil.sh -password db_password
   ```
4. Select Miscellaneous Settings.
5. Select Enable integration using Identity Manager Driver for Entity Data Model, then click Save.
6. To enable the new configuration, restart the application server that hosts Entity Data Model.

## 2.5.2 Integrating Entity Data Model Data with Identity Manager

The Entity Data Model driver helps you integrate data that Entity Data Model collects from application sources with role and resource data in Identity Manager. You might want to do this if your Entity Data Model environment collects permissions from applications that are not also connected systems in Identity Manager. After you set up the integration, you can export the permissions and their assignments from the non-connected applications to Identity Manager.

For more information, see [“Integrating Collected Data with identity Manager”](https://www.netiq.com/documentation/identity-governance-35/admin-guide/data/b1i1id2j.html) in the [NetIQ Identity Governance Administrator Guide](https://www.netiq.com/documentation/identity-governance-35/admin-guide/data/front.html).
