# 1.1 Driver Concepts

## 1.1.1 Data Transfer Between Systems

Identity Manager drivers support two data transfer channels between the Identity Vault and the connected system, called the Publisher and Subscriber channels. The Publisher channel handles data and events from the connected system into the Identity Vault. The Subscriber channel handles data and events from the Identity Vault into the connected system.

The G Suite Driver only supports data transfers from the Identity Vault into Google Apps. Communication is one-way only. Communication channels are discussed in the following sections:

### The Publisher Channel

The Publisher Channel is not currently supported by this driver.

### The Subscriber Channel

* Monitors the Identity Vault for new objects and changes to existing objects.
* Any relevant changes are sent to the shim to be executed in the Google Apps system.

Through the use of filters and policies, the driver can be configured to control and manage what changes are detected and sent to Google Apps.

## 1.1.2 How the Driver Works

The following diagram illustrates the data flow between Identity Manager and Google Apps API’s:

*Figure 1-1* G Suite Driver Data Flow

![](../graphics/figure01.png)

The Identity Manager engine uses XDS, a specialized form of XML, to represent events in the Identity Vault. Identity Manager passes the XDS to the driver policy, which can consist of basic policies, DirXML Script, and XSLT style sheets.

After driver policy has been applied, the driver shim communicates securely over https to the Google Apps API's for your domain. The results are then communicated back to the driver. The driver then processes that information converting it into an appropriate XDS that is reported back to the Identity Manager engine.

## 1.1.3 Understanding the Google APIs

Google has many different APIs available for managing data into and out of the many different Google applications. API Access must be turned on in the G Suite Admin Console. The driver supports the following APIs:

Directory API
:   – The Directory API is responsible for creating users and group objects. It is required to turn this API on inside the G Suite Admin Console.

Contact API \*
:   – The Contacts API creates a Domain Contact inside of the Address Book (Contacts).

Groups Settings API
:   – The Groups Settings API provides enhanced control of permissions and other group attributes.

GMAIL API
:   – Gmail user account settings, labels, forwarding, send as, and delegation

*NOTE:*The Contact API Add events may not show in the G Suite Admin Console and Address Book (Contacts) for up to 24 hours even though they are usable objects right away. Modify events will show immediately.
