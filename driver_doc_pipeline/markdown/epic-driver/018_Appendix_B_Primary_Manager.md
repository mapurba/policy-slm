# B.0 Appendix B - Primary Manager

There are certain conditions that must be met for a user to be assigned as a manager. These conditions are listed below:

* The Epic manager record’s ID must be present in the Users Managers List.
* The target Epic manager must have an InBasketClassification with "In Basket" security point "14-Manage Clinic" or "16-Trusted Manager".
* If the value of the user’s manager attribute has an association ref (dn reference) the association value is used, otherwise the value is used.

  <value association-ref="113" timestamp="1530022566#6" type="dn">\IDV47\_TREE\data\users\Tester2</value>

  or

  <value timestamp="1530022566#6" type="dn">FAMMD</value>

  *NOTE:*The value used must match the Epic ID of the target Epic manager.
