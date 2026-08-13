# 17.4 Adding API Support to SSH Secure Shell

SSH\* Communications Security produces a secure login application known as SSH Secure Shell. Source is available at ftp://ftp.ssh.com/pub/ssh. SSH Secure Shell is a commercial product. The rules governing the commercial and non-commercial use of SSH Secure Shell can be found at the [SSH Communications Security Web Site](http://www.ssh.com).

You can install Platform Services on your server and modify the Secure Shell daemon, sshd, to use the AS Client API to authenticate users.

The sshd using the Identity Manager Fan-Out Driver allows users to skip setting up passphrases, because the authentication stage of setting up the Secure Shell connection is achieved with the driver instead of public-private key cryptography. After you have authenticated, your Secure Shell session is securely encrypted, as normal.

The Identity Manager Fan-Out Driver provides sample instructions for modifying the Secure Shell sshunixuser.c module. These instructions are distributed in the ASAM/bin/PlatformServices/PlatformClient/SSH directory created by the Platform Services installation process.
