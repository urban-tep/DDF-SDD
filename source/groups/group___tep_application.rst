.. _group___tep_application:

Application
-----------







.. req:: TS-DES-110
	:show:

	Data flow along with services are built into the Thematic Application inside this component. 

This component manages the TEP applications

Thematic Application brings a simple way to define an application of a specific aspect of the thematic. It specifies togheter the form of the application, its features such as the map and the layers, its data and services.

Thematic Application over OWS data model 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*This section shall further describe how the component uses the OWS Context model to represent the dataset collections, the services, maps, features layers...*

It depends on other components as

- delegates :ref:`Data <group___tep_data>` for the data management in the application with the definition of the collection and data packages references.

- delegates :ref:`Service <group___tep_service>` for the processing service management in the application with the defintion of the service references .



This component manages the following business objects: :ref:`class_terradue_1_1_tep_1_1_thematic_application`



