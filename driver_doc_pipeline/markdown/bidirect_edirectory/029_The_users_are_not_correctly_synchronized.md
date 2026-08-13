# 10.4 The users are not correctly synchronized

If you add a user on the connected eDirectory system by using the same Authentication ID that was specified in the driver configuration, the newly created user might be synchronized with Identity manager without password.

If the loopback detection is enabled, the change-log fails to pick any changes when you create or modify an object with the same credentials as used in Authentication ID. Authentication ID should be a unique ID in the connected eDirectory that is not used by any users for object creation, modification, or deletion.
