# 9.8 Error Displayed for Assigning Roles and User-Based Security Groups

While configuring entitlements for Assignable Roles and User-Based Security Groups, the following error could appear:

```
DirXML Log Event -------------------
     Driver:   \SLES12SP3_1302_TREE\system\driverset1\Workday
     Channel:  Subscriber
     Object:   \SLES12SP3_1302_TREE\data\workday\users\abaker001
     Status:   Error
     Message:  Subscriber execute exception : com.netiq.dirxml.driver.workday.exception.StatusException: <?xml version="1.0" encoding="utf-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><SOAP-ENV:Fault xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wd="urn:com.workday/bsvc"><faultcode>SOAP-ENV:Client.authenticationError</faultcode><faultstring>invalid username or password</faultstring></SOAP-ENV:Fault></SOAP-ENV:Body></SOAP-ENV:Envelope>
        at com.netiq.dirxml.driver.workday.soap.conn.AbsAuthConnection.sendRequest(AbsAuthConnection.java:365)
        at com.netiq.dirxml.driver.workday.entitlements.EntitlementEventProcessor.process(EntitlementEventProcessor.java:72)
        at com.netiq.dirxml.driver.workday.WDSubscriberShim.processEntitlementModification(WDSubscriberShim.java:252)
        at com.netiq.dirxml.driver.workday.WDSubscriberShim.process(WDSubscriberShim.java:218)
        at com.netiq.dirxml.driver.workday.WDSubscriberShim.execute(WDSubscriberShim.java:183)
        at com.novell.nds.dirxml.engine.Subscriber.execute(Subscriber.java:473)
        at com.novell.nds.dirxml.engine.Subscriber.execute(Subscriber.java:304)
        at com.novell.nds.dirxml.engine.Subscriber$ModifyProcessor.process(Subscriber.java:1760)
        at com.novell.nds.dirxml.engine.Subscriber.processEvent(Subscriber.java:1197)
        at com.novell.nds.dirxml.engine.Subscriber.processEvents(Subscriber.java:1010)
        at com.novell.nds.dirxml.engine.Driver.submitTransaction(Driver.java:901)
        at com.novell.nds.dirxml.engine.DriverEntry.submitTransaction(DriverEntry.java:1174)
        at com.novell.nds.dirxml.engine.DriverEntry.processCachedTransaction(DriverEntry.java:1058)
        at com.novell.nds.dirxml.engine.DriverEntry.eventLoop(DriverEntry.java:866)
        at com.novell.nds.dirxml.engine.DriverEntry.run(DriverEntry.java:640)
        at java.lang.Thread.run(Thread.java:748)
```

Issue: This error indicates that the user does not have the required permissions to assign the resource.

Workaround: Provide the require permission to the user for performing the action.
