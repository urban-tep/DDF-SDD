.. _group___tep_service:

Service
-------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___tep_service.iuml

This component controls the processing services registered in the platform.

Dependencies
^^^^^^^^^^^^
- uses :ref:`WPS Factory <group___cloud_wps_factory>` to discover the dynamic WPS providers in the Cloud.

- uses :ref:`WPS <group___core_w_p_s>` to analyse and manage the WPS services.


