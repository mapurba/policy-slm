# 9.1 General Troubleshooting Issues

When troubleshooting, keep in mind these issues:

* When you make any changes to policies by clicking New, Edit, or Remove on the page where the policies are listed, the Entitlements Service Driver is stopped. The driver is not restarted unless you click Restart on that page.

  This feature prevents the driver from granting or revoking entitlements in your production environment while your changes to policies are incomplete.

  If you don’t use the Restart button on the page, you see the following in the trace:

  ```
  DirXML Log Event -------------------
       Driver:   \ACME-LAB-LDAP\acme\Drivers\IDM\RBE-Entitlements Service
       Status:   Fatal
       Message:  Code(-9005) The driver returned a "fatal" status indicating that the driver should be shut down. Detail from d
  river: &lt;description>Entitlement Policy editor is currently locked by 'acme\admins\admin@127.0.0.1'.&lt;/description>
  &lt;document xml:space="preserve">&lt;nds dtdversion="3.5" ndsversion="8.x">
          &lt;source>
                  &lt;product version="3.6.1.4427">DirXML&lt;/product>
                  &lt;contact>Novell, Inc.&lt;/contact>
          &lt;/source>
          &lt;input>
                  &lt;init-params src-dn="\ACME-LAB-LDAP\acme\Drivers\IDM\RBE-Entitlements Service"/>
          &lt;/input>
  &lt;/nds>&lt;/document>
  &lt;application>DirXML &lt;/application>
  &lt;module>RBE-Entitlements Service &lt;/module>
  &lt;object-dn>&lt;/object-dn>
  &lt;component>DirXML Engine&lt;/component>
  ```
* Similarly, the Entitlements Service Driver won’t start if more than one person appears to be editing Entitlement Policies at the same time.
* Because one Entitlements Service Driver is used per driver set, an entitlement policy can manage only users that are in a read/write or master replica on the server that is associated with that driver set.
