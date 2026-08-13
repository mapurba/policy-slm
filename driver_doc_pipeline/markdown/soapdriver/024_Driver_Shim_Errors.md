# 8.1 Driver Shim Errors

The following errors might occur in the core driver shim. Error messages that contain a numerical code can have various messages, depending on the application or Web service.

* [307 Temporary Redirect](cacidgee.html#b8uakzv)
* [408 Request Timeout](cacidgee.html#b8ualt9)
* [503 Service Unavailable](cacidgee.html#b8uan7w)
* [504 Gateway Timeout](cacidgee.html#b8uapbn)
* [200-299 Messages](cacidgee.html#b8ubd26)
* [Other HTTP Error Messages](cacidgee.html#b8ubj6d)
* [Problem communicating with HTTP server. Make sure the server is running and accepting requests.](cacidgee.html#b8ubnu5)
* [The HTTP/SOAP driver doesn’t return any application schema by default.](cacidgee.html#b8ubs1o)
* [Subscriber.execute() was called but the Subscriber was not configured correctly. The command was ignored.](cacidgee.html#b8ubu2z)
* [pubHostPort must be in the form host:port](cacidgee.html#b8ubw6x)
* [MalformedURLException](cacidgee.html#b8ucab4)
* [Multiple Exceptions](cacidgee.html#b8ucbcq)
* [HTTPS Hostname Wrong: Should Be ...](cacidgee.html#b8ucf8y)
* [SOAP driver waits indefinitely on a response from the SOAP service](cacidgee.html#bvevhp7)

307 Temporary Redirect

Source:
The status log or DSTrace screen.

Explanation:
The Subscriber channel attempted to send data to the application or Web service but received a 307 Temporary Redirect response.

Possible Cause:
The Web service is not available.

Action:
The Subscriber waits for a period of time (usually 30 seconds) and tries again.

Level:
Retry

408 Request Timeout

Source:
The status log or DSTrace screen.

Explanation:
The Subscriber channel attempted to send data to the application or Web service but received a 408 Request Timeout response.

Possible Cause:
The Web service or application is busy.

Action:
The Subscriber waits for a period of time (usually 30 seconds) and tries again.

Level:
Retry

503 Service Unavailable

Source:
The status log or DSTrace screen.

Explanation:
The Subscriber channel attempted to send data to the application or Web service but received a 503 Service Unavailable response.

Possible Cause:
The Web service or application is down.

Action:
The Subscriber waits for a period of time (usually 30 seconds) and tries again.

Level:
Retry

504 Gateway Timeout

Source:
The status log or DSTrace screen.

Explanation:
The Subscriber channel attempted to send data to the application or Web service but received a 504 Gateway Timeout response.

Possible Cause:
The gateway is down.

Action:
The Subscriber waits for a period of time (usually 30 seconds) and tries again.

Level:
Retry

200-299 Messages

Source:
The HTTP server.

Explanation:
Messages in the 200-299 range indicate success.

Action:
No action required.

Level:
Success

Other HTTP Error Messages

Source:
The status log or DSTrace screen.

Explanation:
Other numerical error codes result in an error message containing the code and the message provided by the HTTP server. In most cases, the driver continues to run, and the command that caused the error isn’t retried.

Possible Cause:
There are multiple causes for the different errors.

Action:
See [RFC 2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) for a list of all HTTP error codes and explanations.

Level:
Error

Problem communicating with HTTP server. Make sure the server is running and accepting requests.

Source:
The status log or DSTrace screen.

Explanation:
The Subscriber channel received an IOException while communicating or attempting to communicate with the HTTP server.

Possible Cause:
The HTTP server is not running.

Possible Cause:
The HTTP server is overloaded.

Possible Cause:
There are firewall restrictions blocking access to the HTTP server.

Possible Cause:
The URL provided in the Subscriber configuration is not correct. See [Subscriber Options](driver-configuration.html#bs4ccga) for more information.

Action:
Start the HTTP server.

Action:
Remove services, if the HTTP server is overloaded.

Action:
Change the firewall restrictions to allow access to the HTTP server.

Level:
Retry

The HTTP/SOAP driver doesn’t return any application schema by default.

Source:
The status log or DSTrace screen.

Explanation:
The driver is not returning any application schema, but the driver continues to run.

Possible Cause:
The Identity Manager engine calls the DriverShim.getSchema() method of the driver, and the driver is not using the SchemaReporter customization.

Action:
A Java class needs to be written that implements the SchemaReporter interface, and the driver needs to be configured to load the class as a Java extension.

Level:
Warning

Subscriber.execute() was called but the Subscriber was not configured correctly. The command was ignored.

Source:
The status log or DSTrace screen.

Explanation:
The Subscriber channel of the driver isn’t initialized properly. The driver continues to run but displays this message each time an event is received by the Subscriber channel.

Possible Cause:
An improperly formatted driver configuration.

Action:
Configure the driver correctly. See [Section 5.0, Customizing the Driver](customize-driver.html) for more information.

Action:
Clear the Subscriber’s filter so it doesn’t receive commands.

Level:
Warning

pubHostPort must be in the form host:port

Source:
The status log or DSTrace screen.

Explanation:
The driver cannot communicate.

Possible Cause:
An error occurred with the Publisher channel configuration.

Action:
Review the Publisher channel parameters to verify that both a valid host and a valid port number are provided. See [Publisher Options](driver-configuration.html#bs4cgqb) for more information.

Level:
Fatal

MalformedURLException

Source:
The status log or the DSTrace screen.

Explanation:
There is a problem with the format of the URL.

Possible Cause:
The URL supplied in the Subscriber channel parameters isn’t in a valid URL format.

Action:
Change the URL to a valid format. See [Publisher Options](driver-configuration.html#bs4cgqb) for more information.

Level:
Fatal

Multiple Exceptions

Source:
The status log or the DSTrace screen.

Explanation:
The HTTP listener fails to properly initialize.

Possible Cause:
There are a variety of reasons for this error.

Action:
Check your Publisher settings to make sure you have specified a port that is not already in use and that the other Publisher settings are correct. See [Publisher Options](driver-configuration.html#bs4cgqb) for more information.

Level:
Fatal

HTTPS Hostname Wrong: Should Be ...

Source:
The status log or the DSTrace screen.

Explanation:
An SSL handshake failed on the Subscriber channel.

Possible Cause:
The subject presented with the server certificate doesn’t match the IP address or hostname given in the HTTPS URL.

Action:
Use a DNS hostname rather than an IP address in the URL.

Level:
Retry

SOAP driver waits indefinitely on a response from the SOAP service

Source:
The status log or DSTrace screen.

Explanation:
The driver continues to send the information to the Web server but does not receive any response and appears to be in the waiting state. You can verify this state in the trace log file.

Possible Cause:
SOAP service does not provide a response for the transaction when communicating with the SOAP driver.

Action:
Perform one of the following actions:

* Restart eDirectory, restart the webservice, and then restart the driver.
* Pass the additional request-headers to the http post, which will result in the SOAP driver waiting on a response from the webservice for a finite number of seconds and then continuing to the next operation.

  Example: Use the following operation-data element to pass the additional request-header for the driver to wait for 60 seconds and then continue:

  ```
  <operation-data>
  <request-headers remove-existing="false">
  <request-header name="Expect">60-continue</request-header>
  </request-headers>
  </operation-data>
  ```

Level:
Fatal
