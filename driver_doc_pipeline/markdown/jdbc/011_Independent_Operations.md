# 3.1 Independent Operations

The Association utility supports seven independent operations:

*Table 3-1* Independent Operations

| Operation | Description | Read-Write Functionality |
| 1 | Lists objects associated with a driver (default). | Read-only |
| 2 | Lists objects that have multiple associations to a driver. | Read-only |
| 3 | Lists objects that have invalid associations to a driver.  An association is invalid if:  * It is malformed.  For example, the association is missing the schema RDN, missing the table RDN, or the schema keyword is misspelled. * It contains database identifiers that do not map to identifiers in the target database.  For example, an association includes a mapping to a table that does not exist. * It maps to no row or multiple rows.  An association is broken if it doesn’t map to a row. Also, associations aren’t unique if they map to more than one row. | Read-only |
| 4 | Lists objects that need to be normalized.  A normalized association is valid, correctly ordered, and uses the correct case. Normal case is uppercase for case-insensitive databases and mixed case for case-sensitive databases. | Read-only |
| 5 | Normalizes object associations listed during operation 4. | Write |
| 6 | Lists object associations to be modified.  Allows for global replacement of schema, table, and column names based on search criteria.  This operation requires two parameters (oldRDN and newRDN). See [Parameters for Searching and Replacing](parameters-used-in-association-utility-for-searching-and-replacing-operations.html). | Read-only |
| 7 | Modifies object associations listed during operation 6.  This operation requires two parameters (oldRDN and newRDN). See [Parameters for Searching and Replacing](parameters-used-in-association-utility-for-searching-and-replacing-operations.html). | Write |
