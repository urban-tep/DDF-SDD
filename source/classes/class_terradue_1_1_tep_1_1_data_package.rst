.. _class_terradue_1_1_tep_1_1_data_package:

DataPackage
-----------


Data package. 



It represents a container for datasets, owned by a user. This container manages remote datasets by reference. It acts as a view over the Collection. Therefore, it can represent static datasets list or a dynamic set via search query. A Data Package is OpenSearchable and thus can be queried via an opensearch interface. 

Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+-----------------------------------------------------------+-------------+--------------------------------------------+
| Type                                                      | Name        | Summary                                    |
+===========================================================+=============+============================================+
| :ref:`UserTep <class_terradue_1_1_tep_1_1_user_tep>`      | Owner       | Owner of the data package                  |
+-----------------------------------------------------------+-------------+--------------------------------------------+
| :ref:`Collection <class_terradue_1_1_tep_1_1_collection>` | Collections | Collections included in the Data Package   |
+-----------------------------------------------------------+-------------+--------------------------------------------+

