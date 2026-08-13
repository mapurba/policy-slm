# 5.2 Configuring Authentication Between Drivers

In addition to providing the mandatory certificates needed to use SSL, you can set up additional security by configuring the Subscriber channel on one eDirectory driver to authenticate to the Publisher channel on the other driver.

Set a driver object password and application password on each driver. Make sure the driver object password of the first driver matches the application password of the second driver, and that the driver object password of the second driver matches the application password of the first driver. For example:

*Table 5-2* Driver Object and Application Passwords

|  | Driver Object Password | Application Password |
| Driver 1 | Provo | Cambridge |
| Driver 2 | Cambridge | Provo |

For information about setting the passwords, see [Driver Object Password](driver-configuration.html#driver-object-password) and [Authentication](driver-configuration.html#authentication).
