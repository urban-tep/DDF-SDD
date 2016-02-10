.. _design_dataagency :

Data Agency
===========

The Data Agency is a set of components providing with services for faciliting the data flow.
For that purpose it first includes a catalogue to store dataset metadata and perform complex queries.
It also expose a data pipe service with the data gateway that helps finding the best location for the
data according to paramaters such as the processing service or location.
Finally a data agent is in charge of monitoring data sources for new datasets by harvesting data source
and ingesting new datasets and their location in the catalogue.

.. include:: component_diagram.rst

.. toctree::
   :maxdepth: 1
   
   Catalogue <catalogue>
   Data gateway <datagateway>

   
