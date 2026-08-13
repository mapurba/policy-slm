# 3.4 Enabling Auditing for the Fanout Agent

The Fanout agent supports both XDAS and legacy auditing solutions. The files required for enabling auditing are included in the Identity Manager installation package.

For more information about configuring the auditing, see [NetIQ Identity Manager - Configuring Auditing in Identity Manager](../../../identity-manager-48/configure_auditing/data/bookinfo.html#bookinfo).

To enable XDAS auditing, navigate to the <FanoutAgent Default Installation Location>/config folder and rename the xdasconfiguration.properties.template file to xdasconfiguration.properties. For more information about configuring XDAS, see [NetIQ Identity Manager - Configuring Auditing in Identity Manager](../../../identity-manager-48/configure_auditing/data/bookinfo.html#bookinfo).

For more information about XDAS auditing, see [XDASv2 Administration Guide.](https://www.netiq.com/documentation/edir88/edirxdas_admin/data/bookinfo.html)

*NOTE:*The Fanout agent does not support XDAS event caching.
