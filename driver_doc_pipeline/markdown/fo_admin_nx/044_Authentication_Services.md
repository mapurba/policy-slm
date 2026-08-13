# 8.2 Authentication Services

Authentication Services uses eDirectory for functions such as user authentication. The Platform Services Process, together with the System Intercept, provides Authentication Services on a platform.

z/OS\*, Linux and UNIX systems can redirect password verification and password changes through Authentication Services to eDirectory. An IBM\* i (i5/OS and OS/400) system can authenticate users locally, but uses Authentication Services to replicate passwords in its password store from the passwords of objects in eDirectory that correspond to its users. z/OS, Linux and UNIX systems can supplement password redirection with password replication for fail-safe operation.

The Identity Manager Fan-Out Driver uses the system intercept on Windows\* systems to capture password change information and store it in eDirectory. Password change information from eDirectory is delivered to authorized systems as provisioning events, replicating password information from eDirectory.

You can use the platform configuration file to specify which users use Authentication Services and which ones authenticate locally. The driver has a built-in list of special users that, by default, are excluded from Authentication Services. For more information about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html). For more information about the standard exclude list, see [Standard Exclude List](babchigb.html).
