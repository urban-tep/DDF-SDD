.. _group___elastic_cas:

ElasticCas
----------





ElasticCas is the component enabling the gateway with :ref:`Elasticsearch <namespace_elasticsearch>` in both directions.

For dataset ingestion, it transform the metadata feed in JSON documents to index in elasticsearch. For dataset query, it exploit :ref:`Elasticsearch <namespace_elasticsearch>` search engine to retrieve the documents in JSON and transform them in metadata feed.

The transformation and query semantics are defined trough plugins to enables several metadata models and feed formats.

It depends on other components as

- uses :ref:`Elasticsearch <namespace_elasticsearch>` as indexing backend.


It interacts with interfaces as it

- implements :ref:`Geosquare API <group___geosquare_a_p_i>` interface to manage dataset metedata.

- implements :ref:`OpenSearch <group___open_search>` interface to query dataset.


