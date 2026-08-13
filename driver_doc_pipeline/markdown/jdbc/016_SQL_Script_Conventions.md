# 4.1 SQL Script Conventions

The following table lists default locations for SQL scripts:

*Table 4-1* Default Locations for SQL Scripts

| Platform | Default Location |
| Windows | c:\Novell\IdentityManager\NDS\DirXMLUtilities\jdbc\sql\ |
| UNIX/Linux | /opt/novell/eDirectory/lib/dirxml/rules/jdbc/sql/ |

For example, when the scripts are installed on a SUSE Linux Enterprise Server with eDirectory, the DB2 scripts are found in opt/novell/eDirectory/lib/dirxml/rules/jdbc/db2\_udb/install directory.

All SQL scripts use the same conventions, regardless of the database.

The maximum size of a DB2 identifier is 18 characters. This least common denominator length defines the upper bound of database identifier length across all SQL scripts. Because of this restricted length, abbreviations are used. The following table summarizes identifier abbreviations and their meanings:

*Table 4-2* Identifier Abbreviations and Meanings

| Abbreviation | Interpretation |
| proc\_ | stored procedure/function |
| idx\_ | index |
| trg\_ | trigger |
| \_i | on insert trigger |
| \_u | on update trigger |
| \_d | on delete trigger |
| chk\_ | check constraint |
| pk\_ | view primary key constraint |
| fk\_ | view foreign key constraint |
| mv\_ | view multi-valued column |
| sv\_ | view single-valued column (implicit default) |

Instead of proc\_, the more common abbreviation is sp\_. This prefix is reserved for system-stored procedures on Microsoft SQL Server. Also, this prefix forces lookup of a procedure first in the master database before evaluating any qualifiers (for example, database or owner). To maximize procedure lookup efficiency, this prefix has been deliberately avoided.

The following table indicates identifier naming conventions for indexes, triggers, stored procedures, functions, and constraints:

*Table 4-3* Identifier Naming Conventions

| Database Object | Naming Convention | Examples |
| stored procedure/function | proc\_procedure-or-function-name | proc\_idu |
| index | idx\_unqualified-table-name\_sequence-number | idx\_indirectlog\_1 |
| trigger | tgr\_unqualified-table-name\_triggering-statement-type\_sequence-number | tgr\_usr\_i\_1 |
| primary key constraint | pk\_unqualified-table-name\_column-name | pk\_usr\_idu |
| foreign key constraint | fk\_unqualified-table-name\_column-name | fk\_usr\_idu |
| check constraint | chk\_unqualified-table-name\_column-name | chk\_usr\_idu |

Other conventions:

* All database identifiers are lowercase.

  This is the most commonly used case convention between databases.
* String field lengths are 64 characters.

  Fields of this length can hold most eDirectory attribute values. You might want to refine field lengths to enhance storage efficiency.
* For performance reasons, primary key columns use native, scalar numeric types whenever possible (such as BIGINT as opposed to NUMERIC).
* The record\_id column in event log tables has the maximum numeric range permitted by each database to avoid overflow.
* Identity columns and sequence objects do not cache values. Some databases throw away cached values when a rollback occurs. This action can cause large gaps in identity column or sequence values.
