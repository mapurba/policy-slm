# B.2 Creating Home Directories

You can use the user template to create home directories in the destination eDirectory. In the policy, set the value for the Set Operation Template DN (do-set-op-template-dn) as the DN of the template that is used to create the home directory.

*NOTE:*You must also set Create Home Directory to Yes on the User class in the driver filter.

*Example B-1* Example

```
    <actions>
        <do-set-op-template-dn>
        <arg-dn>
              <token-text xml:space="preserve">Data\Users\UserCreationTemplate</token- text>
        </arg-dn>
        </do-set-op-template-dn>
    </actions>
```
