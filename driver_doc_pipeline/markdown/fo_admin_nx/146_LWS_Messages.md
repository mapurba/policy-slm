# D.17 LWS Messages

Messages beginning with LWS are issued by the Core Driver as it functions as an HTTP server.

LWS0001I Server has been initialized.

Explanation:
The server has successfully completed its initialization phase.

Action:
None. Informational only.

LWS0002I All services are now active.

Explanation:
All of the services offered by the server are now active and ready for work.

Action:
None. Informational only.

LWS0003I Server shut down successfully.

Explanation:
The server processing completed normally. The server ends with a return code of 0.

Action:
No action is required.

LWS0004W Server shut down with warnings.

Explanation:
The server processing completed normally with at least one warning. The server ends with a return code of 4.

Action:
See the message log for additional messages that describe the warning conditions.

LWS0005E Server shut down with errors.

Explanation:
The server processing ended with one or more errors. The server ends with a return code of 8.

Action:
See the message log for additional messages that describe the error conditions.

LWS0006I Starting service.

Explanation:
The server is starting the specified service.

Action:
None. Informational only.

LWS0007E Failed to start service.

Explanation:
The server attempted to start the specified service, but the service was unable to start. The server terminates processing.

Action:
See the message log for additional messages that describe the error condition.

LWS0008I Stopping all services.

Explanation:
The server was requested to stop by an operator STOP command. All services are notified and will subsequently end processing.

Action:
None. Informational only.

LWS0009I Local host is host\_name ( IP\_address).

Explanation:
This message shows the host name and IP address of the machine the server is running on.

Action:
None. Informational only.

LWS0010I Local host is IP\_address.

Explanation:
This message shows the IP address of the machine the server is running on.

Action:
None. Informational only.

LWS0011I Server is now processing client requests.

Explanation:
The server has successfully started all configured services, and it is ready for clients to begin requests.

Action:
None. Informational only.

LWS0012I service is now active on port number.

Explanation:
The server service is running on the specified TCP port number. Clients can begin making requests to the specified service.

Action:
None. Informational only.

LWS0013I service is now inactive on port number.

Explanation:
The server service is not active on the specified TCP port number. Processing continues, but no client requests can be made to the service until it becomes active again.

Action:
None. Informational only.

LWS0014E An error was encountered while parsing execution parameters.

Explanation:
An error occurred while parsing the EXEC PARMs. The server terminates with a minimum return code of 8.

Action:
Collect diagnostic information and contact Support.

LWS0015E service failed to start with error number.

Explanation:
The specified service failed to start. The server terminates with a minimum return code of 8.

Action:
Collect diagnostic information and contact Support.

LWS0020I Server version level: level.

Explanation:
This message contains information detailing the current service level for the server program being executed. The value of version indicates the current release of the server. The value of level is a unique sequence of characters that can be used by software support to determine the maintenance level of the server being executed.

Action:
Normally, no action is required. However, if a problem with the server is called in to Support, you might be asked to provide the information in the message.

LWS0023I Listen port number is already in use.

Explanation:
The displayed listen port is already in use by another task running on the local host. The server retries establishing the listen port.

Action:
Determine what task is using the required port number and restart the server when the task is finished, or specify an alternate port in the configuration file. If the port number is changed for the server, the client must also specify the new port number.

LWS0024W Too many retries to obtain port number.

Explanation:
The server tried multiple attempts to establish a listen socket on the specified port number, but the port was in use. The server terminates with a return code of 4.

Action:
Determine what task is using the required port number, and restart the server when the task is finished, or specify an alternate port in the configuration file. If the port number is changed for the server, the client must also specify the new port number.

LWS0025I Local TCP/IP stack is down.

Explanation:
The server detected that the local host TCP/IP address space is not active or is unavailable. The server retries every two minutes to reestablish communication with the TCP/IP address space.

Action:
Ensure that the TCP/IP address space is running.

LWS0026E Unrecoverable TCP/IP error number returned from internal\_function\_name.

Explanation:
An unrecoverable TCP/IP error was detected in the specified internal server function name. The server ends with a minimum return code of 8. The error number reported corresponds to a TCP/IP errno value.

Action:
Correct the error based on TCP/IP documentation for the specified errno.

LWS0027W Listen socket was dropped for port number.

Explanation:
The server's connection to the displayed listen port was dropped. The server attempts to reconnect to the listen port so that it can receive new client connections.

