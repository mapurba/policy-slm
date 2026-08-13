# 13.6 Troubleshooting Account Redirection

If a user cannot access the local Linux or UNIX system through the Name Service Switch and Platform Services Cache Daemon, but can log in through eDirectory, check the following:

* The user is present in the Census and platform search object.
* The user has been extended with the posixAccount auxiliary class.
* A Universal Password policy exists and is configured to allow agents to retrieve the Universal Password.
* The driver filter is configured with the posixAccount class and attributes.
