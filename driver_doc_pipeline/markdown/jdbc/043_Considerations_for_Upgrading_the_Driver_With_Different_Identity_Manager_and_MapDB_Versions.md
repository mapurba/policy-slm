# 7.3 Considerations for Upgrading the Driver With Different Identity Manager and MapDB Versions

If the newer driver includes a different version of state file persistence API (MapDB or ZoomDB), then the upgraded driver in a triggerless mode can no longer make use of the state files from the old driver. The below table provides details about the state persistence API versions that can help you determine whether the existing state files will continue to work with the newer driver version.

| Identity Manager Version | Persistence API Version | JDBC Driver Version | State File |
| Identity Manager 4.7 | mapdb 3.0.5 | 4.1.0.1 | jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8 |
| Identity Manager 4.6.3 | mapdb 1.0.9 | 4.0.5.0 | * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8 * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8.p * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8.t |
| Identity Manager 4.6 | mapdb 1.0.9 | 4.0.3.0 | * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8 * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8.p * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8.t  *NOTE:*The version of the driver version shipped with Identity Manager 4.6 is 4.0.3.0. However, the version of the driver shipped with Identity Manager 4.5.6 is 4.0.4.1. Therefore, when moving from version 4.5.6 to 4.6, ensure that you upgrade the driver to 4.0.4.1. |
| Identity Manager 4.5.6 | mapdb 1.0.8 | 4.0.4.1 | * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8 * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8.p * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8.t |
| Identity Manager 4.5 | mapdb 1.0.4 | 4.0.0.2 | * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8 * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8.p * jdbc\_e53fdaf6-b825-4074-8cf5-f6da3fe525b8.t |

*NOTE:*Prior to Identity Manager 4.x, the extension of driver state files was <tao number>.db or .lg.
