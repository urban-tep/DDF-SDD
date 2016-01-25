.. _group___tep_community:

Community
---------







.. req:: TS-DES-080
	:show:

	TEP ICT provider rights are enforced by this component with the support of the Authorization component.



.. req:: TS-DES-060
	:show:

	TEP expert user rights are enforced by this component with the support of the Authorization component.



.. req:: TS-DES-050
	:show:

	TEP Resource Administrator rights are enforced by this component with the support of the Authorization component.



.. req:: TS-DES-040
	:show:

	TEP Content Authority rights are enforced by this component with the support of the Authorization component.



.. req:: TS-DES-030
	:show:

	TEP data provider rights are enforced by this component with the support of the Authorization component.



.. req:: TS-DES-020
	:show:

	TEP end user rights are enforced by this component with the support of the Authorization component.

This component manages the TEP users and thematic groups along with the user roles.

Thematic Group simplifies management of the user community and help focus the user objective for thematical business within those groups. It is an important concept in the Thematic Exploitation Platform to gather users around a specific aspect or an organization ot the thematic.

For instance, an instituion may create its own thematic group with its selected members and experts. It may also have business relationship with a data or ICT provider that are representated as a role within the group.

User notifications 
^^^^^^^^^^^^^^^^^^^

This component notifies users about status change for the following items:

- The completion of a job in a service
- The modification of dataset in a data package
- The arrival in new dataset in a dynamic data package

The notification is configurable in the user profile and can be enabled as the following:

- Email notification
- Web notification (a box is deplayed during the navigation on the site)

It depends on other components as

- uses :ref:`Authorisation <group___authorisation>` to manage the users in the groupswith their roles and their access accordingly.



This component manages the following business objects: :ref:`class_terradue_1_1_tep_1_1_group_tep`, :ref:`class_terradue_1_1_tep_1_1_role_tep`, :ref:`class_terradue_1_1_tep_1_1_user_tep`



