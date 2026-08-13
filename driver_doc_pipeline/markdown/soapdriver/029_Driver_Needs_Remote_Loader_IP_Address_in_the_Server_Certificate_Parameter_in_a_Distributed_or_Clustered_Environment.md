# 9.2 Driver Needs Remote Loader IP Address in the Server Certificate Parameter in a Distributed or Clustered Environment

The SOAP driver fails to connect with the Remote Loader if the IP address of the Remote Loader is not specified in the default server certificate provided to the Remote Loader.

To workaround this issue, specify the IP address of the Remote Loader in the Subject Alternative Names parameter in Identity Console using the following steps:

1. Log in to Identity Console.
2. Click Certificate Management > Server Certificate Management.
3. Click ![](../graphics/create_certificate.png), Create Server Certificate pane appears.
4. Create a custom server certificate
5. Go to Input Parameters tab, in the Subject Alternative Names add new name and specify the Remote Loader's IP address.
6. Accept the rest of the certificate defaults.
7. Review the summary, click OK, then click Close.
