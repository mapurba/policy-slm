# 1.5 How Subscriber and Publisher Channels Work

The following sections contain information about how the Subscriber and Publisher channels work with the JMS driver. This driver functions differently than traditional Identity Manager drivers, so it’s important to review this information.

* [Subscriber Channel](how-subscriber-and-publisher-channel-works.html#b5j2636)
* [Publisher Channel](how-subscriber-and-publisher-channel-works.html#b5j2662)

## 1.5.1 Subscriber Channel

The Subscriber channel is capable of sending messages to (and optionally receiving messages from) multiple destinations on a single broker. Multi-broker support is not yet implemented. As a side effect of sending a JMS message, the Subscriber channel can receive a response within a specified timeout interval. Message routing and RPC (Remote Procedure Call) emulation are achieved via three special attributes: jms:send-to, jms:receive-from and jms:receive-timeout.

#### Example Special Attributes

```
<jms:message xmlns:jms="urn:idm:jms"
               jms:send-to="queueA"
               jms:receive-from="queueB"
             jms:receive-timeout-seconds="10"/>
```

These attributes can be used on a jms:message envelope tag or any XDS command that is a child of input/output elements. The destination names used in these parameters can either be the JNDI (Java Naming and Directory Interface) name or the unique Identity Manager identifier assigned to the destination in the driver configuration. By default, the Subscriber sends messages to the first-defined send destination and does not wait for a message response (meaning that the message receipt is assumed to be asynchronous).

By using a JMS message envelope, it is possible to override headers/properties or add vendor-specific properties or application properties.

```
<jms:message xmlns:jms="urn:idm:jms">
   <jms:headers>
   <!-- override standard headers -->
       <jms:header jms:name="JMSType">type</jms:header>
       <jms:header jms:name="JMSCorrelationID">blah</jms:header>
      <jms:header jms:name="JMSDeliveryMode">non-persistent</jms:header>
      <jms:header jms:name="JMSExpiration">10000</jms:header>
      <jms:header jms:name="JMSPriority">9</jms:header>
      <jms:header jms:name="JMSReplyTo">A</jms:header>
   </jms:headers>
   <jms:properties>
      <!-- add/override vendor-specific properties -->
      <jms:property jms:name="JMS_IBM_Format">MQSTR</jms:property>
      <!-- add/override application properties -->
      <jms:property jms:name="Novell_IDM_MessageType">bytes</jms:property>
      <jms:property jms:name="Novell_IDM_ContentType">xml</jms:property>
      <jms:property jms:name="Novell_IDM_CharEncoding">UTF-8</jms:property>
   </jms:properties>
   <jms:body>text</jms:body>
</jms:message>
```

## 1.5.2 Publisher Channel

The Publisher channel is essentially a Subscriber channel (you can send messages to a broker as a side effect of publishing messages—including heartbeat documents—and wait for a response) with the added ability to periodically monitor specified destinations to receive messages for publication.

You can configure the Publisher channel to monitor an unlimited number of destinations on a single message broker bounded only by certain practical considerations. Having too many monitored destinations can significantly slow down rendering of driver parameters in Identity Console or Designer, as currently implemented. Having too many destinations can result in decreased performance because all destinations are being monitored by a single thread. Furthermore, there is a finite amount of space available for storing a driver's configuration (64 KB).

The Publisher channel polls each monitored destination in a round-robin fashion, starting with the first declared destination. A polling cycle ends when all monitored destinations fail to return messages, at which time the Publisher sleeps for the specified polling interval until it's time to start a new polling cycle.

The Publisher channel receives messages in a synchronous fashion as opposed to an asynchronous one. The main reason for this is to prevent client overrun—when the message broker feeds messages to the driver faster than it can process them—that can lead to memory exhaustion.
