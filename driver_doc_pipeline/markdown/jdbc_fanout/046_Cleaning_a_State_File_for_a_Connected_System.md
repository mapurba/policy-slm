# 7.9 Cleaning a State File for a Connected System

The State Directory specifies the location of the state data stored by the driver instance. The state data might be used to store additional state information in the future. The driver constructs the state files using the object GUID of the connected instance. It begins with jdbc\_ and ends with the GUID of the driver instance. Each driver instance has one state file with a unique file format: jdbc\_<driver instance guid>\_1. For example, jdbc\_bd2a3dd5-d571-4171-a195-28869577b87e\_1.

To clean a state file for a driver instance, remove the corresponding state file from the State Directory.
