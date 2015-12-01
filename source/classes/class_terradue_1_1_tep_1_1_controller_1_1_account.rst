.. _class_terradue_1_1_tep_1_1_controller_1_1_account:

Account
-------

:ref:`Account <class_terradue_1_1_tep_1_1_controller_1_1_account>`. 


.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/classes/class_terradue_1_1_tep_1_1_controller_1_1_account.iuml

This object represents an account owned by a user or a group. Each account has a balance value to represent the credit avaialable for the owner. 

Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+-----------------------------------------------------------------------+------------+---------------------------------+
| Type                                                                  | Name       | Summary                         |
+=======================================================================+============+=================================+
| :ref:`UserTep <class_terradue_1_1_tep_1_1_controller_1_1_user_tep>`   | UserOwner  | User the account belongs to.    |
+-----------------------------------------------------------------------+------------+---------------------------------+
| :ref:`GroupTep <class_terradue_1_1_tep_1_1_controller_1_1_group_tep>` | GroupOwner | Group the account belongs to.   |
+-----------------------------------------------------------------------+------------+---------------------------------+
| double                                                                | Balance    | Credit balance of the account   |
+-----------------------------------------------------------------------+------------+---------------------------------+

