# 5.2 Installing on Linux

You need to install the integration module as the root user.

1. Download the Integration Module (driver shim) for Sentinel, sentinel\_driver\_install\_linux.bin, from the [NetIQ Download Web site](https://dl.netiq.com/).
2. Execute the sentinel\_driver\_install\_linux.bin file on the Linux machine, which is either the Identity Manager server or the Remote Loader, depending on where you want to install the driver shim.

   * If the Linux machine has a windowing system, execute the installer in GUI mode by using the following command:

     ```
     <path>/sentinel_driver_install.bin
     ```
   * If the Linux machine does not have a windowing system, execute the installer in console mode by using the following command line:

     ```
     <path>/sentinel_driver_install_linux.bin -i console
     ```
3. Follow the installer prompts.
