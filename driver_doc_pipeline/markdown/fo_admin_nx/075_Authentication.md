# 12.3 Authentication

Users associated with a connected Linux or UNIX platform managed by the Fan-Out Driver can authenticate in any of the following ways, depending on how you have installed Platform Services.

* [Local Authentication](bfqqmfq.html#bfqqxxq)
* [Authentication Redirection](bfqqmfq.html#bfqqztf)
* [Authentication Redirection with Local Failover](bfqqmfq.html#bfqr0u7)
* [Name Service Switch Authentication](bfqqmfq.html#bfqr1fu)

## 12.3.1 Local Authentication

With local authentication, passwords are stored locally (in /etc/shadow for example) and users that log onto the Linux or UNIX system will authenticate with this password. To synchronize passwords with the Identity Vault, ensure the following keyword statement is located inside your asamplat.conf file:

```
  UPDATEPASSWORD
```

*NOTE:*If you use the UPDATEPASSWORD statement, you also may include a CRYPTTYPE statement in the asamplat.conf file.

The CRYPTTYPE statement allows you to override the password storage format (DES, MD5, BLOWFISH, SHA256, SHA512 or SUN\_MD5) that is automatically configured by the driver. For more information, see [CRYPTTYPE Statement](beiffigc.html#bucg2ea).

The Platform Receiver (asamrcvr file) needs to be running to keep passwords synchronized with the Identity Vault. For more information, see [Starting the Platform Receiver](bfmrhmm.html#bfn7bkm).

## 12.3.2 Authentication Redirection

With redirected authentication, passwords are not stored locally. Instead, when a user logs on to the Linux or UNIX system, the Fan-Out Driver’s PAM (or LAM) module will redirect the request to the Identity Vault, where the password is checked along with eDirectory Password and Login rules. Optionally, password policies can be enforced.

To configure your system to use the PAM module for authentication redirection, you will need to manually configure PAM for each application that is to be PAM-enabled. For details on manually configuring PAM, see [PAM Configuration Notes](chdibedb.html).

If you are running AIX and chose to use LAM for authentication redirection, you will need to manually configure LAM as detailed in [LAM Configuration Notes](brk5h3s.html).

The Platform Services Process (asampsp file) also needs to be running to provide a connection pool and driver load balancing. For more information, see [Starting the Platform Services Process](bfmrhmm.html#bfn7ho4).

## 12.3.3 Authentication Redirection with Local Failover

Authentication redirection with local failover is a hybrid of local authentication and authentication redirection. In such a scenario, authentication is redirected unless the connection between Platform Services and the Identity Vault is unavailable, in which case local authentication takes place. In this configuration, you will need the Platform Receiver running to synchronize passwords and the Platform Services Process running to provide authentication. For information about starting these two services, see [Starting Platform Services](bfmrhmm.html#bfmrj2a).

## 12.3.4 Name Service Switch Authentication

If you have chosen the virtual provisioning option (see [Provisioning](bfqqm8v.html)), users will authenticate to the Linux or UNIX system using the Name Service Switch, which is supplied by Platform Services. Virtual users and their password information are kept in a local protected cache on the connected system. This provides the system with a local copy and therefore all the advantages of using local provisioning. If you wish to enforce eDirectory password and login rules, you will also need to manually configure PAM for authentication redirection.
