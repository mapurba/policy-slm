# 3.2 Activating the Driver

The Identity Manager driver for SOAP is part of the Identity Manager Integration Module for Tools. This integration module includes the following drivers:

* Identity Manager driver for Delimited Text
* Identity Manager driver for REST
* Identity Manager driver for SOAP

This integration module requires a separate activation. After purchasing the integration module, you will receive activation details in your NetIQ Customer Center.

If you create a new SOAP driver in a driver set that already includes an activated driver from this integration module, the new driver inherits the activation from the driver set.

If you create the driver in a driver set that has not been previously activated with this integration module, the driver will run in the evaluation mode for 90 days. You must activate the driver with this integration module during the evaluation period; otherwise, the driver will be disabled.

If driver activation has expired, the trace displays an error message indicating that you need to reactivate the driver to use it. For more information about activation, refer to [Activating Identity Manager](../../../identity-manager-48/idm_overview_planning/data/activating-identity-manager.html#activating-identity-manager) in the [NetIQ Identity Manager Overview and Planning Guide](../../../identity-manager-48/idm_overview_planning/data/netiq-identity-manager-overview-and-planning.html#netiq-identity-manager-overview-and-planning).
