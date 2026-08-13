# B.1 Overview

If the application you are using with the SOAP driver uses non-XML data, you can create Java extensions to convert the non-XML data to XML data. Or, you might want to change various protocols, including XML and HTTP. For example, the default HTTP can be replaced. These Java extensions can be used to operate on data and they must be used to convert non-XML data to XML data. As illustrated in [Figure B-1](bvpan6k.html#b1poma2), there are eleven points where functionality can be extended:

* Four in the Subscriber channel
* Four in the Publisher channel
* Two to specify the transport
* One to report the application schema

*Figure B-1* Using Java to Extend Functionality

![](../graphics/java_ext_diag_a.png)

The SOAP driver is designed to be flexible and extensible. For the Java programmer who wants to extend or modify the capabilities of the driver, there are programming interfaces that can be used for this purpose. These interfaces should be used only when you need to do transformations that cannot be done in policies or style sheets.

The [Javadoc](http://www.novell.com/documentation/dirxmldrivers/javadoc/api/index.html) describes these interfaces.

There are five Java interfaces that can be used to extend or customize the driver behavior. They are DocumentModifiers, ByteArrayModifiers, PublisherTransport, SubscriberTransport, and SchemaReporter.

DocumentModifiers and ByteArrayModifiers serve a similar purpose, so you should probably use one or the other. They are both used to access and to modify the commands and events passing through the driver shim, if this is desired. DocumentModifiers gives you access to the data as XML DOM documents. ByteArrayModifiers gives you access to the same data, but serialized as byte arrays.

The PublisherTransport interface allows you to replace the default HTTP listener that the driver uses on the Publisher channel with something else. Your PublisherTransport implementation can either be event-driven, or it can poll at a specified interval.

If you want to replace the HTTP or HTTPS connections that the driver uses on the Subscriber channel with something else, you would implement a SubscriberTransport.

The remaining interface, SchemaReporter, can be used if you have a way of programatically determining the classes and attributes used by the remote Web service. The advantage to this is that creating schema mapping rules is easier if the schema can be dynamically determined.