Action:
Determine why connections are being lost on the local host. Ensure that the host's TCP/IP services are up and running.

LWS0028E Unable to reestablish listen socket on port number.

Explanation:
The listen socket on the specified port number was dropped. The server tried multiple attempts to reestablish the listen socket, but all attempts failed. The server ends with a return code of 8.

Action:
Determine if the host's TCP/IP service is running. If the host's TCP/IP service is running, determine if another task on the local host is using the specified port.

LWS0029I < id> Client request started from ip\_address on port number.

Explanation:
A new client request identified by id has been started from the specified IP address on the displayed port number.

Action:
None. Informational only.

LWS0030I < id> Client request started from host ( ip\_address) on port number.

Explanation:
A new client request identified by id has been started from the specified host and IP address on the displayed port number.

Action:
None. Informational only.

LWS0031W Unable to stop task id: reason.

Explanation:
The server attempted to terminate a service task identified by id. The server was unable to stop the task for the specified reason. The server ends with a return code of 4.

Action:
See the reason text for more information about why the task was unable to terminate.

LWS0032I < id> Client request has ended.

Explanation:
The client requested identified by id has ended.

Action:
None. Informational only.

LWS0033I < id> Client request: resource.

Explanation:
The client connection identified by id issued a request for resource.

Action:
None. Informational only.

LWS0034W < id> Write operation for client data has failed.

Explanation:
A write operation failed for the connection identified by id. This is normally because the client dropped the connection. The client connection is dropped by the server.

Action:
Ensure that the client does not prematurely drop the connection. Retry the client request if necessary.

LWS0035W < id> Read operation for client data has timed out.

Explanation:
A read operation on the connection identified by id has timed out because of inactivity. The client connection is dropped by the server.

Action:
Ensure that the client does not prematurely drop the connection. Retry the client request if necessary.

LWS0036W < id> Client request error: error\_code - error\_text.

Explanation:
The server encountered an error while processing the client request. The server terminates the request.

Action:
Determine why the request was in error by viewing the error code and error text that was generated.

LWS0037W < id> Client request error: code.

Explanation:
The server encountered an error while processing the client request. The server terminates the request.

Action:
Determine why the request was in error by viewing the error code and error text that was generated.

LWS0038I Received command: command\_text.

Explanation:
The server has received the displayed command from the operator. The server processes the command.

Action:
None. Informational only.

LWS0043E Task id ended abnormally with RC= retcode.

Explanation:
The server detected a task that ended with a non-zero return code. The server ends with a minimum return code of 8.

Action:
View the message log for other messages that might have been generated regarding the error.

LWS0045I Idle session time-out is number seconds.

Explanation:
The message shows the idle time limit for connections. The server automatically terminates sessions that are idle for longer than the specified number of seconds.

Action:
None. Informational only.

LWS0046I Maximum concurrent sessions limited to number.

Explanation:
The message shows the maximum number of concurrent sessions allowed. The server only allows the specified number of concurrent sessions to be active at any given time. All connections that exceed this limit are forced to wait until the total number of connections drops below the specified value.

Action:
None. Informational only.

LWS0047W Unable to delete log file filename.

Explanation:
The log file could not be deleted as specified through the Web interface.

Possible Cause:
The ASAM Master User does not have file system rights to delete old log files.

Action:
Verify that the ASAM Master User has the appropriate rights.

Examine the current logs for related messages.

LWS0048I Log file filename successfully deleted.

Explanation:
The log file has been deleted as specified through the Web interface.

Action:
None. Informational only.

LWS0049E Error error authenticating to the directory as fdn.

Explanation:
The connection manager was unable to connect to the directory as user fdn. The error was error.

Possible Cause:
The Driver object configuration parameters do not contain the correct password for the ASAM Master User object.

Action:
Correct the cause of the error as determined from error.

Verify that the ASAM Master User has the appropriate rights.

Verify that the password given for the ASAM Master User object in the configuration parameters is correct.

LWS0050E Server application initialization failure was detected.

Explanation:
During server initialization, an error was detected while trying to initialize the server's application object.

Action:
See the error logs for additional messages that indicate the cause of the error.

LWS0051E Server initialization failure was detected.

Explanation:
The server failed to initialize properly because of an operating system specific initialization error.

Action:
See the error logs for additional messages that indicate the cause of the error.
