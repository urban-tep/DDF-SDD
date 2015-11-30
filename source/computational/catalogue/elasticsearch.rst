.. _catalogue_elasticsearch:

Elasticsearch
-------------

.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/elasticsearch.iuml

Elasticsearch is a third party tool for querying written words. It can perform some other nifty tasks, but at its core it’s made for wading through text, returning text similar to a given query and/or statistical analyses of a corpus of text.

More specifically, elasticsearch is a standalone database server, written in Java, that takes data in and stores it in a sophisticated format optimized for language based searches. Working with it is convenient as its main protocol is implemented with HTTP/JSON. Elasticsearch is also easily scalable, supporting clustering and leader election out of the box.

.. req:: TS-DES-120
  :show:

  Elasticsearch is written in Java

Whether it’s searching a database of retail products by description, finding similar text in a body of crawled web pages, or searching through posts on a blog, elasticsearch is an obvious choice. When facing the task of cutting through the semi-structured muck that is natural language, Elasticsearch is an excellent tool.


