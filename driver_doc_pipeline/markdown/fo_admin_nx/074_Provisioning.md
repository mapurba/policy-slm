# 12.2 Provisioning

There are two primary methods for provisioning: local and virtual.

Local provisioning uses the Platform Receiver (asamrcvr file) and supplied scripts to locally create or modify user and group account information using native commands, such as useradd and user mod. Attributes such as uid, home directory, and login shell can be populated from the Identity Vault or managed by the local Linux or UNIX system.

After installation, the connected Linux or UNIX system can be fully synchronized with the Identity Vault to make associations and synchronize data fields. For more information on this task, see [Running a Full Synchronization](bfmrhmm.html#bfmrj29).

The Platform Receiver needs to be running to keep the system synchronized with the Identity Vault. For more information, see [Starting the Platform Receiver](bfmrhmm.html#bfn7bkm).
