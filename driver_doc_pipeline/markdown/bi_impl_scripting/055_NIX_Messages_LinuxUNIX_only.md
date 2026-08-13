# B.8 NIX Messages (Linux/UNIX only)

Messages beginning with NIX are issued by the driver shim.

NIX000I nameversion Copyright 2005 Omnibond Systems, LLC. ID=code\_id\_string.

Explanation:
This message identifies the system component version.

Action:
No action is required.

NIX001S An error occurred attempting to attach the shared memory segment to an address space (errno=errno).

Explanation:
The driver uses shared memory as the mechanism for providing information to the scripts. An error occurred attempting to attach the shared memory to a physical address for access.

Possible Cause:
The calling process has no access permissions for the requested attach type.

Possible Cause:
An invalid or non-page-aligned address was provided to the system routine.

Possible Cause:
Memory could not be allocated for the descriptor or for the page tables.

Action:
Restart the driver process and ensure that there are adequate memory resources. Verify that the driver process is run as root and has permissions to read its configuration files. Contact NetIQÂ® Support for additional instructions if necessary.

NIX002S An error occurred while attempting to allocate a shared memory segment (errno = errno).

Explanation:
The driver uses shared memory as the mechanism for providing information to the scripts. An error occurred attempting to allocate a shared memory segment.

Possible Cause:
The memory size was too small or too large.

Possible Cause:
The system shared memory settings might not have adequate values

Possible Cause:
The memory segment could not be created because it already exists. This could be caused by an abnormal termination of a previous driver process.

Possible Cause:
All possible shared memory IDs have been taken.

Possible Cause:
Allocating a segment of the requested size would cause the system to exceed the system-wide limit on shared memory.

Possible Cause:
No shared memory segment exists for the given key.

Possible Cause:
The user or process does not have permission to access the shared memory segment.

Possible Cause:
No memory could be allocated for segment overhead..

Action:
Restart the driver process and ensure that there is sufficient memory.

Action:
Verify that the driver process is run as root and has permissions to read its configuration files.

Action:
Verify that the driver process is run as root and has permissions to read its configuration files

Action:
If there are other applications on the server that use shared memory, ensure that they are running, healthy, and do not conflict with the requirements for the driver.

Action:
Contact NetIQ Support for additional instructions if necessary.

NIX003S An error occurred attempting to create a System V IPC key. The project identifier pathname = pathname.

Explanation:
The driver uses shared memory as the mechanism for providing information to the scripts. An error occurred attempting to create the key used to specify the shared memory segment.

Possible Cause:
The project pathname is invalid or does not exist.

Action:
Restart the driver process.

Action:
Ensure that the file pathname is correct and that the process has adequate permissions to read the path.

NIX004S An error occurred while writing data to shared memory (bytes = bytes, allocationSize = allocationSize).

Explanation:
The driver uses shared memory as the mechanism for providing information to the shell scripts. An error occurred while writing data from the driver process into the shared memory segment.

Possible Cause:
Invalid memory resources or internal error.

Action:
Contact NetIQ Support.

NIX005S An error occurred attempting to set an environment variable.

Explanation:
The driver uses environment variables for some of the communication between the driver and other processes called from the scripts. An error occurred setting an environment variable.

Possible Cause:
There was not enough space to allocate the new environment.

Action:
Restart the driver and ensure that there are adequate memory resources for the driver process.

NIX006S An error occurred attempting to execute the script [script].

Explanation:
The driver uses scripts to update the system for events from the Identity Vault. An error occurred while attempting to execute one of these scripts.

Possible Cause:
The script does not exist on the local system.

Possible Cause:
A memory or environment allocation failure occurred.

Action:
Restart the driver and ensure that the script exists on the local system.

NIX007S An error occurred attempting to terminate the script [script].

Explanation:
The driver uses scripts to update the system for events from the Identity Vault. An error occurred while attempting to terminate the script.

Possible Cause:
The script does not exist on the local system.

Possible Cause:
A memory or environment allocation failure occurred.

Action:
Restart the driver and ensure that the script exists on the local system.

NIX008S The shared memory tool was unable to retrieve a key from the environment.

Explanation:
The shared memory tool uses an environment variable to retrieve the key used to unlock the shared memory region and access driver shim data. The tool could not obtain the key from the environment.

Possible Cause:
The driver shim cannot set environment variables, or the environment has become corrupt during event processing.

Action:
Restart the driver shim process and clear any residual shared memory segments.Action:
