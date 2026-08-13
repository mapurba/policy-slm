# C.3 Driver Limitations

* [Password Levels](b3wxlbx.html#b4n1wwt)
* [Character Fields](b3wxlbx.html#b4n1x0h)
* [Distribution Directory Entry Limits](b3wxlbx.html#b4xc8je)

## C.3.1 Password Levels

Password levels (i5/OS QPWDLVL system value) 0 and 1 support a maximum password length of ten characters. The allowable characters for passwords are the uppercase letters (A–Z), the digits (0–9), the dollar sign ($), the at sign (@), the octothorpe (#), and the underscore (\_).

If you use password level 0 or 1, the Subscriber channel CL programs convert passwords to uppercase and truncate passwords to ten characters. The Publisher shim converts passwords to lowercase.

With password levels 2 and above, passwords can be mixed case and can be up to 128 characters long.

We recommend that you use password level 2 or above for best integration with Identity Manager.

## C.3.2 Character Fields

Data is converted to the default coded character set identifier (CCSID) for the driver shim job. This is usually the QCCSID system value. You can use the CHGUSRPRF command to specify a CCSID for the user profile that runs the job. By default, the installation program creates a user profile named I5OSDRV for the driver shim job.

## C.3.3 Distribution Directory Entry Limits

Distribution directory entries are linked to user profiles by a two-element USRID value, which comprises a user ID and a user address. These elements can have a maximum of 8 characters. User profile names can have a maximum of 10 characters. The Subscriber shim CL programs obtain the user ID by truncating user profile names to 8 characters and set the user address to the system name. To avoid collisions in the distribution directory, IBM recommends that you limit user profile names to 8 characters.
