# B.12 RDXML Messages

Messages beginning with RDXML are issued by the embedded Remote Loader.

RDXML000I nameversion Copyright 2005 Omnibond Systems, LLC. ID=code\_id\_string.

Explanation:
This message identifies the system component version.

Action:
No action is required.

RDXML001I Client connection established.

Explanation:
A client has connected to the driver. This can be the Metadirectory engine connecting to process events to and from the driver, or a Web-based request to view information or publish changes through the SOAP mechanism.

Action:
No action required.

RDXML002I Request issued to start Driver Shim.

Explanation:
The driver received a command to start the driver shim and begin processing events.

Action:
No action required.

RDXML003E An unrecognized command was issued. The driver shim is shutting down.

Explanation:
The driver received an unrecognized command from the Metadirectory engine. The driver shim is shutting down to avoid further errors.

Possible cause:
Network error.

Possible cause:
Invalid data sent to the driver.

Possible cause:
The Metadirectory engine version might have been updated with new commands that are unrecognized by this version of the driver.

Possible cause:
This message is logged when the driver shim process is shut down from the connected system rather than from a Driver object request. The local system can queue an invalid command to the driver shim to simulate a shutdown request and terminate the running process.

Action:
Ensure that the network connection is secured and working properly.

Action:
Apply updates for the engine or driver if necessary.

Action:
If the driver shim process was shut down from the local system, no action is required.

RDXML004I Client Disconnected.

Explanation:
A client has disconnected from the driver. This might be the Metadirectory engine disconnecting after a driver shutdown request or a Web-based request that has ended.

Action:
No action required.

RDXML005W Unable to establish client connection.

Explanation:
A client attempted to connect to the driver, but was disconnected prematurely.

Possible cause:
The client is not running in SSL mode.

Possible cause:
Mismatched SSL versions or mismatched certificate authorities.

Possible cause:
Problems initializing SSL libraries because of improperly configured system entropy settings.

Action:
Ensure that both the Metadirectory engine and the driver are running in the same mode: either clear text mode or SSL mode.

Action:
If you are using SSL, ensure that the driver and Metadirectory engine have properly configured certificates, and that the driver system is configured properly for entropy.

RDXML006E Error in Remote Loader Handshake.

Explanation:
The Metadirectory engine attempted to connect to the driver, but the authorization process failed. Authorization requires that both supply mutually acceptable passwords. Passwords are configured at installation.

Possible cause:
The Remote Loader or Driver object passwords do not match.

Action:
Set the Remote Loader and Driver object passwords to the same value for both the driver and the driver shim. Use iManager to modify the driver properties. Re-configure the driver shim on the connected system.

RDXML007I Driver Shim has successfully started and is ready to process events.

Explanation:
The Metadirectory engine has requested the driver to start the shim for event processing, and the driver shim has successfully started.

Action:
No action required.

RDXML008W Unable to establish client connection from remoteName.

Explanation:
A client attempted to connect to the driver, but was disconnected prematurely.

Possible cause:
The client is not running in SSL mode.

Possible cause:
Mismatched SSL versions or mismatched certificate authorities.

Possible cause:
Problems initializing SSL libraries because of improperly configured system entropy settings.

Action:
Ensure that both the Metadirectory engine and the driver are running in the same mode: either clear text mode or SSL mode.

Action:
If you are using SSL, ensure that the driver and Metadirectory engine have properly configured certificates, and that the driver system is configured properly for entropy.

RDXML009I Client connection established from remoteName.

Explanation:
A client has connected to the driver. This can be the Metadirectory engine connecting to process events to and from the driver, or a Web-based request to view information or publish changes through the SOAP mechanism.

Action:
No action required.
