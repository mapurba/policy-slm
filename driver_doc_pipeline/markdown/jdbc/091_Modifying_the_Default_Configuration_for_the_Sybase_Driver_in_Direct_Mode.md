# 15.3 Modifying the Default Configuration for the Sybase Driver in Direct Mode

When you add users using the default configuration on the subscriber channel for the Sybase driver in direct mode, an error is displayed. Change the driver settings as follows:

* Set the Generation/retrieval method (table-global) to Subscriber-generated.
* Set the Retrieval timing (table-global) to after row insertion.
* Leave the Method and timing (table-local) as blank

When you change the value for the Method and timing option, you need to edit the sample procedures appropriately. For example, if you set it to view\_usr("indirect.proc\_idu(pk\_idu)"); view\_grp("indirect.proc\_idg(pk\_idg)"), you must edit the indirect.proc\_idu and indirect.proc\_idg procedures so that unique values are returned for the idg and idu columns respectively.
