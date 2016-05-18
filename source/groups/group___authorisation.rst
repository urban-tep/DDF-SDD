.. _group___authorisation:

Authorisation
-------------







.. req:: TS-SEC-020
	:show:

	Service Authorisation scheme paradigm is described in this section.



.. req:: TS-SEC-010
	:show:

	Collection / Series / Data Package Authorisation scheme paradigm is described in this section.



.. req:: TS-FUN-380
	:show:

	Authorisation scheme paradigm is described in this section.

It provides with the functions to define privileges for users or groups on Entity objects for which restrictions are useful, such as entities that represent resources (:ref:`Service <group___service>`, :ref:`Series <group___series>` ...).

The following class diagram describes the base authorization scheme implemented in the :ref:`Security <group___security>` component providing with the access control mechanism to the :ref:`Core <group___core>` and depending components.



.. uml::
	:caption: Authorisation scheme Class Diagram
	:align: center


	
	        Group  *-right-"0..*" User : has >
	        User -down-"0..*" Domain : belongs >
	        Group -down-"0..*" Domain : belongs >
	        abstract class Entity
	        Entity <|-up- Domain
	        Entity <|-up- Object
	        Entity -- EntityType : is specified by >
	        EntityType -right- Privilege : defines >
	        Role *-down- Privilege : is granted >
	        class Permission
	        User -- Object : accesses >
	        Group -- Object : accesses >
	        Object -right- Domain : belongs >
	
	        (User, Domain) . Role
	        (Group, Domain) . Role
	        (User, Object) . Permission
	        (Group, Object) . Permission
	
	

The following defintions supports this scheme:

- User and Group are defined according the regular convention that a group is a set of zero or many users.
- A Domain is an organizational unit to regroup User, Group and Objects (Entity).
- A Role defines the set of privileges that are granted to a User or a Group for a specific Domain or globally.
- The assignement of a Role to a User or a Group is called a "Role Grant". A Role Grant can be associated to a Domain and is therefore called "Domain Role Grant". A Role Grant not associated to any domain is a "Global Role Grant".
- A Privilege is an access control for a given entity (object) type. For all objects, there are 6 basic privileges : "Can Create", "Can Change", "Can Delete", "Can View", "Can Search" and "Can Manage". For instance, "Can Create" for :ref:`Series <group___series>` specify the possibility to create a  in the system
- A Permission is a specific Privilege for a User or a Group for a given Object (Entity). For instance: "Can View" for the ENVISAT :ref:`Series <group___series>` speificy the possibility to view the ENVISAT :ref:`Series <group___series>` in the results of a search.

And the following rules applies:

- Users and Groups with a Domain Role Grant on a certain Domain have all the privileges defined by that Role on all Objects belonging to that Domain.
- Users and Groups with a Global Role Grant have all the privileges defined by that Role on all Objects, whether belonging to a Domain or not.
- A specific permission for a specific object is granted to a specific User or Group.

The authorisation consists of two phases:

- a generic phase where the current User 's access privileges are compared to the necessary privileges for the accessed object according to the domain or the global.
- an optional specific phase where the same check is performed for the requested operation. This phase is specific to the entity object in question as the possible operations are entity-specific.

The authorisation for a specific operation must be ensured by the code of the Entity object. The central authorisation model supports this task by initialising the properties corresponding to the operation privilege that are applicable to the entity subclass.



