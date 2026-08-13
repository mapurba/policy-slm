# 3.1 Installing the Linux and UNIX Scripting Driver Shim

Topics in this section include

* [Installing the Linux and UNIX Scripting Driver Shim](b8moq22.html#b8moqh0)
* [Running the Driver Shim](b8moq22.html#b8moue0)

## 3.1.1 Installing the Linux and UNIX Scripting Driver Shim

1. Log in to the target application server as root.
2. Obtain the <os>\_scriptdriver\_install.bin file from your installation media and execute this self-extracting file on your Linux or UNIX system.
3. Specify a language choice.
4. Read and accept the license agreement.
5. After the package is installed onto your system, you are prompted to enter Driver and Remote Loader passwords. These passwords are used to verify that an authorized driver shim is communicating with the Identity Manager engine. Follow the prompts:

   1. Enter and confirm the Remote Loader password.
   2. Enter and confirm the driver password.
6. Next, you are prompted to retrieve an SSL certificate. NetIQ® eDirectory™ must be running to retrieve the certificate. The certificate allows SSL encryption between the Identity Manager engine and the driver shim. Enabling SSL is optional but is recommended for better security. To retrieve the certificate, follow the prompts:

   1. Specify the DNS name or IP address of your eDirectory server.
   2. Specify the LDAP secure port, default 636.
   3. Enter Y to accept the certificate.
7. You are prompted for a Scripting language to be used on this system. Enter Perl for the sample Perl scripts to be installed or enter Shell for the sample Bourne Shell scripts to be installed.
8. If you select Perl, you are optionally asked to install the Perl IDMLib perl module into the Perl system path to be accessible by the sample Perl scripts. Enter Yes or No to install this library.
9. The installation of the driver shim is finished, with the option of starting the Driver Shim Service. Proceed to the next section to complete the installation of the driver.

## 3.1.2 Running the Driver Shim

Start the driver engine component in NetIQ iManager.

The driver shim is a UNIX daemon process. Use the UNIX startup script usdrvd to start and stop the NetIQ Identity Manager Linux and UNIX Script Driver (see [Section 6.0, Using the Scripting Driver](b8nnhcs.html).)
