# 3.3 Gmail Settings Attributes

Several attributes are exposed for the Google Schema that update a user’s default email settings within a Google Domain. These attributes are not mapped to an eDirectory attribute but can be set on modify events.

*NOTE:*Due to limitations in the Gmail API and Directory API interactions, it is not possible to set these attributes during user creation. It is recommended that a delay of at least five seconds or more be used between the creation of a new user and any attempted setting of a Gmail Setting attribute.

The following sections provide information these attributes:

## 3.3.1 GmailSettingsDelegates

Use this attribute to add, remove, or list the assigned delegates to a user’s Gmail account. The attribute takes one of two forms: a string value which consists of the email address of the designated delegate or a distinguished name syntax with an association reference for the designated delegate for this user. The connector will take either form.

## 3.3.2 GmailSettingsEnableIMAP

Use this attribute to enable or disable the IMAP feature of a user’s account. The attribute takes two values: true or false.

This attribute does not support remove-value or remove-all-values as a user’s IMAP settings cannot be removed. Change the state of this setting with an add-value command.

## 3.3.3 GmailSettingsEnablePOP

Use this attribute to manage a user’s POP settings. This attribute takes a structured value with the following components:

* EnableFor

  + Whether to enable POP for all mail, or mail from now on.
  + Enumerated
  + Required
  + Values:

    - ALL\_MAIL
    - MAIL\_FROM\_NOW\_ON
* Action

  + What Google Mail should do with its copy of the email after it is retrieved using POP
  + Enumerated
  + Required
  + Values:

    - KEEP
    - ARCHIVE
    - DELETE
  + Enable

    - Whether to enable/disable POP access
    - Boolean

This attribute does not support remove-all-values and remove-value commands as POP settings cannot be removed from users. Send any changes as an add-value command.

## 3.3.4 GmailSettingsForwarding

Use this attribute to set and update a user’s auto-forwarding rule. The attribute takes a structured value with the following components:

* Enable

  + Whether to enable forwarding of incoming mail
  + Boolean
* ForwardAddress

  + The email address to which the email will be forwarded
  + This must be verified, which means it must satisfy one of these tests:

    - It belongs to the same domain
    - It belongs to a subdomain of the same domain
    - It belongs to a domain alias configured as part of the same G Suite account
* Action

  + What Google Mail should do with its copy of the email after forwarding it on
  + Enumerated
  + Values

    - KEEP

      * Keep it in the inbox
    - ARCHIVE

      * Archive it
    - DELETE

      * Delete it
    - MARK\_READ

      * Mark it as read

This attribute only supports add-value changes. Use an add-value command to update or disable auto-forward.

## 3.3.5 GmailSettingsLabel

This attribute can be used to list, add to, and remove from a user’s configured set of labels within Gmail. Note that the API only allows access to the user custom labels. The pre-defined system default labels cannot be manipulated with the API. The attribute accepts string syntax values representing the label to be created or removed. It supports add-value, remove-value, and remove-all-values commands.

## 3.3.6 GmailSettingsLanguage

This attribute can be used to change or display the language setting for a user’s Gmail account. Note that the values accepted and displayed by this API are strictly constrained by the API service to be in RFC 3066 language tag format.

See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/languagetags/)

The attribute is string syntax containing the language tag desired. It only supports add-value commands.

## 3.3.7 GmailSettingsSendAs

This attribute can be used to display, set, and remove SendAs aliases. A SendAs alias is a configuration on a user’s account that allows them to send mail as another name and email address. Note that the collection of SendAs alias on any user account includes a system entry, the primary SendAs, which will be displayed when queried, but cannot be removed. The attribute is structured with the following components:

* Name

  + The display name for the send as alias
* SendAs

  + The email address used for the send as alias
* ReplyTo

  + The reply-to address used for the send as alias
* isDefault

  + Whether or not this alias is the default SendAs configuration for this user
  + Takes the value of either true or false

The attribute supports add-value, remove-value, and remove-all-values.

## 3.3.8 GmailSettingsSignature

This attribute can be used to display or change a user’s signature. The attribute takes a string value which is the signature for the user and applies it to their account.

## 3.3.9 Gmail Settings Attribute Syntax and Examples

*Table 3-2* Gmail Settings Attribute Syntax and Examples

| Application Attribute Name | Syntax |  |
| GmailSettingsDelegates | DN/String |  |
| Example  This can be formatted as a distinguished name with an association-ref or as a plain string in the form of an email address of the delegate.   ```  <modify-attr attr-name="GmailSettingsDelegates">        <add-value> <value association-ref=user@mydomain.com" type="dn">/data/users/my-user</value>        </add-value> </modify-attr>  == OR == <modify-attr attr-name="GmailSettingsDelegates">        <add-value> <value type="string">user@mydomain.com</value>        </add-value> </modify-attr>  ``` | | |
|  |  |  |
| GmailSettingsEnableIMAP | Boolean |  |
| Example  <modify-attr attr-name="GmailSettingsEnableIMAP">   ```         <add-value>               <value type="string">true</value>        </add-value> </modify-attr>  ``` | | |

| Application Attribute Name | Syntax |  |
| GmailSettingsEnablePop | Structured |  |
| Example   ```  <modify-attr attr-name="GmailSettingsEnablePOP">        <add-value>               <value type="structured"> <component name="EnableFor">ALL_MAIL</component> <component name="Action">KEEP</component> <component name="Enable">true</component>               </value>        </add-value> </modify-attr>  ``` | | |
|  |  |  |
| GmailSettingsForwarding | Structured |  |
| Example   ```  <modify-attr attr-name="GmailSettingsForwarding">        <add-value>              <value type="structured"> <component name="ForwardAddress">user@domain.com</component> <component name="Action">KEEP</component> <component name="Enable">true</component>               </value>        </add-value> </modify-attr>  ``` | | |
|  |  |  |

| Application Attribute Name | Syntax |  |
| GmailSettingsLabel | String |  |
| Example   ```   <modify-attr attr-name="GmailSettingsLabel">        <add-value>               <value type="string">MyProject</value>        </add-value> </modify-attr>  ``` | | |
|  |  |  |
| GmailSettingsLanguage | String |  |
| Example   ```  <modify-attr attr-name="GmailSettingsLanguage">        <add-value>               <value type="string">Eng</value>        </add-value> </modify-attr>  ``` | | |
|  |  |  |

| Application Attribute Name | Syntax |  |
| GmailSettingsSendAs | Structured |  |
| Example   ```   <modify-attr attr-name="GmailSettingsSendAs">        <add-value>               <value type="structured"> <component name="Name">My Name</component> <component name="SendAs">name@idmtest.org</component> <component name="ReplyTo">name@idmtest.org</component> <component name="IsDefault">true</component>               </value>        </add-value> </modify-attr>  ``` | | |
|  |  |  |
| GmailSettingsSignature | String |  |
| Example   ```   <modify-attr attr-name="GmailSettingsSignature">        <add-value>               <value type="string">Signature Data</value>        </add-value> </modify-attr>  ``` | | |
