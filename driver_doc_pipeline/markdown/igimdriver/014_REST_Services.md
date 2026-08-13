# 3.0 REST Services

The IGIM driver exposes REST APIs that enable you to perform the following operations for clients and consumers:

* Create, read, update, and delete consumers
* Obtain or delete events from the Identity Vault for a particular consumer
* Restart the driver
* View the driver filter

The APIs use HTTP methods that return results in JSON format. You can configure HTTP or HTTPS access to enable the REST APIs in the driver parameters. HTTP connections are not secure because they exchange credentials and data in clear text. You are highly recommended to use HTTPS.

The APIs are protected by using Basic Authentication, and all requests require a base64-encoded username and password included in the Authorization header. All requests to the APIs must be authenticated by using the credentials of the one user object that is security equivalent of the driver object. The collector configuration must also use the same user.

You can access the APIs after the driver is started. To invoke the APIs, use the following base URL in a browser:

```

      https://<hostname>:<port>/idv/driver
```

The APIs support GET, POST, PUT, and DELETE requests.

By default, the number of events displayed per page is 100. You can change this setting in driver parameters or by using the pageSize query parameter in the APIs.
