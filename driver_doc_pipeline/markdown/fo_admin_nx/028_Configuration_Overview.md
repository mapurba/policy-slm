# 6.1 Configuration Overview

Before beginning, remember that the Fan-Out Driver includes two principal parts: the Core Driver and Platform Services. Information in this section focuses on the Core Driver’s configuration, and additional configuration will need to be performed on each platform.

## 6.1.1 Core Driver Configuration

Core Driver configuration information is maintained in the Driver object and in objects in the ASAM System container. The Core Driver installation process creates the initial configuration.

You use iManager to maintain the configuration information.

* For information about managing the Driver object configuration parameters, see [Driver Object Configuration Parameters](br3n4tb.html#cegdedii).
* For information about managing the objects in the ASAM System container, see [Applications For Configuration](chdijbdi.html) and [Management Tasks](br3n4tb.html).

You also can use the Driver Shim configuration file to make setting about how the Core Driver communicates with Platform Services. For information about options in the fanout.conf file see [The Driver Shim Configuration File](b4baik6.html).

## 6.1.2 Platform Services Configuration

The Core Driver maintains configuration objects that represent each target platform for its own use in the ASAM System container.

Target platforms each obtain local configuration information from their respective platform configuration file. For more information about the platform configuration file, see [Section III, Platform Services Planning](bexh6ay.html).
