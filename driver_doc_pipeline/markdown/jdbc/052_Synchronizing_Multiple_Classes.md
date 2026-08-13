# 9.6 Synchronizing Multiple Classes

When synchronizing multiple eDirectory classes, synchronize each class to a different parent table or view. Each logical database class must have a unique primary key column name. The Publisher channel uses this common column name to identify all rows in the event log table pertaining to a single logical database class. For example, both the logical database classes usr and grp have a unique primary key column name.

```
CREATE TABLE usr
(
    idu   INTEGER         NOT NULL,
    lname VARCHAR2(64)  NOT NULL,
    --...
    CONSTRAINT pk_usr_idu PRIMARY KEY(idu)
);
```

```
CREATE TABLE grp
(
    idg  INTEGER  NOT NULL,
    --...
    CONSTRAINT pk_grp_idg PRIMARY KEY(idg)
);
```
