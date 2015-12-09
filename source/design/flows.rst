.. _flow:

Information flows
=================

This section describes the main data flow between the defined interfaces and the components.


Portal and Catalogue metadata exchange
--------------------------------------

The :ref:`portal` relies on the :ref:`catalogue` for all the metadata of the dataset . The portal only stores a reference url to the catalogue in the collection or data packages definition


Portal and PUMA for data visulization
-------------------------------------

:ref:`puma` is integrated as an external tool with expert visualization functions. To enable TEP data visulization in :ref:`puma`, the portal must upload the data processed in the TEP Urban :ref:`portal` to :ref:`puma` via the :ref:`group___geo_node_a_p_i` interface of the latter. Then, based on defined parameters, a URL pointing to PUMA is built by the portal to redirect the user directly to the PUMA web interface with the selected data allready loaded. This URL is associated with the result dataset by an update to the catalogue via a :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_offering` of the `OGC OWS Context Conceptual Model <https://portal.opengeospatial.org/files/?artifact_id=55182>`_. This offering is recognized by the portal that then offers a special button next to the dataset to go to the PUMA visualization.


Accounting data flow
--------------------

:ref:`apel` component collects the usage records for all the resources providers of the platform via the :ref:`group___apel_accounting`. They are then reported via the :ref:`group___apel_reporting` interface from which the portal gets the aggregated usage records. These usage records contain the cost of a unit the amount of the resources (units) consumed for a certain :ref:`class_terradue_1_1_tep_1_1_user_tep` or :ref:`class_terradue_1_1_tep_1_1_group_tep`. This amount is then debited from the credit :ref:`class_terradue_1_1_tep_1_1_account` of this user or group.



Portal and Processing centers job submission
--------------------------------------------

In the :ref:`portal`, any users may register a new :ref:`WPS server <class_terradue_1_1_portal_1_1_wps_provider>`. The component :ref:`core WPS <group___core_w_p_s>` discovers the processing :ref:`WPS processing services <class_terradue_1_1_portal_1_1_wps_process_offering>` available by the :ref:`class_terradue_1_1_portal_1_1_wps_provider` and the user selects the services he wants to integrate in its :ref:`Thematic Application <class_terradue_1_1_tep_1_1_thematic_application>`. The users accessing the :ref:`Thematic Application <class_terradue_1_1_tep_1_1_thematic_application>` have access to the selected :ref:`processing service <class_terradue_1_1_portal_1_1_wps_process_offering>` and the :ref:`portal` will proxy the job request to the :ref:`WPS server <class_terradue_1_1_portal_1_1_wps_provider>` and grant the access or not according to the user or group :ref:`class_terradue_1_1_tep_1_1_account` credit balance. 



Processing centers and Catalogue metadata exchange
--------------------------------------------------

Processing centers will offer an `OGC Catalogue Service <http://www.opengeospatial.org/standards/cat>`_ of all datasets and metadata available, which is continually updated. The processing center catologue service can be harvested by the :ref:`portal` and if necessary by other processing centers. This mechanism will allow the portal and processing centers to refer to and use existing data resources



Processor deployment
--------------------

Any registered user may use the help desk of the :ref:`portal` to get the technical specifications of the processing centres that are suitable for his envisioned processor along with the development kit for creating new processors. The selected processing centre will also provide specific experimental environment (e.g. a virtual machine image or connection information to the experimental infrastructure directly at the processing centre) with sample data for the user to test their processor during the development. The user will then have to build his software according to the specifications, validate it in the experimental environment and package and submit the software package via the help desk. An Urban TEP help desk operator will manage the deployment of the processor with the selected processing centre help desk and its integration to the `OGC Web Processing Service <http://www.opengeospatial.org/standards/wps>`_ in the processing centre and the portal.

The concepts of processor integration with frameworks and languages supported, packaging examples, and runtime environment are described for each respective processing centre, in section 4.5.7.4 and 4.6.3.3. Supported processor integration tools and languages are described in section 5.5 of the System and Service Technical Note. More detailed operational process for the processor deployment is described in section 4.1.4 of the Sustainable Operations Concept TN.



Processing results data flow
----------------------------

After an `OGC Web Processing Service <http://www.opengeospatial.org/standards/wps>`_ request is sent from the :ref:`portal` to the procesing centre in question, the WPS response will contain URL and authentication credentials to the SFTP/SCP interface at the processing centre containing the results. Once the portal is aware that processing is complete, it is able to retrieve the results for visualisation and/or provide them to the user for download.



