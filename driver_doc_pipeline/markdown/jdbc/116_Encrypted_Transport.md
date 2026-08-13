# D.8 Encrypted Transport

*Question:*
Does the driver support encrypted transport?

*Answer:*
No. How the driver communicates with a given database depends upon the third-party driver being used. Some third-party drivers support encrypted transport, but others do not. Even if encrypted transport is supported, no standardized way exists to enable encryption between third-party JDBC drivers.

The general solution for this problem is to remotely run the JDBC driver and your third-party driver. This method allows both the JDBC driver and the third-party driver to run locally on the database server. Then all data traveling across the network between the Identity Manager engine and the JDBC driver are SSL encrypted.

Another possibility is to use a type 3 or type 2 third-party JDBC driver. Database middleware and client APIs usually provide encrypted transport mechanisms.
