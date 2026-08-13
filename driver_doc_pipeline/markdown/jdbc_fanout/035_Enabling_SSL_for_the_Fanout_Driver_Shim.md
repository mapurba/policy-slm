# 6.3 Enabling SSL for the Fanout Driver Shim

1. Copy the client.ks and client.ts files to the Identity Manager server.
2. Edit the following driver properties using Designer:

   * *AMQ Keystore Path:*
     Specify the client.ks path.
   * *AMQ Keystore Password:*
     Specify the password for client.ks.
   * *AMQ Truststore Path:*
     Specify the client.ts path.
   * *AMQ Truststore Password:*
     Specify the password for client.ts.
3. Save the configuration changes.
4. Deploy the driver.
