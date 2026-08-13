# 3.2 Before You Begin

Modifying associations can cause problems. If associations are corrupted, Identity Manager ceases to function. Therefore, use write operations only when necessary. To avoid unintentionally corrupting an association, the Association utility creates an undo ldiff file for all write operations.

Review the following cautions before using the utility:

* The Association utility, like the driver, assumes that database identifiers are undelimited (unquoted and contain no special characters).
* Update all object associations related to a driver at the same time.

  Updating associations at the same time is extremely important.

  To see all of the objects associated with a particular driver, run the Association utility on the Identity Manager server associated with a particular driver instance.

  The LDAP search base must contain all of the objects associated with a particular driver.

  To ensure complete containment, we recommend that you use your tree’s root container as the search base.
* Make sure that the JDBC URL of the target database supplied to this utility is the same as the URL that the driver uses. Pointing this utility at a case-insensitive database when the database is actually case-sensitive might result in associations being normalized to the wrong case.
* Because the Association utility runs locally, it uses an unsecured connection. Therefore, the Identity Vault LDAP server must be temporarily configured to accept clear text passwords. Depending upon the third-party JDBC driver you are using, the database connection established by this utility might not be secure.

  We recommend changing the driver’s authentication password on the database after you run this utility.
