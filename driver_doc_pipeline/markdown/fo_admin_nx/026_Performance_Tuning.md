# 5.4 Performance Tuning

The Fan-Out Driver provides a unique Identity Management solution by extending its services to many clients both simultaneously and among mixed environments. This section describes best practices for ensuring optimal performance in the Core Driver Shim’s ability to deliver this functionality.

## 5.4.1 Secondary Drivers

Adding secondary Drivers can provide your Fan-Out platform clients with failover and load balancing. If you have multiple eDirectory servers and plan to deploy the Fan-Out Platform Services to many different systems, it’s recommended that you install and deploy the Fan-Out driver to more than one server.

## 5.4.2 Platform Operation Modes

The Fan-Out Platform Receiver, the component that connects to the Core Driver to receive events from Identity Manager, can be configured to run in five different operation modes (see [Modes of Operation](babdcabj.html#babfijbb)). Three of these modes, in particular, may have an impact on the performance of the Core Driver Shim, as described in [Table 5-1](bfmn9rs.html#bfmptu5).

*Table 5-1* Effect of Operation Modes on Core Driver performance.

| Mode | Function | Effect on Performance |
| Persistent | The Platform Receiver connects and remains connected to the Fan-Out Driver to receive events in real-time, which is desirable if it is necessary for your platform to receive events as they occur in the Identity Vault. | Maintaining the open connection and its resources does carry an overhead in both memory and CPU usage for the Driver Shim. |
| Polling | The Platform Receiver connects to the Fan-Out Driver on configurable intervals to catch up on events since its last poll. | Positive: Can allow the Driver Shim to release its connection and free up resources. Because each and every event will not be delivered to the Platform immediately, this mode will deliver a single event with all of the needed provisioning information to the Polling platform, making the delivery more efficient.  Negative: Can also cause delayed event delivery and, depending on the polling interval, you may see the same memory issues if you have too many platforms connecting too frequently. |
| Scheduled | Very similar to Polling mode with one exception: it only runs once. Allows the system to decide when to launch the Platform Receiver using another facility, such as a cron. | Can provide your systems with nightly or weekly updates and also allow you to stagger the event deliveries, which safeguards against overloading your Fan-Out Driver with too many requests at once. |
