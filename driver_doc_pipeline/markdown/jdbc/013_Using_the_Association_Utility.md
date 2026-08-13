# 3.3 Using the Association Utility

Run the Association utility once for each instance of the driver installed on an Identity Manager server. In the install-dir\DirXMLUtilities\jdbc\util directory, a batch file association.bat or shell script association.sh (depending upon your platform) starts the utility.

A properties file containing association utility parameters is provided for each supported database. These files are in the install-dir\DirXMLUtilities\jdbc\util directory.

*Table 3-2* Properties Files

| Database | Properties Filename |
| IBM DB2 Universal Database | properties\_db2.txt |
| Informix Dynamic Server | properties\_ifx\_ansi.txt1 properties\_ifx\_log.txt properties\_ifx\_no\_log.txt |
| Microsoft SQL Server | properties\_ms.txt |
| MySQL | properties\_my.txt |
| Oracle | properties\_ora.txt |
| PostgreSQL | properties\_pg.txt |
| Sybase Adaptive Server Enterprise | properties\_syb.txt |

This utility does not work with Informix ANSI-compliant databases.

1. Stop the driver.
2. Use association.bat or association.sh to run the Association utility to identify and remove extraneous associations (operations 2 and 3).

   No object associated by this product should have multiple associations. Manually remove extraneous associations on a per object basis. Operation 3 might help you identify which of the multiple associations is actually valid. After you know this, you can probably discard the extraneous associations.
3. Run the Association utility to identify and fix invalid associations (operation 3 and possibly operations 6 and 7).

   As a general rule, if the problem is isolated, manually edit each invalid association. If the problem is repetitive and affects a large number of associations, consider using operations 6 and 7. This utility can replace bad identifiers on a global basis, but cannot insert or remove them where they do not already exist. See [Parameters for Searching and Replacing](parameters-used-in-association-utility-for-searching-and-replacing-operations.html) for information about search parameters.
4. Run the Association utility to normalize associations (operations 4 and 5).
