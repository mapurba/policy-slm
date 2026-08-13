# 1.0 Introduction

The Identity Manager Drivers for Oracle E-Business Suite synchronize users between the Identity Vault and the Oracle E-Business Suite. Oracle E-Business Suite (EBS) is a comprehensive suite of integrated, global business applications that includes modules for finance, human resources, supply chain management, customer relationship management, and business intelligence. There are mainly three types of user records in the Oracle EBS system. They are:

* *EBS User Record:*
  Represents a record in the FND\_USER table in the Oracle EBS system. To log in to the Oracle EBS system, a user must have a record in the FND\_USER table.
* *HRMS/PERSON Record:*
  Represents a Human Resources Management System (HRMS) record in the Oracle EBS system. Some applications in the Oracle EBS system; for example, iExpense require a user to have a HRMS (Person) record. The Person record can be of different types like Employee, Part-time worker, Contractor, and so on. Person records are stored in the PER\_ALL\_PEOPLE\_F table in the Oracle EBS system.
* *Customer/Vender Record:*
  Represents a TCA record in the HZ\_PARTIES table in the Oracle EBS system. Some applications in the Oracle EBS system such as iStore, iProcurement require users to have a Trading Community Architecture (TCA) record that are representatives or employees of customers and vendors.

There are three different Identity Manager drivers for synchronizing Oracle EBS users with the Identity Vault. They are:

* Driver for User Management
* Driver for HR
* Driver for TCA

Each driver has a definite purpose and allows administrators to propagate user data among Oracle systems and other business applications and databases without the need for custom integration solutions. Administrators can decide what data to share and how to present data within their enterprises. The drivers offer the following features:

* Automated, rule-based user creation, modification, and deletion of user data with the Oracle EBS system
* Bidirectional attribute synchronization
* Basic password set and synchronization
* Support for standard Identity Manager features such as entitlements, identity tracking, and reporting

[Table 1-1](introduction.html#b14xkn58) distinguishes features of each driver:

*Table 1-1* Driver Features

| Driver for UserManagement | Driver for User Management with HR Foundation | Driver for User Management with TCA Foundation |
| Synchronizes attributes between the Oracle EBS system and the Identity Vault. | Synchronizes attributes between the Oracle EBS system and the Identity Vault. | Synchronizes attributes between the Oracle EBS system and the Identity Vault. |
| Creates FND\_USER records in the Oracle EBS system for the Identity Manager users and grants them roles and responsibilities. | Creates basic HRMS users in the PER\_ALL\_PEOPLE\_F table. | Creates FND\_USER records in the Oracle EBS system for the Identity Manager users and grants them roles and responsibilities.  Creates basic TCA records in the HZ\_PARTIES table and links them to the FND\_USER table records. For example, the PERSON\_PARTY\_ID column in the FND\_USER table is linked with the PARTY\_ID column of the HZ\_PARTIES table. |

To use all the three drivers together, you must use entitlements.
