.. _group___t2_a_p_i:

Terradue API
------







.. req:: TS-ICD-100
	:show:

	T2 API provides with an :ref:`OpenSearch <group___open_search>` interface



.. req:: TS-ICD-020
	:show:

	OGC :ref:`OWS Context <group___o_w_s_context>` is used as the most as possible for representing objects in the portal

T2 API is an external backend interface of the platform exposed for any users and mainly intented for the web site pages and widgets to interacts with the system.

It is a REST web service with usual CRUD (create, read, update, delete) functions for the objects managed by the portal:



- Collection
- Data Package
- Web Feature
- Group
- Image
- News
- Series
- Service
- User
- Wps Provider
- Contest
- Benchmark

It also offers for most of the items an :ref:`OpenSearch <group___open_search>` interface to discover or search them efficiently. The results are provided in the :ref:`OWS Context <group___o_w_s_context>` model and in the feed format requested.

The following normative references are applied to this component:

- `OpenSearch 1.1 <http://www.opensearch.org/Specifications/OpenSearch/1.1>`_

- `OGC OWS Context Conceptual Model <https://portal.opengeospatial.org/files/?artifact_id=55182>`_


