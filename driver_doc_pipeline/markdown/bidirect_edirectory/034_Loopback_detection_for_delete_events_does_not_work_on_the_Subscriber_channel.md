# 10.9 Loopback detection for delete events does not work on the Subscriber channel

A delete event from the Identity Vault is looped back on the Publisher channel even if loopback detection is enabled on the Publisher channel. This causes an additional event in the Publisher channel. However, the engine ignores the additional event and there is no functionality loss.

Loopback detection for delete events does not work in Bi-directional driver. For the delete events, the eDirectory doesn't provide the modifier's (deleter's) name. As a result, the changelog module is not able to flag the Loopback event for delete events. Since the changes are same, the engine ignores it.

*NOTE:*This issue is not reported on add or modify events.
