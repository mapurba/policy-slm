# M.2 Setting Up the OCI Client

Set up the Oracle Instant Client on the machine where the JDBC driver is running (not on the machine where Oracle is running).

1. Log into Linux as root, and create the following structure:

   /oracle /oracle/client /oracle/client/bin /oracle/client/lib /oracle/client/network/admin
2. Unzip all files from instantclient-basic-linux32-11.1.0.7.zip to /oracle/client/lib.
3. Unzip all files from instantclient-sqlplus-linux32-11.1.0.7.zip to /oracle/client/bin.
4. Copy libsqlplus.so from /oracle/client/bin to /oracle/client/lib.
5. Copy libsqlplusic.so from /oracle/client/bin to /oracle/client/lib.
6. Using chmod, ensure that the file sqlplus in /oracle/client/bin is executable.
7. Copy a valid tnsnames.ora into /oracle/client/network/admin.

   If you don’t have a tnsnames.ora file, use the Oracle configuration tool to create one.

   Make sure that the tnsnames.ora filename is in lowercase.
8. Modify the profile.local file by adding the following lines:

   ```
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/oracle/client/lib
   ```

   ```
   export TNS_ADMIN=/oracle/client/network/admin
   ```

   ```
   export PATH=$PATH:/oracle/client/lib
   ```

   The profile.local file is in the /etc folder. If the file doesn’t exist, create one. The file can consist of only the three export lines.

   The profile.local file extends the LD\_LIBRARY\_PATH, sets TNS\_ADMIN, and extends the PATH. This file is read when the server boots.
9. Ensure that the exports in the profile.local file are always valid.
10. Copy the appropriate jar files to the Identity Manager classes directory.

    These .jar files are supplied with the Instant Client.

    The Identity Manager classes directory is the directory where your driver is located.
11. Start SQL Plus with the following example command (assuming that the directory is /oracle/client/bin):

    ./sqlplus username/password@sid
