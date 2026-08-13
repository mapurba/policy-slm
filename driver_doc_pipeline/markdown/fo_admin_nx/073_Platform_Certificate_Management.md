# 12.1 Platform Certificate Management

Connections between Platform Services and Core Drivers use Secure Sockets Layer (SSL). SSL connections are authenticated through the use of certificates.

The certificates used by the Identity Manager Fan-Out Driver are minted by the Certificate Services component of the Core Driver. When you install and configure Platform Services, you obtain a certificate.

To obtain a new certificate for your platform, run the plat-config script and select option 1.

Platform certificates are stored in the ASAM/data/platformservices/certs directory. Ensure that access to the certs directory is limited to the appropriate users.
