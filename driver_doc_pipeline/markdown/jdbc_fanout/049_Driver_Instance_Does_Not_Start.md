# 7.12 Driver Instance Does Not Start

The driver instance might not start if one of the following conditions exists in your environment:

* The JDBC driver instance object is available but the corresponding named password is not created. Make sure that you are using any of the following order to create a named password and instance object:
* The third-party JDBC drivers are not included in the Fanout agent.

You must create named password and instance object in one of the following ways:

* Create a named password and add the instance object.
* Add the instance object in disabled state, add the named password, and then enable the instance object.
