# 1.2 Driver Organization

The Fan-Out Driver has two functional divisions.

* *Authentication Services*
  Provides real-time Identity Vault (eDirectory) access for user authentication and related purposes.
* *Identity Provisioning*
  Provides user and group management.

The Fan-Out Driver has two structural divisions.

* *The Core Driver*
  Interfaces with eDirectory to provide Authentication Services (such as password verification) and provisioning events (such as Add User or Remove Group).
* *Platform Services*
  Uses the Core Driver to bring common authentication and account life cycle management to a broad selection of supported platforms.
