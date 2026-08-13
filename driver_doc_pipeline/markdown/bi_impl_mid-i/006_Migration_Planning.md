# 2.2 Migration Planning

* If you install the password exit during installation, the installation program sets the QPWDVLDPGM system value to \*REGFAC and installs a Validate Password exit program. If you want to publish password change information and if you currently use a Password Validation program, you must write a new one that can be registered for the QIBM\_QSY\_VLD\_PASSWRD exit point.
* We recommend that you use password level (IBM i QPWDLVL system value) 2 or above. For details, see [Password Levels](b3wxlbx.html#b4n1wwt).
* You can use any security level (IBM i QSECURITY system value) with the driver. IBM recommends security level 40.
* Where are the objects that you plan to manage with the IBM i driver currently stored?
* Can you use a Matching policy to select the objects to manage based on criteria, such as department, group membership, or some other attribute?
