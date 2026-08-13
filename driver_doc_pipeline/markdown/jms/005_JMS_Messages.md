# 1.4 JMS Messages

The following sections contain information about JMS message structures and message types, as well as examples for each.

* [Message Structure](jms-messages.html#b5j1tsq)
* [Message Types](jms-messages.html#b5j23nz)

## 1.4.1 Message Structure

JMS messages consist of metadata (comprised of headers and properties) and message data (a body). In order to make message metadata accessible to policy processing, messages sent to the driver can be wrapped in an envelope, and messages received by the driver and sent to the Identity Manager engine are also wrapped in an envelope. All message envelope elements and special attributes must have a namespace prefix bound to urn:idm:jms. For consistency, the namespace prefix jms is used throughout this document. The root message envelope element jms:message must be a child of the XDS input/output elements.

#### Example JMS Message Envelope

```
<jms:message xmlns:jms="urn:idm:jms">
<jms:headers>
      <!-- standard JMS headers start with "JMS" -->
      <!-- client-assignable headers -->
      <jms:header jms:name="JMSDeliveryMode"/>
      <jms:header jms:name="JMSExpiration"/>
      <jms:header jms:name="JMSPriority"/
      <jms:header jms:name="JMSReplyTo"/>
      <jms:header jms:name="JMSCorrelationID"/>
      <jms:header jms:name="JMSType"/>
   </jms:headers>
   <jms:properties>
      <!-- standard JMS properties start with "JMSX" -->
      <jms:property jms:name="JMSXUserID"/>
      <jms:property jms:name="JMSXAppID"/>
      <jms:property jms:name="JMSXProducerTXID"/>
      <jms:property jms:name="JMSXConsumerTXID"/>
      <jms:property jms:name="JMSXRcvTimestamp"/>
      <jms:property jms:name="JMSXDeliveryCount"/>
      <jms:property jms:name="JMSXState"/>
      <jms:property jms:name="JMSXGroupID"/>
      <jms:property jms:name="JMSXGroupSeq"/>
      <!-- provider-specific properties start with "JMS_" -->
      <!-- application-specific properties start with anything else -->
   </jms:properties>
  <jms:body/>
</jms:message>
```

## 1.4.2 Message Types

Message type refers to how a message is sent, not necessarily what its content is. For example, a text message can be sent as text or bytes. The driver supports both text and bytes messages.

#### Example Text Message

```
<jms:message xmlns:jms="urn:idm:jms">
   <jms:properties>
      <!-- send message as text -->
      <jms:property name="Novell_IDM_MessageType">text</jms:property>
   </jms:properties>
   <jms:body>content</jms:body>
</jms:message>
```

#### Example Bytes Message

```
<jms:message xmlns:jms="urn:idm:jms">
   <jms:properties>
      <!-- send message as bytes -->
      <jms:property name="Novell_IDM_MessageType">bytes</jms:property>
   </jms:properties>
   <jms:body>content</jms:body>
</jms:message>
```
