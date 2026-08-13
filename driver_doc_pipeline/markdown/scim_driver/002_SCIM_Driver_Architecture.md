# 1.1 SCIM Driver Architecture

The following diagram illustrates the bi-directional relationship between Identity Manager and the connected application.

*Figure 1-1* Architecture of SCIM Driver

![](../graphics/scim_architecture.png)

The Identity Manager engine and eDirectory reside on a single host computer. The SCIM Driver Module is Java based driver, that can execute on the same host system, or on a Remote Loader instance. The Identity Manager Engine loads the driver module dynamically.

The Identity Manager engine uses XDS (a specialized form of XML) to represent events in the Identity Manager. In the Subscriber channel, the XDS events from Identity Manager are converted to SCIM compliant JSON using policy conversions. The driver operation data in the driver shim, converts the SCIM compliant JSON to the appropriate HTTP requests or responses to communicate with the connected application.

In the Publisher channel, the driver fetches data from the connected application using the conversion policy. The connected application processes the request, and returns a HTTP response to the driver shim. The Publisher channel periodically polls for additions and modifications of the objects in the connected application.
