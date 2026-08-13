# 2.4 Installation Tasks

## 2.4.1 Installing the Driver Shim on the Linux Server

1. Log in to the target Linux server as root.
2. Make sure Perl 5 is installed.

   1. On Red Hat, yum install perl
   2. On SLES, zypper install perl
3. Install the required Perl modules through your package manager, or use yum install on Red Hat and zypper install on SLES systems:

   * perl-JSON
   * perl-JSON-XS
   * perl-libwww-perl

   *NOTE:*For Red Hat 8.1, you will also need to install perl-LWP-Protocol-https.
4. If any of the Perl Modules are not available through your system package manager, they may also be installed through CPAN:

   * cpan JSON
   * cpan JSON::XS
   * cpan LWP::UserAgent
5. Obtain the linux\_x86\_64\_bbdriver\_install.bin file from your installation media and execute this self-extracting file on your Linux system.
6. Specify the language choice.
7. Read and accept the license agreement.
8. After the package is installed onto your system, you are prompted to enter Driver and Remote Loader passwords. These passwords are used to verify that an authorized driver shim is communicating with the Identity Manager engine. Follow the prompts:

   1. Enter and confirm the Remote Loader Password.
   2. Enter and confirm the Driver Object password.
9. Next, you are prompted to retrieve an SSL certificate. NetIQ eDirectory must be running to retrieve the certificate. The certificate allows SSL encryption between the Identity Manager engine and the driver shim. Enabling SSL is optional, but is recommended for better security. To retrieve the certificate, follow the prompts:

   1. Specify the DNS name or IP Address of your eDirectory server.
   2. Specify the LDAP secure port, default 636.
   3. Enter Y to accept the certificate.
10. The installation of the driver shim is finished, with the option of starting the Driver Shim Service. Proceed to the next section to complete the installation of the driver.

## 2.4.2 Extending the Schema for Identity Manager

If you plan on using the Identity Vault to manage connected system attributes that are not already mapped to standard eDirectory™ attributes, you will need to extend the schema. Otherwise, it is not necessary.

Extending the schema adds auxiliary classes to eDirectory User and Group objects for Blackboard user and group attributes. It also extends the schema for an effective class called DirXML-BB-Enrollment that can be used to represent an enrollment in a Blackboard Course or Organization.

To extend the schema:

1. Obtain the blackboard.sch file for browser access, depending on the operating system you are running:

   * *Linux or Solaris:*
     Copy the blackboard.sch file from /opt/netiq/eDirectory/lib/lib/nds-schema/ on the Blackboard application server where you installed the RPM to a location accessible to your web browser.

     *Windows:*
     Copy the blackboard.sch file from the Additional\_Drivers/Blackboard directory in the ISO image for Windows to a location accessible to your web browser.
2. In iManager, select the Extend Schema task under Schema.
3. Select Import data from file on disk, then click Next.
4. Select a file type of Schema File.
5. Type or browse for blackboard.sch as the file to import, then click Next.
6. Specify the host name or IP address and the LDAP port number of your Metadirectory server.
7. To connect to the non-secure LDAP port (389), you must have the Require TLS for Simple Binds with Password option disabled on your LDAP Group. If necessary, you can edit this option using the LDAP Options task under LDAP in iManager. For details, see the NetIQ eDirectory Administration Guide.
8. Select Authenticated login and log in as Admin or another user with rights to extend the schema.
9. Click Next to go to the summary.
10. Click Finish to extend the schema.

## 2.4.3 Configuring the REST API on your Blackboard Learn Instance

1. Setup a Blackboard Learn Application Key and Secret for your installation.

   1. Login to <https://developer.blackboard.com>. You may need to create an account.
   2. Register a new application.
   3. You will need to fill out the first three fields:

      * Application Name: NetIQ Blackboard Driver
      * Description: Provisions users and courses to Blackboard.
      * Domain(s): myschool.edu (This is the domain of your Blackboard server instance)
   4. Once the API Key is generated, note the Application Key, Secret and Application ID.
2. Create a Blackboard Learn System Role for use by the driver.
3. Assign privileges to this System Role so that courses, organizations and users can be created, deleted and modified by the driver. Privileges required:

   * Administrator Panel (Courses) > Courses
   * Administrator Panel (Courses) > Courses > Create Course
   * Administrator Panel (Courses) > Courses > Delete Courses
   * Administrator Panel (Courses) > Courses > Edit
   * Administrator Panel (Courses) > Courses > Edit > Enrollments
   * Administrator Panel (Courses) > Courses > Edit > Enrollments > Add Enrollment
   * Administrator Panel (Courses) > Courses > Edit > Enrollments > Delete Enrollment
   * Administrator Panel (Courses) > Courses > Edit > Enrollments > Edit Enrollment
   * Administrator Panel (Organizations) > Organizations
   * Administrator Panel (Organizations) > Organizations > Create Organization
   * Administrator Panel (Organizations) > Organizations > Delete Organization
   * Administrator Panel (Organizations) > Organizations > Edit > Enrollments
   * Administrator Panel (Organizations) > Organizations > Edit > Enrollments > Add Enrollment
   * Administrator Panel (Organizations) > Organizations > Edit > Enrollments > Delete Enrollment
   * Administrator Panel (Organizations) > Organizations > Edit > Enrollments > Edit Enrollment
   * Administrator Panel (Users) > Users
   * Administrator Panel (Users) > Users > Create User
   * Administrator Panel (Users) > Users > Delete Users
   * Administrator Panel (Users) > Users > Edit > Change Password
   * Administrator Panel (Users) > Users > Edit > User Properties
   * Administrator Panel (Users) > Users > Edit > View Course Enrollments
   * Administrator Panel (Users) > Users > Edit > View Organization Enrollments
   * Course/Organization Control Panel (Users and Groups) > Users > Remove Users from Course/Organization
   * Course/Organization Control Panel (Users and Groups) > Users > Change User’s availability in Course/Organization
4. Create a Blackboard Learn User for use by the driver and assign the System Role you created above.
5. Follow Blackboard’s instructions to setup a REST integration: [Blackboard REST Integration](https://help.blackboard.com/Learn/Administrator/Hosting/System_Integration/Compare_Building_Blocks_and_Rest#register-a-rest-integration-in-blackboard-learn_OTP-4)

   * Specify the user created in Step 2 as the Learn User for the REST Integration.

     *NOTE:*End User Access should be set to No.
   * Enter the Application ID from Step 1.
