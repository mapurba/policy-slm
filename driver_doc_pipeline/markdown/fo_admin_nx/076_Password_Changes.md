# 12.4 Password Changes

You will need to decide whether users should be allowed to change their passwords from the Linux or UNIX system, using PAM-enabled tools such as passwd, or require users to change their passwords from another system, such as a Web portal or eDirectory client.

When you allow password changes from the Linux or UNIX system, configured with Platform Services, the PAM passwd module is automatically configured to redirect password changes back to the Identity Vault. No manual configuration is required.
