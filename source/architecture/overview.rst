.. _static_overview :

Overview
========

The following schema provide a static overview of the main componenents that comes into play in Urban TEP.


.. include:: component_diagram.rst

    
The figure above describes all the internal or external interfaces of the TEP Urban system. In Blue and green are colored the external interfaces. The green ones are general user interface, typically web page. In red are colored the internal interfaces and in yellow the one for which the visibility is not yet defined.

This section describes them by subsystem:

- The **portal** is the main front-end end to the end-user interfaces via the **Web UI**. It is supported by the **Web Server** back-end via many web services to discover the collections, services and other :ref:`business objects <objects>` registered and searchable in the TEP Urban portal. It also uses directly WPS interface as the processing request endpoint for all the completed, ongoing or new processing tasks to request. The **Web Server** manages all :ref:`business objects <objects>` internally and store them peristemctly in the TEP database. For dataset query in the collection, it dispatches request to the catalogue. It is also the case for WPS queries, they are proxied when necessary. Additionally, the UI also integrates a link to the ticketing System to manage the underspecified tasks triggered via the email interface.

- The **APEL** independant Server is a subsystem that collects accounting records via the accounting interface. It provides then with an reporting interface to provide with aggregated accounting.
   
- **PUMA** supports the portal for specific data visualization and analysis functionnalities.

- All **Processing Center** subsystems are in charge of the processing services from integration to production. For integration and processor deployment, they all have a specific integration point for new services in the processing center. They also exposes all a WPS endpoint for processing tasks management at the processing center level. Finally, process results of the completed processing tasks are accessible in a data result pool.

- The **Data Agency** hosts the services for dataset metadata ingestion and query using the catalogue as a service. Data Gateway is intended to be the main data access endpoint. It handles the data requests either by proxying the data or redirecting to its location.

- Each **data provider** should expose interfaces for dataset discovery and download.


:ref:`design` chapter describes each of the main subsystems and their behaviour individually

   
   
