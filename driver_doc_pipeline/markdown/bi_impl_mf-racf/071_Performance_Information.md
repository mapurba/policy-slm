# C.4 Performance Information

This section presents the results of a performance case study of the Identity Manager 4.8 driver for RACF. The study is based on software and hardware configurations that may vary from your production deployment. Therefore, the results, which include real-time throughput and mainframe resource usage, are offered only as approximations for calculating similar measurements in your environment.

## C.4.1 Configuration Information

The system on which Identity Manager was installed was a VMWare virtual machine with the following configuration:

* Single Intel\* Xeon\* CPU at 2.5 GHz
* 8 GB RAM
* SLES 10.2 x86\_64
* 64-bit eDirectory 8.8 SP5 (20219.15)
* 64-bit Identity Manager 3.6.1 (3.6.10-20090520)
* Single Driver Set with one driver (RACF)
* Engine trace level 10

The connected z/OS system running RACF consisted of:

* IBM System z10 Business Class Mainframe 2098-E10 model D02
* 8 MB memory
* z/OS 1.10
* RACF with 1000 users

## C.4.2 Performance Metrics

All tests in the case study used three or more of the following benchmarks:

* Real-Time Speed
* CPU-Time
* EXCP-Cnt
* Memory Usage

### Real-Time Speed

This measurement describes the amount of time for a particular transaction in real seconds or milliseconds. It is useful for ascertaining how long a large migration may take or how many events per day can be processed by a particular channel in real time. Real-time measurements are helpful in previewing what to expect in a production deployment; however, they are dependent on a variety of factors, including speed of the mainframe and vault systems, size of the RACF database, size and layout of Identity Vault, operating systems workload, network delays, disk I/O speeds, trace levels, and customized policies.

### CPU-Time

On the mainframe, CPU-Time is a measurement of the amount of CPU processing time consumed by a particular job. This figure can be used for capacity planning.

### EXCP-Cnt

The EXCP-Cnt is the total number of blocks transferred for I/O requests. I/O utilization may also be used for capacity planning.

### Memory Usage

Memory usage is the number of frames allocated by a running task on z/OS. Each frame represents 4096 bytes of memory. In all tests for this study, the memory recorded was the highest observed peak that occurred during transactions.

## C.4.3 Idle Performance

Idle performance measures how the Driver Shim started task performs while no event transactions are being processed.

### Phase Discussion

Driver Shim idle performance is measured in four phases:

* Shim Startup
* Shim Idle (not connected)
* Shim Connection
* Shim Idle (connected)

#### Shim Startup

When the RACF Driver Shim (RACFDRV) is started, various internal tasks are created and executed to create a network listener.

#### Shim Idle (not connected)

This phase describes the time after the Driver Shim has been started and before the engine has established a network connection.

#### Shim Connection

The connection between Identity Manager and the Driver Shim uses SSL negotiations and a handshake, which involves the exchange of passwords for the remote loader and driver. Internally, two new tasks are created to read and parse data exchange and to poll the change log data set.

#### Shim Idle (connected)

Once a connection is established, the Driver Shim periodically polls the change log data set for any new events to publish. In addition, Identity Manager sends keep-alive packets to the Driver Shim to ensure the connection remains intact. For this case study, this phase was tested with a 5-minute publisher polling interval.

### Results

*Table C-3* RACFDRV Idle Performance

| Phase | CPU-Time | EXCP-Cnt | Memory Usage |
| Startup | 0.85 seconds | 1027 | 1447 (5.9 MB) |
| Idle (not connected) | 0.12 seconds/hour | 0/hour | 1447 (5.9 MB) |
| Connection | 1.3 seconds | 477 | 1971 (8.1 MB) |
| Idle (connected) | 1.37 seconds/hour | 455/hour | 1972 (8.1 MB) |

*NOTE:*The polling interval will affect the results for the Idle (connected) phase. For this study, the polling interval was set to 300 seconds (or 5 minutes) and the driver heartbeat was disabled.

*Table C-4* LDXLOGR (LDXLOGRP) Idle Performance

| Phase | CU-Time | EXCP-Cnt | Memory Usage |
| Startup | 0.03 seconds | 8 | 279 (1.1 MB) |
| Idle | 0.04 seconds/hour | 0/hour | 283 (1.2 MB) |

## C.4.4 Subscriber Performance

The Subscriber channel processes events originating in Identity Manager that need to be replicated in the RACF database. In this study, 1000 events were timed for each use case and the results were averaged across all 1000 events. Six event types were included:

* Add User - A new user in Identity Manager is replicated on the connected system using the minimum required fields
* Modify User - A change to a user in Identity Manager causes a change to that user’s REVOKE field in RACF
* Delete User - A user’s deletion in Identity Manager causes that user’s deletion in RACF
* Change Password - A user’s new password in Identity Manager is replicated in RACF
* Entry Query User - Identity Manager queries a user in RACF and reads its NAME field
* Search Query User - Identity Manager queries RACF with a search on the NAME field

Each test was run both with and without the REXX extensions. When the Driver Shim invokes the REXX scripts to execute commands, additional CPU, Time and I/O are consumed to accomplish the task. However, using REXX allows you to customize the provisioning process with native z/OS policy decisions.

