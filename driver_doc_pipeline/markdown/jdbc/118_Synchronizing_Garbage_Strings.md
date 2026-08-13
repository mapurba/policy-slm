# D.10 Synchronizing Garbage Strings

*Question:*
Why is the driver synchronizing garbage strings?

*Answer:*
The database and the third-party driver are probably using incompatible character encoding. Adjust the character encoding that your third-party driver uses.

For more information, refer to [Character Encoding Values](http://java.sun.com/j2se/1.5.0/docs/guide/intl/encoding.doc.html), defined by Sun.
