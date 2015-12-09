.. _catalogue_data_gateway:

Data Gateway
^^^^^^^^^^^^

General design
""""""""""""""

The Data Gateway is Data as a Service platform of Terradue to resolve the best location and access to the data.
It resolves the best location from the catalogue but also based on rules.


.. req:: TS-FUN-100
  :show:

  The data gateway mechanism is fully described in this section


Rule Based design
"""""""""""""""""

The Data Gateway implements a rule-based mechanism to control data partnership and access policies and scenario. 
The rules conditions are applicable to:
- origin of the data request (IP, user, processing center)
- location of the data as recorded in the catalogue
- data provider of the data
- the authorization applied to that resource at portal level

The rules are combinable.


Data Access Policies enforcement
""""""""""""""""""""""""""""""""

.. req:: TS-FUN-480
  :show:

  Data Access policies enforcement is described in this section


.. warning:: 

  Here shall be a sequence diagram to explain hot the data gateway interacts with the portal to get the user authorization and apply it`


SciHub
""""""

Data Gateway service implements a channel for harvesting and retrieving data from Copernicus Sentinels Scientific Hub (https://scihub.esa.int/).








