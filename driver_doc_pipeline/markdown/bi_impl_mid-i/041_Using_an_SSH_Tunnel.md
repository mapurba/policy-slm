# 8.2 Using an SSH Tunnel

In the event that SSL cannot be used, you may also secure the communications channel between the Metadirectory engine and the driver shim on the connected system using an SSH tunnel.

Ensure that the SSHD server is running on your IBM i box. To start the server, run the following command:

STRTCPSVR SERVER(\*SSHD)

You must enable the server to automatically start with TCP/IP. For more information, see [How to setup the IBM i SSH daemon to autostart with TCP/IP](https://www.ibm.com/support/pages/how-setup-ibm-i-ssh-daemon-autostart-tcpip).

Login to your identity vault server as the user you will use for ssh authentication. You can enable the key based authentication to avoid providing a password each time the ssh client is started. To enable key based authentication, perform the below steps based on your operating system:

On Windows:

* Start a Command Prompt

Both on Windows and Linux:

1. Run the following command: ssh-keygen
2. Press enter to accept the defaults and do not specify a passphrase. If you are asked to overwrite, select no.
3. Open id\_rsa.pub and copy the contents to your i box. On Linux, this file will be located at ~/.ssh/id\_rsa.pub. On windows, this file will be located at %HOMEPATH%\.ssh\id\_rsa.pub.

Login to your i box as the user you will use for ssh.

1. Run QSH
2. From QSH, run the following command: mkdir ~/.ssh
3. Next, run the following command from QSH: chmod 700 ~
4. Next, run the following command from QSH: chmod 600 ~/.ssh
5. Place the contents of id\_rsa.pub file identified above into ~/.ssh/authorized\_keys. You may need to create this file.
6. From QSH, run the following command: chmod 600 ~/.ssh/authorized\_keys

Start the ssh client on your Identity Vault server to tunnel the connection to your i box using the following commands based on your operating system. Be default, the port will be 8090.

On Linux:

* ssh -fN -i ~/.ssh/id\_rsa -L <port>:localhost:<port> <ssh-user>@<ibm-i-host>

On Windows:

* You may need to install the OpenSSH client. For more information, see Installation of [OpenSSH for Windows Server 2019 and Windows 10](https://docs.microsoft.com/en-us/windows-server-administration/openssh/openssh_install_firstuse).
* ssh -i %HOMEPATH%\.ssh\id\_rsa -L <port>:localhost<port> <ssh-user>@<ibm-i-host>

On your IBM i box, perform the following steps to modify I5OSDRV configuration file:

1. Run the following command: GO I5OSDRV/I5OSDRV
2. Choose option 3 to modify the configuration file
3. Remove ca=/usr/local/i5osdrv/keys/ca.pem from the -connection line.
4. Choose option 2 to stop I5OSDRV driver shim, then option 1 to start it back up.

In iManager, perform the following steps:

1. Go to the configuration for your i5/OS driver and remove kmo="SSL CertificateDNS" from the remote loader connection parameters.
2. Change the hostname to localhost.
3. Restart the driver and the connection to your IBM i box should succeed over the SSH tunnel.
