# 2.9 Extending Schema for Supporting Custom Attributes

For full support of driver functionality, the driver uses schema not available in the base eDirectory schema definition. A schema file containing the necessary attributes has been provided. The classes and attributes defined in this schema file are as follows:

* Classes

  + pdsEpicUser √¢¬Ä¬ì Auxiliary class
* Attributes (Optional Attributes of pdsEpicUser class)

  + pdsEmployeeEndDate √¢¬Ä¬ì Time, Single Valued, Sync Immediate
  + pdsEmployeeEndDateString √¢¬Ä¬ì Case Ignore String, Single Valued, Sync Immediate
  + pdsEmployeeStartDate √¢¬Ä¬ì Time, Single Valued, Sync Immediate
  + pdsEmployeeStartDateString √¢¬Ä¬ì Case Ignore String, Single Valued, Sync Immediate
  + pdsEpicLinkSER √¢¬Ä¬ì Boolean, Single Valued, Sync Immediate
  + pdsProviderAddress √¢¬Ä¬ì Case Ignore String, Sync Immediate

You can upload new attributes through the Identity Manager to extend the schema. The following steps explain the procedure to extend the schema:

1. Navigate to the extracted driver zip folder > schema.
2. Copy the .sch file to the system where Identity Manager is installed.
3. Execute the following ndssch command.

   ndssch [-h hostname[:port]] [-t tree\_name] [-d] admin\_FDN schemafile [schema\_description]

   For example, ndssch -h 10.71.131.123:524 -t SLES12SP3\_Quality\_131123\_TREE -d admin.sa.system /root/schema/pdsEpicUser.sch
4. The log file is created in the default location, /root/schema.log for troubleshooting.
