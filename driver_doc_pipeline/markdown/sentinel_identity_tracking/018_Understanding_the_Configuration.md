# 6.1 Understanding the Configuration

You need to implement the driver by using two Designer packages: Sentinel REST API BASE and Sentinel Identity Tracking. When you import these packages, they create a driver with a set of rules and policies suitable for synchronizing identities and their associated account information with Sentinel. If your requirements for the driver are different from the default policies, you need to change them to effect the policies you want. Pay close attention to the default matching policies. The data that you trust to match users usually is different from the default. The policies themselves are commented and you can gain a greater understanding of what they do by creating a test driver and reviewing the policies with Designer.

When Identity Manager determines that a Sentinel Identity must be created from an Identity Vault User object, the driver first checks the existing Sentinel Identity objects to determine if it should use an existing Identity object should be used. The need for this arises when you install or reinstall the driver into a system that has previously tracked identity information, or when resynchronizing identity data for any purpose.

The driver performs the searches in the following order:

* *Match by Distinguished Name:*
  The DN and source Identity Vault name of the originating Identity Vault User object are stored as part of the Sentinel Identity object. The first search attempts to find an existing Sentinel Identity object with the same Identity Vault name and DN as the originating Identity Vault User object.
* *Match by GUID:*
  The driver stores the GUID value of the originating Identity Vault User object in the Sentinel Identity object Source Identity Id field. The second search attempts to find a Sentinel Identity object with a Source Identity Id value that matches the Identity Vault User object GUID value.
* *Match by User Attribute Values:*
  For information on matching attributes, see, [Step 7](creating-the-driver.html#bzpvbnb1).
