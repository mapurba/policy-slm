# 1.1 Driver Concepts

This section provides the following information:

* [Data Management](t4avmq76q86m.html#t4avmq76qfwf)
* [How the Driver Works](t4avmq76q86m.html#t4avmq76rarn)

## 1.1.1 Data Management

The Workday driver communicates with Workday using the Workday SOAP API; especially the Human\_Resource API. Some of the important Human resource APIs used in the driver, are mentioned below:

* Get\_Workers
* Get\_Worker\_Photos
* Get\_Locations
* Get\_Organizations
* Get\_Job\_Profiles
* Get\_Job\_Families
* Update\_Workday\_Account
* Get\_Assign\_User-Based\_Security\_Group
* Get\_Assign\_User-Based\_Security\_Groups
* Put\_Assign\_User-Based\_Security\_Groups
* Assign\_Roles
* Change\_Other\_IDs
* Get\_Server\_Timestamp
* Put\_Worker\_Photo

### SOAP

SOAP (Simple Object Access Protocol) is an XML-based protocol for exchanging messages. It defines the message exchange but not the message content. The driver supports SOAP 1.1.

SOAP documents are organized into three elements:

* *Envelope:*
  The root XML node.
* *Header:*
  Provides context knowledge such as a transaction ID and security information.
* *Body:*
  The method-specific information.

SOAP follows the HTTP request/response message model, which provides SOAP request parameters in an HTTP request and SOAP response parameters in an HTTP response.

### XML

XML (Extensible Markup Language) is a generic subset of Standard Generalized Markup Language (SGML) that allows for exchange of structured data on the Internet.

### HTTP

HTTP is a protocol used to request and transmit data over the Internet or other computer network. The protocol works well in an Internet infrastructure and with firewalls.

HTTP is a stateless request/response system because the connection is usually maintained only for the immediate request. The client establishes a TCP connection with the server and sends it a request command. The server then sends back its response.

*NOTE:*Workday communication always happens over HTTPS.

## 1.1.2 How the Driver Works

The following diagram illustrates the data flow from Workday service to Identity Manager and vice-versa:

*Figure 1-1* Workday Driver Data Flow

![](../graphics/idv-workday-sync-3.png)

The Workday driver polls data from Workday as SOAP request. Workday processes the request, and returns a SOAP response to the driver shim. The driver processes the response, converting it into appropriate XDS, a specialized form of XML, using XSLT style sheets. The driver stores the response data in a cache file. The Publisher channel periodically polls for additions and modifications to the objects in Workday. On a successful retrieval of the changes, it stores the polling time for use in the next polling cycle. Driver uses the cache file to submit the optimized XDS modify document to the Identity Manager Engine.

The Identity Manager engine uses XDS to represent events in the Identity Vault. On the Subscriber channel, the Identity Manager engine passes the XDS event to the driver policy channel, which consists of basic policies, DirXML Script, and XSLT style sheets. The driver shim receives the XDS document from the policy channel. The driver shim uses XSLT style sheets to convert the XDS document to appropriate SOAP request.

The Publisher channel uses two different ways of polling the Workday server for fetching the changes:

* *Recurring Polling:*
  Recurring polling happens at a fixed interval. This type of polling happens for Worker, Relation and Job Profile object classes. Recurring polling queries the Workday server for changes from the last successful recurring polling cycle.
* *Scheduled Polling:*
  Scheduled polling happens once in a day at a fixed time. This type of polling happens for Terminated Workers, Location, Worker Photo, Job Family and Organization object classes.
