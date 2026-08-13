# 1.1 Supported PeopleSoft Versions

You can use the PeopleSoft driver 5.2 with PeopleTools application v8.5x or above. The PeopleSoft driver 5.2.4.0 has been certified with People Tools v8.57, v8.58, 8.59 v8.60 and v8.61.

## 1.1.1 Support for People Tools Version 8.61

Following steps allows the driver to connect to PeopleSoft using JOLT LLE:

1. Add JVM Options in identity console as:

   Go to Edit Driver Set Properties > Driver Set Configuration tab > Java Environment Parameters > JVM options. Specify -DTM\_ALLOW\_NOTLS=Y in JVM options.
2. Restart the edirectory.

Perform the below steps to connect the driver with SSL / TLS:

1. Execute the steps as mentioned in [SSL Configuration for PeopleSoft Application](t4it1bnkyo8s.html).

   *NOTE:*The default length of RSA key is 2048. To specify the minimum length allowed for RSA key, set the Java property TM\_MIN\_PUB\_KEY\_LENGTH under JVM options in identity console. For example, DTM\_MIN\_PUB\_KEY\_LENGTH=1024.
2. Restart the edirectory.
