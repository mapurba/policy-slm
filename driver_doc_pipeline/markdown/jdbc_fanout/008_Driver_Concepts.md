# 1.7 Driver Concepts

* *Connection Objects:*
  Connection objects are instances of the DirXML-Resource class. Each connection object holds authentication information of the server or database you are connecting to and the trace information for the instances that the Fanout agent configures and loads. For more information, see DirXML-Data.

  The Fanout driver uses the following attributes of the connection object to determine the status of the connection object:

  + *DirXML-ContentType:*
    The driver uses this attribute to determine if it is a connection object or any other driver resource. To qualify for a connection object, this attribute should have one of the following values:

    - *application/vnd.novell.dirxml.fanout+xml:*
      This MIME value signals that the current connection object is disabled.
    - *application/vnd.novell.dirxml.fanout-enabled+xml:*
      This MIME value signals that the current connection object is enabled.

    Enabled connection objects are loaded by the Fanout agent.
  + *DirXML-Data:*
    This attribute contains the connection and trace information for the JDBC driver instance. The following is a sample of the XML document that DirXML-Data contains:

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <connection>
       <authentication-info>
          <server>jdbc:jtds:sqlserver://111.111.1.1:1433/idm</server>
          <user>idm</user>
       </authentication-info>
       <trace-info>
          <driverTraceFile>/home/sqlserver2.log</driverTraceFile>
          <driverTraceLevel>5</driverTraceLevel>
          <driverTraceFileSize />
       </trace-info>
       <connection-password-ref display-name="Connection Password" name="com.fanout.conn.passwd">
          <value>fanout.connection_2.passwd</value>
       </connection-password-ref>
    </connection>
    ```

    The JDBC Fanout driver supports three trace levels. For information about what each trace level contains, see [Setting Up Trace Levels](set-jdbc-fan-out-trace-levels.html). For more information about the trace levels supported by generic JDBC driver, see [Trace Levels](../../jdbc/data/define-trace-levels-for-jdbc-driver.html#define-trace-levels-for-jdbc-driver) in the [NetIQ Identity Manager Driver for JDBC Implementation Guide](../../jdbc/data/netiq-identity-manager-driver-for-jdbc.html#netiq-identity-manager-driver-for-jdbc).

    To change the connection or trace information for a JDBC Fanout driver instance in Designer:

    1. In the Outline view or Modeler, right-click the driver icon, then select Fanout Configuration.
    2. In the Fanout configuration page, select the driver instance in the left navigation and change the driver’s connection or trace settings.
    3. To save the changes, click Save in Designer’s main menu.
    4. Deploy the driver.

* *Filter:*
  The driver filter includes two additional classes: DirXML-Resource and DirXML-Driver to allow you to handle dynamic changes to the connection objects. The changes made to the connection objects do not require you to restart the Fanout driver. Depending on the changes made to the connection objects, the Fanout agent restarts or stops the JDBC driver instances.

For more information about the general concepts of the JDBC driver, see [Understanding the Identity Manager Driver for JDBC](../../jdbc/data/introduction-to-identity-manager-jdbc-driver.html#introduction-to-identity-manager-jdbc-driver) in the [NetIQ Identity Manager Driver for JDBC Implementation Guide](../../jdbc/data/netiq-identity-manager-driver-for-jdbc.html#netiq-identity-manager-driver-for-jdbc).