*Table C-5* RACFDRV Performance Per Transaction (with REXX)

| Event | CPU-Time | EXCP-Cnt | Memory Usage | Real Time |
| Add User | 0.61 seconds | 310 | 2900 (11.9 MB) | 1.38 seconds |
| Modify User | 0.48 seconds | 181 | 2200 (9.0 MB) | 1.11 seconds |
| Delete User | 0.47 seconds | 294 | 2043 (8.4 MB) | 1.19 seconds |
| Change Password | 0.74 seconds | 399 | 2008 (8.2 MB) | 0.79 seconds |
| Entry Query User | 0.26 seconds | 165 | 2022 (8.3 MB) | 1.85 seconds |
| Search Query User | 1.16 seconds | 3264 | 2023 (8.3 MB) | 3.04 seconds |

*Table C-6* RACFDRV Performance per Transaction (without REXX)

| Event | CPU-Time | EXCP-Cnt | Memory Usage | Real Time |
| Add User | 0.28 seconds | 94 | 2900 (11.9 MB) | 0.87 seconds |
| Modify User | 0.21 seconds | 15 | 2200 (9.0 MB) | 0.71 seconds |
| Delete User | 0.20 seconds | 86 | 2043 (8.4 MB) | 0.77 seconds |
| Change Password | 0.15 seconds | 15 | 2008 (8.2 MB) | 0.65 seconds |
| Entry Query User | 0.10 seconds | 41 | 2022 (8.3 MB) | 0.60 seconds |
| Search Query User | 0.60 seconds | 1199 | 2023 (8.3 MB) | 1.70 seconds |

## C.4.5 Publisher Performance

The Publisher channel processes events originating in the connected system’s RACF database that need to be replicated in the Identity Vault. In this study, 1000 events were timed for each use case and the results were averaged across all 1000 events. Five event types were included:

* Add User - A new user created in RACF with minimum required fields is replicated in Identity Manager
* Add Group - A new group created in RACF with minimum required fields is replicated in Identity Manager
* Modify User - A change to a user’s REVOKE field in RACF causes a change to that user’s account in Identity Manager
* Delete User - A user deleted in RACF causes that user’s deletion in Identity Manager
* Change Password - A user’s new password in RACF is replicated in Identity Manager

For each test, a CLIST containing the commands for each event type, was executed against RACF. To gain accurate samples, measurements were taken in steps:

* First, LDXLOGR was started to move the events from cross memory to the change log.
* Then the CLIST was executed to begin queueing commands and changes. This implies that the performance of the LDXLOGR during this phase was in contention with the actual RACF commands being executed by RACF.
* Finally, the Drive Shim (RACFDRV) was started to fetch each event and publish to the Identity Vault. Default matching rules and placement policies were used.

When LDXLOGRP (monitored on the mainframe as LDXLOGRP) is not bottlenecked by RACF and started after the cross memory queue is populated with events, the CPU-Time and Real Time performance is more efficient. This is demonstrated by the bulk processing results in [Table C-8](bmn9uvw.html#bqkpn80).

*Table C-7* LDXLOGR (LDXLOGRP) Performance Per Transaction (Individual Processing)

| Event | CPU-Time | EXCP-Cnt | Memory Usage | Real Time |
| Add User | 0.002 seconds | 5 | 285 (1.2 MB) | 0.18 seconds |
| Add Group | 0.002 seconds | 5 | 285 (1.2 MB) | 0.18 seconds |
| Modify User | 0.002 seconds | 5 | 285 (1.2 MB) | 0.18 seconds |
| Delete User | 0.002 seconds | 5 | 285 (1.2 MB) | 0.18 seconds |
| Change Password | 0.002 seconds | 5 | 285 (1.2 MB) | 0.18 seconds |

*Table C-8* LDXLOGR (LDXLOGRP) Performance Per Transaction (Bulk Processing)

| Event | CPU-Time | EXCP-Cnt | Memory Usage | Real Time |
| Add User | 0.001 seconds | 5 | 285 (1.2 MB) | 0.003 seconds |
| Add Group | 0.001 seconds | 5 | 285 (1.2 MB) | 0.003 seconds |
| Modify User | 0.001 seconds | 5 | 285 (1.2 MB) | 0.003 seconds |
| Delete User | 0.001 seconds | 5 | 285 (1.2 MB) | 0.003 seconds |
| Change Password | 0.001 seconds | 5 | 285 (1.2 MB) | 0.003 seconds |

*Table C-9* RACFDRV Performance Per Transaction

| Event | CPU-Time | EXCP-Cnt | Memory Usage | Real Time |
| Add User | 0.027 seconds | 7 | 1977 (8.1 MB) | 0.14 seconds |
| Add Group | 0.023seconds | 7 | 1976 (8.1 MB) | 0.12 seconds |
| Modify User | 0.022 seconds | 7 | 1977 (8.1 MB) | 0.10 seconds |
| Delete User | 0.022 seconds | 7 | 1977 (8.1 MB) | 0.10 seconds |
| Change Password | 0.027 seconds | 7 | 1975 (8.1 MB) | 0.14 seconds |
