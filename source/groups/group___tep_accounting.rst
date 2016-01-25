.. _group___tep_accounting:

Accounting
----------







.. req:: TS-FUN-420
	:show:

	Quota mechanism based on the account balance of the user or groups is described in this section.



.. req:: TS-FUN-410
	:show:

	Business objects used to represent user or group account are referenced in this section.



.. req:: TS-FUN-400
	:show:

	The mechanism of debit and credit of user or group accounts is described in this section.

This component makes the integrated accounting of the TEP.

Accounting to user/group accounts 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Periodically, it collects the usage records from the :ref:`Apel Server <group___apel_server>` and use them to balance the user accounts with credits.

*Here shall be a sequence diagram to describe the periodical user account balance*

Credit Authorization and Quota restrictions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The quota restriction is implemented using the balance of the user or group account used to query the resource.

*Here shall be a sequence diagram to describe the credit authorization mechanism and the quota restriction*

It depends on other components as

- :ref:`Persistence of Data <group___persistence>` stores the user accounts in the database


It interacts with interfaces as it

- connects :ref:`Apel Reporting <group___apel_reporting>` to retrieve the aggregated usage records.



This component manages the following business objects: :ref:`class_terradue_1_1_tep_1_1_account`, :ref:`class_terradue_1_1_tep_1_1_rates`



