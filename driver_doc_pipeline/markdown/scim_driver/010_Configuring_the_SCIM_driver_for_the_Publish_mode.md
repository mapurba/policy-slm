# 2.6 Configuring the SCIM driver for the Publish mode

The SCIM driver supports the Publish mode. In this mode, the driver exposes SCIM endpoints to receive events from the connected SCIM service and then pushes those events to the Identity Vault.

## 2.6.1 Supporting Identity Manager engine through SCIM endpoints

The SCIM driver exposes SCIM endpoints to the Identity Manager engine. This allows external applications and services to communicate with OpenText eDirectory and Identity Manager engine through the SCIM API.

*NOTE:*The authentication header and content type are mandatory for SCIM methods.

The following table lists the URLs for the different methods and resources:

*Table 2-3* List of URLs with methods and resources

| Resource | Method | URL |
| Users | GET, POST | http://{ipaddress}:{port}/scim/api/v2/Users |
| Specific user | GET, PUT, PATCH, DELETE | http://{ipaddress}:{port}/scim/api/v2/Users/{id} |
| Groups | GET, POST | http://{ipaddress}:{port}/scim/api/v2/Groups |
| Specific group | GET, PUT, PATCH, DELETE | http://{ipaddress}:{port}/scim/api/v2/Groups/{id} |
| Custom | GET, POST | http://{ipaddress}:{port}/scim/api/v2/custom/{resourceName} |
| Specific custom | GET, PUT, PATCH, DELETE | http://{ipaddress}:{port}/scim/api/v2/custom/{resourceName}/{id} |

### POST method

The following table lists an example of the POST method:

*Table 2-4*

| Method: POST |  |
| User URI | http://{ipaddress}:{port}/scim/api/v2/Users |
| Payload | ``` {    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],    "userName": "johndoe@gmail.com",    "externalId": "4wJRiuTHyEC45uMCUYrkxmn=",    "name": {        "givenName": "John",        "familyName": "Doe"    },    "emails": [{ "value": "Johndoe@gmail.com", "type": "work", "primary": true }],    "active": true} ``` |
| Authorization | Basic c3lzdGVtL3N5c3RlbQ== |
| Content-Type | application/json |
| Response | ``` 201 Created{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User"    ],    "userName": " johndoe@gmail.com ",    "externalId": "4wJRiuTHyEC45uMCUYrkxmn=",    "name": {        "givenName": "John",        "familyName": "Doe"    },    "emails": [        {            "value": " johndoe@gmail.com ",            "type": "work",            "primary": true        }    ],    "active": true,    "id": "CqekLDjY7UW3HAqnpCw42A=="} ``` |

*NOTE:*The ID returned in the POST response body is the unique system identifier. This ID is required for all subsequent operations (GET, PUT, PATCH, and DELETE) targeting that specific resource. Thus, you must capture and store the ID.

### DELETE method

The following table lists an example of the DELETE method:

*Table 2-5*

| Method: DELETE |  |
| User URI | http://{ipaddress}:{port}/scim/api/v2/Users/{id} |
| Payload | Not required |
| Authorization | Basic c3lzdGVtL3N5c3RlbQ== |
| Content-Type | application/json |
| Response | 204 No Content |

### GET method

The following table lists an example of the GET method:

*Table 2-6*

| Method: POST |  |
| User URI | http://{ipaddress}:{port}/scim/api/v2/Users |
| Payload | Not applicable |
| Authorization | Basic c3lzdGVtL3N5c3RlbQ== |
| Content-Type | application/json |
| Response | ``` {    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],    "totalResults": 1,    "itemsPerPage": 100,    "Resources": [        {            "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],            "id": "nhjkuijkskhdid==",            "userName": " johndoe@gmail.com ",            "active": true        }    ]    "nextCursor": "rO0ABXNyACxjb20ubm92ZWxs...BZAO0ig=="} ``` |

### PATCH method

The following table lists an example of the PATCH method:

*Table 2-7*

| Method: PATCH |  |
| User URI | http://{ipaddress}:{port}/scim/api/v2/Users/{id} |
| Authorization | Basic c3lzdGVtL3N5c3RlbQ== |
| Content-Type | application/json |
| Payload | ``` {    "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],    "Operations": [        {            "op": "replace",            "path": "name.familyName",            "value": "Doejohn@gmail.com"        }    ]} ``` |
| Response | 200 OK |

### PUT method

The following table lists an example of the PUT method:

*Table 2-8*

| Method: PUT |  |
| User URI | http://{ipaddress}:{port}/scim/api/v2/Users/{id} |
| Authorization | Basic c3lzdGVtL3N5c3RlbQ== |
| Content-Type | application/json |
| Payload | ``` {    "id": "CqekLDjY7UW3HAqnpCw42A==",    "userName": " johndoe@gmail.com ",    "externalId": "4wJRiuTHyEC45uMCUYrkxmn=",    "name": {        "givenName": "John",        "familyName": "Doe"    },    "emails": [        {            "value": " johndoe@gmail.com ",            "type": "work",            "primary": true        }    ],    "active": true,    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"]} ``` |
| Response | ``` 200 OK{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User"    ],    "userName": " johndoe@gmail.com ",    "externalId": "4wJRiuTHyEC45uMCUYrkxmn=",    "name": {        "givenName": "John",        "familyName": "Doe"    },    "emails": [        {            "value": " johndoe@gmail.com ",            "type": "work",            "primary": true        }    ],    "active": true,    "id": "CqekLDjY7UW3HAqnpCw42A=="} ``` |

### GET method for specific user

The following table lists an example of GET method that the driver supports for a specific user:

*Table 2-9*

| Method: GET |  |
| User URI | http://{ipaddress}:{port}/scim/api/v2/Users/{id} |
| Payload | Not applicable |
| Authorization | Basic c3lzdGVtL3N5c3RlbQ== |
| Content-Type | application/json |
| Response | ``` {    "emails": [        {            "type": "work",            "value": " johndoe@gmail.com "        }    ],    "name": {        "familyName": "John",        "givenName": "Doe"    }    "active": "false",    "id": "CqekLDjY7UW3HAqnpCw42A==",    "userName": " johndoe@gmail.com ",    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User"    ]} ``` |
