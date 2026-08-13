# 9.7 Error Message for Incorrectly Configuring OAuth 2.0

If any parameters are missed while configuring the Workday driver with OAuth 2.0 authentication method, the connection terminates and displays an error.

For example, if the Client ID parameter value is missing the following error message appears:

```
DirXML Log Event -------------------
     Driver:   \SLES12SP3_MAHESH_1302_TREE\system\driverset1\Workday
     Channel:  Subscriber
     Status:   Fatal
     Message:  Code(-9005) The driver returned a "fatal" status indicating that the driver should be shut down. Detail from driver: Error occured in subscriber init. Reason : com.netiq.dirxml.driver.workday.exception.StatusException: Error: Client Id cannot be empty.
        at com.netiq.dirxml.driver.workday.soap.conn.OAuthConnection.handleEmptyOAuthParam(OAuthConnection.java:120)
        at com.netiq.dirxml.driver.workday.soap.conn.OAuthConnection.&lt;init>(OAuthConnection.java:54)
        at com.netiq.dirxml.driver.workday.soap.conn.AuthConnFactory.getAuthConnInstance(AuthConnFactory.java:63)
        at com.netiq.dirxml.driver.workday.WDSubscriberShim.init(WDSubscriberShim.java:120)
        at com.novell.nds.dirxml.engine.Subscriber.init(Subscriber.java:274)
        at com.novell.nds.dirxml.engine.Subscriber.&lt;init>(Subscriber.java:136)
        at com.novell.nds.dirxml.engine.Driver.startShim(Driver.java:1722)
        at com.novell.nds.dirxml.engine.Driver.initialize(Driver.java:329)
        at com.novell.nds.dirxml.engine.Driver.&lt;init>(Driver.java:295)
        at com.novell.nds.dirxml.engine.DriverEntry.run(DriverEntry.java:626)
        at java.lang.Thread.run(Thread.java:748)
```

Workaround: You must stop the driver, specify the required parameter and configure the driver as explained in [Creating the Driver Object](t4avmq79xc47.html).
