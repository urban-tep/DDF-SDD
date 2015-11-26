.. _class_terradue_1_1_tep_1_1_controller_1_1_user_tep:

UserTep
-------

TEP User 


.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/classes/class_terradue_1_1_tep_1_1_controller_1_1_user_tep.iuml

A user in the TEP platform has a basic profile (defined in the platform) It can also be integrated with third party profiles (:ref:`Github <namespace_terradue_1_1_github>`, :ref:`Terradue <namespace_terradue>` Cloud Platform).  

Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+-----------------------------------------------------------------------+-------------------------+------------------------------------------------------------------+
| Type                                                                  | Name                    | Summary                                                          |
+=======================================================================+=========================+==================================================================+
| :ref:`GroupTep <class_terradue_1_1_tep_1_1_controller_1_1_group_tep>` | Groups                  | Thematic groups the user belongs to.                             |
+-----------------------------------------------------------------------+-------------------------+------------------------------------------------------------------+
| string                                                                | TerradueCloudPlatformId | :ref:`Terradue <namespace_terradue>` Cloud Platform identifier   |
+-----------------------------------------------------------------------+-------------------------+------------------------------------------------------------------+

