.. _group___authorisation:

Authorisation
-------------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___authorisation.iuml

It provides with the functions to define privileges for users or groups on entities for which restrictions are useful, such as entities that represent resources (computing resources or processing services etc.).

The authorisation consists of two phases:

- a generic phase where the current user's access privileges are compared to the necessary privileges for the accessed resource
- an optional specific phase where the same check is performed for the requested operation. This phase is specific to the entity subclass in question as the possible operations are entity-specific.

*true*



.. uml::


	!define DIAG_NAME Authorisation mechanism Activity Diagram
	
	start
	:Load entity item considering access policies and user/group privileges;
	if (Are view privileges for current user sufficient?) then (yes)
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
	if (Is specific privilege required for requested operation) then (yes)
	    if (Does user have this privilege?) then (no)
	        :Operation rejected (throw exception);
	        stop
	    else (yes)
	    endif
	else (no)
	endif
	:Operation allowed;
	stop
	
	footer
	DIAG_NAME
	(c) Terradue Srl
	endfooter
	

.. req:: TS-FUN-380
	:show:

	Authorisation scheme paradigm is described in this section.



.. req:: TS-SEC-010
	:show:

	Collection / Series / Data Package Authorisation scheme paradigm is described in this section.



.. req:: TS-SEC-020
	:show:

	Service Authorisation scheme paradigm is described in this section.



Dependencies
^^^^^^^^^^^^
- :ref:`Persistence of Data <group___persistence>` reads/writes the privileges persistently

- uses :ref:`Context <group___context>` to identify the user and the session



Objects
^^^^^^^
- :ref:`class_terradue_1_1_portal_1_1_group`

