# E.0 Appendix E 芒聙聯 Supported Epic SER Attributes

The following Epic SER attributes are supported to read by Epic for query operations:

| Active  Whether the practitioner's record is in active use.  * Type: Boolean * Example: true |
| Communication  A language the practitioner is able to use in patient communication.  * Type: CodeableConcept[] (coding, text) * Example: { 芒聙聹coding芒聙聺: { 芒聙聹code芒聙聺: 芒聙聹芒聙聺, 芒聙聹display芒聙聺: 芒聙聹芒聙聺}, 芒聙聹text芒聙聺: 芒聙聹芒聙聺 } |
| Gender  The gender of the practitioner.  * Type: String * Examples: 芒聙聹Male芒聙聺, 芒聙聹Female芒聙聺, 芒聙聹Unknown芒聙聺 |
| Identifier  The practitioner or user ID.  * Type: Identifier[] (id, idtype, ini, system, type, use, value) |
| Name  The name of the practitioner, including all prefixes and suffixes available.  * Type: HumanName[] (family, given[], prefix, suffix, text) |
| Photo  Contains parameters related to the practitioner photo.  * Type: Attachment[] (url) |
| PractitionerRole  Contains parameters related to the practitioner photo.  * Type:PractitionerRole (active, code, location, practitioner, speciality, telecom) * Example: { "resourceType": "PractitionerRole", "id": "DcYFyJ3YM", "active": true, "practitioner": { "reference": "Practitioner/emDkOufD", "display": "Joe Smith" }, "code": [ { "coding": [ { "code": "1", "display": "Physician" } ], "text": "Physician" } ], "specialty": [ { "coding": [ { "code": "19", "display": "Family Practice" } ], "text": "Family Practice" }, { "coding": [ { "code": "32", "display": "Internal Medicine" } ], "text": "Internal Medicine" } ] } |
| Qualification  The practitioner's qualifications.  * Type: Qualification[] (code[]) |
| Telecom  Returned only for Epic user-based practitioners. Not returned in a MyChart context.  * Type: ContactPoint[] (system, value) |
