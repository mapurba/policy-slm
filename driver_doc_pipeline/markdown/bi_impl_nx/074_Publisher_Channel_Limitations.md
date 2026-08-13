# C.6 Publisher Channel Limitations

The Publisher channel generates events based on modifications that are discovered by polling. Because events are interpreted after they have occurred, some assumptions must be made. This can lead to unexpected results under certain circumstances.

For example, a user might be renamed on the local Linux or UNIX system. If the user’s UID is not changed, the polling script can determine that the event is a rename, not a delete followed by an add. However, if a user is renamed and its UID is changed, the polling script must assume that this is a delete followed by an add.

You can modify the polling script to provide a more accurate approach using additional contextual clues that are specific to your particular environment. For example, you might modify the polling script behavior to additionally look at the password hash or a gecos field component to decide whether a user has been deleted or simply renamed. Preserving the user’s identity might be essential to preserving the appropriate rights and resources to another connected system.
