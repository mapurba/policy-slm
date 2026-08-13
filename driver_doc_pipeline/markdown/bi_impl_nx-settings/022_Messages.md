# C.0 Messages

The Identity Manager driver for Linux and UNIX Settings appends status elements containing message text to XDS commands as necessary to report unexpected conditions. You can view these in a trace. The driver produces the following status messages:

Error finding sambaSID object for context userDN Error finding sambaSID object searchDN

Explanation:
The sambaSID could not be determined for a user. The samba SID is stored in the sambaSID attribute of a sambaDomain object. The sambaDomain object is located by searching the user’s container, and then each higher container up the tree until a sambaDomain object is located. The user’s sambaSID is set to the sambaSID of the sambaDomain object concatenated with a hyphen and the value of the user’s uidNumber attribute.

The sambaDomain object is created when NetIQ® Samba is configured on OES using YaST.

Possible Cause:
A sambaDomain object does not exist in the same context as the User object or in a parent container of the User object.

Action:
Create a sambaDomain object in the same context as the User object or in a parent container of the User object.

Error searching for uidInUse searchDN Error searching for gidInUse searchDN

Explanation:
The driver received an error from Identity Manager while checking to see if a uidNumber or gidNumber is already in use.

Possible Cause:
The searchDN is not valid.

Action:
Ensure that the searchDN is correct. You can modify the searchDN with GCVs for the driver. These are located under the Data Integrity heading. Inspect and modify the following settings if necessary:

* Subtree to Search for Existing UIDs to Avoid Duplicate UID Assignment
* Subtree to Search for Existing GIDs to Avoid Duplicate GID Assignment

Could not retrieve LUM object UnixConfigDN

Explanation:
The driver could not locate the Linux/UNIX Config object used to hold UID and GID information for LUM.

The Linux/UNIX Config object is created when LUM is configured on OES using YaST.

Possible Cause:
The Linux/UNIX Config object is not at the location specified by the GCV named LUM Linux/UNIX Configuration Object DN.

Action:
Ensure that the GCV named LUM Linux/UNIX Configuration Object DN is set to the DN of an existing Linux/UNIX Config object.

Error finding NxSettings document

Explanation:
The driver could not locate the NxSettings Stylesheet object that holds UID and GID information.

Possible Cause:
The NxSettings Stylesheet object has been deleted, or an error occurred when the driver was imported.

Action:
Import the driver again.

Setting set settingSetName not found

Explanation:
The policy uses XPath calls to retrieve settings from the NxSettings Stylesheet object. A settings element name was referenced that does not exist in the NxSettings Stylesheet object.

Possible Cause:
A settings element name that does not exist in the NxSettings Stylesheet object was referenced in a policy.

Action:
Ensure that the policy does not reference a settings element name that does not exist.

In the following code snippet, DefaultSet is the settings name:

```
<token-xpath expression='driverShim:getNextGIDFromXMLDoc($driverShimInstance,"DefaultSet", "gid", $searchBase)'/>
```

The settings name DefaultSet is defined in the following NxSettings Stylesheet object:

```
<?xml version="1.0" encoding="UTF-8"?>
<nxSettings>
  <settings name="DefaultSet">
    <setting name="uid" type="range">
      <ranges last-used="601">
        <range end="56500" start="600"/>
      </ranges>
    </setting>
    <setting name="gid" type="range">
      <ranges last-used="601">
        <range end="56500" start="600"/>
      </ranges>
    </setting>
  </settings>
</nxSettings>
```

Setting settingName not defined in setting set settingSetName

Explanation:
The policy uses XPath calls to retrieve settings from the NxSettings Stylesheet object. A setting element name was referenced that does not exist in the NxSettings Stylesheet object.

Possible Cause:
A setting element name that does not exist in the NxSettings Stylesheet object was referenced in a policy.

Action:
Ensure that the policy does not reference a setting element name that does not exist.

In the following code snippet, gid is the setting name:

```
<token-xpath expression='driverShim:getNextGIDFromXMLDoc($driverShimInstance,"DefaultSet", "gid", $searchBase)'/>
```

The setting name gid is defined in the following NxSettings Stylesheet object:

```
<?xml version="1.0" encoding="UTF-8"?>
<nxSettings>
  <settings name="DefaultSet">
    <setting name="uid" type="range">
      <ranges last-used="601">
        <range end="56500" start="600"/>
      </ranges>
    </setting>
    <setting name="gid" type="range">
      <ranges last-used="601">
        <range end="56500" start="600"/>
      </ranges>
    </setting>
  </settings>
</nxSettings>
```
