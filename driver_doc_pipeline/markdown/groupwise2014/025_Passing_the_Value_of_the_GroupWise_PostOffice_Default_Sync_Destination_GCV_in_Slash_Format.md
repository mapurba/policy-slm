# 8.3 Passing the Value of the GroupWise PostOffice Default Sync Destination GCV in Slash Format

After the driver upgrade, if you see the following trace message when a user is added, verify that the value of the Default Sync Destination: GroupWise PostOffice is in dot format:

```
DirXML Log Event -------------------

    Driver  = \GW12-LNX86\system\driverset1\GroupWise-Jun10_2014

    Thread  = Subscriber

    Object  = \GW12-LNX86\data\users\user (DOMAIN\PO1)

    Level   = error

    Message = <code>java.lang.IllegalArgumentException: Placement Rule Destination string DOMAIN\PO1 was not found</code>
```
