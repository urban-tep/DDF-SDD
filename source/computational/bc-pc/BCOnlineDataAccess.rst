.. _bcpc_part1 :

BC online data access component
===============================

Implementation software and configuration
-----------------------------------------

The Online Data Access component is a shared BC component hosted on two machines, a disk array for the storage and an FTP front end in the external network running vsfptd and openssh. ZFS is used as file system of the disk array. 

The configuration specific for Urban TEP comprises:

 * a volume on the file system as staging area
 * a configuration of certain users to allow (S)FTP, in particular for exchange between processing centres

State representation and persistent data
----------------------------------------

The persistent data of this component is the file system content:

 * a directory ``/data/urbantep/staging/<user>/`` per user

The staging area is also mounted into the Apache Tomcat server for serving processing results via HTTP(S).

Computational service and functions
-----------------------------------

The computational service of this component is that of a file system, i.e. the data storage in files, organisation in directories, the provision of access control rules, and the functions of reading files and writing files. The access is provided by the ZFS processes and an NFS server internally, and vsftpd and sshd externally.

Interfaces and interface items
------------------------------

The interfaces are:

 * NFS for internal access by Processing Gateway/WPS
 * SCP/SFTP for internal access by Ingestion and Proessing Control
 * FTP/SFTP by other processing centres and by dedicated users

Requirements for the design of BC online data access component
--------------------------------------------------------------

.. req:: TS-FUN-630
  :show:

  (Dataset exchange) The Online Data Access/FTP provides an (S)FTP access for other Processing Centres (DLR, IT4I) for dataset exchange.

.. req:: TS-FUN-690
  :show:

  (Processing result provision) The Online Data Access hosts the staging area where the Processing Request Gateway/WPS places results for access by users via the gateway (HPPT(S)) or Online Data Access/FTP itself ((S)FTP).

.. req:: TS-FUN-720
  :show:

  (Reference data upload) The FTP access also allows upload of reference data by users. The Operator ingests this data into HDFS after verification.

.. req:: TS-FUN-740
  :show:

  (Software upload) The FTP access also allows upload of processor implementations by well-known users. The Operator deploys processors after verification.

.. req:: TS-SEC-610
  :show:

  (Authentication) The Online Data Access/FTP uses the BC User Management to authenticate users. Among them is the Urban TEP Portal user.

.. req:: TS-ICD-220
  :show:

  (Result Access Interface) Processing results provided to users via HTTP(S) by the Processing Request Gateway/WPS are hosted in the staging area of the Online Data Access component.

.. req:: TS-ICD-230
  :show:

  (Processor and Reference Data Upload Interface) The FTP access also allows upload of reference data and/or processor implementations by well-known users. The Operator deploys processors and ingests reference data after verification.

.. req:: TS-ICD-250
  :show:

  (Processor and Data Exchange Interface) The Online Data Access/FTP provides an (S)FTP access for other Processing Centres (DLR, IT4I) for dataset exchange and processor software exchange.
