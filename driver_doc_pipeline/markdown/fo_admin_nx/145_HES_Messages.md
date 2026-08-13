# D.16 HES Messages

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
The client is trying to connect to its desired server.

Action:
None.

HES003W Core Driver has an incorrect certificate. rc = rc.

Explanation:
The security certificate for a Core Driver could not be verified. Message HES002I precedes this message and identifies the Core Driver involved.

Possible Cause:
The certificate files for the Core Driver might be missing or invalid.

Action:
Obtain a new certificate for the Core Driver.
