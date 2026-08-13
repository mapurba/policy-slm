# B.1 General Settings

*Table B-1* Global Configuration Values - General Settings

| Name | Display Name | Description | Default Value |
| use\_entitlements | Enable the driver to use Approval Flow or Role-Based Entitlements with the Entitlements Service driver. | N/A | N/A |
| use\_scope\_filtering | Limit the driver to a base container in the Identity Vault for synchronization? | Limit events the driver processes to a base container in eDirectory | True |
| container\_scope\_filter\_user | Specify the base container in the Identity Vault for User synchronization. | This container is used in the Subscriber channel Event Transformation policies to limit the Identity Vault objects being synchronized. For example: [users.myorg] | N/A |
| container\_scope\_filter\_group | Specify the base container in the Identity Vault for Group synchronization. | This container is used in the Subscriber channel Event Transformation policies to limit the Identity Vault objects being synchronized. For example: [groups.myorg] | System |
| disable\_or\_delete\_enrollments | What action should be taken on an enrollment when a Person is removed from a Group? | If set to Delete enrollments dropped from a Group will result in the Person being removed from the Course or Organization. If set to Disable the Person's enrollment will be disabled in the Course or Organization. | Delete |
