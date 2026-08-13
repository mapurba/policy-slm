# 9.4 Direct Synchronization

In a direct synchronization model, the driver maps the following:

*Table 9-4* Mappings in Direct Synchronization

| Identity Vault Object | Database Object |
| Classes | Views |
| Attributes | View Columns |
| Class | View |
| Single-value attribute | View Column |
| Multivalue attribute | View Column |

The update capabilities of views vary between databases. Most databases allow views to be updated when they are comprised of a single base table. (That is, they do not join multiple tables.) If views are read-only, they cannot be used for subscription. Some databases allow update logic to be defined on views in instead-of-triggers, which allow a view to join multiple base tables and still be updateable.

For a list of databases that support instead-of-triggers, see [Database Features](characteristics-of-databases.html#bvowloe). Instead-of-trigger logic can be simulated, regardless of database capability using embedded SQL. See [Virtual Triggers](set-virtual-triggers-for-jdbc-drivers.html).

* [View Column Meta-Identifiers](direct-synchronization.html#b87s0bc)
* [Primary Key Columns](direct-synchronization.html#b87s0bs)
* [Schema Mapping](direct-synchronization.html#b87s0bt)

## 9.4.1 View Column Meta-Identifiers

A view is a logical table. Unlike tables, views do not physically exist in the database. As such, views usually cannot have traditional primary key/foreign key constraints. To simulate these constructs, the JDBC driver embeds constraints and other metadata in view column names. The difference between these constraints and traditional ones is that the former are not enforced at the database level. They are an application-level construct.

For example, to identify to the driver which fields to use when constructing association values, place a primary key constraint on a parent table. The corollary to this for a view is to prefix one or more column names with pk\_ (case-insensitive).

The following table lists the constraint prefixes that can be embedded in view column names.

*Table 9-5* Constraint Prefixes

| Constraint Prefixes (case-insensitive) | Interpretation |
| pk\_ | primary key |
| fk\_ | foreign key |
| sv\_ | single-value |
| mv\_ | multivalue |

The following example views contain all of these constraint prefixes. These are examples and not the actual samples. Therefore, they should not be used in the driver implementation. The real samples are bundled with the Identity Manager media.

```
CREATE VIEW direct.view_usr
(
    pk_idu,            -- primary key column; implicitly single-valued
    sv_fname,          -- single-valued column
    mv_phoneno,        -- multi-valued column
    fk__idu__manager,  -- self-referential foreign key column; refers
                       --   to primary key column idu in view_usr;
                       --   implicitly single-valued
    fk_mv__idg__mbr_of -- extra-referential foreign key column; refers
                       --   to primary key column idg in view_grp;
                       --   multi-valued
)
AS
-- ...
```

```
CREATE VIEW direct.view_grp
(
    pk_idg,            -- primary key column; implicitly single-valued
    fk_mv__idu__mbr    -- extra-referential foreign key column; refers
                       --   to primary key column idu in view_usr;
                       --   multi-valued
)
AS
-- ...
```

#### BNF

The BNF (Backus Naur Form) notation for view column meta-identifiers:

```
<view-column-name> ::= [<meta-info>] <column-name>

<column-name> ::= <legal-unquoted-database-identifier>
<meta-info> ::= <referential> | <non-referential>

<non-referential> ::= [<single-value> | <multiple-value>]

<single-value> ::= "sv_"

<multiple-value> ::= "mv_"

<referential> ::= <primary-key> | <foreign-key>

<primary-key> ::= "pk_" [<single-value>] [<column-group-id>]
                  [<referenced-column-name>]
```

```
<column-group-id> ::= <non-negative-integer> "_"

<referenced-column-name> ::= "_" <column-name> "__"

<foreign-key> ::= "fk_" [<non-referential>] [<column-group-id>]
                  <referenced-column-name>
```

#### Normalized Forms

By default, all view column names are single-valued. Therefore, explicitly specifying the sv\_ prefix in a view column name is redundant. For example, sv\_fname and fname are equivalent forms of the same column name.

Also, primary key column names implicitly refer to themselves. Therefore, it is redundant to specify the referenced column name. For example, pk\_idu is equivalent to pk\_\_idu\_\_idu.

The JDBC driver uses two normalized forms of view meta-identifiers:

* Database native form

  Database native form is the column name as declared in the database. This form is usually much more verbose than schema mapping form, and contains all necessary meta information.
* Schema mapping form

  Schema mapping form is returned when the driver returns the application schema. This form is much more concise than database native form because much of the meta information included in database native form is represented in XDS XML and not in the identifier.

  The referential prefixes pk\_ and fk\_ are the only meta information preserved in schema mapping form. This limitation ensures backward compatibility.

The following table provides examples of each form:

*Table 9-6* Example Normalized Forms of View Meta-Identifiers

| Database Native Form | Schema Mapping Form |
| pk\_idu | pk\_idu |
| sv\_fname | fname |
| mv\_phoneno | phoneno |
| fk\_mv\_\_idg\_\_mbr\_of | fk\_mbr\_of |

#### Equivalent Forms

A view column name without meta information is called its “effective” name, which is similar to a directory object’s “effective” rights. For the driver, view column name equivalency is determined without respect to meta information by default. For example, pk\_idu is equivalent to idu, and fk\_mv\_\_idg\_\_mbr\_of is equivalent to mbr\_of. Any variant form of a view meta column identifier can be passed to the driver at runtime. For backward compatibility reasons, meta information can be treated as part of the effective view column name. See [Enable Meta-Identifier Support?](configure-jdbc-driver-specific-parameters.html#b1pu3ni).

## 9.4.2 Primary Key Columns

Primary key column names must be unique among all views in the synchronization schema.

## 9.4.3 Schema Mapping

Schema mapping conventions for views and view columns are equivalent to that used for parent tables and parent table columns.
