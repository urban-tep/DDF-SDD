.. _class_terradue_1_1_portal_1_1_service:

Service
-------


Abstract base object for processing services.





Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+--------+-------------+----------------------------------------------------------------+
| Type   | Name        | Summary                                                        |
+========+=============+================================================================+
| string | Description | Description text of the service                                |
+--------+-------------+----------------------------------------------------------------+
| string | Version     | Version of the service                                         |
+--------+-------------+----------------------------------------------------------------+
| string | Url         | URL pinting to the service                                     |
+--------+-------------+----------------------------------------------------------------+
| string | IconUrl     | Icon URL of the logo representing the service.                 |
+--------+-------------+----------------------------------------------------------------+
| int    | Rating      | Rating of the service                                          |
+--------+-------------+----------------------------------------------------------------+
| int    | ClassId     | Class identifier. Can be used to classify the maturity level.  |
+--------+-------------+----------------------------------------------------------------+

Methods
^^^^^^^

.. cssclass:: propertiestable

============= ================= ========================
Type          Name              Summary
============= ================= ========================
void          CheckParameters() Checks the parameters. 

abstract void BuildTask()       Builds the task. 

============= ================= ========================

