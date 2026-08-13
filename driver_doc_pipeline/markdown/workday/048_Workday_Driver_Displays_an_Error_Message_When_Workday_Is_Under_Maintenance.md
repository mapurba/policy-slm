# 9.5 Workday Driver Displays an Error Message When Workday Is Under Maintenance

Workday driver displays the following error message when the driver requests for time stamp from the Workday server and if the server is under maintenance.

```
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><SOAP-ENV:Fault xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wd="urn:com.workday/bsvc"><faultcode>SOAP-ENV:Client.validationError</faultcode><faultstring>Invalid request</faultstring></SOAP-ENV:Fault></SOAP-ENV:Body></SOAP-ENV:Envelope>
```

This is assumed that the Workday server is under maintenance when you receive this error while requesting for time stamp.
