# 1.1 Driver Concepts

This section contains the following information:

* [Data Management](salesforce-driver-concept.html#cegfdbga)
* [How the Driver Works](salesforce-driver-concept.html#cegiiiji)

## 1.1.1 Data Management

The Salesforce.com driver communicates with Salesforce.com using the Salesforce.com partner API. The partner API is represented as XML and its transport is SOAP 1.1 over HTTPS.

* [SOAP](salesforce-driver-concept.html#cegjfbbh)
* [XML](salesforce-driver-concept.html#cegbfdcj)
* [HTTP](salesforce-driver-concept.html#cegjjagg)

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

*NOTE:*Salesforce.com communication mostly happens over HTTPS.

## 1.1.2 How the Driver Works

The following diagram illustrates the data flow between Identity Manager and Salesforce.com service:

*Figure 1-1* Salesforce.com Driver Data Flow

![](../graphics/simple_overview_a.png)

The Identity Manager engine uses XDS, a specialized form of XML, to represent events in the Identity Vault. Identity Manager passes the XDS to the driver policy, which can consist of basic policies, DirXML Script, and XSLT style sheets.

The driver shim receives the XML from the driver policy. The driver shim uses HTTPS to communicate with Salesforce.com.

Salesforce.com processes the request, and returns a response to the driver shim. The driver processes the response, converting it into appropriate XDS that is reported back to the Identity Manager engine. The Publisher channel periodically polls for additions and modifications to the objects in Salesforce.com. On a successful retrieval of the changes, it stores the polling time for use in the next polling cycle. To prevent loopback, the driver discards modifications done by users that the Subscriber channel uses to update Salesforce.com.
