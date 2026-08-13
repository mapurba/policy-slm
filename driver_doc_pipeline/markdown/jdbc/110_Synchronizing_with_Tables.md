# D.2 Synchronizing with Tables

*Question:*
How do I synchronize with tables located in multiple schemas?

*Answer:*
Do one of the following:

* Alias the tables into the synchronization schema.
* Synchronize to intermediate tables in the synchronization schema and move the data across schema boundaries.
* Use a view.
* Create a virtual schema by using the Table/View Names parameter.

  See [Table/View Names](configure-jdbc-driver-specific-parameters.html#b1pu3kx).
