# 2.2 Migration Planning

Since identities will be synchronized between the Vault and ACF2, you will need to consider the following:

* Where will these identities be located and managed in the Vault?
* Can you use the default Matching policy to associate Logonid LID fields with the Vault CN attribute, or will you need to base matching on other properties?
* How will you handle existing Vault IDs that do not meet the requirements for ACF2?

You will also need to decide whether to use the migration tool provided with Identity Manager or a more manual process for importing your data.
