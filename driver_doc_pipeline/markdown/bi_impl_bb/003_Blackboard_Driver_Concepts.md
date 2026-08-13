# 1.2 Blackboard Driver Concepts

The following sections explain concepts you should understand before implementing the Blackboard driver:

* [Default Data Flow](btvi7q3.html#btvhxy7)
* [Policies](btvi7q3.html#btvim36)
* [Driver Components](btvi7q3.html#btviwjt)

## 1.2.1 Default Data Flow

A channel is a combination of rules, policies, and filters that is used to synchronize data between two systems. The Subscriber and Publisher channels describe the direction in which the data flows. The Subscriber and Publisher channels act independently; actions in one channel are not affected by what happens in the other.

* [Subscriber Channel](btvi7q3.html#btvhyun)
* [Publisher Channel](btvi7q3.html#btx091a)

### Subscriber Channel

The Subscriber channel is the channel of communication from the Identity Vault to Blackboard. The channel takes events generated in the Identity Vault and sends them to the Blackboard system. The Subscriber channel also supports queries into Blackboard.

[Figure 1-1](btvi7q3.html#btvi37l) illustrates this data flow.

*Figure 1-1* Data Flow Through The Subscriber Channel

![](../graphics/dirxml_sub_a.gif)

The driver can be configured to work with Blackboard, versions 9 and later.

### Publisher Channel

The Publisher channel is not implemented.

## 1.2.2 Policies

Policies are used to control the synchronization of data between the Identity Vault and Blackboard. The Blackboard driver is designed to be used with Identity Manager 4.8 Packages, but for backward compatibility the policies have been provided in an XML preconfiguration document. For information about the policies installed in the preconfiguration, see [Section A.0, Policies](btyjlp4.html). All policies contained in the Packages are included in the preconfiguration file for Identity Manager 3.6.

## 1.2.3 Driver Components

The driver contains the following components:

* *Default Driver Configuration File for Identity Manager 4.8:*
  A file you can import to set up default rules, style sheets, and driver parameters. The driver configuration file included with this driver is BlackboardRESTDriver.xml.
* *Driver Shim Installation File:*
  linux\_x86\_64\_bbdriver\_install.bin
* *Schema File:*
  blackboard.sch contains optional schema extensions to be used with the Blackboard driver.
