.. _group___core:

Core
----




.. uml::
  :align: center
  :caption: Core component diagram

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___core.iuml

The Core component is a set of library developed as the base implementation of a Content Management System (CMS) for EO world entities. It implements basic subcomponent to deal with basic EO business objects such as dataset series, WPS service, user context, jobs... It also implements the low level functions to store and read data persistently on the database or to apply a configuration. 


This component manages the following business objects: :ref:`class_terradue_1_1_portal_1_1_user`, :ref:`class_terradue_1_1_portal_1_1_wps_process_offering`, :ref:`class_terradue_1_1_portal_1_1_wps_provider`




This component is implemented in the following software packages: :ref:`namespace_terradue_1_1_portal`




This component contains the sub-components described in the following sections.


.. toctree::
  :maxdepth: 0

  group___computing_resource
  group___persistence
  group___context
  group___web_context
  group___scheduler
  group___series
  group___service
  group___task
  group___core_w_p_s

