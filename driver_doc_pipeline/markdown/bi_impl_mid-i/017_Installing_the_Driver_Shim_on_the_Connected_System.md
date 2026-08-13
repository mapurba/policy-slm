# 3.7 Installing the Driver Shim on the Connected System

You can install multiple instances of the driver on one IBM i system if necessary to support applications via customized CL programs. By default, the driver shim installation uses the I5OSDRV library and the /usr/local/i5osdrv IFS path.

For details see [Driver Shim Library and IFS Contents](b4ab5n6.html).

The driver uses an embedded Remote Loader. It is not necessary to install Java on the connected system.

1. Sign on as QSECOFR or an equivalent user to the target IBM i system.
2. Use the following command to create a temporary file to contain the driver shim distribution package:

   ```
   CRTSAVF FILE(QSYS/NOVELLDIST)
   ```
3. On the workstation that you used in [Step 2](b3xd1sq.html#b4rpe2a), use FTP to transfer i5osdrv.sav to the NOVELLDIST file just created in [Step 2](b3xehpq.html#b4rpm3n) on your target IBM i system:

   ```
   >ftp server_address
   (Authenticate to the server)
   ftp> cd qsys
   ftp> bin
   ftp> put i5osdrv.sav novelldist.file
   ftp> quit
   ```
4. On the IBM i system, execute the following command to restore the driver shim distribution library:

   ```
   RSTLIB SAVLIB(NOVELLDIST) DEV(*SAVF) SAVF(QSYS/NOVELLDIST)
   ```
5. Remove the temporary file:

   ```
   DLTF FILE(QSYS/NOVELLDIST)
   ```
6. Execute the installation program:

   ```
   CALL PGM(NOVELLDIST/INSTALL)
   ```
7. Respond to the prompts as appropriate to complete the installation:

   1. Read and accept the license agreement.
   2. Specify the driver library name and the driver IFS path. These default to I5OSDRV and to /usr/local/i5osdrv respectively.

      ```
      The driver requires a library in i5os and a path in the Integrated File System.
      Library: I5OSDRV
      ```

      ```
      IFS Path: /user/local/i5osdrv
      ```
   3. Specify the TCP port number for the driver shim to listen on. The default port is 8090.

      ```
      The driver must listen on a port for connections from the Metadirectory server.
      ```

      ```
      Remote Loader Port: 8090
      ```
   4. Create a new User profile for the driver or specify an existing profile.

      ```
      The driver requires a User Profile with *SECADM and *ALLOBJ Special Privileges. A new Profile can be created by the installation, or an existing Profile can be used.
      Create New Profile: Y
      ```

      ```
      User Profile: I5OSDRV
      ```
   5. Specify a subsystem and a job queue for the driver.

      ```
      The driver must be assigned to a subsystem and a job queue.
      ```

      ```
      Subsystem: QSYSWRK
      ```

      ```
      Job Queue: QSYSNOMAX
      ```
   6. Specify whether the driver should be automatically started when the system starts.

      ```
      Autostart Job at IPL: Y
      ```
   7. Specify whether to install the profile exits, the distribution directory exit, and the password exit.

      If you do not install the exits, the driver cannot publish the corresponding information.

      ```
      Exits must be installed for the driver to publish profile and password changes to the Identity Vault.
      ```

      ```
      Install Profile Exits: Y
         QIBM_QSY_CHG_PROFILE
         QIBM_QSY_CRT_PROFILE
         QIBM_QSY_DLT_PROFILE
         QIBM_QSY_RST_PROFILE
      ```

      ```
      Install Distribution Directory Exit: Y
         QIBM_QOK_NOTIFY
      ```

      ```
      Install Password Exit: Y
         QIBM_QSY_VLD_PASSWRD
      ```
   8. Provide the Remote Loader and Driver object passwords that you entered when creating the driver in [Step 7](b3xdkfa.html#b12f3q0b).

      ```
      Enter Remote Loader Password:
      Confirm Remote Loader Password:
      Enter Driver Object Password:
      Confirm Driver Object Password:
      ```
   9. Specify the Metadirectory server host name or IP address and secure LDAP port number.

      These are used to secure the driver shim with SSL.

      ```
      DNS name or IP address of the LDAP Server:
      TCP port number for LDAP SSL (default 636):
      ```
8. Start the driver shim.

   Enter GO I5OSDRV/I5OSDRV, then select option 1.

   If you did not use the default library name, substitute your driver library name as shown in the following example:

   ```
   GO yourDriverLibrary/I5OSDRV
   ```
