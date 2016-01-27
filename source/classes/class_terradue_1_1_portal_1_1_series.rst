.. _class_terradue_1_1_portal_1_1_series:

Data :ref:`Series <class_terradue_1_1_portal_1_1_series>`
---------------------------------------------------------


Represents a series of data sets that are available from a catalogue.






The following properties define the object

.. cssclass:: propertiestable

+--------+-------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Type   | Name                    | Summary                                                                                                                  |
+========+=========================+==========================================================================================================================+
| string | Description             | Detailed description of the series.                                                                                      |
+--------+-------------------------+--------------------------------------------------------------------------------------------------------------------------+
| string | CatalogueDescriptionUrl | :ref:`OpenSearch <namespace_terradue_1_1_portal_1_1_open_search>` description document URL of the remote dataset series  |
+--------+-------------------------+--------------------------------------------------------------------------------------------------------------------------+

The following functions are applicable to the object

.. cssclass:: propertiestable

=============================== ===========================================================================================================
Name                            Summary
=============================== ===========================================================================================================
GetLocalOpenSearchDescription   Generates the corresponding :ref:`OpenSearch <namespace_terradue_1_1_portal_1_1_open_search>` description.

FromOpenSearchUrl               Create the series from an :ref:`OpenSearch <namespace_terradue_1_1_portal_1_1_open_search>` url. 

=============================== ===========================================================================================================

