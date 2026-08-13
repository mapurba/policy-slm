# 8.8 The Platform Receiver

The Platform Receiver obtains provisioning events from the Event Journal Services component of the Core Driver. The Platform Receiver examines each event and the current status of users and groups on the platform. Then the Platform Receiver calls Receiver scripts as necessary to perform needed changes. On password replication platforms, the Platform Receiver also updates the local password store.

The Platform Receiver provides failover support for connections to Event Journal Services.

The Platform Receiver obtains configuration information, such as its mode of operation and the location of the Core Driver, from the platform configuration file. For additional information about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).

## 8.8.1 Modes of Operation

The Platform Receiver can be configured to obtain and process provisioning events in five different modes.

### Full Sync Mode

In Full Sync Mode, the Platform Receiver connects to Event Journal Services and requests a Full Sync. Event Journal Services provides, and the Platform Receiver processes, a complete set of provisioning events to populate the users and groups for the platform. Then the Platform Receiver ends.

The first time a Platform Receiver is run for a new platform, it automatically receives provisioning events for all users and groups for the platform. If this process is interrupted, processing resumes the next time the Platform Receiver is run. There is no need to run the Platform Receiver in Full Sync Mode during routine installation.

You can run the Platform Receiver in Full Sync Mode to recover from a disaster on the platform that affects the user or group population.

You can run the Platform Receiver in Full Sync Mode any other time as appropriate to ensure that the user and group population on the platform is consistent with eDirectory.

If a Full Sync operation is interrupted, the provisioning process resumes the next time the Platform Receiver is run in Persistent Mode, Polling Mode, or Scheduled Mode. Do not start the Platform Receiver in Full Sync Mode to recover from an interrupted Full Sync operation, because Full Sync processing starts from the beginning each time.

### Check Mode

Check Mode functions similarly to Full Sync Mode, except that Receiver scripts are invoked in Check Mode. In Check Mode, the base scripts take no actions to alter the user or group population on the platform.

If you extend the base scripts, take no actions that alter the user or group population while Check Mode is in effect.

Operation in Check Mode does not affect the queue of pending events maintained by Event Journal Services for the platform.

Check Mode is useful for testing your extensions to Receiver scripts.

You can use Check Mode at any time to verify that the user and group population on the platform is consistent with eDirectory.

### Persistent Mode

In Persistent Mode, the Platform Receiver connects to Event Journal Services, obtains queued provisioning events, and processes them. It then remains connected, processing additional events as they become available.

### Polling Mode

In Polling Mode, the Platform Receiver connects to Event Journal Services, obtains queued provisioning events, and processes them. The Platform Receiver then closes the connection, waits for five minutes, and repeats the process until you stop it. For details about specifying the interval between polling cycles, see [POLLINT Statement](beiffigc.html#brg3ye0) and [POLLRAND Statement](beiffigc.html#bhf0ja6).

### Scheduled Mode

In Scheduled Mode, the Platform Receiver connects to Event Journal Services, obtains queued provisioning events, and processes them. It then closes the connection and ends. Scheduled Mode is designed for use with external job schedulers, such as the UNIX cron utility.

## 8.8.2 Selecting a Mode of Operation

You specify the mode of operation for the Platform Receiver through the RUNMODE statement in the platform configuration file or through a command line parameter. For details about specifying the RUNMODE statement, see [RUNMODE Statement](beiffigc.html#chdihjdd).

You can periodically run the Platform Receiver in Full Sync Mode to ensure that accounts on the platform are consistent with eDirectory.

For routine operations, we recommend that, unless you need the real-time processing of events provided by Persistent Mode, you run the Platform Receiver in Polling Mode or Scheduled Mode. This reduces the number of concurrent connections that must be serviced by the Core Driver host. The frequency of change activity in the population, the operating schedule of the platform, and the nature of the connection between the platform and the Core Driver should help you determine which of these modes to use.

You can use Check Mode for testing extensions to Receiver scripts.
