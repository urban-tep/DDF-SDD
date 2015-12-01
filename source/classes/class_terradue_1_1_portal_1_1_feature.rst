.. _class_terradue_1_1_portal_1_1_feature:

Feature
-------

A :ref:`Feature <class_terradue_1_1_portal_1_1_feature>` is a container for an item on the portal or on the web that the portal features in a way or another depending on the user interface (e.g. front page carousel). It has all the properties for storing the cnecessary contents (title, url, image, description). 


.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/classes/class_terradue_1_1_portal_1_1_feature.iuml



Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+--------+-------------+----------------------------------------------------------------------------------------------------+
| Type   | Name        | Summary                                                                                            |
+========+=============+====================================================================================================+
| string | Title       | Title.                                                                                             |
+--------+-------------+----------------------------------------------------------------------------------------------------+
| string | Description | Description.                                                                                       |
+--------+-------------+----------------------------------------------------------------------------------------------------+
| string | Image       | :ref:`Image <class_terradue_1_1_portal_1_1_image>` url representing the feature                    |
+--------+-------------+----------------------------------------------------------------------------------------------------+
| string | ImageStyle  | :ref:`Image <class_terradue_1_1_portal_1_1_image>` style, used to customize the image apperance.   |
+--------+-------------+----------------------------------------------------------------------------------------------------+
| string | ButtonText  | Link text.                                                                                         |
+--------+-------------+----------------------------------------------------------------------------------------------------+
| string | ButtonLink  | Link to the feature                                                                                |
+--------+-------------+----------------------------------------------------------------------------------------------------+

