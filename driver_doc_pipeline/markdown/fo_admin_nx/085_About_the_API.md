# 14.0 About the API

NetIQ® Identity Manager Fan-Out Driver platforms provide an Authentication Services (AS) application programming interface (API) that can be used by applications to access eDirectory™. This API is compatible with the AS Client API that was provided in the NDS® Authentication Services and the Account Management 3.0 products. To use this API, you must obtain and install the Identity Manager Fan-Out Driver.

The platform configuration file provides the information necessary for establishing communications with a Core Driver. For details about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).

In the C language environment, a call must be made to ASC\_INIT() or ASC\_INIT\_EXT() to process the platform configuration file and initialize the environment before API calls can be made to the Core Driver. The header file ascauth.h provides the function prototypes for the API calls and their return value definitions.

In the Java environment, a call must be made to the INIT() method to process the platform configuration file and initialize the environment before API calls can be made to the Core Driver. Class com.novell.asam.JAscAuth.JAscAuth provides the methods used to call the API.

Details about platforms/environments with which you use the API are provided in earlier sections of this guide. Also be aware that this guide is one of three available administration guides for the Fan-Out Driver, each tailored to the range of platforms with which it can work:

* Identity Manager Fan-Out Driver for Linux and UNIX Administration Guide
* Identity Manager Fan-Out Driver for Mainframes Administration Guide (z/OS)
* Identity Manager Fan-Out Driver for Midrange Administration Guide (IBM i, OS/400, i5/OS)

Topics in this section are

* [Using the API in the Linux/UNIX Environment](chddebjb.html)
* [API Function List](chdifjfj.html)
