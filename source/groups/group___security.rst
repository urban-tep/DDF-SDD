.. _group___security:

Security
--------




.. uml::
  :align: center
  :caption: Security component diagram

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___security.iuml

The Security component is a set of library in charge with all the authorisation or authentication functions and also with the privileges management between users, groups and other business objects. The security scheme is open and offers many possibilities to plug other component to implement specific authentication mechanism or authorization scheme. 


This component is implemented in the following software packages: :ref:`namespace_terradue_1_1_authentication_1_1_umsso`




This component contains the sub-components described in the following sections.


.. toctree::
  :maxdepth: 0

  group___auth___umsso
  group___authentication
  group___authorisation

