# 11.4 Uninstalling Platform Services

Your installation of Platform Services includes an uninstall script for easy removal of the product from a target platform. If your installation included the use of PAM (or LAM for AIX), you must manually remove those components before running the uninstall script.

## 11.4.1 Removing PAM

If you have configured your system to use the Fan-Out Driver PAM module for authentication, make sure you first remove the Fan-Out Driver Platform Services module, ascauth, from your PAM configuration before uninstalling the product. Leaving PAM with invalid library references can leave your system in an unpredictable state for new logon requests.

## 11.4.2 Removing LAM

If you have configured your system to use the Fan-Out Driver LAM module (/usr/lib/security/DCE) for authentication, make sure you first remove any LAM-related modifications you made to the following files:

```
  /etc/security/user
  usr/lib/security/methods.cfg
```

## 11.4.3 Running the Uninstall Script

To uninstall Platform Services, run the following script:

```
  /usr/local/ASAM/bin/PlatformServices/plat-uninstall
```
