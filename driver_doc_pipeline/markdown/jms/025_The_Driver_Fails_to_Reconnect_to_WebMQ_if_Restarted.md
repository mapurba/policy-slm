# 7.1 The Driver Fails to Reconnect to WebMQ if Restarted

The JMS driver fails to reconnect with the following exception when connecting to either Web MQ 7.1 or 7.5.

```
Exception in thread "JMSCCThreadPoolMaster"
java.lang.IllegalThreadStateException
at java.lang.ThreadGroup.addUnstarted(Unknown Source)
at java.lang.Thread.init(Unknown Source)
at java.lang.Thread.init(Unknown Source)
at java.lang.Thread.<init>(Unknown Source)
at
com.ibm.msg.client.commonservices.j2se.workqueue.WorkQueueManagerImpl
ementation$ThreadPoolWorker.<init>(WorkQueueManagerImplementation.java:950)
at
com.ibm.msg.client.commonservices.j2se.workqueue.WorkQueueManagerImpl
ementation.createNewThread(WorkQueueManagerImplementation.java:496)
at
```

This issue is only observed with the latest third party Websphere JMS Client 7.5 and Websphere 7.1 jar files.

To workaround this issue, use the driver with Remote Loader.
