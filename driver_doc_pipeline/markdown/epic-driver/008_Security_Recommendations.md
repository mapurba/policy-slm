# 2.3 Security Recommendations

* The Epic driver must have the ability to read objects and attributes listed in the driver subscriber filter in addition to standard Identity Manager driver security requirements.

  For more information about object synchronization, see [Synchronizing Objects](../../../identity-manager-48/driver_admin/data/b3uv74q.html#b3uv74q) in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle).
* Epic’s Web Services are accessible over HTTPS. The Epic driver must be able to connect to the Epic Interconnect server over this https connection. Ensure that any firewall rules are updated to allow the Epic driver to communicate with Epic (TCP port 443 unless otherwise configured in the Epic implementation).
* Audit User in Epic – The identifier of the record creating the new User record. Epic recommends that this field be left blank, although some implementations may require a value.
*  Epic Client ID – Starting with the February 2019 Epic build, all API calls must have a Client ID. The Epic driver uses the http header option.

  For more information, see [Activating the Driver](t4et2p5p3uml.html#t4et2p5p4pg1).
* Trust all Certs – There are security risks associated with utilizing this functionality as it can open the system to potential MIM attacks. Therefore, though it is not recommended, if the Epic system is utilizing a self-signed certificate, the “Trust All Certs” driver configuration may be enabled.
