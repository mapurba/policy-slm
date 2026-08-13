# A.1 Known Issues

* In the MSSQL database the underline base table can be modified through a view only if the INSERT, UPDATE and DELETE statements refers to the column of the single base table.
* If you are connecting the driver to Microsoft SQL database, the driver does not support Windows NTLM and Windows Single Sign-On authentication.
* For modifications of the referential attributes (for example: Manager), the JDBC driver returns a success status even if the referenced object or user does not have the association (not present in the target database).
* Due to the above mentioned reason, if the Out of Band sync is enabled for the referential attribute, there is a possibility of event loss if the modify event of the referential attribute is processed before the referenced user's add event was processed. Hence, NetIQ recommends not to enable Out of Band events for referential attributes.
* The Fanout driver configuration page of Identity Console displays the Remote Loader option. Ensure that you do not use this option with the Fanout driver.
* The Fanout driver does not support direct synchronization mode for MySQL InnoDB. This is because the driver does not support the Subscriber Add operation in this mode.
* If you use the Tab key to navigate the Password field in the Fanout Configuration page of Designer, Designer prompts you to save the resource when no change is made to the resource.
* Identity Manager does not support the non-root installation of the Fanout agent.
* When you stop the Fanout agent, the command server log file displays a warning message stating that one thread cannot be stopped. Ignore the warning message.
* If you are connecting to a Sybase database, additional operations cannot be performed if the transaction log is full. The JDBC driver instance waits for the transaction log to be cleared before processing further events.
* JDBC drivers stop working if a wrong password is specified when a driver is authenticating with a connected system. This is an expected behavior. However, the JDBC driver for Sybase continues to retry the connection and does not stop.
* Changes in Fanout instance names do not reflect in the DirXML-Accounts and DirXML-Associations attributes. Therefore, they become invalid. NetIQ does not recommend you to change the connection object names and the instance names.
* Sometimes when a codemap refresh is done, you may not receive codemap data of all the connected databases. You may get errors such as “Unable to complete the CODE MAP refresh for entitlement” in catalina.out. This is due to the time taken by the query to return the codemap results. Hence, you need to increase the timeout for the following parameters:

  + Default Query Timeout (IDMProv web UI > Roles and Resources > Configure Roles and Resource Settings > Entitlement Query Settings > Default Query Timeout).

    If the value of this parameter is 10 minutes, then increase the value of NCPCLIENT\_REQ\_TIMEOUT parameter.
  + NCPCLIENT\_REQ\_TIMEOUT

    Refer to [Knowledgebase](https://www.netiq.com/support/kb/doc.php?id=7016855) for more information on how to increase the value of this parameter.
* If you upgraded to Identity Manager 4.7 and updated the base packages for your driver, the package update process does not overwrite the default setting (False) of Enable Service Channel ECV.

  To workaround this issue, manually change the ECV for the driver.

  This issue does not occur when you create a new driver.

  To change the ECV in Designer:

1. In Modeler, right-click the driver line.
2. Select Properties > Engine Control Values.
3. Click the tooltip icon to the right of Engine Controls for Server.

   If a server is associated with the Identity Vault, and if you are authenticated, the engine control values display in the large pane.
4. Change the value for Enable Subscriber Service Channel.
5. Click OK.
6. For the change to take effect, deploy the driver to the live Identity Vault.

To change the ECV in Identity Console:

1. Click the IDM Administration tile.
2. On the Driver Dashboard locate the driver, then click the driver icon.
3. Click the Configuration tab.
4. Expand the Engine Control Values section.
5. Change the value for Enable Subscriber Service Channel.
6. Save.
7. For the change to take effect, restart the driver.
