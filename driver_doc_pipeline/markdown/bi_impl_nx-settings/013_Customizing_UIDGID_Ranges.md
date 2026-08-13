# 5.2 Customizing UID/GID Ranges

You can assign UID and GID numbers from a style sheet in the driver. Alternatively, you can use the LUM Linux/UNIX Config object to assign UID and GID numbers. For details about using the LUM Linux/UNIX Config object, see the Linux User Management Technology Guide, which is available from the [NetIQÂ® OES documentation Web site](http://www.novell.com/documentation/oes/index.html).

UID and GID ranges are defined in the NxSettings style sheet. You can edit this style sheet to modify the ranges that UIDs and GIDs are allocated from.

## 5.2.1 Editing UID/GID Ranges

*IMPORTANT:*The NxSettings style sheet holds the last assigned UID and GID number. Stop the driver before you edit this document. Failure to stop the driver before editing this document could result in the same UID or GID being assigned to multiple users or groups.

To edit the NxSettings style sheet:

1. Open iManager and navigate to the Driver Overview page for the Linux and UNIX Settings driver.
2. Click the View All Policies icon ![](../graphics/viewallpoliciesicon_n.png) to display the View All Policies dialog box.
3. Click the link to the NxSettings Stylesheet object under the Identity Manager Driver heading to display the NxSettings style sheet, then click Enable XML editing.
4. Make changes as desired. For details, see [NxSettings Style Sheet Details](b3gdtex.html#b3ge7z6).
5. Click OK.

## 5.2.2 NxSettings Style Sheet Details

The initial NxSettings style sheet is similar to the following example:

```
<?xml version="1.0" encoding="UTF-8"?><nxSettings>
  <settings name="DefaultSet">
    <setting name="uid" type="range">
      <ranges last-used="0">
        <range end="1000" start="400"/>
      </ranges>
    </setting>
    <setting name="gid" type="range">
      <ranges last-used="0">
        <range end="1000" start="400"/>
      </ranges>
    </setting>
  </settings>
</nxSettings>
```

You can change the start and end attributes of a range tag and the last-used attribute for the ranges tag. (Because the attributes are stored in alphabetical order, the end attribute of a range element is listed before the start attribute.)

You can add ranges by adding more range tags as shown in the following example:

```
<ranges last-used="0">
  <range end="1000" start="400"/>
  <range end="2000" start="1001"/>
  <range end="5000" start="3000"/>
</ranges>
```

Ranges do not need to be contiguous. If there are gaps, the driver skips over them. If the value of the last-used attribute falls outside of all ranges, then the next number is assigned from the range with the next start value. In the preceding example, the next number assigned is 400. The value assigned after 2000 is 3000.

You can also add more settings and setting tags to the style sheet for your own purposes. Do not reuse the setting name DefaultSet.

For details about retrieving values with a policy, see [Retrieving Values with a Policy](b3gy8qc.html).
