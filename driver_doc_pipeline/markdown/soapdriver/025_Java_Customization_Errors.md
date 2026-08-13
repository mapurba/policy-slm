# 8.2 Java Customization Errors

The following errors might occur in the customized Java extensions:

* [SchemaReporter init problem: extension-specific message](cacijgdi.html#b8ucgt5)
* [Extension (custom code) init problem: extension-specific message](cacijgdi.html#b8uci3b)
* [Various other errors](cacijgdi.html#b8ueynp)

SchemaReporter init problem: extension-specific message

Source:
The status log or DSTrace screen.

Explanation:
The SchemaReporter Java customization had a problem initializing, and the driver shuts down.

Possible Cause:
The Java extension is not initialized correctly.

Action:
Verify the Java extension is enabled in the driver.

Level:
Fatal

Extension (custom code) init problem: extension-specific message

Source:
The status log or DSTrace screen.

Explanation:
One of the following Java extensions failed to initialize:

* SubscriberTransport
* PublisherTransport
* DocumentModifiers
* ByteArrayModifiers

Possible Cause:
The Java extension is incorrect.

Action:
Review the Java extension and verify that it is enabled in the driver.

Level:
Fatal

Various other errors

Source:
The interfaces provided for Java extensions return error messages on the trace screen and sometimes to the Identity Manager engine.

Explanation:
Sometimes it is difficult to distinguish errors of this type from other errors that originate in the core driver shim. If you get errors that are not listed in this section and you are using Java extensions, check with whomever provided you with the extensions for a list of error codes for that particular extension.

Level:
Varies
