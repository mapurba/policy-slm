# 2.12 Activating the Driver

To activate the Workday driver, activate the Metadirectory engine, then activate the driver by using the separate Workday activation key. If you created the driver in a driver set that has not been activated, you must activate the Metadirectory engine and the driver within 90 days. Otherwise, the driver stops working.

If driver activation has expired, the following error message is displayed in the ndstrace window:

```
DirXML Log Event -------------------
Driver: \METADIRECTORY\system\DriverSet\WorkdayDriver
Channel: Subscriber
Status: Error
Message: Code(-9075) Shutting down because DirXML engine evaluation period has expired. Activation is required for further use.
```

To use the driver, you must reactivate it.

For more information on activation, see [Activating Identity Manager](../../../identity-manager-48/idm_overview_planning/data/activating-identity-manager.html#activating-identity-manager) “”in the [NetIQ Identity Manager Overview and Planning Guide](../../../identity-manager-48/idm_overview_planning/data/netiq-identity-manager-overview-and-planning.html#netiq-identity-manager-overview-and-planning).
