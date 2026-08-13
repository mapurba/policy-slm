# D.11 CRT Messages

Messages beginning with CRT are issued by Certificate Services.

CRT001E Error: Certificate Authority not found.

Explanation:
The certificate authority could not be found.

Possible Cause:
The Core Driver was not properly installed, or the certificate authority is damaged, missing, or in the wrong location.

Action:
Verify that the Core Driver is properly installed and that its files are not damaged.

CRT002E Error: Could not contact directory. Check username and password.

Explanation:
The username/password provided for basic authentication failed.

Possible Cause:
The username and password specified in response to a prompt are incorrect.

The ASAM Master User and ASAM Master User Password are not correct.

Action:
Ensure that the fully distinguished username and password are specified correctly.

Ensure that the ASAM Master User and ASAM Master User Password are specified correctly.

CRT003E Error: Certificate Services not properly configured.

Explanation:
The Certificate Services configuration object and its attributes were not found.

Possible Cause:
The Core Driver installation did not complete properly.

The Core Driver configuration specifies the wrong ASAM System OU.

Action:
Verify that the Core Driver installation completed normally.

Verify that the ASAM System Container Core Driver parameter is correct.

CRT004E Error: component\_name not properly configured.

Explanation:
Configuration information for component\_name is missing or incomplete.

Possible Cause:
The administrator did not create and complete the proper component configuration using the Web interface.

Action:
Examine the configuration object for the component with the Web interface. Provide any missing information, such as network address.

CRT005E Error: Internal Server Error.

Explanation:
The Core Driver encountered an unknown error, such as out of memory or memory allocation failure.

Action:
Ensure that sufficient memory is available.

CRT006E Error: Insufficient rights to create component\_name configuration object.

Explanation:
You do not have sufficient rights to create the component configuration object.

Action:
Obtain sufficient rights to the ASAM System container.

CRT007E Error: Insufficient rights to modify component\_name configuration object.

Explanation:
You do not have sufficient rights to modify the component configuration object.

Action:
Obtain sufficient rights to the ASAM System container.

CRT008I All certificate and host information has been checked and verified successfully.

Explanation:
The certificate autocheck procedure has determined that all certificates for this particular driver have been located and include the correct host information.

Action:
None. Informational only.

CRT009I Certificates have been updated with new host information.

Explanation:
The certificate autocheck procedure has determined that the certificates for this driver are not current with the host information provided by the Fan-Out system. Therefore, new certificates have been created to include the correct host information.

Possible Cause:
This driver might have been moved to another server, the server might have had a network configuration change, or the administrator might have added new host address information for this host.

Action:
Use the Web interface to ensure that the correct host information is specified.

CRT010I New driver certificates were created.

Explanation:
The certificate autocheck procedure was unable to locate an existing certificate for this driver. A new certificate authority was generated, along with a new certificate containing host information provided by the Fan-Out system.

Possible Cause:
This can be caused by a new installation or upgrade.

Action:
If this is not the expected behavior, check the file system under ASAM/CoreDriver/certs/ for an existing certificate authority and driver certificates. Make sure that the driver has appropriate access to these files.

CRT011I The certificate authority was retrieved successfully from the primary Core Driver.

Explanation:
The certificate autocheck procedure was unable to locate a certificate authority and requested the information from the primary Core Driver. Upon retrieving the data successfully, new certificates were created for this driver with appropriate host information.

Possible Cause:
This can result from a new installation or upgrade of a secondary Core Driver.

Action:
If this behavior is not expected, check ASAM/CoreDriver/certs/ for existing certificates, and make sure that the driver is configured properly as a primary or secondary driver.
