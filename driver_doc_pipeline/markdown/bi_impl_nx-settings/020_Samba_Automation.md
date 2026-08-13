# B.2 Samba Automation

The Linux and UNIX Settings driver can automate enabling OES users for NetIQ Samba. The driver performs the following steps:

1. Obtains the sambaSID and sambaPrimaryGroupSID attributes.

   To get the SID attributes, the driver searches the user芒聙聶s container for a sambaDomain object. If one is not found there, the driver searches each higher container until a sambaDomain object is found.
2. Sets the sambaSID attribute on the user object with the value from the sambaDomain object, a dash, and the value of the user芒聙聶s UID.

   For example, if the value of the sambaSID attribute from the sambaDomain object is S-1-5-21-948752240-2140611863-4084635154 and the user芒聙聶s GID is 1007, the value of the user芒聙聶s sambaSID attribute is set to S-1-5-21-948752240-2140611863-4084635154-1007.
3. Sets the sambaPrimaryGroupSID attribute on the user object with the value from the sambaDomain object, a dash, and the value of the user芒聙聶s UID.

   This works the same way as for the sambaSID attribute in the preceding example.
4. Adds the object class sambaSAMAccount to the user.
5. Adds the object class sambaAccount to the user.
