# 3.0 Customizing the Workday Driver

*NOTE:*The resulting XML is the data interpreted between Identity Manager and Workday environment. For the most efficient processing, the external stylesheet must return the attributes only that have a different value or any new attributes. However, it is advised to retain the code that generates association as is, to ensure that the results of the external stylesheet are correctly merged with the results from the internal stylesheet.

Apart from the default attributes available in Identity Manager, you can customize the attributes by modifying the default stylesheet of Workday Driver. As Workday supports multiple attributes, and the business need may not use all the attributes that are supported by Workday, the stylesheet customization provides the flexibility to manage only the attributes that are required for your business environment.

The following sections explain how the attributes can be customized:

* [Customizing the Publisher Channel for Additional Attributes](t4eqyl8053wa.html)
* [Customizing the Subscriber Channel for Additional Attributes](t4eqymkdeu0j.html)
* [Customizing Entitlements](t4finm19niw9.html)
