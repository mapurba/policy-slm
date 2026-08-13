# 12.13 Implementing Check Object Password

Unlike password set, check object password does not require embedded SQL statements or attributes. Only a user account name is required. This could be obtained from an association value (assuming that associations are being maintained manually), a directory attribute, or a database field. If stored in the directory or database, a query must be issued to retrieve the value.

The example .xml configuration file stores database user account names in database fields.

*NOTE:*Some databases, such as Sybase Adpative Server Enterprise and Microsoft SQL Server, differentiate between user account names and login account names. Therefore, you might need to store two names, not just one.

To implement check object password, append a dest-dn attribute value to the <check-object-password> event. In the following example, the dest-dn attribute is bolded:

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <check-object-password dest-dn="jdoe">
        <password>whatever</password>
    </check-object-password>
</input>
```
