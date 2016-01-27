.. _group___r_e_s_t:

REST handler
------------





This component enables the full web service stack to interact with the back-end. It allows to control many of the business objects in the system with REST CRUD (Create, Read, Update, Delete) operations

It depends on other components as

- CRUD operations for user accounts managed :ref:`Accounting <group___tep_accounting>`

- CRUD operations for thematic application managed by :ref:`Application <group___tep_application>`

- CRUD operations for user and groups managed by :ref:`Community <group___tep_community>`

- CRUD operations for editorial contents managed by :ref:`Contents <group___tep_contents>`

- CRUD operations for collections and data packages managed by :ref:`Data <group___tep_data>`

- CRUD operations for services managed by :ref:`Service <group___tep_service>`


It interacts with interfaces as it

- implements :ref:`T2 API <group___t2_a_p_i>` interface

- implements :ref:`OpenSearch <group___open_search>` interface


