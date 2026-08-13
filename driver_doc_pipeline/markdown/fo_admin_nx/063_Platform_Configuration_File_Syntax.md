# 10.2 Platform Configuration File Syntax

Use the following syntax guidelines for the platform configuration file:

* Any line beginning with an asterisk (\*), a semicolon (;), or an octothorpe (#) is a comment. All text that follows a semicolon or an octothorpe is a comment.
* Configuration file statements are case-insensitive.
* Except as noted, the order in which statements appear in the file does not matter.
* Any parameter value that contains spaces must be enclosed in quotes. Do not use quotes with other values. For example:

  ```
  PASSWORDPROMPT "Password: "
  PROVISIONING cdriver1.digitalairlines.com
  ```
