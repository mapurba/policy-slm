# 8.3 Identity Provisioning

Identity Provisioning uses events from eDirectory to provision user and group account information to the platform. The Platform Receiver, together with the Receiver scripts, provides Identity Provisioning on a platform.

You can use the platform configuration file to specify which users and groups are managed using Identity Provisioning and which ones are managed locally. The driver has a built-in list of special users and groups that, by default, are excluded from Identity Provisioning. For more information about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html). For more information about the standard exclude list, see [Standard Exclude List](babchigb.html).

Each managed user and group is assigned the same UID and GID number across all Linux/UNIX platforms in a Platform Set.
