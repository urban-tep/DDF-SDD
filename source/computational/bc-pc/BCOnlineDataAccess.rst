.. _bcpc_part1 :

BC online data access component
===============================

Implementation software and configuration
-----------------------------------------

State representation and persistent data
----------------------------------------

Computational service and functions
-----------------------------------

Interfaces and interface items
------------------------------

...

Requirements
------------

.. req:: TS-FUN-630 Dataset exchange
  :show:

  The Online Data Access/FTP from one Processing Centre shall exchange datasets from the other Processing Centres. 

.. req:: TS-FUN-690 Processing result provision
  :show:

  The Processing Request Gateway/WPS or the Online Data Access/FTP shall provide the processing result to the users and the portal for online access. 

.. req:: TS-FUN-720 Reference data upload
  :show:

  The Processing Request Gateway/WPS may allow users to upload reference data for validation purpose.

.. req:: TS-FUN-740 Software upload
  :show:

  The processing centres shall support the upload of custom processors by well-known users. As baseline the external user sends the agreed algorithm code to the Urban TEP Processing Centre Operating and they validate and make it available for processing in Urban TEP Config and Processor Repo.

.. req:: TS-SEC-610 Authentication
  :show:

  Processing Centre User Management shall accept a dedicated portal user for authentication.

.. req:: TS-ICD-220 Result Access Interface

  The Processing Request Gateway/WPS shall expose an HTTP(S) interface to access the processing results, as shown in Figure 4 1. The Online data access/FTP shall expose an (S)FTP interface to the same data. 

.. req:: TS-ICD-230 Processor and Reference Data Upload Interface

  The Processing Request Gateway/WPS or the Online data access/FTP shall expose an HTTP(S) or (S)FTP interface to upload custom processors or reference data.

.. req:: TS-ICD-250 Processor and Data Exchange Interface

  The Online data access/FTP shall expose an (S)FTP interface to exchange data and processors between processing centres.

