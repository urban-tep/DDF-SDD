.. _class_terradue_1_1_portal_1_1_entity:

Entity
------


Abstract base class of all entity types that usually correspond to real-world entities.





Properties
^^^^^^^^^^

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

Methods
^^^^^^^

.. cssclass:: propertiestable

==== =================================== =======================================================================================================================================
Type Name                                Summary
==== =================================== =======================================================================================================================================
void Load()                              Reads the information of an item from the database.</sum 

void Load()                              Reads the information of an item using the specified IDataReader.

void Store()                             Writes the item to the database.

void StorePrivilegesForUsers()           Sets the privileges on the resource represented by the instance for the specified users according to the privilege properties.

void StorePrivilegesForGroups()          Sets the privileges on the resource represented by the instance for the specified user groups according to the privilege properties.

void StoreGlobalPrivileges()             Sets global privileges on the resource represented by the instance that will apply to all users according to the privilege properties.

void RemoveGlobalPrivileges()            Sets global privileges on the resource represented by the instance that will apply to all users according to the privilege properties.

void Delete()                            
void GetAllowedAdministratorOperations() 
==== =================================== =======================================================================================================================================

