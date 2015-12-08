.. _background :

System Approach
===============


The Urban TEP is based on a generic, modular, multi-purpose design facilitating
maximum flexibility with respect to the adaptation to and integration of user requirements,
application scenarios, processing and analysis technologies, and IT infrastructures.
Considering the thematic and technical objectives of Urban TEO, the essential
requirements on the TUrbO-Hub architecture are:

- Web-based platform to access, explore, generate, analyze, validate and visualize
geospatial data (in particular EO imagery) and derived products.
- Processing infrastructure for very fast, cost effective and operationalwith
  1) access to multiple satellite mission archives (in particular ESA and Sentinel archives), 
  2) implementation and operation of VA processors.
- Thematic value-adding processors providing geo-information products on the urban environment and its development.
- Expert knowledge and user community integration by means of active target community participation. 


Web-based platform
------------------

The central element in the Urban TEP concept is the Web-based platform. It builds
from extensive knowledge acquired by Terradue on the development and maintenance of the
Agency’s Grid Processing on Demand (G-POD) system, the development of the early TEP platforms (Tep-QuickWin then Geohazard TEP) 
and the integration of scientific applications and services for the EC projects GEOWOW and SenSyF.


Data driven plarform
--------------------

Data is the fuel of the Urban TEP platform and thus needs to be managed with systems
in order to harvest, discover and query many collections of datset from various Earth Observation missions.
The catalogue components are an evolution of the experiences and operational deployments
made in the context of the European Commission FP7 GENESI-DEC project and then applied on
the G-POD catalogues. Terradue developed a full system for the data management with state-of-the-art
technology for super fast indexing of dataset metadata document and implementing the community
specifications such as OpenSearch or OWS Context.


Processing infrastructure
-------------------------

Another key component and functionality of the Urban TEP platform is the processing infrastructure provided by the processing centers. Following the idea of a generic and modular character of the overall system design, the processing centers can be
regarded as self-contained infrastructural units providing all necessary functionalities and EO
data (archive, data streams) required for operating highly automated processing chains. These
chains include specific pre-processing procedures as well as methods for the derivation of valueadded,
thematic geo-information products. All EO data required for the processing of the
individual services offered by each processing center will be available locally at the processing
facility.
TEP Urban will include a total of three distributed data and processing centers with individual infrastructural sub-systems: the virtualized environment of DLR’s Geofarm, but also including a Calvalus/Hadoop sub-system, another
Calvalus/Hadoop environment provided by Brockmann Consult, and one HPC-based processing
facility operated by IT4Innovation. However, in general, arbitrary processing centers can be linked to and therewith included into the TEP Urban platform


Data Visualization
------------------

World Bank Group has developed with the expertise of GISAT its Platform for Urban Mapping and Analysis (PUMA),
which is complementary and can benefit from the Tep Urban infrastructure, products and services development.
It is a key element for the data analysis and visualization of the Urban thematic data.



A complete system
-----------------

Based on functional software components describesdin the previous sections, mainly based on existing/established software packages, configured specifically for their use in Urban TEP, the consortium will provide an integrated system. This system will group the components into subsystems for the portal, visualisation, and decentralised processing centres with different EO datasets interfaces between components for the workflows implementing the Urban TEP use cases, flexible enough to allow for new use cases. The integration with existing external systems, e.g. for visualisation (PUMA) and processing clusters are also taken into account in the design of the system.

