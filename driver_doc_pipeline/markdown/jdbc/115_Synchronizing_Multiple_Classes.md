# D.7 Synchronizing Multiple Classes

*Question:*
Can the driver synchronize multiple classes?

*Answer:*
Yes. However, primary key column names must be unique between logical database classes. For example, if class1 is mapped to table1 with primary key column name key1, and class2 is mapped to table2 with primary key column name key2, then the name of key1 cannot equal key2.

This requirement can always be satisfied, no matter which synchronization model is employed.
