# 2.5 Creating a Web Service Endpoint

The driver uses a SOAP/REST endpoint to synchronize the Identity Manager events in the Subscriber channel and poll the Oracle database for fetching events.

1. Create a new SOAP/REST endpoint. Run the following shell script on the Oracle EBS server:

   ```
   export FND_TOP=/u01/app/VIS/apps/apps_st/appl/fnd/12.0.0
   export APPL_TOP=/u01/app/VIS/apps/apps_st/appl
   . $APPL_TOP/APPS_instancename_hostname-ora.env
   #. /configure_EBS.sh
   ```

   *NOTE:*Currently, this script is available only for UNIX platforms.

   You must specify appropriate values for FND\_TOP and APPL\_TOP variables in the commands.
2. Using a Web browser, log into the Oracle EBS system as sysadmin user.
3. On the Dashboard, click the Integrated SOA Gateway link.
4. Click Integration Repository under the Integrated SOA Gateway tab, then change the view to By option to Product Family.

   The Novell IDM Suite displays.
5. Expand the view and click Novell IDM Suite > Driver > Subscriber > IDM Subscriber.

   * In case you are using SOAP API, click on SOAP Web Service > Generate WSDL > Deploy.
   * In case you are using REST API, click on REST Web Service and perform the following steps:

     1. Specify REST endpoint name in the Service Alias field. For example, you can specify idmebs.
     2. Select the Subscribe IDM Events check box.
     3. Click on Deploy.
     4. Click on View WADL.

        *NOTE:*You must use the resource base URL from the WADL file as your REST endpoint URL. You must use the URL without quotes and ending slash. For example, http://oracleebs.labs.blr.novell.com:8010/webservices/rest/idmebs
6. Click Generate WSDL, then click Deploy.
7. Select the Subscribe Identity Manager Events method under Procedures and Functions, then click Create Grant.
8. Select the user as sysadmin and click Apply.

On executing this command, if you get the error message, "Can't locate Class/MethodMaker.pm in @INC (@INC contains:..." , you need to install the Perl modules. For installation instructions, see the [Oracle E-Business Suite Integrated SOA Gateway Implementation Guide](https://docs.oracle.com/cd/E18727-01/doc.121/e12169/T511175T543269.htm).

If the deployment fails, go to the /u01/app/VIS/inst/apps/VIS\_sles11sp164-ora/soa/PLSQL/4723/SUBSCRIBE\_EVENTS.wsdl file and remove the line, IRepOverloadSeq="1" under the operation tag, then save the file and use the GUI method to redeploy the SOAP service.
