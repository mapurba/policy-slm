# 3.4 Parameters for Searching and Replacing

The Association utility requires two parameters (oldRDN and newRDN) for operations 6 and 7 in order to search and replace.

The first value (for example, schema) in the parameter is the search criterion. The second value (for example, old) is the replacement value. Under certain scenarios, you can use the wildcard character \* to generalize the search criterion or replacement value.

Three types of search and replace operations are possible:

*Table 3-3* Search and Replace Operations

| Option | Description | Example |
| Replace the schema name | Replace schema old with schema new. Wildcards are supported on the right side only. | oldRDN: schema=old newRDN: schema=new |
| Replace the table name | Replace table old with table new. Wildcards are not supported. | oldRDN: table=old newRDN: table=new |
| Replace the column name | Replace column old with column new. Wildcards are required on the right side, but they aren’t supported on the left side. | oldRDN: old=\* newRDN: new=\* |
