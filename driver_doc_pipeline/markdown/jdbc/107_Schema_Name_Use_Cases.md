# C.2 Schema Name Use Cases

In the Schema Name under schema-aware mode the driver qualifies the tables according to the following rules:

* Every table that contains a primary key constraint is considered as an object class. For example, the following usr table created by the SQL code is considered as an object class by the driver shim if the Schema Name is set to indirect.

  ```
  CREATE TABLE indirect.usr
  (
    idu         INTEGER  NOT NULL,
    fname       VARCHAR2(64),
    lname       CHAR(64),
    CONSTRAINT pk_usr_idu     PRIMARY KEY (idu),
  )
  ```

  The above table will contain two single-valued attributes; fname and lname. The driver will build its associations based on the value of the column referenced in the primary key constraint, which in this case is column idu.
* Every table that only has a Foreign Key constraint is considered as a multi-valued attribute of the class that holds the primary key pointed by the said foreign key constraint. In the following example, if the driver parameter, Schema Name is set to indirect, then the usr\_phone.phoneno table is considered a multi-valued attribute belonging to the class usr.

  *NOTE:*The child table usr\_phone only has a foreign key constraint to the parent table usr. The table usr is considered an object class since it has a primary key constraint.

  ```
  CREATE TABLE indirect.usr
  (
    idu         INTEGER  NOT NULL,
    fname       VARCHAR2(64),
    lname       CHAR(64),
    CONSTRAINT pk_usr_idu     PRIMARY KEY (idu),
  )
  CREATE TABLE indirect.usr_phone
  (
    idu      INTEGER       NOT NULL,
    phoneno  VARCHAR2(64)  NOT NULL,
    CONSTRAINT fk_phone_idu FOREIGN KEY (idu)
      REFERENCES indirect.usr(idu) ON DELETE CASCADE
  )
  ```

  DN-type references between the two objects will have different requirements based on whether the reference points back to the same object class or to a different object class. DN-type references also change depending on whether the DN attribute is single valued or multi-valued.
* If the attribute is single-valued and points back to the same object class, then the table that contains that class will have a foreign key constraint to itself and uses a local column to store the value. An example is the manager attribute in eDirectory. In the example below, if the driver parameter Schema Name is set to indirect, then the attribute manager will be a DN-type attribute that points to another row inside the usr table.

  ```
  CREATE TABLE indirect.usr
  (
    idu         INTEGER  NOT NULL,
    fname       VARCHAR2(64),
    lname       CHAR(64),
    manager     INTEGER,
    CONSTRAINT pk_usr_idu     PRIMARY KEY (idu),
    CONSTRAINT fk_usr_manager FOREIGN KEY (manager)
      REFERENCES indirect.usr(idu) ON DELETE SET NULL
  )
  ```
* If the attribute is multi-valued and points back to the same object class, then we need a child table with columns, each having its own foreign key constraint to the same parent table. An example is the directReports attribute in eDirectory. In the following example, if the driver parameter Schema Name is set to indirect, then the attribute usr\_directReports.repname will be a DN-type attribute that points to one or more rows inside the usr table.

  ```
  CREATE TABLE indirect.usr
  (
    idu         INTEGER  NOT NULL,
    fname       VARCHAR2(64),
    lname       CHAR(64),
    CONSTRAINT pk_usr_idu     PRIMARY KEY (idu),
  )
  CREATE TABLE indirect.usr_directReports
  (
    idu      INTEGER       NOT NULL,
    repname  VARCHAR2(64)  NOT NULL,
    CONSTRAINT fk_directReports_idu FOREIGN KEY (idu)
      REFERENCES indirect.usr(idu) ON DELETE CASCADE,
    CONSTRAINT fk_directReports_repname FOREIGN KEY (idu)
      REFERENCES indirect.usr(idu) ON DELETE CASCADE
  )
  ```
