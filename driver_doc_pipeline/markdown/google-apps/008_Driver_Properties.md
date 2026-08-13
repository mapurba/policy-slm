# 3.1 Driver Properties

The Driver Properties page (right click on the driver in Designer and choose Properties from the menu) contains all the items that the driver needs to startup and connect to Google.

The following sections provide information on driver properties:

## 3.1.1 Driver Configuration

### Driver Module Tab

* This tab sets the Java class name or allows configuring for remote loader.

### Authentication Tab

Application ID:
:   The admin account whose rights are used by the driver to do work inÂ theÂ GÂ Suite domain.

Connection Information:
:   The primary domain name of the GÂ Suite domain.

Set Password:
:   As the driver uses the OAuth2 service account for authentication, thisÂ password is unnecessary.

    If you are configuring the remote loader, set up that authentication information here.

### Startup Option

Auto start:
:   The driver will start when the eDirectory server starts.

Manual:
:   The driver will start only from user interaction in iManager or Designer.

Disabled:
:   The driver will not start, and no events will be cached for the driver.

### Driver Parameters

#### Driver Options

Service Account Email Address:
:   Email address associated with the Service Account credential created in Google Developers Console

P12 Private Key File:
:   Path and filename of credential file associated with Service Account credential created in Google Developers Console

#### Subscriber Options

Hash passwords before sending them to Google:
:   Set this value to true to cause the driver to hash passwords being set on GÂ Suite users.

#### Publisher Options

Publisher Heartbeat Interval:
:   If you have policies which need to fire periodically on the publisher channel, set the heartbeat interval value here. The driver will send a heartbeat message to the Identity Manager engine each time the interval expires. This feature is not used in the GÂ Suite driver.

## 3.1.2 GVCs

### Account Tracking Tab

* Account Tracking is documented by Micro Focus documentation

### Managed System Information Tab

* Managed System Information is documented by Micro Focus documentation

### User Settings Tab

* Entitlement settings for User objects
* RBPMS Settings

### Groups Settings Tab

* This tab is currently not used by the driver config.

### Google Config tab

Google Apps Primary Domain Name:
:   This is the domain name of the primary GÂ Suite domain to which the driver is connecting.

Google Apps Secondary Domain Names:
:   This is a list of secondary Google domain names the driver can service.

### Password Settings Tab

* Google Apps Password Settings configures how passwords are generated for new users being created in GÂ Suite.

  + You can select using a random password, specifying how many characters and numbers are required.
  + You can select using a value from an existing attribute.
* Password Synchronization: configures policy configurations around how passwords are synchronized from the ID Vault to GÂ Suite for a given user.

### OU Settings Tab

User placement settings:
:   This variable controls placement policies to not generate placement, use Mirrored placement, or Entitlement based placement.

Advanced RBPM Settings

The last tab in the list is named using the driver name and is intended to be a bucket for administrators to place their own GCV definitions.

## 3.1.3 Trace

Trace Level:
:   For normal production use this value should be set to 0. For driver testing and debug information set this to trace level 3. Trace level 5 is used to dump more information about the driver operations between GÂ Suite and the Driver Shim. Trace level 6 provides debug messaging and is not recommended for routine use. Trace level 6 is the highest level at which any G Suite driver debug messages are written.

Trace file:
:   If you are tracing you should set the path and name of the file you want to trace to. For example, /var/log/googleappsdriver.log. If you set this option, ensure to set the Trace file size limit as it defaults to Unlimited.

Trace file encoding: Recommended not to change from default settings

Trace file size limit:
:   Typically set to no more than 1024 MB.

Trace name:
:   Typically set to GoogleApps. This is not a required entry.
