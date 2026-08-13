# 7.3 Increasing the memory heap size

The oafm module handles Webservices in the Oracle EBS system. To increase the memory heap size,

1. Go to the opmn.xml file in the /u01/app/VIS/inst/apps/VIS\_sles11sp164-ora/ora/10.1.3/opmn/conf directory and search for oafm <process-type> id.
2. Edit the start-parameters and stop-parameters. Increase the Xmx to 2048, Xms to 1024, and MaxPermSize to 512.