* If the attribute is single-valued and points to a different object class, then the table that contains that class will have a foreign key constraint to the table for the other object class, and a local column to store that value. An example is the Host Server attribute in eDirectory. In the following example, if the driver parameter Schema Name is set to indirect, then the attribute hostsrv will be a DN-type attribute that points to a row inside the server table. In this example, both the volume table and the server table represent object classes.

  ```
  CREATE TABLE indirect.volume
  (
    idv         INTEGER  NOT NULL,
    vname       VARCHAR2(64),
    hostsrv     INTEGER,
    CONSTRAINT pk_volume_idv     PRIMARY KEY (idv),
    CONSTRAINT fk_volume_hostsrv FOREIGN KEY (ids)
      REFERENCES indirect.server(ids) ON DELETE SET NULL
  )
  CREATE TABLE indirect.server
  (
    ids         INTEGER  NOT NULL,
    srvname     VARCHAR2(64),
    CONSTRAINT pk_server_ids PRIMARY KEY (ids)
  )
  ```
* If the attribute is multi-valued and points to a different object class, then we need a child table with two columns, each having a foreign key constraint to a different parent table. An example is the Group Membership attribute in eDirectory. In the following example, if the driver parameter Schema Name is set to indirect, then the attribute usr\_mbr\_of.idu will be a DN-type attribute that points to a row inside the grp table. In this example, both the usr table and the grp table represent object classes.

  ```
  CREATE TABLE indirect.usr
  (
    idu         INTEGER  NOT NULL,
    fname       VARCHAR2(64),
    lname       CHAR(64),
    CONSTRAINT pk_usr_idu     PRIMARY KEY (idu),
  )
  CREATE TABLE indirect.grp
  (
    idg         INTEGER  NOT NULL,
    for_insert  INTEGER,
    CONSTRAINT pk_grp_idg PRIMARY KEY (idg)
  )
  CREATE TABLE indirect.usr_mbr_of
  (
    idu  INTEGER  NOT NULL,
    idg  INTEGER  NOT NULL,
    CONSTRAINT fk_mbr_of_idu FOREIGN KEY (idu)
      REFERENCES indirect.usr(idu) ON DELETE CASCADE,
    CONSTRAINT fk_mbr_of_idg FOREIGN KEY (idg)
      REFERENCES indirect.grp(idg) ON DELETE CASCADE
  )
  ```

Security/Performance:

* For performance and security reasons, run the driver remotely on the database server whenever possible. Be sure to enable SSL encryption between the Identity Vault and the Remote Loader service.
* You should enable SSL encryption for third-party drivers whenever the JDBC driver is not running remotely on the database server. For information on the security capabilities of supported third-party drivers, see [Section 14.0, Third-Party JDBC Drivers](third-party-jdbc-drivers.html).
* In a production environment, turn off tracing.

Other:

* For direct synchronization, prefix one or more view column names with “pk\_” (case-insensitive).
* For both direct and indirect synchronization, use different primary key column names between logical database classes.
* Delimit (double-quote) primary key values placed in the event log table\_key field if they contain the following characters: , ; ' + = \ " < > This caution is usually an issue only if the primary key column is a binary type.
* When an Identity Vault is the authoritative source of primary key values, GUID rather than CN is recommended for use as a primary key. Unlike CN, GUID is single-valued and does not change.
* From publication triggers, omit foreign key columns that link child and parent tables.
* If primary key columns are static (they do not change), do not include them in publication triggers.
* Place the jdbc:type="query" attribute value on all embedded SELECT statements. Place the jdbc:type="update" attribute value on all embedded INSERT, UPDATE and DELETE statements.
* To avoid issues that arise when you run a sql query that has a reserved word as a column name, specify a fully qualified name for the column.

  For example, when you use group as a column name under usr table, group being is a sql keyword, your query might not be properly executed. To avoid this, specify a fully qualified name such as usr.group (<Tablename>.<Columnname>) for the column.
* By design, the driver doesn't allow primary keys on child tables in the Synch Schema mode. To comply with standard database best practices, if you add a primary key on all tables including the child tables containing multi-valued attributes, the driver doesn't work properly in this mode. You must operate the driver in the Synch Tables/Views mode to allow primary keys on child tables. The Synch Tables/Views mode prevents the driver from adding the child tables to the list of synchronized tables.
