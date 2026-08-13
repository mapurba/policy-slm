# 2.4 Started Task User IDs

You must prepare user IDs for each started task to use. For details, see [Preparing User IDs for the Started Tasks](b3xehpq.html#b6gwp0h).

These user IDs have special requirements.

* [Change Log Started Task User Requirements](b6gej85.html#b6gwhns)
* [Driver Shim Started Task User Requirements](b6gej85.html#b6gwhry)

## 2.4.1 Change Log Started Task User Requirements

The change log started task must run as a user that can update the change log data set.

## 2.4.2 Driver Shim Started Task User Requirements

The driver shim started task user must have rights to update the change log data set and to perform the Subscriber channel actions carried out by the REXX execs, such as creating and modifying users and groups, defining alias information in the catalog, and creating home directories. For details about using the TSS ADMIN command to assign administrative authorities, see your CA Top Secret Security for z/OS Command Functions Guide.
