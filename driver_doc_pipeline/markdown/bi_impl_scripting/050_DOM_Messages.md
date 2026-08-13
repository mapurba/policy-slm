# B.3 DOM Messages

Messages beginning with DOM are issued by driver components as they communicate among themselves.

DOM0001W XML parser error encountered: errorString.

Explanation:
An error was detected while parsing an XML document.

Possible Cause:
The XML document was incomplete, or it was not a properly constructed XML document.

Action:
See the error string for additional details about the error. Some errors, such as no element found, can occur during normal operation and indicate that an empty XML document was received.
