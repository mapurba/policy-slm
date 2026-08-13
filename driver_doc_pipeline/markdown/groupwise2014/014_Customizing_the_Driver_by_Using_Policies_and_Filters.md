# 5.0 Customizing the Driver by Using Policies and Filters

This section explains how to use and modify policies and filters to synchronize data between the Identity Vault and GroupWise according to your specific business rules.

The GroupWise driver synchronizes data and events from the Identity Vault through a series of policies. Policies help Identity Manager make decisions as the documents traverse a channel. A policy might determine that a document needs to be transformed in some way before continuing to the destination. For example, a Create policy specifies that a User object must have a value for the CN attribute, so any attempt to create a User object without a CN value is not allowed by that policy.

The policies in this section are examples of the many possible solutions for your company’s business rules. The code segments show simple and partial solutions and do not cover all situations and conditions. In addition, the code segments only process the attributes of interest and do not handle other attributes.

* [Default Driver Actions](ad8a2vj.html)
* [Modifying Default Settings in Policies and the Filter](modify-default-settings-policies-filter.html)
* [Modifying Policies](modify-policies.html)
* [Setting GroupWise Client Options with the Driver](setting-groupwise-client-options.html)
* [Client Options Quick Reference](b9q9on5.html)
