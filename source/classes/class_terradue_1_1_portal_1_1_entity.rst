.. _class_terradue_1_1_portal_1_1_entity:

:ref:`Entity <class_terradue_1_1_portal_1_1_entity>`
----------------------------------------------------


Generic object of all entity types that usually correspond to real-world entities. The object provides generic interaction with data that is persistently stored in a relational database. The data location and structure are defined in the extended object which represent real-world entities.  





The following properties define the object

.. cssclass:: propertiestable

+--------+------------+-----------------------------------------------------------------+
| Type   | Name       | Summary                                                         |
+========+============+=================================================================+
| int    | Id         | The database ID, i.e. the numeric key value of an entity item.  |
+--------+------------+-----------------------------------------------------------------+
| string | Identifier | Unique identifier of an entity item.                            |
+--------+------------+-----------------------------------------------------------------+
| string | Name       | Human-readable name of an entity item item.                     |
+--------+------------+-----------------------------------------------------------------+

The following functions are applicable to the object

.. cssclass:: propertiestable

========================== =======================================================================================================================================
Name                       Summary
========================== =======================================================================================================================================
Load                       Reads the information of an item from the database.</sum 

Load                       Reads the information of an item using the specified IDataReader.

Store                      Writes the item to the database.

StorePrivilegesForUsers    Sets the privileges on the resource represented by the instance for the specified users according to the privilege properties.

StorePrivilegesForGroups   Sets the privileges on the resource represented by the instance for the specified user groups according to the privilege properties.

StoreGlobalPrivileges      Sets global privileges on the resource represented by the instance that will apply to all users according to the privilege properties.

RemoveGlobalPrivileges     Sets global privileges on the resource represented by the instance that will apply to all users according to the privilege properties.

Delete                     Remove the entity from the database

========================== =======================================================================================================================================

