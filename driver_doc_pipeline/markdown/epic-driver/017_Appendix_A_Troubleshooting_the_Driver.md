# A.0 Appendix A - Troubleshooting the Driver

Refer to the following sections if you are experiencing an issue with the Epic Driver.

Driver is not starting or connecting to Epic

* Validate that the configured Epic Interconnect Server URL is correct
* Validate that the IDM server’s firewall ports are open to allow access to Epic
* Validate that the Authentication ID is in the format EMP:<ID> (i.e. EMP:BSMITH)
* Ensure that the driver is fully activated. For more information, see [Activating the Driver](t4et2p5p3uml.html#t4et2p5p4pg1).

User update is failing

If a user record is locked in Epic (i.e. currently open in the Epic Hyperspace application), the driver will not be able to update the user. There is an error reported in the driver trace.

Error "com.sun.xml.internal.ws.client.ClientTransportException: The server sent HTTP status code 500: System.ServiceModel.ServiceActivationException" in trace

* This issue can occur occasionally when there are scarce resources in Epic Interconnect (i.e., memory or CPU)
* This issue can occur in particular instances on certain versions of Epic Interconnect
* Turn on driver trace level 5, duplicate issue, then provide the Web Service details (specifically the full URL of the endpoint that was being called when the error occurred) to your Epic support representative

Error “INVALID-CLIENT-ID details: Provided client ID is invalid” in trace

Ensure that the driver is fully activated. For more information, see [Activating the Driver](t4et2p5p3uml.html#t4et2p5p4pg1).

Exception “java.lang.NoSuchMethodException” in trace

* This exception will be displayed in the trace when attempting to sync an attribute that isn’t supported by Epic
* Review the description of the message in the trace to help isolate the specific attribute(s)
* Review the driver Filter policy and ensure that the specific attribute(s) is not set to “Synchronize”
