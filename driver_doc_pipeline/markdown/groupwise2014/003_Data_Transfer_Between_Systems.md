# 1.2 Data Transfer Between Systems

There are two data transfer channels between the Identity Vault and GroupWise: Subscriber channel and Publisher channel. The driver supports communication in one-way only on Subscriber channel.

* *Subscriber Channel:*
  Transfers data and events from the Identity Vault to the GroupWise system.

  The Subscriber channel controls data transfer as follows:

  + It monitors the Identity Vault for new objects and any change to the existing objects.
  + It sends the relevant changes to the driver shim to be executed in the GroupWise system.
* *Publisher Channel:*
  This channel is not supported for the driver. However, the driver automatically synchronizes EMail Address and Internet EMail Address attributes on the channel. A user add event on the Subscriber channel fetches these attributes from the GroupWise system that in turn trigger a Publisher event which synchronizes the attributes to the Identity Vault unless the attributes are not disabled in the driver filter.

*IMPORTANT:*Some Identity Vault attributes contain multiple values for which GroupWise allows only one value. When you modify a multivalued attribute in the Identity Vault, the driver overwrites the value for this attribute in GroupWise. If you delete any value from a multivalued attribute from the Identity Vault, the driver deletes the attribute from GroupWise.
