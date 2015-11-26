.. _group___tep_application:

Application
-----------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___tep_application.iuml

This component manages the TEP applications

Thematic Application brings a simple way to define an application of a specific aspect of the thematic. It specifies togheter the form of the application, its features such as the map and the layers, its data and services.

Dependencies
^^^^^^^^^^^^
- delegates :ref:`Data <group___tep_data>` for the data management in the application with the definition of the collection and data packages references.

- delegates :ref:`Service <group___tep_service>` for the processing service management in the application with the defintion of the service references .


