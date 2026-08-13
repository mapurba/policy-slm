# A.0 Appendix √¢¬Ä¬ì Multi Email Domain Support

While the connector is capable of managing multiple domains within one connector instance, in many cases, it is recommended that a one domain per driver instance model be used. This is a best practice recommendation. The connector does not support a one to many model between IDV users and Google domain users. As a result, a single IDV user instance can only be in one domain at a time, if all domains are managed by a single driver instance. Configuring a driver instance per domain (each child domain is set as the primary domain for the driver serving that domain) gives considerable flexibility for provisioning users and groups in multiple domains from a single IDV source object.

The G√Ç¬ÝSuite email application √¢¬Ä¬ì Gmail √¢¬Ä¬ì is included with all versions of Google Apps. This application can be turned off by an administrator for the entire domain or a subset of users (via an organization). There are three types of mail domains within Google Apps:

Primary Domain
:   √¢¬Ä¬ì This domain is tied to the name of the G√Ç¬ÝSuite Domain name: i.e.√Ç¬Ý<https://www.google.com/a/mycompanys.com>

Domain Alias
:   √¢¬Ä¬ì A domain Alias is an alternate domain name for the primary domain only. If√Ç¬Ýyou create a domain alias named myothercompany.com a user named name@mycompany.com will be able to receive an email via name@myothercompany.com.

Secondary or Sub Domain
:   √¢¬Ä¬ì A secondary domain is a separate email domain within G√Ç¬ÝSuite. An example of a secondary domain would be name@staff.mycompany.com. In the Google admin interface, it would be possible to have two accounts called √¢¬Ä¬úname√¢¬Ä¬ù with one being in the primary domain and one in the secondary domain. It is not possible to create a√Ç¬ÝDomain Alias for a secondary domain.

Planning out your email strategy within G√Ç¬ÝSuite should be completed and verified prior to synchronizing accounts with the driver.

The Google Driver can:

* Create and modify settings on a user in the Primary or Secondary Domain
* Use the GmailSettingsSendAs to set the users From Name and Email Address if there is a domain alias. Note that it is not possible to setup a SendAs with an account in a Secondary Domain.
* Switch users between parent and child domain via a rename operation

  + Rename the user from username@domain1.org to username@domain2.org
  + If the domains are within the same G√Ç¬ÝSuite service, the user account should switch to the other domain.

In order to create a user in a specific e-mail domain all you have to do is set the UserName (Google Attribute Name mapped to CN by default) to the domain name of your choice i.e. user@domain.com. The driver import comes with disabled policies for adding a secondary domain. These policies can be copied if there is more than one policy.

To enable these policies, you must first decide which users will go to which domain. This can be via entitlements, group membership, attribute values or containment within a container. For example, the√Ç¬Ýfollowing policy (used in the create rule) will create a user in the students.com email domain if the√Ç¬Ýattribute employeeType is set to the value of student:

*Figure A-1* Sample User Creation Policy

![](../graphics/figure51.png)

Note that you will need to modify your matching rule in a similar fashion.

Groups also fall into the same category as users. A policy would need to be written in the matching and create rule to facilitate adding a secondary domain for groups. The attribute that facilitates this is the DirXML-GAGroupEMailAddress. As with users all you have to do is set the attribute to determine which email domain the group will belong to with the email address of the group.√Ç¬Ý

The Google Apps driver packages included with Designer have examples of how to setup entitlements for multiple email domains.
