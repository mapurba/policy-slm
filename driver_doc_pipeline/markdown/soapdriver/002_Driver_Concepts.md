# 1.1 Driver Concepts

This section contains the following information:

* [Data Management](soap-driver-concepts.html#cegfdbga)
* [How the Driver Works](soap-driver-concepts.html#cegiiiji)

## 1.1.1 Data Management

The driver uses various Internet protocols and languages to exchange data between Identity Manager and a Web service.

* [SOAP](soap-driver-concepts.html#cegjfbbh)
* [SPML and DSML](soap-driver-concepts.html#cegjdhbj)
* [XML](soap-driver-concepts.html#cegbfdcj)
* [HTTP](soap-driver-concepts.html#cegjjagg)
* [HTTPS](soap-driver-concepts.html#bs9endy)

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

### SPML and DSML

The SOAP driver includes sample configurations for the SPML 1.0, SPML 2.0, and DSML 2.0 protocols.

* *SPML:*
  Service Provisioning Markup Language is an XML-based provisioning request and response protocol. A client issues an SPML request to a server. The request describes the operation to be performed at a given service point. The service point performs the necessary operations to implement the requested service. After completing the operation, the service point returns an SPML response to the client detailing any results or errors pertinent to that request.

  The driver supports SPML 1.0 or SPML 2.0 depending on the sample configuration selected. SPML binds with SOAP 1.1 and uses HTTP and HTTPS 1.1 as the transport.
* *DSML:*
  Directory Services Markup Language represents directory structural information, directory queries and updates, and the results of these operations as XML documents.

DSML binds with SOAP 1.1 and uses HTTP and HTTPS 1.1 as the transport.

For more information about the sample SPML and DSML configurations included with the driver, see [Understanding the DSML Configuration](understand-dsml-configuration.html) and [Understanding the SPML Configuration](understand-spml-configuration.html).

### XML

XML (Extensible Markup Language) is a generic subset of Standard Generalized Markup Language (SGML) that allows for exchange of structured data on the Internet.

### HTTP

HTTP is a protocol used to request and transmit data over the Internet or other computer network. The protocol works well in an Internet infrastructure and with firewalls.

HTTP is a stateless request/response system because the connection is usually maintained only for the immediate request. The client establishes a TCP connection with the server and sends it a request command. The server then sends back its response.

### HTTPS

HTTPS is the HTTP protocol over Secure Socket Layer (SSL) as a sub-layer under the regular HTTP application layering. HTTPS encrypts and decrypts user page requests as well as the pages that are returned by the Web server.

## 1.1.2 How the Driver Works

The following diagram illustrates the data flow between Identity Manager and a Web service:

*Figure 1-1* SOAP Driver Data Flow

![](../graphics/simple_overview_a.png)

The Identity Manager engine uses XDS, a specialized form of XML, to represent events in the Identity Vault. Identity Manager passes the XDS to the driver policy, which can consist of basic policies, DirXML Script, and XSLT style sheets.

The driver policy translates the XDS to XML, such as SOAP, on the Subscriber channel. On the Publisher channel, the driver policy translates other forms of XML, such as SOAP, into XDS.

The driver shim receives the XML from the driver policy. The driver shim uses HTTP to communicate with the Web service. Generally the handoff between the driver shim and the application is serialized XML.

For example, suppose the driver is using the DSML sample configuration to talk to a DSML server that is configured only as a Subscriber. When an event occurs in the Identity Vault, Identity Manager creates an XDS command to represent that event. Identity Manager passes the XDS command to the driver policy.

The driver policy transforms that XDS command with an output transformation style sheet. The XSLT style sheet converts the XDS to a SOAP envelope containing DSML. That SOAP envelope is handed to the driver shim. The driver shim converts the SOAP envelope into an array of bytes, makes the appropriate HTTP connection, and performs an HTTP POST operation to submit the data to the Web service.

The Web service or application processes the request, and returns a SOAP response to the driver shim. The shim receives the response as an array of bytes, and converts it to an XML document before passing it back to the driver policies. The input transformation style sheet processes the response, converting it into appropriate XDS that is reported back to the Identity Manager engine.

## 1.1.3 Understanding Driver Operation Data

The driver shim applies special handling to Subscriber commands based on an XML element embedded in the command, which appears in the driver shim as <driver-operation-data>. The <driver-operation-data> element has two purposes. First, it can be used to match commands with the responses they generate, and can be used to create associations in transformation policies. Second, it can be used to override default Subscriber channel connection attributes.

The <driver-operation-data> element is added to the command from one of the Subscriber channel policies. The driver shim removes the <driver-operation-data> element from the command before it is sent to the application, and restores the <driver-operation-data> element to the resulting response.

By default, when the <driver-operation-data> element is restored on the response, it is appended as a child element of the root node. This can be overridden by providing one or more parent-node-n attributes to the <driver-operation-data> element, where n is a number beginning with 1 that is incremented for each parent specifier you want to provide. The driver shim examines the operation data node, looking for parent-node-n attributes. If attributes are found, each is tried in turn and if the named node exists, the node is used as the parent for the operation data on the response.

*NOTE:*Earlier versions of the driver shim uses the <operation-data> element to achieve this purpose. The driver shim still supports this for backward compatibility. However, use of the <operation-data> element for this purpose will be depreciated in future releases.

NetIQ recommends that you use the <driver-operation-data> element.

To see how the <driver-operation-data> element works, see [Managing Driver Operation Data](manage-driver-operation-data.html).
