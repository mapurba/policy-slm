# 10.5 The NDS password does not synchronize on the Subscriber Channel with Read-Only, Filter Read-Only, and Filter Read/Write replicas

The driver fails to synchronize NDS passwords on the Subscriber Channel because changes cannot be written to the replicas enabled with Read-Only, Filter Read-Only, or Filter Read/Write setting. If Prefer Chaining setting is enabled on the replica server, though users are synchronized on the Subscriber channel over the LDAP protocol, the NDS passwords are not synchronized.
