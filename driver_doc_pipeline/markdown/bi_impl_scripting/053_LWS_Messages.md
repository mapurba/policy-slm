# B.6 LWS Messages

Messages beginning with LWS are issued by the integrated HTTP server.

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
See the log for additional messages that describe the warning conditions.

LWS0005E Server shut down with errors.

Explanation:
The server processing ended with one or more errors. The server ends with a return code of 8.

Action:
See the log for additional messages that describe the error conditions.

LWS0006I Starting service.

Explanation:
The server is starting the specified service.

Action:
None. Informational only.

LWS0007E Failed to start service.

Explanation:
The server attempted to start the specified service, but the service could not start. The server terminates processing.

Action:
See the log for additional messages that describe the error condition.

LWS0008I Stopping all services.

Explanation:
The server was requested to stop. All services are notified and will subsequently end processing.

Action:
None. Informational only.
