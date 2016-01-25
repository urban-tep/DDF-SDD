.. _class_terradue_1_1_portal_1_1_service:

Abstract base object for processing services.
---------------------------------------------








The following properties define the object

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

The following functions are applicable to the object

.. cssclass:: propertiestable

================= ========================
Name              Summary
================= ========================
CheckParameters   Checks the parameters. 

BuildTask         Builds the task. 

================= ========================

