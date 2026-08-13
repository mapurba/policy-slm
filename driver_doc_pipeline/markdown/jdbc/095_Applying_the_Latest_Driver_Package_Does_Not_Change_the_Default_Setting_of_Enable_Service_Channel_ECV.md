# 15.7 Applying the Latest Driver Package Does Not Change the Default Setting of Enable Service Channel ECV

*Issue:*
If you upgraded to Identity Manager 4.7 and updated the base packages for your driver, the package update process does not overwrite the default setting (False) of Enable Service Channel ECV.

This issue does not occur when you create a new driver.

Workaround: Manually change the ECV for the driver.

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
2. On the Driver Dashboard, locate the driver icon and click the icon to display the driver’s properties page.
3. Click the Configuration tab.
4. Expand the Engine Control Values section.
5. Change the value for Enable Subscriber Service Channel.
6. Save changes.
7. Restart the driver for the changes to take effect.
