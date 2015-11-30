.. _group___series:

Series
------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___series.iuml

This component manages all types of dataset series. It implements the machnaism to search for the dataset defined in the series via an OpenSearchable interface.

Dependencies
^^^^^^^^^^^^
- :ref:`Persistence of Data <group___persistence>` stores persistently the series information in the database

- :ref:`Authorisation <group___authorisation>` controls the access on the series


Interfaces
^^^^^^^^^^
- connects to :ref:`OpenSearch <group___open_search>` interfaces defined in the series to proxy the queries



Objects
^^^^^^^
- :ref:`class_terradue_1_1_portal_1_1_series`

