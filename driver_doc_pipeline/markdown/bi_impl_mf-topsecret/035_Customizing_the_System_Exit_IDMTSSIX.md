# 6.5 Customizing the System Exit, IDMTSSIX

The default exit module, IDMTSSIX, queues events to cross-memory for the logger started task, which, in turn, updates the change log. If the logger is unavailable, or the system cannot process events quickly enough, these events will become backed up into ECSA storage. To prevent memory exhaustion and alert operators of the problem, IDMTSSIX includes these hard-coded features:

* When the number of events in ECSA reach 1000, the warning message LDX9998E is issued.
* When the number of events in ECSA reach 10,000, the warning message LDX9999E is issued and events are no longer queued to ECSA.

The above values, 1000 and 10,000, can be changed by applying a ZAP modification to the Exit module, IDMTSSIX. Included in the SAMPLIB dataset is the job, ZAPTSSIX. If you wish to modify these values, customize ZAPTSSIX with the location of IDMTSSIX and the new cutoff values and submit.

For calculation reference, an event may be a password-change event or a command-image event. With password-change events, a single event occupies 52 bytes. Single command-image events are variable in length, averaging about 250 bytes.
