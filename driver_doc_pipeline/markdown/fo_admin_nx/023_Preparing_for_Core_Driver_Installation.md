# 5.1 Preparing for Core Driver Installation

Please review this section carefully for a high-level overview of the tasks and considerations you will encounter during the installation of the Core Driver. This information will help you later as you determine which steps are relevant to your particular installation scenario(s).

## 5.1.1 Essentials

* Verify that you meet minimum system requirements. For details, see [Requirements](babffihg.html).
* Obtain the Core Driver distribution package for your target operating system from the [NetIQ downloads site](http://download.novell.com). In other words, you will need the package that is designed for the operating environment in which Identity Manager is running.
* Always check the [NetIQ Support Web Site](http://support.netiq.com) for the latest support pack and product update information. Check the Release Notes and Readme files for the version you are installing for any special actions that might be required.

## 5.1.2 Other Advance Considerations

Topics in this section include:

* [Specifying Primary and Secondary Core Drivers](cegddcgh.html#bfil5n1)
* [Complete Checklist of Considerations Before Installation](cegddcgh.html#bfil4vt)

### Specifying Primary and Secondary Core Drivers

During software installation, you will be asked if you are establishing a primary Core Driver or adding a secondary Core Driver. Following are some guidelines for determining how to respond:

* You must have one primary Core Driver. If you are installing a Core Driver for the first time, it will automatically be designated as the primary.
* The primary Core Driver must have access to a read/write replica of the entire ASAM System container and all User and Group objects defined by the Census.
* Secondary drivers can service authentication requests and deliver events to connected platforms but will not perform tasks such as trawls or update enterprise objects in the Census. Therefore, the primary Core Driver must be active and running in order to provide connected platforms with new provisioning information.

For additional information on assessing secondary driver requirements, see [Performance Tuning](bfmn9rs.html).

### Complete Checklist of Considerations Before Installation

* A Quick Start guide for installing the Fan-Out Driver is available for each target platform. Although this Administration Guide includes detailed procedures for all installation scenarios, you may find the Quick Start helpful in focusing on primary steps. The quick starts, listed below, are available at the [Identity Manager 4.8 Drivers Documentation Web site](https://www.netiq.com/documentation/identity-manager-47-drivers).

  + Fan-Out Driver Installation Quick Start for Linux and UNIX Systems
  + Fan-Out Driver Installation Quick Start for Midrange Systems
  + Fan-Out Driver Installation Quick Start for Mainframe Systems
* During software installation, you will be asked if you are establishing a primary Core Driver or adding a secondary Core Driver. For guidelines, see [Specifying Primary and Secondary Core Drivers](cegddcgh.html#bfil5n1).
* To complete the Core Driver installation you will use one of two available application interfaces for configuration:

  *iManager*
  Newer versions of this standard NetIQ Web interface include a Fan-Out Driver application plug-in for driver configuration. The Core Driver software includes a copy of this plug-in in case you have an older version of iManager. The installation instructions include steps for installing this plug-in after you have run the initial installation software.

  *Designer*
  This interface, which comes as part of the Identity Manager 4.8 product, is an offline tool you can use to plan and model large deployments of the Fan-Out Driver. Designer includes its own Fan-Out Driver application plug-in, which is already installed as part of the Designer interface. For more information on Designer, see [Applications For Configuration](chdijbdi.html).
* Once you have installed the Core Driver and completed its initial configuration in iManager, you still won’t be able to test the installation until you have installed Platform Services on the system(s) you will connect to. This will involve an additional software installation and configuration on each of these systems. Therefore, you may want to preview Part IV of this Administration Guide, “Platform Services Administration,” for details about this additional process.
* Installation of the Core Driver will create an ASAM directory in the file system on each server that includes any of its components. Access to each copy of this directory should be restricted to the driver itself and its administrators to ensure protection of sensitive identity information.

## 5.1.3 General Installation Sequence

Following is a general overview of the process for installing the Core Driver.

*NOTE:*This section is provided to help you prepare for installation. More detailed instructions are provided later in [Step-By-Step Installation Instructions](bfg23nl.html).

1. Read [Essentials](cegddcgh.html#bfg27ln) and [Other Advance Considerations](cegddcgh.html#bfg1i7j).
2. Know in advance which of the following installation scenarios you wish to perform:

   * New installation of a primary Core Driver running on Linux or Windows
   * New installation of a secondary Core Driver running on Linux or Windows
   * Upgrade of an existing Core Driver running in “Local” mode (default, not using Remote Loader) running on Linux or Windows
   * Upgrade of an existing Core Driver running in “Remote” mode (already using NetIQ Remote Loader) running on Linux or Windows
3. Run the Core Driver installation program and respond to the prompts. This will install the Core Driver software components also known as the Driver Shim.
4. If required, install the iManager plug-in for the Fan-Out Driver Web application.
5. Using iManager and the plug-in, create objects in the Identity Vault to support the Core Driver. This includes importing an XML default configuration file that comes with the Core Driver installation software.
6. Populate your Census with the users and groups that you will use for your initial testing.

   This includes defining Census Search objects and then running a Census Trawl. For details about this procedure, see [Configuring the Census](br3n4tb.html#chdfigcf).
7. Assign users of the Fan-Out Web program (in iManager) the rights they need.

   For details, see [Rights Required for Web Application Use](chdijbdi.html#bfnnjh3).
8. Define the UID/GID sets that you will use for your initial testing. For details, see [Configuring Linux/UNIX UID/GID Sets](br3n4tb.html#chdjdaff).
9. Define the Platform Sets that you will use for your initial testing. For details, see [Configuring Platform Sets](br3n4tb.html#chddcggj).

   You must define at least one UID/GID Set before you can define a Platform Set.
10. Define the platforms that you will use for your initial testing. For details, see [Configuring Platforms](br3n4tb.html#bfijtk0).
11. Use iManager to start the Core Driver object in Identity Manager.
12. Use system tools to start the Driver Shim in the local operating environment.
13. Install and configure Platform Services to match the platforms you defined in iManager during the previous steps.

    *IMPORTANT:*This step involves individual software installations and configurations on each system you will connect to with the Fan-Out Driver. For detailed information about this separate process, see Part IV of this Administration Guide, “Platform Services Administration.”
14. After testing, install additional Core Drivers for performance and redundancy according to the guidelines in [Performance Tuning](bfmn9rs.html).
15. Before the 90-day evaluation period expires, activate the Identity Manager Fan-Out Driver.

    You can use the driver for evaluation purposes for 90 days. The driver will not work thereafter unless it has been activated. For details, see [Activating the Driver After Evaluation](anhms6o.html).
16. Fully deploy the Fan-Out Driver throughout your enterprise as you gain confidence and experience.
