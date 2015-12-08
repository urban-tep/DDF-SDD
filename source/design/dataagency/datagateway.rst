.. _catalogue_data_gateway:

Data Gateway
^^^^^^^^^^^^

General design
""""""""""""""

The Data Gateway is Data as a Service platform of Terradue to resolve the best location and access to the data.
It resolves the best location from the catalogue but also based on rules.


.. req:: HEP-TS-FUN-040
  :show:

  The data gateway mechanism is fully described in this section


Partnership Policies
""""""""""""""""""""

The Data Gateway implements 3 methods to access data from data providers:

- remote access either by user redirection or by piping the data request download
- caching the data resource on a custom data storage for a defined retention time
- mirroring the data resource on a custom data storage for an undefined time limit


.. req:: HEP-TS-FUN-041
  :show:

  The data gateway's partnership policies implementation is fully described in this section


Rule Based design
"""""""""""""""""

The Data Gateway implements a rule-based mechanism to control data partnership and access policies and scenario. 
The rules conditions are applicable to:
- origin of the data request (IP, user, processing center)
- location of the data as recorded in the catalogue
- data provider of the data
- the authorization applied to that resource at portal level

The rules are combinable.


.. req:: HEP-TS-FUN-042
  :show:

  The data gateway's rule based mechanism is fully described in this section


Data Access Policies enforcement
""""""""""""""""""""""""""""""""

.. req:: HEP-TS-SEC-051
  :show:

  Data Access policies enforcement is described in this section


.. warning:: 

  Here shall be a sequence diagram to explain hot the data gateway interacts with the portal to get the user authorization and apply it`


SciHub
""""""

Data Gateway service implements a channel for harvesting and retrieving data from Copernicus Sentinels Scientific Hub (https://scihub.esa.int/).


.. req:: HEP-TS-ICD-034
  :show:

  Data Access policies enforcement is described in this section






