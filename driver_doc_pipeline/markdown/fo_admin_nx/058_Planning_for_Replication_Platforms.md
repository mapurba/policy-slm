# 9.5 Planning for Replication Platforms

When planning for Replication Platforms, include the following considerations:

* By default, the Core Driver converts passwords to lowercase before sending them to the Platform Receiver. For more information, see [Lower Password Case](br3n4tb.html#bfprpgq).
* The Permit Password Replication attribute of a Platform object determines whether provisioning events for user accounts are sent to the platform before the passwords for these accounts are known to the Identity Manager Fan-Out Driver.

  Platforms configured with Permit Password Replication set to Yes do not receive Provisioning events for user accounts until the account passwords are known to the driver.

  Platforms configured with Permit Password Replication set to If Available do receive Provisioning events when they occur for an account, even if the password is not known to the driver.

  The driver uses system intercepts to collect password information. To be provisioned onto a platform configured with Permit Password Replication set to Yes, users must either change their passwords on a platform where the system intercepts are installed and configured, or authenticate on a participating redirection platform.

  By planning a staged deployment of the driver so that most users have authenticated using other platforms first, you can ensure the availability of these users to password replication platforms when you are ready to deploy the driver on them.

  For more information, see [Configuring Platforms](br3n4tb.html#bfijtk0).
