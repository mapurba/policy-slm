# 2.7 Setting Up ActiveMQ Startup Service

This section provides details about setting up ActiveMQ as a startup service.

* [Enabling the ActiveMQ Service on Linux](how-to-setup-activemq-startup-service.html#b1ingazo)
* [Enabling the ActiveMQ Service on Windows](how-to-setup-activemq-startup-service.html#b1ingazp)

## 2.7.1 Enabling the ActiveMQ Service on Linux

1. Set the path for the JAVA\_HOME environment variable.
2. Set the path for the ACTIVEMQHOME environment variable in the /root/.profile file to point to the ActiveMQ installation location. The .profile file needs to be created if it does not exist.
3. Navigate to the ActiveMQ installation directory and run activemqAddSvc by executing the following command:

   ./activemqAddSvc
4. To start the ActiveMQ service, execute the following command:

   /etc/init.d/activemqdxml start

To stop the ActiveMQ service, execute the following command:

/etc/init.d/activemqdxml stop

## 2.7.2 Enabling the ActiveMQ Service on Windows

To add the ActiveMQ service to the Windows services list, navigate to ACTIVEMQ\_HOME/bin/win64 and run InstallService.bat.

This creates the ActiveMQ service in the Windows service list. This service automatically starts when the system reboots.

To remove the ActiveMQ service from the Windows services list, run UninstallService.bat.
