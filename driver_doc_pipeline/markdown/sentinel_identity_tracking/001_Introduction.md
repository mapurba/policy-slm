# 1.0 Introduction

Users in an IT environment have accounts with multiple applications and sometimes have multiple account identifiers with a single application. For example, if a user has accounts with both Active Directory and an LDAP directory, the user can log in to either of the application or both applications.

Sentinel tracks events related to user activities in applications but, without additional data, Sentinel cannot correlate account activity in different applications with the single user who initiated the actions.

The Driver for Sentinel provides the additional data required to correlate actions in disparate applications with the initiating use. The driver integrates Sentinel with NetIQ Identity Manager to track the user identity associated with each user account and which events those identities have performed. This allows you to rapidly solve a variety of complex business problems. For example, the account tracking solution helps you monitor rogue administration and define what action is taken if this occurs.

* [Components for Identity Tracking](components-for-identity-tracking.html)
* [How the Driver Works](how-the-driver-works.html)
* [Data Transfer Between Systems](data-transfer-between-systems.html)
