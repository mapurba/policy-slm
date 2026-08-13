# 7.2 Troubleshooting Driver Issues

The following known issues exist for this version of the driver:

## 7.2.1 NDSTrace shows http connection protocol on the Publisher channel

The trace shows http when https has been setup on the Publisher channel.

## 7.2.2 OutOfMemory Error

1If the driver shuts down with a java.lang.OutOfMemory error, do the following:

1. Try setting or increasing the DHOST\_JVM\_INITIAL\_HEAP and DHOST\_JVM\_MAX\_HEAP environment variables.
2. Restart the driver.
3. Monitor the driver to make sure that the variables provide enough memory.

For more information, see "[Configuring Java Environment Parameters](../../../identity-manager-48/driver_admin/data/bg0n8f8.html#bg0n8f8)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).
