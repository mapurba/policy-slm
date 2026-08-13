# 3.7 Use GÂ Suite Custom Schema

The GÂ Suite Directory API provides the ability to extend the schema of a UserEntry object through the use of Google Custom Schema. Customers can create multiple custom schemas, each of which can define multiple custom attributes. These fields can be used to hold attribute data. Adding Custom Schema effectively extends the application schema managed by the driver. When the driver is asked to refresh application schema from Designer or iManager, the driver queries all of the Custom Schema objects, and adds all of the attributes to the application schema. Once the driver has returned the new schema attributes, the attributes are available to be included in the filter, schema mapped, and used in the Policy Builder. Google Custom Schema attribute definitions carry metadata to indicate whether or not the attribute is multi-valued, as well as the datatype of the field. Google supports the following datatypes:

* BOOL
* DATE
* DOUBLE
* EMAIL
* INT64
* PHONE
* STRING
