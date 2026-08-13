# 14.1 Using the API in the Linux/UNIX Environment

Access to the API using C in the Linux/UNIX environment is through calls to the shared library. The shared library and the C header file ascauth.h are copied to system-specific directories during the Linux/UNIX Platform Services installation process.

Access to the API using Java is through calls to the methods of class com.novell.asam.JAscAuth.JAscAuth. The jascauth.jar file is copied to the ASAM/bin/PlatformServices/PlatformClient/Java directory during Platform Services installation.

The caller must have read access to the /usr/local/ASAM/data/PlatformServices/certs directory.

For additional information about the Linux/UNIX platform, see the Identity Manager Fan-Out Driver for Linux and UNIX Administration Guide.
