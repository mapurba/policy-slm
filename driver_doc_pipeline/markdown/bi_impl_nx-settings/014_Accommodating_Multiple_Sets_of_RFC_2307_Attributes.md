# 5.3 Accommodating Multiple Sets of RFC 2307 Attributes

It might be desirable to have more than one set of Linux/UNIX settings attributes on a User object so the user can have different settings on different systems. For example, a user with accounts on a Linux system and a Solaris system might need a different login shell on each system.

You can extend the schema with iManager to accommodate additional attributes. Then you can modify driver policies to set the desired attribute values. Text settings can be added to the GCVs for the driver, and range attributes can be added to the NxSettings style sheet.
