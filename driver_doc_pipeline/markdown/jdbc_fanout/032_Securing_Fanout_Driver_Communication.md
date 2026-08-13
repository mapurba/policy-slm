# 6.0 Securing Fanout Driver Communication

NetIQ recommends using Secure Socket Layer (SSL) protocols for driver communication. By default, the SSL protocol is not configured among the Fanout components. You must configure the SSL connection among the following Fanout components:

* Between the Fanout driver shim and ActiveMQ

  Refer to the following sections for instructions:

  + [Creating a Keystore and a Truststore](how-to-create-keystore-and-truststore-for-jdbc-fan-out-driver.html)
  + [Enabling SSL for the Fanout Driver Shim](how-to-enable-ssl-for-jdbc-fan-out-driver.html)
  + [Enabling SSL for ActiveMQ](how-to-enable-ssl-for-activemq.html)
* Between ActiveMQ and the Fanout agent

  Refer to the following sections for instructions:

  + [Creating a Keystore and a Truststore](how-to-create-keystore-and-truststore-for-jdbc-fan-out-driver.html)
  + [Enabling SSL for ActiveMQ](how-to-enable-ssl-for-activemq.html)
  + [Enabling SSL for the Fanout Agent](how-to-enable-ssl-for-jdbc-fan-out-agent.html)

*Figure 6-1* Secured Connection among Fanout Components of the JDBC Fanout Driver

![](../graphics/configuring_ssl_conn_in_jdbcfanoutdriver.png)

To support the SSL connections, you need to create keystore and truststore files. This section explains how to create, export, and store this certificate on your server

After the secured connection is enabled, the Fanout components perform an SSL handshake to establish a secure channel.
