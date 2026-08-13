# 8.7 Exception Reported When Running Groupwise Driver and Google Apps Driver on the Same Server

*Issue:*
The default configuration of the Google Apps driver modifies the Java API which creates a compatibility issue with the GroupWise driver when both the drivers are running on the same server. As a result, the GroupWise driver reports the following error while processing events on the Subscriber channel:.

```
13:22:28 E9C03700 Drvrs: gw2014 ST:
DirXML Log Event -------------------
Driver: \WGSDVAULT\SD\driverset\GroupWise2014
Channel: Subscriber
Object: \WGSDVAULT\SD\Teachers\aegerter
Status: Error
Message: Code(-9010) An exception occurred: javax.xml.transform.TransformerFactoryConfigurationError: Provider javax.xml.transform.sax.SAXTransformerFactory could not be instantiated: java.lang.IllegalAccessException: Class javax.xml.transform.FactoryFinder can not access a member of class javax.xml.transform.sax.SAXTransformerFactory with modifiers "protected"
```

*Workaround:*
Set Override JAXP Factory to false on the Google Apps driver, or run the GroupWise Driver and Google Apps Driver on different servers.
