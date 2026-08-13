# 4.4 Configuring Business Process

As a part of Workday Business Process, you can specify the container details where the information for delta and future objects must be created in the Identity Vault.

After creating the driver object in designer, double click the connector line and navigate to GCVs > Business Process. The Business Process Configuration page appears. Specify the values as shown below:

* Enable Delta and Future Object Creation: Select the value to true. The associated fields appear as shown below:

  + Delta Object Placement Container: The location of the container in Identity Vault where the delta objects will be created.

    For example, data\workday\deltaObjects is the location in Identity Vault, and the name of the container is deltaObjects.
  + Future Object Placement Container: The location of the container in Identity Vault where the future objects will be created.

    For example, data\workday\futureObjects is the location in Identity Vault, and the name of the container is futureObjects.
  + Future Object Creation Days in Advance: The number of days in advance the future object data must be created in Identity Vault.

    For example:

    - 3: Indicates that the future object will be created 3 days in advance to the effective hiring date.
    - 0: Does not create a future object in advance.
    - -1: Indicates that the future object is to be created after the effective hiring date.
  + Delta and Future Object Retention Period in Days: The number of days the Delta and Future Object must be retained in Identity Vault. If you specify -1, the delta and future state objects will not be cleared.
