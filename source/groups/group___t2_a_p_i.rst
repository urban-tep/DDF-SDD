.. _group___t2_a_p_i:

T2 API
------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___t2_a_p_i.iuml

T2 API is an external backend interface of the platform exposed for any users and mainly intented for the web site pages and widgets to interacts with the system.

It is a REST web service with usual CRUD (create, read, update, delete) functions for the objects managed by the portal:



- Data Package
- Web Feature
- Group
- Image
- News
- Series
- Service
- User
- Wps Provider

It also offers for most of the items an OpenSearch interface to discover or search them efficiently.

