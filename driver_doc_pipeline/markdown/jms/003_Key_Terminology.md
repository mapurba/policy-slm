# 1.2 Key Terminology

The following terms are used throughout this document:

* *JMS:*
  Java Messaging Service. The driver uses two main specifications of JMS, 1.0.2b and 1.1.
* *JNDI:*
  Java Naming and Directory Interface. JNDI is used to look up, connect, and authenticate to message brokers.
* *Message Broker:*
  The server that handles message interchange between messaging clients.
* *Messaging Client:*
  Messaging clients produce and consume messages. The driver is a messaging client, and so are third-party applications.
* *Destination:*
  The abstract term for a topic or a queue.
* *Session:*
  A per-thread connection. Each thread creates one or more sessions from a connection to communicate with the message broker.
* *Persistence:*
  Persistence guarantees that a message is delivered only once; this can be controlled on a per-message basis. Message brokers usually support persistent storage via an underlying database. This is sometimes referred to as stable storage.
* *Durability:*
  The message broker stores messages for a message receiver when the receiver is inactive or disconnected.
* *Acknowledgement:*
  When transactions are not being used, a client acknowledges receipt of a message to the message broker in CLIENT\_ACKNOWLEDGE mode. In this mode, the client must explicitly acknowledge receipt of one or more messages by committing the current transaction. By rolling back the current transaction, all received messages are re-delivered (or set to retry, in Identity Manager terminology.)
