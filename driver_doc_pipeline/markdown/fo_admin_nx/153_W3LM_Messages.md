# D.24 W3LM Messages

Messages beginning with W3LM are issued by Web Services.

W3LM001I Object driverDN created by webUserDN.

Explanation:
A Core Driver was created by the specified user through the Web interface.

Action:
None. Informational only.

W3LM002I Object driverDN deleted by webUserDN.

Explanation:
A Core Driver was deleted by the specified user through the Web interface.

Action:
None. Informational only.

W3LM003I Event Listener eventListenerDN deleted by webUserDN.

Explanation:
The Event Listener was deleted by the specified user through the Web interface.

Action:
None. Informational only.

W3LM004I Trawl Initiated by webUserDN.

Explanation:
A Trawl was started by the specified user through the Web interface.

Action:
None. Informational only.

W3LM007I Platform platformDN deleted by webUserDN.

Explanation:
A Platform object was deleted by the specified user through the Web interface.

Action:
None. Informational only.

W3LM008I Platform platformDN created by webUserDN.

Explanation:
A Platform object was created by the specified user through the Web interface.

Action:
None. Informational only.

W3LM009I Platform Set platformSetDN marked for deletion by webUserDN.

Explanation:
The specified Platform Set was marked for deletion by the specified user through the Web interface.

Action:
None. Informational only.

W3LM010I Platform Set platformSetDN created by webUserDN.

Explanation:
The specified Platform Set was created by the specified user through the Web interface.

Action:
None. Informational only.

W3LM011I UID/GID Set UIDGIDSetDN marked for deletion by webUserDN.

Explanation:
The UID/GID Set was deleted by the specified user through the Web interface.

Action:
None. Informational only.

W3LM012I UID/GID Set UIDGIDSetDN created by webUserDN.

Explanation:
The specified UID/GID set was created by the specified user through the Web interface.

Action:
None. Informational only.

W3LM013I SearchObject searchObjectDN created by webUserDN.

Explanation:
The Search object was created by the specified user through the Web interface.

Action:
None. Informational only.

W3LM014I SearchObject searchObjectDN deleted by webUserDN.

Explanation:
The specified Search object was deleted by the specified user through the Web interface.

Action:
None. Informational only.

W3LM015I Object objectDN modified by webUserDN.

Explanation:
The specified object was modified by the specified user through the Web interface.

Action:
None. Informational only.

W3LM016I Connection (default) netAddress attribute on object objectDN modified by webUserDN.

Explanation:
Connection (default) netAddress attribute on the specified object was modified by the specified user through the Web interface.

Action:
None. Informational only.

W3LM017I netAddress attribute on object objectDN modified by webUserDN.

Explanation:
The netAddress attribute of the specified object was modified by the specified user through the Web interface.

Action:
None. Informational only.

W3LM018W Web Interface login Failure loginDN.

Explanation:
An attempt to authenticate to the Web interface by loginDN failed.

Possible Cause:
Invalid login ID, password, or insufficient rights.

Action:
Log in with sufficient rights.

W3LM019I Successful Web Interface login by loginID.

Explanation:
The user successfully logged in to the Web interface.

Action:
None. Informational only.

W3LM020W Web Interface login attempt with invalid credentials.

Explanation:
An attempt to log in to the Web interface failed because of invalid credentials.

Possible Cause:
The user attempting to log in has invalid credentials

Action:
Check user credentials.

W3LM021W Web Interface login attempt with invalid DN Syntax.

Explanation:
An attempt to log in to the Web interface was made with invalid DN syntax.

Possible Cause:
DN syntax was invalid.

Action:
Correct DN syntax and try logging in again.

W3LM022W Web Interface login attempt for an unknown user.

Explanation:
The user attempting to log in to the Web Interface is invalid because a Census entry for the user was not found.

Possible Cause:
The user is not in Census.

Action:
Make sure the user is in the Census.

W3LM023W Web Interface login attempt failure with an unknown error.

Explanation:
An attempt to log in to the Web interface failed with an unknown error.

Action:
Examine the log for related messages.

W3LM024E Check the Trawl Time-Out value and re-enter.

Explanation:
The Trawl Time-Out value is invalid.

Possible Cause:
An invalid Trawl Time-Out value was specified.

Action:
Correct the Trawl Time-Out value.
