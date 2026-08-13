# B.2 Default Required Attribute Settings

*Table B-2* Global Configuration Values - Default Required Settings on New Blackboard Objects

| Name | Display Name | Description | Default Value |
| auto\_set\_ids | Automatically set the required Id attribute for new Person, Course, and Organization objects to the source name of the object. | If true then the required id attribute for Person, Course, and Organization types in Blackboard will be automatically set to Source Name if the id attribute is not already set. The attributes are DirXML-BB-p-id for Person, DirXML-BB-c-id for Course, and DirXML-BB-o-id for Organization. | True |
| auto\_set\_title | Automatically set the required title attribute for new Course, and Organization objects to the source name of the Group. | Automatically set required attribute DirXML-bb-c-course-title to the source name for Course objects if it is not already set. Automatically set required attribute DirXML-bb-o-title to source name for Organization objects. | True |
| auto\_set\_roles | Automatically set the required user roles attributes for Person objects. | If true the default roles chosen below will be set for a user if they are not present on the user object. | True |
| default\_user\_role | Default System Role for new users | N/A | USER |
| default\_portal\_role | Default Institutional Role for new users.  Example: STUDENT, STAFF, ALUMNI, GUEST, FACULTY, OBSERVER, or any custom defined roles | N/A | STUDENT |
| add\_aux\_classes | Automatically add a required Blackboard auxiliary class to Person and Course or Organization objects. | If true automatically add the DirXML-BB-Person auxiliary class to Person objects and the DirXML-BB-Course auxiliary class to Course or Organization objects. | True |
| bb-course-subtree | Apply DirXML-BB-Course to groups in the following subtree | N/A | N/A |
| bb-organization-subtree | Apply DirXML-BB-Organization to groups in the following subtree. | N/A | N/A |
| auto\_set\_email | Automatically set required Person attribute DirXML-BB-p-email if it is not set. | N/A | True |
| default\_email\_domain | Domain name to use for default email address. | Email address is a required attribute for a Person in Blackboard. This value will be used to set the email address attribute in Blackboard for users who do not have an email address specified in their eDirectory User object. The CN of the user will be used with the value provided to create the email address. | N/A |
