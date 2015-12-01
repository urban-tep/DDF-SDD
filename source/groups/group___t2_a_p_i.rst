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

It also offers for most of the items an :ref:`OpenSearch <group___open_search>` interface to discover or search them efficiently. The results are provided in the :ref:`OWS Context <group___o_w_s_context>` model and in the feed format requested.

.. req:: TS-ICD-020
	:show:

	OGC :ref:`OWS Context <group___o_w_s_context>` is used as the most as possible for representing objects in the portal



.. req:: TS-ICD-100
	:show:

	T2 API provides with an :ref:`OpenSearch <group___open_search>` interface



Normative References
^^^^^^^^^^^^^^^^^^^^
- `OpenSearch 1.1 <http://www.opensearch.org/Specifications/OpenSearch/1.1>`_

- `OGC OWS Context Conceptual Model <https://portal.opengeospatial.org/files/?artifact_id=55182>`_


