# B.11 NET Messages

Messages beginning with NET are issued by driver components during verification of SSL certificates.

NET001W Certificate verification failed. Result is result.

Explanation:
A valid security certificate could not be obtained from the connection client. Diagnostic information is given by result.

Possible cause:
A security certificate has not been obtained for the component.

Possible cause:
The security certificate has expired.

Possible cause:
The component certificate directory has been corrupted.

Action:
Respond as indicated by result. Obtain a new certificate if appropriate.
