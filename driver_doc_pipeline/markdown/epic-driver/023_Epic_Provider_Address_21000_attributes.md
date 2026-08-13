# F.1 Epic Provider Address (21000 attributes)

In Epic the 21000 attributes store provider address information. This information includes telephone, fax, and email attributes. For those who are accustomed to thinking in eDirectory terms, the attributes can best be described as a multi-valued, structured attribute. There are two keys to the addressing or updating of these attributes. These are the 21000 field which is assigned by Epic, and the 21200 field which is the external identifier. It is through this external identifier that the driver tracks updates to the address record.

The primary attributes that the driver manages are:

| Epic Field | Description |
| 21000 | Address Unique ID\* |
| 21010 | Address Street line 1 |
| 21020 | Address Street line 2 |
| 21030 | Address Street line 3 |
| 21040 | Address City |
| 21050 | Address State |
| 21060 | Address Zip Code |
| 21080 | Address Country |
| 21090 | Address Is Primary |
| 21110 | Address Phone |
| 21120 | Address Fax |
| 21130 | Address EMail |
| 21200 | Address External ID |

\*The driver passes a value of “\*” (star) to Epic for 21000 on every event. This is the recommendation from Epic for creating and managing provider address records. It is intended by Epic that Address External ID (21200) is the unique identifier for managing addresses via external means (API calls).

The driver updates/manages these fields with the Epic SER Default Configuration package. Additional fields are supported but require customization of the default package.
