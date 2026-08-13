# 2.10 Creating the Driver Object

To create the Epic driver object in Designer, the previously listed driver packages must first be installed in the Designer project’s Package Catalog. When creating the driver object, these packages must be added to the driver object, the driver set, and the User Application driver object, and then configured for the target environment.

## 2.10.1 Importing the Current Driver Packages

To import the driver packages into Designer, use the following steps:

1. Open Designer.
2. In the Outline view, right-click the Package Catalog.
3. Click Import Package.
4. Browse to the location where the Epic Base, Epic EMP Default Configuration, Epic EMP Entitlements, Epic SER Default Configuration, Epic SER Entitlements packages were downloaded.
5. Select the Epic Base package, and then the Epic (EMP or SER) Default Configuration and Epic (EMP or SER) Entitlements respective packages, for the Epic driver.
6. Click Select All to import all of the packages displayed on the screen.
7. Click OK to import the selected packages, then click OK on the successfully imported packages message.
8. After the packages are imported the driver object may be created and configured for the target environment.

## 2.10.2 Activating the Driver

The Epic driver is activated by loading the Epic Driver OpenText license key.

Note that the driver must be activated within 90 days of installation, else the driver stops working and an activation error will be displayed in the driver trace file.

Additionally, the driver must also be registered with Epic for use in the customer's Epic environments. This is done in 1 of 3 manners:

* The customer's App Orchard Point Person (AOPP) searches the Epic Connection Hub for the application name "IdentitySync – IAM Integration Module for Micro Focus IDM".
* The customer's App Orchard Point Person (AOPP) contacts their Epic App Orchard TS and provides them with the application name "IdentitySync – IAM Integration Module for Micro Focus IDM".
* The customer contacts their OpenText Account Executive who could have the driver registered on the customer's behalf.
