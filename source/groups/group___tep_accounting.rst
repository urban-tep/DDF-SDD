.. _group___tep_accounting:

Accounting
----------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___tep_accounting.iuml

This component makes the integrated accounting of the TEP.

Periodically, it collects the usage records from the :ref:`Apel Server <group___apel_server>` and use them to balance the user accounts with credits.

Dependencies
^^^^^^^^^^^^
- :ref:`Persistence of Data <group___persistence>` stores the user accounts in the database


Interfaces
^^^^^^^^^^
- connects :ref:`Apel Reporting <group___apel_reporting>` to retrieve the aggregated usage records.


