# 1.2 How the Driver Works

[Figure 1-1](how-servicenow-works.html#b1i9dwlp) illustrates the data flow between Identity Manager and a ServiceNow driver.

*Figure 1-1* ServiceNow Driver Data Flow

![](../graphics/service_now_a.png)

The Identity Manager engine uses XDS, a specialized form of XML (Extensible Markup Language), to represent events in the Identity Vault. Identity Manager passes the XDS to the driver policy which can consist of basic policies, DirXML Script, and XSLT (Extensible Stylesheet Language Transformation) style sheets. The ServiceNow driver uses SOAP (Simple Object Access Protocol) protocol to handle the HTTP (Hypertext Transfer Protocol) transport of data between the Identity Vault and ServiceNow. The Subscriber channel receives XDS command documents from the Identity Manager engine, converts them to ServiceNow API (Application Program Interface) calls, and executes them.

The driver shim translates the XDS to XML payload on the Subscriber channel and then invokes the appropriate SOAP endpoints exposed by ServiceNow for Object CRUD (Create, Read, Update, and Delete) operations.

The driver uses the following Internet protocols and languages to exchange data between Identity Manager and ServiceNow.

* [SOAP](how-servicenow-works.html#b1i9e050)
* [HTTP](how-servicenow-works.html#b1i9e2ue)
* [HTTPS](how-servicenow-works.html#b1i9e2uf)

## 1.2.1 SOAP

SOAP is an XML-based protocol for exchanging messages. It defines the message exchange but not the message content. The driver supports SOAP 1.1.

SOAP documents are organized into three elements:

* *Envelope:*
  The root XML node.
* *Header:*
  Provides context knowledge such as a transaction ID and security information.
* *Body:*
  The method-specific information.

SOAP follows the HTTP request/response message model, which provides SOAP request parameters in an HTTP request and SOAP response parameters in an HTTP response.

## 1.2.2 HTTP

HTTP is a protocol used to request and transmit data over the Internet or other computer network. The protocol works well in an Internet infrastructure and with firewalls.

HTTP is a stateless request/response system because the connection is usually maintained only for the immediate request. The client establishes a TCP connection with the server and sends a request command. The server then sends back its response.

## 1.2.3 HTTPS

HTTPS is the HTTP protocol over SSL (Secure Socket Layer) as a sub-layer under the regular HTTP application layering. HTTPS encrypts and decrypts user page requests as well as the pages that are returned by the Web server.

ServiceNow processes the request and returns a SOAP response to the driver shim. The shim receives the response as an array of bytes and converts it to an XML document before passing it back to the driver policies. The input transformation style sheet processes the response and converts it into appropriate XDS that is reported back to the Identity Manager engine.
