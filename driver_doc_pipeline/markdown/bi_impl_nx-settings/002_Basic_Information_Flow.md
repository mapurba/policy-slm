# 1.1 Basic Information Flow

1. A user is created or granted an entitlement in the Identity Vault.
2. The Linux and UNIX Settings driver receives the Create or Entitlement event and sets RFC 2307 attributes on the User objects.
3. Platform drivers, like the Linux and UNIX driver, can use the attributes set on User objects to populate users on the platforms.
