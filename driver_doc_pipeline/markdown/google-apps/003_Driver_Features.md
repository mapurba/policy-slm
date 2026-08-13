# 1.2 Driver Features

The G√ā¬†Suite driver can use the local installation of Identity Manager or the Remote Loader Service. The driver can be installed on either Linux or Windows where the Identity Manager Engine or Remote Loader Service resides.

The following sections provide information about how the G√ā¬†Suite Driver supports these standard driver features:

## 1.2.1 Supported Operations

The basic configuration files for the G√ā¬†Suite driver are capable of performing the following operations:

* User Objects √Ę¬Ä¬ď Add, Modify, Delete, Query, Rename, Set/Change Password
* Group Objects √Ę¬Ä¬ď Add, Modify, Delete, Query
* Contact Objects √Ę¬Ä¬ď Add, Modify, Delete, Query
* Organization Unit Objects √Ę¬Ä¬ď Add, Modify, Delete, Query

## 1.2.2 Entitlement Support

The driver has support for both RBE and RBPMs entitlements under Identity Manager 4.x. These entitlements may be used for User account, placement, and group membership.

## 1.2.3 Multiple E-Mail Domain Support

The driver is capable of managing multiple email domains within the same G√ā¬†Suite domain. It is, however, a best practice recommendation to use one driver instance per domain, even when the domains are within the same Google account. The one instance per domain model allows discrete IDV objects to be provisioned into each domain as per business requirements. When one instance is used for multiple domains, IDV objects, such as users, can only be in one domain at a time. Please see Appendix A √Ę¬Ä¬ď Multi E-Mail Domain Support on how to configure the driver.
