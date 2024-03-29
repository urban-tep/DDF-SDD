.. _class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_ows_context:

OWS Context
-----------


This class is the overall container class for the OWS context document. 






The following properties define the object

.. cssclass:: propertiestable

+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type                                                                                         | Name            | Summary                                                                                                                                                                |
+==============================================================================================+=================+========================================================================================================================================================================+
| string                                                                                       | Title           | A Human Readable Title for the OWS Context Document                                                                                                                    |
+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| string                                                                                       | Abstract        | Description of the Context Document Purpose/Content                                                                                                                    |
+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DateTimeOffset                                                                               | UpdateDate      | Date when the Context Document was updated                                                                                                                             |
+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| List< string >                                                                               | Authors         | Identifier for the author of the document                                                                                                                              |
+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| string                                                                                       | Publisher       | Identifier for the publisher of the document                                                                                                                           |
+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`OwcCreator <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_creator>`   | Creator         | The tool/application used to create the context document and its properties                                                                                            |
+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`OwcResource <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_resource>` | Resources       | The description of a resource and its access parameters and configuration                                                                                              |
+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| object                                                                                       | ContextMetadata | Additional metadata describing the context document itself. The format recommendation is ISO19115 complaint metadata. The metadata standard used should be specified   |
+----------------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

