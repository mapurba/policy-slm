# 4.2 Attributes and Values for Blackboard Enumeration Types

The following tables list valid values for enumeration type attributes supported by the driver.

*Table 4-6* DirXML-BB-Course Enumeration Types And Valid Values

| Enumeration Type Attribute | Valid Values | Description |
| DirXML-BB-c-duration-type | Continuous | Course is active on an ongoing basis. |
| DateRange | Course is only intended to be available between specific date ranges. |
| FixedNumDays | Course is only available for a set number of days. |
| DirXML-BB-c-enrollment-type | EmailEnrollment | Instructors have the ability to enroll users, and students can email requests to the instructor for enrollment. |
| InstructorLed | Enrollment tasks for the course can only be performed by the instructor. |
| SelfEnrollment | Instructors have the ability to enroll users, and students can also enroll themselves in the course. |

*Table 4-7* DirXML-BB-Person Enumeration Types And Valid Values

| Enumeration Type Attribute | Valid Values | Description |
| DirXML-BB-p-educ-level | Freshman | College or university freshman. |
| GraduateSchool | Graduate school student. |
| HighSchool | Grades 9 through 12. |
| Junior | College or university junior. |
| K8 | Kindergarten through 8th grade. |
| PostGraduateSchool | Post-graduate school student. |
| Senior | College or university senior. |
| Sophomore | College or university sophomore. |
| Unknown | Education level is not known, or not specified. |
| DirXML-BB-p-gender | Female | Female. |
| Male | Male. |
| Unknown | Gender is not known, or not specified. |
| DirXML-BB-p-sys-role | AccountAdmin | Account Administrator role. |
| CourseCreator | Course Creator role. |
| CourseSupport | Course Support role. |
| Guest | Guest role. |
| Integration | This role is private, used only for special processes that interact for data integration authentication. |
| Observer | Observer role. |
| Portal | Portal Administrator role. |
| SystemAdmin | System Administrator role. |
| SystemSupport | System Support role. |
| User | Normal user role. |
| (User-defined system roles) | To set a user-defined system role, click the Blackboard Administrator Panel > System Role and select a Role ID. |

*Table 4-8* DirXML-BB-Enrollment Enumeration Types And Valid Values

| Enumeration Type Attribute | Valid Values | Description |
| DirXML-BB-enr-role | CourseBuilder | The Course Builder role has access to most areas of the Control Panel. This role is appropriate for a user to manage the Course without having access to Student grades. A Course Builder can still access the Course if the Course is unavailable to Students. A Course Builder cannot delete an Instructor from a Course. |
| Grader | A Grader assists the Instructor in the creation, management, delivery, and grading of items, such as Tests and Discussion Board posts. A Grader also assists the Instructor with managing the Grade Center. A Grader cannot access a Course if it is unavailable to Students. |
| Guest | Guests have no access to the Control Panel. Areas within the Course are made available to Guests. Visitors, such as prospective Students, alumni, or parents may be given the role of Guest. |
| Instructor | Instructors have access to all areas in the Control Panel. This role is generally given to those developing, teaching, or facilitating the class. Instructors may access a Course that is unavailable to Students. |
| Student | Student is the default Course Role. Students have no access to the Control Panel. |
| TeachingAssistant | The Teaching Assistant role is that of a co-teacher. Teaching Assistants are able to administer all areas of a course. Their only limitations are those imposed by the Instructor or Blackboard administrator at your school. A Teaching Assistant cannot delete an Instructor from a Course. |