.. uml::
	:caption: Authorisation mechanism Activity Diagram
	:align: center


	
	start
	:Load entity item considering access policies and user/group privileges;
	if (Are list/view privileges/permissions for current user sufficient?) then (yes)
	    :Access granted;
	else (no)
	    if (Is current context set to restricted mode?) then (yes)
	        :Access denied (throw exception);
	        stop
	    else (no)
	        :Item flagged as unaccessible for current user (no exception);
	    endif
	    :Access granted;
	endif
	:Generic authorisation check completed;
	:Speficic authorisation checks for operation (performed by entity subclass);
	if (Is specific privilege or permission required for requested operation) then (yes)
	    if (Does user have this privilege in the object's domain or this permission on the specific object?) then (no)
	        :Operation rejected (throw exception);
	        stop
	    else (yes)
	    endif
	else (no)
	endif
	:Operation allowed;
	stop
	
	

Authorisation scheme tailoring for TEP
""""""""""""""""""""""""""""""""""""""

As described previously, the portal authorisation mechanism allows a great flexibility for managing users and groups and their permissions with the items in the system. In order to enable all the requirements specific to the TEP, the :ref:`Community <group___tep_community>` uses the :ref:`Security <group___security>` components as the following:



- :ref:`Terradue.Portal.User <class_terradue_1_1_portal_1_1_user>` is an :ref:`Terradue.Tep.UserTep <class_terradue_1_1_tep_1_1_user_tep>` registered via the :ref:`Authentication <group___authentication>` mechanism integrated in the portal (e.g. EO-SSO)
- :ref:`Terradue.Portal.Group <class_terradue_1_1_portal_1_1_group>` is a :ref:`Terradue.Tep.GroupTep <class_terradue_1_1_tep_1_1_group_tep>` regrouping a set of :ref:`Terradue.Tep.UserTep <class_terradue_1_1_tep_1_1_user_tep>` put together for organisational purpose. For instance, all :ref:`Terradue <namespace_terradue>` staff users are grouped in the :ref:`Terradue <namespace_terradue>` Group.
- :ref:`Terradue.Portal.Domain <class_terradue_1_1_portal_1_1_domain>` is named "Thematic Group" and englobes all users, groups and objects having a thematic scope in common. For instance, there could be a "Volcanoes" thematic group that would have expert users in volcanoes monitoring, the data collections used for monitoring them (e.g. Sentinel-2 and 3), the features related to this domain (e.g. latest most important eruptions) and the all the processing services relative to volcanoes.
- The inital roles are defined as :ref:`Terradue.Tep.RoleTep <class_terradue_1_1_tep_1_1_role_tep>`.

Objects identified and used in TEP are

- :ref:`Terradue.Portal.Series <class_terradue_1_1_portal_1_1_series>` called "Data \ref Collection"
- :ref:`Terradue.Tep.DataPackage <class_terradue_1_1_tep_1_1_data_package>`
- :ref:`Terradue.Portal.Service <class_terradue_1_1_portal_1_1_service>` also called processing services and mainly implemented as :ref:`Terradue.Portal.WpsProcessOffering <class_terradue_1_1_portal_1_1_wps_process_offering>`
- Job representing an instance of a processing service execution
- Terradue::Cloud::CloudProvider providing with Terradue::Cloud::CloudAppliance
- :ref:`Terradue.Tep.ThematicApplication <class_terradue_1_1_tep_1_1_thematic_application>` that combines at user level the previous objects.
- :ref:`Terradue.Portal.Activity <class_terradue_1_1_portal_1_1_activity>` that records all the operations executed from the portal

Additional privilege and permissions for TEP
""""""""""""""""""""""""""""""""""""""""""""

Specific privileges and permissions are implemented for TEP in order to control a precise operation on the platform. The specific operations are described in the folowing table.

+------------------------------------------------------------------------+------------------------+---------------------------------------------------------------------------------+
| Object Type                                                            | Operation Name         | Description                                                                     |
+========================================================================+========================+=================================================================================+
| :ref:`Terradue.Tep.Collection <class_terradue_1_1_tep_1_1_collection>` | Can Search In          | Allows to search for dataset in the collection                                  |
+------------------------------------------------------------------------+------------------------+---------------------------------------------------------------------------------+
| :ref:`Terradue.Tep.Collection <class_terradue_1_1_tep_1_1_collection>` | Can Download           | Allows to download the raw dataset in the collection directly on user desktop   |
+------------------------------------------------------------------------+------------------------+---------------------------------------------------------------------------------+
| :ref:`Terradue.Tep.Collection <class_terradue_1_1_tep_1_1_collection>` | Can Process            | Allows to use the data inside processing service or for processing purpose      |
+------------------------------------------------------------------------+------------------------+---------------------------------------------------------------------------------+
| Terradue::Cloud::CloudProvider                                         | Can Request Sandbox    | Allows to request for a Developer Cloud Sandbox via the related Cloud Provider  |
+------------------------------------------------------------------------+------------------------+---------------------------------------------------------------------------------+
| Terradue::Cloud::CloudProvider                                         | Can Provision Cluster  | Allows to provision a Cluster via the related Cloud Provider                    |
+------------------------------------------------------------------------+------------------------+---------------------------------------------------------------------------------+



It depends on other components as

- :ref:`Persistence of Data <group___persistence>` reads/writes the privileges persistently

- uses :ref:`Context <group___context>` to identify the user and the session



This component manages the following business objects: :ref:`class_terradue_1_1_portal_1_1_group`



