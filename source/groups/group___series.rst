.. _group___series:

Series
------







.. req:: TS-ICD-100
	:show:

	:ref:`OpenSearch <group___open_search>` interface for dataset are supported by the component



.. req:: TS-ICD-090
	:show:

	This component reads dataset series metadata using OWS conceptual model.

This component manages all types of dataset series. It implements the mechanism to search for the dataset defined in the series via an :ref:`OpenSearch <group___open_search>` interface.

It depends on other components as

- :ref:`Persistence of Data <group___persistence>` stores persistently the series information in the database

- :ref:`Authorisation <group___authorisation>` controls the access on the series


It interacts with interfaces as it

- connects to :ref:`OpenSearch <group___open_search>` interfaces defined in the series to proxy the queries



This component manages the following business objects: :ref:`class_terradue_1_1_portal_1_1_series`



