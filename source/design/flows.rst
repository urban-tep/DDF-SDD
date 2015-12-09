.. _flow:

Information flows
=================

This section describes the main data flow between the defined interfaces and the components.


Portal and Catalogue metadata exchange
--------------------------------------

The :ref:`portal` relies on the :ref:`catalogue` for all the dataset metadata. The portal only stores reference url to the catalogue in the collection or data packages definition


Portal and PUMA for data visulization
-------------------------------------

:ref:`puma` is used as an extrnal tool with expert visualization functions. To enable TEP data visulization in :ref:`puma`, the portal must upload the data processed in the TEP Urban :ref:`portal` to :ref:`puma` via the :ref:`group___geo_node_a_p_i` interface of this latter. Then, based on defined parameters, a URL pointing to PUMA is built by the portal for redirecting the user directly to PUMA web interface with the predefined data loaded. This URL is associated to the result dataset by an update to the catalogue via a :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_offering` of the `OGC OWS Context Conceptual Model <https://portal.opengeospatial.org/files/?artifact_id=55182>`_. This offering is recognized by the portal that propose a special button next to the data to go to PUMA visualization.


Accounting data flow
--------------------

:ref:`apel` component collects the usage records for all the resources providers of the platform via the :ref:`group___apel_accounting`. They are then reported via the :ref:`group___apel_reporting` interface from which the portal gets the aggregated usage records. Those usage records contains unit of cost and the amount of the resource consumed for a certain :ref:`class_terradue_1_1_tep_1_1_user_tep` or :ref:`class_terradue_1_1_tep_1_1_group_tep`. Then this amount is debited from the credit :ref:`class_terradue_1_1_tep_1_1_account` of this user or group.



Portal and Processing centers job submission
--------------------------------------------

In the :ref:`portal`, any users may register a new :ref:`WPS server <class_terradue_1_1_portal_1_1_wps_provider>`. The component :ref:`core WPS <group___core_w_p_s>` discovers the processing :ref:`WPS processing services <class_terradue_1_1_portal_1_1_wps_process_offering>` available by the :ref:`class_terradue_1_1_portal_1_1_wps_provider` and the user selects the services he wants to integrate in its :ref:`Thematic Application <class_terradue_1_1_tep_1_1_thematic_application>`. The users accessing the :ref:`Thematic Application <class_terradue_1_1_tep_1_1_thematic_application>` have access to the selected :ref:`processing service <class_terradue_1_1_portal_1_1_wps_process_offering>` and the :ref:`portal` will proxy the job request to the :ref:`WPS server <class_terradue_1_1_portal_1_1_wps_provider>` and grant the access or not according to the user or group :ref:`class_terradue_1_1_tep_1_1_account` credit balance. 



Processing centers and Catalogue metadata exchange
--------------------------------------------------

Processing centers will offer an `OGC Catalogue Service <http://www.opengeospatial.org/standards/cat>`_ of all metadata available, which is continually updated. The processing center catologue service can be harvested by the :ref:`portal` and if necessary by other processing centers. This mechanism will allow the portal and porcessing centers to refer to and use valid data resources



Processor deployment
--------------------

Any registered user may use the help desk of the :ref:`portal` to get the technical specifications of the processing centers. He will have to build his software according to the specifications and submit the software package via the help desk. An oparator will manage deployment and `OGC Web Processing Service <http://www.opengeospatial.org/standards/wps>`_ integration. 



Processing results data flow
----------------------------

After an OGC WPS processing request is sent from the :ref:`portal` to the procesing center in question, the WPS response will contain an URL resource of the location of the results. The results will be accesssible at an SFTP server in the processing center. Once the portal is aware that processing is complete, it is able to retrieve the results for display or use the URL to notify the user where the results are obtainable.



