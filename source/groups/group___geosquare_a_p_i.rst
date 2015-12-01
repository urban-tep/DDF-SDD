.. _group___geosquare_a_p_i:

Geosquare API
-------------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___geosquare_a_p_i.iuml

ElasticCas is the component enabling the gateway with :ref:`Elasticsearch <namespace_elasticsearch>` in both directions.

For dataset ingestion, it transform the metadata feed in JSON documents to index in elasticsearch. For dataset query, it exploit :ref:`Elasticsearch <namespace_elasticsearch>` search engine to retrieve the documents in JSON and transform them in metadata feed.

The transformation and query semantics are defined trough plugins to enables several metadata models and feed formats.

.. req:: TS-ICD-090
	:show:

	Geosquare API provides with feed format supporting :ref:`OWS Context <group___o_w_s_context>`



.. req:: TS-ICD-100
	:show:

	Geosquare API provides with an :ref:`OpenSearch <group___open_search>` interface



