# 4.11 Testing the Database Object Installation

Test scripts for each database are located in the following directories:

*Table 4-4* Location of Database Scripts

| Database | Test SQL Scripts Location |
| IBM DB2 Universal Database | *UNIX/Linux:* install-dir/lib/dirxml/rules/jdbc/sql/db2\_udb/test  *Windows:* install-dir\DirXMLUtilities\jdbc\sql\db2\_udb\test |
| Informix Dynamic Server | *UNIX/Linux:* The test scripts are located in the following directories:  * install-dir/lib/dirxml/rules/jdbc/sql/informix\_ids/test/log * install-dir/lib/dirxml/rules/jdbc/sql/informix\_ids/test/no\_log  *Windows:* The test scripts are located in the following directories:  * install-dir\DirXMLUtilities\jdbc\sql\informix\_ids\log\test * install-dir\DirXMLUtilities\jdbc\sql\informix\_ids\no\_log\test  *Informix:* Informix ANSI test scripts are located in the log subdirectory. |
| Microsoft SQL Server | *UNIX/Linux:* The test scripts are located in the following directories:  * install-dir/lib/dirxml/rules/jdbc/sql/mssql/3or4/test * install-dir/lib/dirxml/rules/jdbc/sql/mssql/5/test  *Windows:* install-dir\DirXMLUtilities\jdbc\sql\mssql\test |
| MySQL | *UNIX/Linux:* The test scripts are located in the following directories:  * install-dir/lib/dirxml/rules/jdbc/sql/mysql/3or4/test * install-dir/lib/dirxml/rules/jdbc/sql/mysql/5/test  *Windows:* install-dir\DirXMLUtilities\jdbc\sql\mysql\test |
| Oracle | *UNIX/Linux:* install-dir/lib/dirxml/rules/jdbc/sql/oracle/test  *Windows:* install-dir\DirXMLUtilities\jdbc\sql\oracle\test |
| PostgreSQL | *UNIX/Linux:*  install-dir /lib/dirxml/rules/jdbc/sql/postgres/test  *Windows:*  install-dir \DirXMLUtilities\jdbc\sql\postgres\test |
| Sybase Adaptive Server Enterprise | *UNIX/Linux:*  install-dir /lib/dirxml/rules/jdbc/sql/sybase\_ase/test  *Windows:*  install-dir \DirXMLUtilities\jdbc\sql\sybase\_ase\test |

You should try the test scripts before starting the sample driver.

If you encounter issues while testing, see the following sections:

* [Recognizing Publication Events](b95va5e.html).
* [Executing Test Scripts](b95vb06.html).
