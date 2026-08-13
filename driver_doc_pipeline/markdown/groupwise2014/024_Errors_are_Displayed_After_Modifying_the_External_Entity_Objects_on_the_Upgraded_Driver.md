# 8.2 Errors are Displayed After Modifying the External Entity Objects on the Upgraded Driver

The user object contains the DirXML-Accounts attribute in the Identity Vault. This attribute is not applicable for the External Entity objects. An External Entity object is represented as User {106} in GroupWise. When the modify association event is triggered for the External Entity object on the upgraded driver, the account tracking policy tries to update the account tracking attribute and results in error.

It is safe to ignore the error because it does not cause any functionality loss.
