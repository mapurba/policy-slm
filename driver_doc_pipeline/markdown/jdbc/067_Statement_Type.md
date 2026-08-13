# 12.7 Statement Type

The Subscriber channel executes embedded SQL statements, but it doesn’t understand them. The JDBC 1 interface defines several methods for executing different types of SQL statements. The following table contains these methods:

*Table 12-1* Methods for Executing SQL Statements

| Statement Type | Method Executed |
| SELECT | java.sql.Statement.executeQuery(String query):java.sql.ResultSet |
| INSERT | java.sql.Statement.executeUpdate(String update):int |
| UPDATE | java.sql.Statement.executeUpdate(String update):int |
| DELETE | java.sql.Statement.executeUpdate(String update):int |
| CALL or EXECUTE SELECT INSERT UPDATE DELETE | java.sql.Statement.execute(String sql):boolean |

The simplest solution is to map all SQL statements to the java.sql.Statement.execute(String sql):boolean method. By default, the Subscriber channel uses this method.

Some third-party drivers, particularly Oracle’s JDBC drivers, incorrectly implement the methods used to determine the number of result sets that this method generates. Consequently, the driver can get caught in an infinite loop leading to high CPU utilization. To circumvent this problem, you can use the jdbc:type attribute on any <jdbc:statement> element to map the SQL statements contained in it to the following methods instead of the default method:

* java.sql.Statement.executeQuery(String query):java.sql.ResultSet
* java.sql.Statement.executeUpdate(String update):int

The jdbc:type attribute has two values: update and query. For INSERT, UPDATE, or DELETE statements, set the value to update. For SELECT statements, set the value to query. In the absence of this attribute, the driver maps all SQL statements to the default method. If placed on any element other than <jdbc:statement>, this attribute is ignored.

Recommendations:

* Place the jdbc:type="query" attribute value on all SELECT statements.
* Place the jdbc:type="update" attribute value on all INSERT, UPDATE, and DELETE statements.
* Place no attribute value on stored procedure/function calls.

The following XML shows an example of the jdbc:type attribute. The attribute is in bold text.

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <add class-name="usr">
        <add-attr name="lname">
            <value>Doe</value>
        </add-attr>
    </add>
    <jdbc:statement jdbc:type="update">
        <jdbc:sql>UPDATE indirect.usr SET fname = 'John'
                  WHERE idu = {$idu}</jdbc:sql>
    </jdbc:statement>
</input>
```
