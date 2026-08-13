# 9.3 Indirect Synchronization

In an indirect synchronization model, the driver maps the following:

*Table 9-2* Mappings in Indirect Synchronization

| Identity Vault Object | Database Object |
| Classes | Tables |
| Attributes | Columns |
| 1 Class | 1 parent table  and  0 or more child tables |
| Single-value attribute | Parent table column |
| Multivalue attribute | Parent table column (holding delimited values)  or  Child table column (preferred) |

* [Mapping eDirectory Classes to Logical Database Classes](indirect-synchronization.html#b87s0ar)
* [Parent Tables](indirect-synchronization.html#b87s0as)
* [Parent Table Columns](indirect-synchronization.html#b87s0av)
* [Child Tables](indirect-synchronization.html#b87s0aw)
* [Referential Attributes](indirect-synchronization.html#b87s0b1)
* [Single-Value Referential Attributes](indirect-synchronization.html#b87s0b2)
* [Multivalue Referential Attributes](indirect-synchronization.html#b87s0b3)

## 9.3.1 Mapping eDirectory Classes to Logical Database Classes

In the following example, the logical database class usr consists of the following:

* One parent table usr
* Two child tables: usr\_phone and usr\_faxno.

Logical class usr is mapped to the eDirectory class User.

```
CREATE TABLE indirect.usr
(
    idu         INTEGER  NOT NULL,
    fname       VARCHAR2(64),
    lname       CHAR(64),
    pwdminlen   NUMBER(4),
    pwdexptime  DATE,
    disabled    NUMBER(1),
    username    VARCHAR2(64),
    loginame    VARCHAR2(64),
    photo       LONG RAW,
    manager     INTEGER,
    CONSTRAINT pk_usr_idu     PRIMARY KEY (idu),
    CONSTRAINT fk_usr_manager FOREIGN KEY (manager)
        REFERENCES indirect.usr(idu)
)
```

```
CREATE TABLE indirect.usr_phone
(
    idu      INTEGER       NOT NULL,
    phoneno  VARCHAR2(64)  NOT NULL,
    CONSTRAINT fk_phone_idu FOREIGN KEY (idu)
        REFERENCES indirect.usr(idu)
)
```

```
CREATE TABLE indirect.usr_fax
(
    idu    INTEGER       NOT NULL,
    faxno  VARCHAR2(64)  NOT NULL,
    CONSTRAINT fk_fax_idu FOREIGN KEY (idu)
        REFERENCES indirect.usr(idu)
)
```

```
<rule name="Schema Mapping Rule">
    <attr-name-map>
        <class-name>
            <nds-name>User</nds-name>
            <app-name>indirect.usr</app-name>
        </class-name>
        <attr-name class-name="User">
            <nds-name>Given Name</nds-name>
            <app-name>fname</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>Surname</nds-name>
            <app-name>lname</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>Password Expiration Time</nds-name>
            <app-name>pwdexptime</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>jpegPhoto</nds-name>
            <app-name>photo</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>manager</nds-name>
            <app-name>manager</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>Password Minimum Length</nds-name>
            <app-name>pwdminlen</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>Facsimile Telephone Number</nds-name>
            <app-name>usr_fax.faxno</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>Telephone Number</nds-name>
            <app-name>usr_phone.phoneno</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>Login Disabled</nds-name>
            <app-name>disabled</app-name>
        </attr-name>
    </attr-name-map>
</rule>
```

## 9.3.2 Parent Tables

Parent tables are tables with an explicit primary key constraint that contains one or more columns. In a parent table, an explicit primary key constraint is required so that the driver knows which fields to include in an association value.

```
CREATE TABLE indirect.usr
(
    idu  INTEGER  NOT NULL,
    -- ...
    CONSTRAINT pk_usr_idu PRIMARY KEY (idu)
)
```

The following table contains sample data for table indirect.usr.

| idu | fname | lname |
| 1 | John | Doe |

The resulting association for this row is

idu=1,table=usr,schema=indirect

The case of database identifiers in association values is determined dynamically from database metadata at runtime.

## 9.3.3 Parent Table Columns

Parent table columns can contain only one value. As such, they are ideal for mapping single-value eDirectory attributes, such as mapping the single-value eDirectory attribute Password Minimum Length to the single-value parent table column pwdminlen.

Parent table columns are implicitly prefixed with the schema name and name of the parent table. It is not necessary to explicitly table-prefix parent table columns. For example, indirect.usr.fname is equivalent to fname for schema mapping purposes.

```
<rule name="Schema Mapping Rule">
    <attr-name-map>
        <class-name>
            <nds-name>User</nds-name>
            <app-name>indirect.usr</app-name>
        </class-name>
        <attr-name class-name="User">
            <nds-name>Given Name</nds-name>
            <app-name>fname</app-name>
        </attr-name>
    </attr-name-map>
</rule>
```

Large binary and string data types should usually be mapped to parent table columns. To map to a child table column, data types must be comparable in SQL statements. Large data types usually cannot be compared in SQL statements.

Large binary and string data types can be mapped to child table columns if the following occur:

* Each <remove-value> event on these types is transformed in a policy into a <remove-all-values>element
* An <add-value> element follows each <remove-value> event

## 9.3.4 Child Tables

A child table is a table that has a foreign key constraint on its parent table’s primary key, linking the two tables together. The columns that comprise the child table’s foreign key can have different names than the columns in the parent table’s primary key.

The following example shows the relationship between parent table usr and child tables usr\_phone and usr\_faxno:

```
CREATE TABLE indirect.usr
(
    idu  INTEGER  NOT NULL,
    -- ...
    CONSTRAINT pk_usr_idu  PRIMARY KEY (idu)
)
```

```
CREATE TABLE indirect.usr_phone
(
    idu      INTEGER       NOT NULL,
    phoneno  VARCHAR2(64)  NOT NULL,
    CONSTRAINT fk_phone_idu FOREIGN KEY (idu)         REFERENCES indirect.usr(idu)
)
```

```
CREATE TABLE indirect.usr_fax
(
    idu    INTEGER       NOT NULL,
    faxno  VARCHAR2(64)  NOT NULL,
    CONSTRAINT fk_fax_idu FOREIGN KEY (idu)         REFERENCES indirect.usr(idu)
)
```

In a child table, constrain all columns NOT NULL.

The first constrained column in a child table identifies the parent table. In the above example, the constrained column in child table usr\_phone is idu. The only purpose of this column is to relate tables usr\_phone and usr. Because constrained columns do not contain any useful information, omit them from publication triggers and Schema Mapping policies.

The unconstrained column is the column of interest. It represents a single, multivalue attribute. In the above example, the unconstrained columns are phoneno and faxno. Because unconstrained columns can hold multiple values, they are ideal for mapping multivalue eDirectory attributes (for example, mapping the multivalue eDirectory attribute Telephone Number to usrphone.phoneno).

The following table contains sample data for indirect.usr\_phone.

*Table 9-3* Sample Data

| idu | phoneno |
| 1 | 111-1111 |
| 1 | 222-2222 |

Like parent table columns, child table columns are implicitly schema-prefixed. Unlike parent table columns, however, a child table column name must be explicitly prefixed with the child table name (for example, usr\_phone.phoneno). Otherwise, the driver implicitly interprets column phoneno (the parent table column) as usr.phoneno, not the child table column usr\_phone.phoneno.

```
<rule name="Schema Mapping Rule">
    <attr-name-map>
        <class-name>
            <nds-name>User</nds-name>
            <app-name>indirect.usr</app-name>
        </class-name>
        <attr-name class-name="User">
            <nds-name>Facsimile Telephone Number</nds-name>
            <app-name>usr_fax.faxno</app-name>
        </attr-name>
        <attr-name class-name="User">
            <nds-name>Telephone Number</nds-name>
            <app-name>usr_phone.phoneno</app-name>
        </attr-name>
      </attr-name-map>
</rule>
```

Map each multivalue eDirectory attribute to a different child table.

## 9.3.5 Referential Attributes

You can represent referential containment in the database by using foreign key constraints. Referential attributes are columns within a logical database class that refer to the primary key columns of parent tables in the same logical database class or those of other logical database classes.

## 9.3.6 Single-Value Referential Attributes

You can relate two parent tables through a single-value parent table column. This column must have a foreign key constraint pointing to the other parent table’s primary key. The following example relates a single parent table usr to itself:

```
CREATE TABLE indirect.usr
(
    idu      INTEGER  NOT NULL,
    -- ...
    manager  INTEGER,
    CONSTRAINT pk_usr_idu     PRIMARY KEY (idu),
    CONSTRAINT fk_usr_manager FOREIGN KEY (manager)         REFERENCES indirect.usr(idu)
)
```

*NOTE:*Single-valued referential columns should be nullable.

```
<rule name="Schema Mapping Rule">
    <attr-name-map>
        <class-name>
            <nds-name>User</nds-name>
            <app-name>indirect.usr</app-name>
        </class-name>
        <attr-name class-name="User">
            <nds-name>manager</nds-name>
            <app-name>manager</app-name>
        </attr-name>
    </attr-name-map>
</rule>
```

In the above example, each user can have only one manager who himself is a user.

## 9.3.7 Multivalue Referential Attributes

You can relate two parent tables through a common child table. This child table must have a column constrained by a foreign key pointing to the other parent table’s primary key. The following example relates two parent tables usr and grp through a common child table member.

```
CREATE TABLE indirect.usr
(
    idu  INTEGER  NOT NULL,
    -- ...
    CONSTRAINT pk_usr_idu PRIMARY KEY (idu)
)
```

```
CREATE TABLE indirect.grp
(
    idg  INTEGER  NOT NULL,
    -- ...
    CONSTRAINT pk_grp_idg PRIMARY KEY (idg)
)
```

```
CREATE TABLE indirect.grp_member
(
    idg  INTEGER  NOT NULL,
    idu  INTEGER  NOT NULL,
    CONSTRAINT fk_member_idg FOREIGN KEY (idg)      REFERENCES indirect.grp(idg),    CONSTRAINT fk_member_idu FOREIGN KEY (idu)      REFERENCES indirect.usr(idu)
)
```

Constrain all columns in a child table NOT NULL.

```
<rule name="Schema Mapping Rule">
    <attr-name-map>
        <class-name>
             <nds-name>Group</nds-name>
             <app-name>indirect.grp</app-name>
        </class-name>
        <class-name>
            <nds-name>User</nds-name>
            <app-name>indirect.usr</app-name>
        </class-name>
        <attr-name class-name="Group">
            <nds-name>Member</nds-name>
            <app-name>grp_member.idu</app-name>
        </attr-name>
    </attr-name-map>
</rule>
```

The first constrained column in a child table determines which logical database class the child table grp\_member belongs to. In the above example, grp\_member is considered to be part of logical database class grp. grp\_member is said to be a proper child of grp. The second constrained column in a child table is the multivalue referential attribute.

In the following example, the order of the constrained columns has been reversed so that grp\_member is part of class usr. To more accurately reflect the relationship, table grp\_member has been renamed to usr\_mbr\_of.

```
CREATE TABLE indirect.usr
(
    idu  INTEGER  NOT NULL,
    -- ...
    CONSTRAINT pk_usr_idu PRIMARY KEY (idu)
)
```

```
CREATE TABLE indirect.grp
(
    idg  INTEGER  NOT NULL,
    -- ...
    CONSTRAINT pk_grp_idg PRIMARY KEY (idg)
)
```

```
CREATE TABLE indirect.usr_mbr_of
(
    idu  INTEGER  NOT NULL,
    idg  INTEGER  NOT NULL,
    CONSTRAINT fk_mbr_of_idu FOREIGN KEY (idu)         REFERENCES indirect.usr(idu) ON DELETE CASCADE,
    CONSTRAINT fk_mbr_of_idg FOREIGN KEY (idg)
        REFERENCES indirect.grp(idg) ON DELETE CASCADE
)
```

```
<rule name="Schema Mapping Rule">
    <attr-name-map>
        <class-name>
             <nds-name>Group</nds-name>
             <app-name>indirect.grp</app-name>
        </class-name>
        <class-name>
            <nds-name>User</nds-name>
            <app-name>indirect.usr</app-name>
        </class-name>
        <attr-name class-name="User">
            <nds-name>Group Membership</nds-name>
            <app-name>usr_mbr_of.idg</app-name>
        </attr-name>
    </attr-name-map>
</rule>
```

In databases that have no awareness of column position (such as DB2/AS400), order is determined by sorting column names by string or hexadecimal value. For additional information, see [Sort Column Names By](configure-jdbc-driver-specific-parameters.html#b1pu3oi).

In general, it is necessary to synchronize only bidirectional, multivalue, referential attributes as part of one class or the other, not both. If you want to synchronize referential attributes for both classes, construct two child tables, one for each class. For example, if you want to synchronize eDirectory attributes Group Membership and Member, you need two child tables.

In practice, when you synchronize User and Group classes, we recommend that you synchronize the Group Membership attribute of class User instead of the Member attribute of class Group. Synchronizing the group memberships of a user is usually more efficient than synchronizing all members of a group.
