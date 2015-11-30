.. _group___e_o_profile:

Earth Observation Metadata profile
----------------------------------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___e_o_profile.iuml

The Earth Observation (EO) Metadata profile of Observations and Measurements is intended to provide a standard schema for encoding Earth Observation product metadata to support the description and cataloguing of products acquired by sensors aboard EO satellites.

EO products are differentiated by parameters such as the date of acquisition and the image footprint as well as characteristics pertaining to the type of sensor, the type of platform, the applied processing chain, and more. This candidate standard identifies the metadata elements that enable the robust description of general EO products and defines specialisations for specific thematic classes of EO products, such as optical, radar, atmospheric, altimetry, limb-looking and systematic/synthesized EO products. In addition, this document describes the mechanism used to extend these thematic schemas for specific EO missions.

.. req:: TS-FUN-180
	:show:

	This is the data model defining the Earth Observation profile used in :ref:`ElasticCas <group___elastic_cas>` and :ref:`OpenSearch <group___open_search>`. 



Normative References
^^^^^^^^^^^^^^^^^^^^
- `OGC Earth Observation Metadata profile of Observations & Measurements (10-157r4) <https://portal.opengeospatial.org/files/61098>`_


