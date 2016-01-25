.. _group___geosquare:

Geosquare
---------




.. uml::
  :align: center
  :caption: Geosquare component diagram

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___geosquare.iuml



.. req:: TS-FUN-120
	:show:

	Geosquare provides with the Catalogue as a service function

Geosquare is a .NET web application for indexing model-aware dataset in elasticsearch. It provides with an interface for searching the dataset in a catalogue via an OpenSearch interface according to a data model.

ElasticCas is the component enabling the gateway with :ref:`Elasticsearch <namespace_elasticsearch>` in both directions.

For dataset ingestion, it transform the metadata feed in JSON documents to index in elasticsearch. For dataset query, it exploit :ref:`Elasticsearch <namespace_elasticsearch>` search engine to retrieve the documents in JSON and transform them in metadata feed.

The transformation and query semantics are defined trough plugins to enables several metadata models and feed formats.


This component contains the sub-components described in the following sections.


.. toctree::
  :maxdepth: 0

  group___geosquare_a_p_i
  group___elastic_cas

