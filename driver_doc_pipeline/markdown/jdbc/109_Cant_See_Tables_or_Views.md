# D.1 Can’t See Tables or Views

*Question:*
Why can’t the driver see my tables or views?

*Answer:*
The driver is capable of synchronizing only tables that have explicit primary key constraints and views that contain one or more columns prefixed with “pk\_” (case-insensitive). The driver uses these constraints to determine which fields to use when constructing associations. As such, the driver ignores any unconstrained tables. If you are trying to synchronize with tables or views that lack the necessary constraints, either add them or synchronize to intermediate tables with the required constraints.

Another possibility is that the driver lacks the necessary database privileges to see the tables. Usually, visibility is determined by the presence or absence of the SELECT privilege.
