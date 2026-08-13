# 8.2 The DirXML-DriverStorage Attribute Does Not Change With the Latest Polling Interval

The Salesforce.com doesn’t frequently change the timestamp. It keeps sending the same timestamp for some time, so the new values are not updated in the DirXML-DriverStorage attribute of the Identity Manager engine. This causes the previous updates to keep replaying for some time. However, it doesn't cause any loss of events.
