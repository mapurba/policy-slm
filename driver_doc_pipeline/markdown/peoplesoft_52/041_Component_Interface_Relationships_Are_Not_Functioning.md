# 8.13 Component Interface Relationships Are Not Functioning

If data does not appear in the attributes, data isn’t getting posted into PeopleSoft, or data is missing, you should begin looking at the Component Interface relationships.

First, verify that the API is getting the data from the PeopleSoft buffer.

After all of the CIs have been tested completely with validation of all processes that the driver is configured to do, there should be no issues regarding the driver accessing PeopleSoft through the CIs. Other problem areas include:

* Connectivity IP address and port for the application server
* ID and password
* Correct naming of all activities in the parameters for the driver.

For troubleshooting these problems, try three basic tests:

1. Manually test all of the processes online using the PeopleSoft applications as configured.
2. Test all of the processes that are using the Component Interfaces.
3. Test the driver connection to the API through the Component Interfaces.
