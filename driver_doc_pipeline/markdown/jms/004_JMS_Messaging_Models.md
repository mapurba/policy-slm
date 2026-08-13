# 1.3 JMS Messaging Models

The driver supports two messaging models: Point-to-Point messaging and Publish/Subscribe messaging.

* [Point-to-Point Messaging](jms-messaging-models.html#b5gjrr4)
* [Publish/Subscribe Messaging](jms-messaging-models.html#b5gjs01)

The JMS API also uses abstract names. To better understand how these abstract names correspond to model terminology, see the table below.

| Abstract Terminology | Point-to-Point Terminology | Publish/Subscribe Terminology |
| Destination | Queue | Topic |
| Sender (or Producer) | Sender | Publisher |
| Receiver (or Consumer) | Receiver | Subscriber |

## 1.3.1 Point-to-Point Messaging

Point-to-Point messaging is used when one client needs to send a message to another client. As illustrated in [Figure 1-1](jms-messaging-models.html#b5gj80u), Client 1 is the sender and Client 2 is the receiver. The queue receives messages, while the message broker receives any acknowledgements.

In Point-to-Point messaging there is a one-to-one relationship between senders and receivers. You configure durability on the broker side.

*Figure 1-1* Point-to-Point Messaging

![](../graphics/p2p_a.png)

## 1.3.2 Publish/Subscribe Messaging

Publish/Subscribe messaging is used when multiple applications need to receive the same messages. Multiple publishers can send messages to a topic, and all subscribers to that topic receive all the messages sent to that topic. This model is useful when a group of applications want to notify each other of a particular event.Publish/Subscribe messaging allows for one-to-many or many-to-many implementations. Durability is configured on either the client side or the broker side.

*Figure 1-2* Publish/Subscribe Messaging

![](../graphics/pubsub_a.png)
