# E.0 Understanding the Driver State Storage

The Workday driver periodically updates its current status in XML format in the DirXML-DriverStorage attribute which is stored in Identity Vault. Driver uses this XML document to resume its operation after a restart. Each element in the XML document is presented in the following format:

```
<Object Class-Poll Type-Status Type>Value</Object Class-Poll Type-Status Type>
```

For example,

```
<worker-regular-poll-start-timestamp>03-12-2019 14:37:20</worker-regular-poll-start-timestamp>
```

In the above example, Worker is the object class, Regular Poll is the poll type and Start Timestamp is the status type. The information related to the following object classes are stored in the XML document:

* Worker
* Terminated Worker
* Job Profile
* Job Family
* Location
* Organization
* Photo

The following Poll Types are stored in the XML document:

* Migration
* Migration\_Restart
* Regular\_Poll

The following table explains the various status types that are stored in the XML document:

*Table E-1* Explanation of Status Types

| Status Type | Description |
| start-timestamp | Start timestamp of the specified latest poll type |
| end-timestamp | End timestamp of the specified latest poll type |
| restart-timestamp | Restart timestamp of the specified latest poll type |
| last-page-poll-start-timestamp | Start timestamp of the last page that is fetched during the specified latest poll type |
| last-page-poll-end-timestamp | End timestamp of the last page that is fetched during the specified latest poll type |
| last-poll-timestamp | The last timestamp for which the polling was requested to the Workday server |
| last-effective-poll-timestamp | The last timestamp for which the effective polling was requested to the Workday server |
| migration-completed | Timestamp of the migration completion |
| last-request-doc | The last request that was sent to the Workday server. This request is stored in Base64 format. |
| page-count | The number of pages fetched during the specified latest poll type |
| total-page | The total number of pages in the Workday response during the specified latest poll type |
| entry-time | The entry timestamp for which the polling was requested to the Workday server |

NOTE:

* The last-request-doc status type will not be stored in the conventional format. It stores the last request that was made to the Workday server irrespective of object class or poll type.
* The effective polling happens once in a day and happens for worker and job profile.
