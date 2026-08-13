# 9.7 Replacing comm Utility for AIX and HP-UX

If you plan to use Identity Manager with a connected system running AIX or HP-UX, you may need to replace the standard comm utility (invoked by the comm command) included with the operating system. Versions of comm that are included with either of these operating systems have been known to fail when used with files that contain long text lines. In general, the problem occurs with text lines longer than 2000 characters.

The Identity Manager driver uses comm to get information from /etc/group. Therefore, if any of your AIX or HP-UX connected systems has an /etc/group file with a line longer than 2000 characters, you should use one of the following vendor-approved GNU packages to replace the comm utility:

| Operating System | Vendor Name and Link to Replacement Utilities |
| AIX | IBM |
| HP-UX | [HP](http://hpux.connect.org.uk/hppd/hpux/Gnu/coreutils-8.23/) |
