# 8.7 The System Intercept

System integration of Platform Services makes use of standard, vendor-provided system control points.

Details about configuring and administering Platform Services are provided in later sections of this guide. Also be aware that this guide is one of three available administration guides for the Fan-Out Driver, each tailored to the range of platforms with which it can work:

* Identity Manager Fan-Out Driver for Linux and UNIX Administration Guide
* Identity Manager Fan-Out Driver for Mainframes Administration Guide (z/OS)
* Identity Manager Fan-Out Driver for Midrange Administration Guide (IBM i, OS/400, i5/OS)

System integration of Platform Services for z/OS makes use of standard exits provided by the security system in use (RACF\*, CA\* ACF2\*, or CA Top Secret\*). For more information, see the Identity Manager Fan-Out Driver for Mainframes Administration Guide.

System integration of Platform Services for most Linux/UNIX systems makes use of the Pluggable Authentication Module (PAM) framework that is defined by OSF RFC 86.0. Applications must make the appropriate PAM API calls in order to be PAM-aware. You can also modify your applications to use the AS Client API directly. For more information, see the Identity Manager Fan-Out Driver for Linux and UNIX Administration Guide.

System integration of Platform Services for AIX\* supports both the Loadable Authentication Module (LAM) system provided by AIX and the PAM framework; you choose which you wish to use. The PAM framework is only recommended for AIX versions 5.3 and later.

Password changes on an IBM i system are provided to the Core Driver through the Password Change Validation Program Exit, which is controlled by system value QPWDVLDPGM. Password changes in eDirectory are received by the platform as provisioning events. For additional information, see the Identity Manager Fan-Out Driver for Midrange Administration Guide.
