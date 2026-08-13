# 5.1 Scripting Driver Data Definition

Topics in this section include

* [Defining Data Classes and Attributes](b8n5d0x.html#b8n5dfz)
* [Associating Identity Vault and Application Classes and Attributes](b8n5d0x.html#b8n6pqx)
* [Defining an Association Rule](b8n5d0x.html#b8n6pqy)
* [Defining Excluded Identities](b8n5d0x.html#b8n6pqz)
* [Defining Relevant Events](b8n5d0x.html#b8n6pr0)

## 5.1.1 Defining Data Classes and Attributes

The first task is to examine your external application’s identity data and to determine what data is relevant and how it should be managed. Below is a series of questions to ask in this process. The list is not all-inclusive; there might be other questions you need to consider.

* Are identities stored in a hierarchical or flat format? In a hierarchical system, objects known as containers can contain identities and perhaps other containers, resulting in a tree-like structure. A flat system contains all identities at a single level.
* What types of identities exist in the external application? For example, NetIQ® eDirectory™ contains Users, Groups and Dynamic Groups, to name a few. Identity types, like Groups, are often aggregates of other identity types.
* What uniquely distinguishes (or names) each type of identity? The name is usually an attribute, known as the naming attribute. Systems often use a human-readable name and a unique serial number. You should determine which is suitable for your needs.
* What relationships exist among the identity types? Suppose Groups can contain Users. Can Groups contain other Groups? Are these relationships one-to-one or one-to-many?
* Is there a way for an identity to link to or represent another identity? For example, eDirectory provides Alias objects, which link to other objects. Your driver might need to handle these types of objects.
* What attributes describe each relevant type of object? Which of these attributes is relevant? What is the data type (string, number, etc.) for each attribute? Can the attribute contain multiple values? Are there restrictions on the attribute’s values, such as being read-only, or are they restricted to a certain range of values?
* How will this data be synchronized between the Identity Vault and the application? Some attributes will be synchronized one-way (eDirectory-to-application or vice versa), and others will be synchronized bi-directionally.
* Does your application need password synchronization? Will password synchronization be one-way or bi-directional? Restrictions might also apply to other sensitive data. You need to study the APIs for your application to determine how this should be done.
* Are there identity types or specific identities that should be excluded from synchronization? Administrative users are often excluded from synchronization to avoid security issues.
* Does data need to be transformed when it is synchronized? For example, eDirectory stores a person’s first name and last name as separate attribute, but an external application might store a name as one attribute. Such transformations can be done in policies or in the scripts.

Through this process, you should make a list of the application’s identity types (also known as classes), their attributes, and each attribute’s data type and special properties. This list can then be specified in the driver’s schema.def file:

```
SCHEMA
   CLASS User
     ATTRIBUTE loginName NAMING REQUIRED
     ATTRIBUTE firstName
     ATTRIBUTE lastName
         (etc.)
```

The format of this schema.def file is the same regardless of operating system and scripting language. See [The Connected System Schema File](b8n6pr6.html) for more information.

## 5.1.2 Associating Identity Vault and Application Classes and Attributes

The next step is to examine the Identity Vault’s classes and attributes and determine which best correspond to the external application’s identities. If the Identity Vault does not provide a suitable class or attribute, you can define your own by modifying the Identity Vault’s schema. For more information, see the NetIQ eDirectory Administration Guide.

The driver’s driver filter allows the Metadirectory engine to determine which attributes and classes are relevant to the driver. For the Subscriber channel, the engine notifies the driver of changes for only those classes and attributes that are set to Synchronize in the filter. When the driver receives application identity changes on the Publisher channel, Synchronize must be set on classes and attributes for those items to be changed in eDirectory. The easiest way to define a driver filter is to create a new driver with the default XML configuration file provided with the Scripting driver (Scripting.xml). In NetIQ iManager, edit the Driver Filter to include relevant classes and attributes. Then, export the driver’s configuration to an XML file for later use. See [Managing Additional Attributes](b8n6prs.html) for more information.

## 5.1.3 Defining an Association Rule

Each identity needs an association that uniquely identifies that identity for both eDirectory and the external application. The association must be based on information shared between both the Identity Vault and the application. The association is usually based on one or more attribute values. Below are some ideas for forming an association:

* If a naming attribute is unique across all classes, you could use that attribute value.
* If a naming attribute is unique for a specific class, concatenate the attribute and class name to form the association. For example, an identity named “Bob” with the class “User” could have association “BobUser”.
* In a hierarchical system (like eDirectory), you could use a name with its complete hierarchical path, assuming that it is unique. For example, an identity with a hierarchical path “Bob.Users.ACME” could use that path as its association.
* A system can provide a serial number for each identity. This unique number can be used for an association.

## 5.1.4 Defining Excluded Identities

You might have a list of identities that you want to exclude from synchronization. Also, if an identity is synchronized with sensitive information, you might want to reject that identity. The include-exclude.conf file allows such specifications:

```
EXCLUDE
   adminUser
   CLASS secureUser
```

The format of this file is the same regardless of operating system and scripting language. See [The Connected System Include/Exclude File](b8n6prd.html) for more information.

## 5.1.5 Defining Relevant Events

When data changes in an identity management system, an event is said to have occurred. In preparation for the next step, evaluate which event types are relevant for your application:

* *Add:*
  An identity is created. All required attributes must be created. Security parameters, such as a password, should be defined for the identity to ensure that security isn’t compromised.
* *Modify:*
  One or more attributes of an existing identity are changed. This might affect identities that have a relationship to the changed identity.
* *Modify-password:*
  An identity’s password has changed. This event type can be considered a subtype of Modify, but because it often requires special handling, it is treated as a separate event type.
* *Delete:*
  An identity is destroyed. This might mean permanent deletion, or a change of status of the identity so that it can be undeleted if necessary. This might affect other identities. For example, deleting a User that is a member of a Group might cause a Modify event for that Group.
* *Rename:*
  An identity’s naming attribute has changed.
* *Move:*
  An identity’s logical location has changed. This usually applies to identities in a hierarchical system.

An event of a certain type in one system can result in an event of a different type in the synchronized system. For example, when a Modify event occurs for an identity that does not yet exist in the external system, an Add event is submitted.

There is one more type of event that does not represent a change but is a request for information: the Query event. NetIQ eDirectory issues queries to your application on the Subscriber channel. You can also query eDirectory from scripts on either Subscriber or Publisher channels.

NetIQ eDirectory supports all of the events above. You should make a list of what the result of a particular event in eDirectory will be in your external application. Conversely, you should list what event types can occur in your external application, which event types are relevant and what the result of relevant events should be in the Identity Vault.
