.. _class_terradue_1_1_portal_1_1_series:

Series
------


Represents a series of data sets that are available from a catalogue.





Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+--------+-------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Type   | Name                    | Summary                                                                                                                  |
+========+=========================+==========================================================================================================================+
| string | Description             | Detailed description of the series.                                                                                      |
+--------+-------------------------+--------------------------------------------------------------------------------------------------------------------------+
| string | CatalogueDescriptionUrl | :ref:`OpenSearch <namespace_terradue_1_1_portal_1_1_open_search>` description document URL of the remote dataset series  |
+--------+-------------------------+--------------------------------------------------------------------------------------------------------------------------+

Methods
^^^^^^^

.. cssclass:: propertiestable

===================== =============================== ===========================================================================================================
Type                  Name                            Summary
===================== =============================== ===========================================================================================================
OpenSearchDescription GetLocalOpenSearchDescription() Generates the corresponding :ref:`OpenSearch <namespace_terradue_1_1_portal_1_1_open_search>` description.

Series                FromOpenSearchUrl()             Create the series from an :ref:`OpenSearch <namespace_terradue_1_1_portal_1_1_open_search>` url. 

===================== =============================== ===========================================================================================================

