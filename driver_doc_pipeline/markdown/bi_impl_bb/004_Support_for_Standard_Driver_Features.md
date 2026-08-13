# 1.3 Support for Standard Driver Features

The Blackboard driver is designed to be run as a Remote Loader Service only.

The following sections provide information about how the driver supports standard driver features:

* [Entitlements](btviyt2.html#btvizrb)
* [Schema](btviyt2.html#btvj1bx)
* [Object Classes](btviyt2.html#btvj1by)
* [Configuration](btviyt2.html#btvj2rr)

## 1.3.1 Entitlements

The Blackboard driver can be configured to use entitlements to manage user accounts in Blackboard. When using entitlements, this driver works in conjunction with external services, such as the User Application with workflow or role-based provisioning or the Entitlements Service driver, to manage entitlement functionality.

## 1.3.2 Schema

The Blackboard driver uses the Blackboard schema to describe the attributes of Person, Course, Organization, and Enrollment objects in Blackboard. Optional schema definitions for the Blackboard driver are included in the blackboard.sch file.

## 1.3.3 Object Classes

The Blackboard driver provides auxiliary classes that can be used to add Blackboard-specific schema attributes to User and Group objects in eDirectory. Optional schema definitions for the Blackboard driver are included in the blackboard.sch file.

## 1.3.4 Configuration

The behavior of an Identity Manager driver is governed by its configuration of options, policies, and filters. The configuration of the Blackboard driver is managed by several packages that can be installed and configured using Designer for Identity Manager.
