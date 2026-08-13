# 8.3 Driver Security Certificates

SSL uses security certificates to control, encrypt, and authenticate communications.

Ensure that the security certificate directory /opt/novell/acf2drv/keys is appropriately protected. The installation program sets secure file permissions for this directory.

The Driver Shim and the Identity Manager engine communicate through SSL using a certificate created in the Identity Vault and retrieved by the driver shim during the installation process. For more information on this certificate and how to renew or install third-party certificates, refer to the Identity Manager Administration Guide.

The Embedded Remote Loader web interface uses a dynamically generated, self-signed certificate for SSL communication. The details of this certificate are as follows:

*Table 8-1* Security Certificate Details

| Property Name | Values / Parameters |
| Subject | SSL Server |
| Issuer | SSL Server |
| Validity | 1 year |
| Serial Number | 0 |
| Key | 1024-bit RSA |

Renewal of this certificate automatically occurs when the Driver Shim is restarted on the connected platform.
