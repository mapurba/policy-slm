# 7.5 Changing ActiveMQ Log Levels

You can view information about an event in transit or waiting state in the ActiveMQ Web console. By default, ActiveMQ displays log messages with a verbosity of INFO and WARN. You can change the log levels in ActiveMQ in the <Apache ActiveMQ Installation Location>/conf/log4j.properties file.

For example, to see log messages for more verbose levels such as DEBUG, add the following line to the log4j.properties file:

```
log4j.logger.org.apache.activemq=DEBUG
```
