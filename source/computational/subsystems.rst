.. _design_subsystems_components_list :

Subsystems components
=====================

The following schema provide a general overview of the main componenents that comes into play in Urban TEP.


.. include:: component_diagram.rst

    
The figure above describes all the internal or external interfaces of the TEP Urban system. In Blue and green are colored the external interfaces. The green ones are general user interface, typically web page. In red are colored the internal interfaces and in yellow the one for which the visibility is not yet defined.

This section describes them by subsystem:

- The portal is the front-end end to the end-user interfaces via the Web UI. It exposes, in a interactive and user friendly form, the following application program interfaces:

   1. Dataset Search Proxy [OpenSearch] is the dataset discovery endpoint for all the collections regis-tered and searchable in the TEP Urban portal. It mainly redirects the search to the main catalogue.

   2. Service Search [OpenSearch] is the service discovery endpoint for all the services registered and accessible in the TEP Urban portal.

   3. Process Request Proxy [WPS] is the processing request endpoint for all the completed, ongoing or new processing tasks to request. It acts as a proxy for the underlying processing facility.

   4. Ticketing System manages the underspecified tasks triggered via the email interface.

   5. Accounting Report is the reporting endpoint for all the usage records collected by the system.

   6. Accounting interface that collects usage records from the processing centers.

- All Processing Center subsystem exposes the following interfaces that are marked as internal at the sys-tem level:

   7. Processor Deployment is the integration point for new services in the processing center.

   8. Process Request [WPS] is the endpoint for processing tasks management at the processing cen-ter level.

   9. Process Result is the data result pool of the completed processing tasks.

- The Catalogue hosts the dataset metadata and expose the following interfaces:

   10. Datase Search [OpenSearch] is the dataset discovery endpoint for all the dataset indexed in the catalogue.

   11. Data Gateway is intended to be the main data access endpoint. It handles the data requests either by proxying the data or redirecting to its location.

- Each data provider should expose 2 interfaces:

   12. Datase Search is the dataset discovery endpoint for all the data accessible from the data provider.

   13. Dataset Download is the download endpoint for the data on the data provider.


Next subsections describe each of the main components individually

.. toctree::
   :maxdepth: 1
   
   Portal <portal/index>
   Catalogue <catalogue/index>
   Brockmann Consult Processing Centre Requirements <bc-pc/index>
   IT4Innovations Processing Centre Requirements <it4i-pc/index>
   DLR Processing Centre Requirements <dlr-pc/index>
