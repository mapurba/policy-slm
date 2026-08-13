# A.1 Password Change Validation Exit

The Core Driver of the NetIQÂ® Identity Manager Fan-Out can call a user-provided routine to enforce local password rules. This routine is called when a password change request is received from a password redirection platform.

The Password Change Validation Exit is passed the fully distinguished name of the user, the old password, the new password, and a message buffer. The exit can accept or reject the password change request and, if the request is rejected, provide an explanation in the message buffer. The explanation is written to the Core Driver Audit log and is displayed to the user.

A sample Password Change Validation Exit is provided in the ASAM directory created by the installation process in asam\bin\coredriver\chgpasswdexit\verpass.c.

To implement the Password Change Validation Exit:

1. Design, write, and build your Password Change Validation Exit. You can use the sample Password Change Validation Exit verpass.c as a guide.
2. Place a copy of the library containing your Password Change Validation Exit on each server that runs a Core Driver.
3. Specify the appropriate Change Password Exit Function and Change Password Exit Library configuration parameters for each Core Driver. For details, see [Driver Object Configuration Parameters](br3n4tb.html#cegdedii).
