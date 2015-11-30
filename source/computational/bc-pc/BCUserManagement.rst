.. _bcpc_part1 :

BC user management
==================

Implementation software and configuration
-----------------------------------------

The BC User Management is a shared service used by several projects. It implementation is based on OpenLDAP.

The configuration specific to Urban TEP comprises:

 * a user group *urbantep*, and a group *urbanwku* (well known user)
 * a dedicated user for the Portal for access to the Processing Gateway/WPS
 * a user account for the other processing centres for data and processor software exchange
 * optionally accounts for well-known users for the upload of reference data and processor bundles

State representation and persistent data
----------------------------------------

The slapd service stores the user and group information in a local database. There are three redundant LDAP servers in the BC infrastructure.

Computational service and functions
-----------------------------------

The computational service of the User Management is:

 * to authenticate users, i.e. to check whether a user is listed and whether the provided credentials match the stored ones
 * to provide user group membership information
 * to add, update or remove entries

Interfaces and interface items
------------------------------

The slapd exposes an LDAP interface. Updates can be performed by scripts (or by LDIF files).

Requirements for the design of BC user management
-------------------------------------------------

.. req:: TS-FUN-640 WPS interface
  :show:

  The BC WPS is secured by simple authentication and a verification of the group membership.

.. req:: TS-FUN-720 Reference data upload
  :show:

  The Processing Request Gateway/WPS checks by authentication and group membership whether a user is entitled to upload reference data.

.. req:: TS-FUN-740 Software upload
  :show:

   The Processing Request Gateway/WPS checks by authentication and group membership whether a user is entitled to upload custom processors by well-known users.

.. req:: TS-SEC-610 Authentication
  :show:

  The User Management provides a user account for the Portal.


.. req:: TS-ICD-210 OGC Web Processing Service Interface
  :show:

  The BC WPS is secured by simple authentication and a verification of the group membership.

.. req:: TS-ICD-220 Result Access Interface
  :show:

  The result access is secured by simple authentication. For well-known users result access is also possible by (S)FTP using the same credentials.

.. req:: TS-ICD-230 Processor and Reference Data Upload Interface
  :show:

  The Processing Request Gateway/WPS checks by authentication and group membership whether a user is entitled to upload reference data or custom processors by well-known users.

.. req:: TS-ICD-250 Processor and Data Exchange Interface
  :show:

  User Management provides a dedicated user for exchange of data and processor software with the other processing centres.

.. req:: TS-ICD-310 OGC Web Processing Service	
  :show:

  The BC WPS is secured by simple authentication and a verification of the group membership.
