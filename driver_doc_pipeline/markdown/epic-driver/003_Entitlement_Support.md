# 1.2 Entitlement Support

The default driver configuration supports entitlements for linkable templates, sub-templates, in basket classifications, blueprints, and external identifiers in Epic. This is accomplished by exporting, from Epic, the relevant data to individual CSV files.

Sample CSV files and formats for the default entitlements are as follows:

Templates.csv (ID,NAME,DESCRIPTION)

```
T00024,CW NURSE TEMPLATE,CW Nurse
T00076,UTILIZATION MANAGER TEMPLATE,Utilization Manager
```

Subtemplates.csv (ID,NAME)

```
1050003,RADIOLOGY HEART CARE FRONT DESK TEMPLATE BUILDER HE
10801,SBO REV/USAGE SUBTEMPLATE
```

ExternalIdentifiers.csv (ID,NAME)

```
1,Document Imaging
2,Dynamic Imaging
```

InBasketClassifications.csv (ID,NAME)

```
1,Staff
2,WORKSTATION
```

Blueprints.csv (ID,NAME)

```
B10000,AMBULATORY PHYSICIAN
B10057,ANESTHESIOLOGIST
```

When a code map refresh is issued to the driver, the query results in the driver shim reading the previously exported CSV file and returning the entitlement values to IDM.
