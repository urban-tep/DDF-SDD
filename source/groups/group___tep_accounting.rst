.. _group___tep_accounting:

Accounting
----------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___tep_accounting.iuml

This component makes the integrated accounting of the TEP.

Accounting to user/group accounts 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Periodically, it collects the usage records from the :ref:`Apel Server <group___apel_server>` and use them to balance the user accounts with credits.
*Here shall be a sequence diagram to describe the periodical user account balance*

Credit Authorization and Quota restrictions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The quota restriction is implemented using the balance of the user or group account used to query the resource.*Here shall be a sequence diagram to describe the credit authorization mechanism and the quota restriction*

.. req:: TS-FUN-400
	:show:

	The mechanism of debit and credit of user or group accounts is described in this section.



.. req:: TS-FUN-410
	:show:

	Business objects used to represent user or group account are referenced in this section.



.. req:: TS-FUN-420
	:show:

	Quota mechanism based on the account balance of the user or groups is described in this section.



Dependencies
^^^^^^^^^^^^
- :ref:`Persistence of Data <group___persistence>` stores the user accounts in the database


Interfaces
^^^^^^^^^^
- connects :ref:`Apel Reporting <group___apel_reporting>` to retrieve the aggregated usage records.



Objects
^^^^^^^
- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_account`
- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_rates`

