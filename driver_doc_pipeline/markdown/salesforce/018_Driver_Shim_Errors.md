# 8.1 Driver Shim Errors

The following identifies errors that might occur in the core driver shim. Error messages that contain a numerical code can have various messages, depending on the application or Web service.

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
The messages in the 200-299 range indicate success.

Action:
No action required.

Level:
Success

Other HTTP Errors Messages

Source:
The status log or DSTrace screen.

Explanation:
Other numerical error codes result in an error message containing that code and the message provided by the HTTP server. In most cases, the driver continues to run, and the command that caused the error isn’t retried.

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
The URL provided in the Subscriber configuration is not correct. See [Driver Parameters](driver-configuration.html#b4m4h9a).

Action:
Start the HTTP server.

Action:
Remove services, if the HTTP server is overloaded.

Action:
Change the firewall restrictions to allow access to the HTTP server.

Level:
Retry

The HTTP/Salesforce.com driver doesn’t return any application schema by default.

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
Configure the driver correctly. See [Section 4.0, Schema Mapping](schema-mapping.html) for more information.

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
Review the Publisher channel parameters to verify that both a valid host and a valid port number are provided.

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
Change the URL to a valid format. .

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
Check your Publisher settings to make sure you have specified a port that is not already in use and that the other Publisher settings are correct.

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
