# 2.6 Subscribing to the Business Events

For the driver to subscribe to the business events from the Oracle EBS system, the driver must log in to the Oracle EBS system through an EBS account.

1. Using a Web browser, log into the Oracle EBS system as sysadmin user.
2. On the Dashboard, click the Workflow Administrator Web Applications link.
3. Click Business Events under the Administrator Workflow tab.
4. Type oracle.apps.fnd.user.insert in the Search text field, then click Go.
5. Click the Subscription link of the search result.
6. Click Create Subscription and specify the following information, then click Next.

   * *system:*
     Click Search, then browse to the correct system name you want to include.
   * *action type:*
     Specify action type as custom.
7. Specify the following information and click Apply:

   * *PL/SQL Rule Function:*
     Enter the IDM\_DRIVER.PUBLISH\_EVENT\_TO\_IDM function.
   * *Owner Name:*
     Specify the name of the owner as PER.
   * *Owner Tag:*
     Specify the tag of the owner as PER.
8. Repeat [Step 1](subscribing-to-the-business-events.html#b1212b5v) to [Step 7](subscribing-to-the-business-events.html#b1212b61) for oracle.apps.fnd.user.update business events.

   When a business event occurs in the Oracle EBS system, the PL/SQL API handles the capturing of the event data and performs an HTTP post to the driver.
9. Provision users in the Oracle EBS system.

   1. Install a custom PL/SQL.

      The PL/SQL API processes events that are sent from Identity Manager via the SOAP/REST endpoint.
   2. Create a SOAP/REST endpoint using IREP of the Oracle EBS system.

      This PL/SQL executes the appropriate SQL API based on the request it receives from the Identity Manager.
