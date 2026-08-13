# 8.5 The Platform Services Process

The Platform Services Process provides the Authentication Services interface to eDirectory by communicating with the Core Driver. This interface is called by the System Intercept for such functions as checking a user's password at log in. It is also used by the Authentication Services (AS) Client API to provide eDirectory access to your own applications. For details about using the AS Client API, see [Section V, API Development](bexh68d.html).

The Platform Services Process maintains persistent connections with Core Drivers for Authentication Services and performs load balancing and failover.

The Platform Services Process obtains configuration information, such as the location of Core Drivers, from the platform configuration file. For additional information about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).

On platforms where the volume of traffic with Core Drivers is so low that running the Platform Services Process is not justified by the performance benefits, you can connect the System Intercept and AS Client API directly to core services. For details, see [DIRECTTOAUTHENTICATION Statement](beiffigc.html#chdecfdc).
