# C.5 HES Messages

Messages beginning with HES are issued by driver components as they use HTTP to communicate.

HES001E Unable to initialize the HTTP client.

Explanation:
Communications in the client could not be initialized.

Possible Cause:
Memory is exhausted.

Action:
Increase the amount of memory available to the process.

HES002I Connecting to host host\_name on port port\_number.

Explanation:
The client is connecting to the specified server.

Action:
None.

HES003W SSL communications have an incorrect certificate. rc = rc.

Explanation:
The security certificate for SSL services could not be verified.

Possible Cause:
The certificate files might be missing or invalid.

Action:
Obtain a new certificate.
