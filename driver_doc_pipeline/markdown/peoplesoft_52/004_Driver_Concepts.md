# 1.3 Driver Concepts

The following sections explain the concepts you should understand before attempting to implement the PeopleSoft driver in your environment:

* [Driver Components](driver-concept.html#driver-components)
* [How the Driver Works](driver-concept.html#how-driver-works)
* [Configuring Your PeopleSoft Environment](driver-concept.html#aht32gc)
* [Configuring Your Identity Manager System](driver-concept.html#aht32xs)

## 1.3.1 Driver Components

The driver includes the following components:

* [Driver Shim](driver-concept.html#bs8g6mg)
* [Driver Packages](driver-concept.html#bs8g6v6)
* [PeopleSoft Service Agent](driver-concept.html#bs8g86r)

### Driver Shim

The driver shim (psoftshim.jar) enables communication between PeopleSoft and the Identity Vault. It bidirectionally reports object change events and applies object modification commands between these systems.

### Driver Packages

The driver packages contain configuration information and policies that enable Identity manager to handle the synchronization and data object manipulation between PeopleSoft and the Identity Vault.

The packages act as a template that contains the most common synchronization tasks performed in a typical integration scenario. You should configure your policies based on your own business processes and integration points. For more information, refer to [Section 4.0, Creating a New Driver Object](create-driver-object.html) and [Modifying Driver Policies](modify-driver-policies.html).

### PeopleSoft Service Agent

The PeopleSoft Service Agent (PSA) is a collection of PeopleSoft application objects developed for use with the driver shim and default driver configuration. Because all of the objects (fields, records, pages, components, component interfaces) are specifically named with a DirXML identifier, the PSA can be deployed onto a PeopleSoft application server without affecting existing PeopleSoft applications and objects.

The various pieces of the PSA provide examples of how data can be integrated between Identity Vault and PeopleSoft, such as the following:

* Implementation of an intermediate staging table. The synchronization between the NetIQ sample Personnel Application and the staging table shows the best practices of PeopleSoft internal application integration using PeopleCode Component Interfaces.
* Integration can be accomplished directly to the sample Personnel Application by simply changing the driver's configuration.
* PeopleCode is provided to show how database events on the sample Personnel Application can be reported to the driver shim via the transaction record interface required by the driver shim.
* PeopleCode is provided to show how to implement a Delete method on a Component Interface.

Similar to the driver configuration, the PSA is not intended for use in a production environment. It acts as a template that contains most of the common synchronization tasks needed in typical integration scenarios. You should configure your policies based on your own business processes and integration points. For more information, refer to [Section 3.0, Configuring Your PeopleSoft Environment](configure-driver-environment.html).

## 1.3.2 How the Driver Works

The following section describes the basic functions of the driver. It uses the Remote Loader configuration as an example; however, the driver does not require the use of the Remote Loader. For more information, refer to [Section 2.0, Installing the Driver Files](install-driver-files.html).

* [The Publisher Channel](driver-concept.html#bs8g9mm)
* [The Subscriber Channel](driver-concept.html#bs8ga4a)

### The Publisher Channel

The Publisher channel synchronizes data from PeopleSoft to the Identity Vault.

*Figure 1-1* The Publisher Channel

![](../graphics/pub1_a.png)

As events occur within PeopleSoft, transactions are placed into a transaction table. These transactions are usually written to the table through PeopleCode (you can use other methods such as Batch SQL, COBOL, SQR, and so forth.) Component Interface (CI) objects enable the driver to access transactions within the PeopleSoft system, and to query for relevant data associated with an individual transaction type. These CI objects are included as part of the PeopleSoft Service Agent (PSA).

The driver accesses the PeopleSoft environment by connecting through the Component Interface at the Application Server level. The driver periodically requests transactions that are waiting to be processed by driver subtype (such as Employee, Student, or Customer.) It processes only those transactions that have an available status and a transaction date and time less than or equal to the current date and time.

The driver then constructs an XML document from the data it retrieves and passes it to the Identity Manager engine for processing. When Identity Manager engine finishes processing the transaction, the driver updates the transaction with the status and any applicable messages in the transaction table inside of PeopleSoft. When events occur within Identity Vault, the driver connects to the appropriate CI and updates the PeopleSoft staging table accordingly. You can also configure the Driver to poll the Application server for event changes.

### The Subscriber Channel

The Subscriber channel synchronizes data from other applications via Identity Vault to PeopleSoft.

*Figure 1-2* The Subscriber Channel

![](../graphics/sub1_a.png)

As events occur within Identity Vault, the driver receives an XML document from the Identity Manager engine and updates PeopleSoft. By configuring the filter on the Subscriber channel, you can specify what data you want updated in PeopleSoft. The driver uses the Schema Component Interface (CI) and updates a staging table inside the PeopleSoft environment.

If you want to move the data from the staging table into PeopleSoft, you can create and apply the necessary PeopleCode to handle this transaction. (All PeopleSoft objects that can interact with the transaction table, application data, as well as the CI, are delivered with the sample project.)

## 1.3.3 Configuring Your PeopleSoft Environment

You must configure your PeopleSoft application to do two things:

* Trap events that occur within PeopleSoft and place transactions into a transaction table.
* Expose the transactions and any other desired data to the driver.

For detailed instructions regarding how to configure these processes, refer to [Section 3.0, Configuring Your PeopleSoft Environment](configure-driver-environment.html).

## 1.3.4 Configuring Your Identity Manager System

The driver interacts with PeopleSoft at the PeopleTools level by using Component Interface (CI) technology. By using existing CI definitions within the PeopleSoft modules, along with a collection of the driver's preconfigured CI objects, you can do the following:

* Create Identity Vault objects as new data is synchronized from PeopleSoft.
* Synchronize data bidirectionally between a PeopleSoft application and Identity Vault.
* Enable bidirectional object Create and Delete events.
* Transform Identity Vault events (such as Delete, Rename, or Move events) into different events in PeopleSoft.
* Maintain publication authority over data.
* Establish Group, Role, or other relationships in Identity Vault based on relationships defined within the PeopleSoft application.
* Provide notifications based on various events or required approval processes.
* Adhere to enterprise business processes and policies.
* Share data with other systems involved in your enterprise provisioning solution.

For more information on configuring your Identity Manager system, refer to [Section 6.0, Customizing the Driver](customize-driver.html).
