.. _dynamic_accounting :

Integrated Accounting: Credit and Quota flows
=============================================


:ref:`design_apel` component collects the usage records for all the resources providers of the platform via the :ref:`group___apel_accounting`. They are then reported via the :ref:`group___apel_reporting` interface from which the portal gets the aggregated usage records. Those usage records contains unit of cost and the amount of the resource consumed for a certain :ref:`class_terradue_1_1_tep_1_1_user_tep` or :ref:`class_terradue_1_1_tep_1_1_group_tep`. Then this amount is debited from the credit :ref:`class_terradue_1_1_tep_1_1_account` of this user or group.

Section :ref:`group___tep_accounting` decribes in details how the portal carries forward the accounting on the user and groups account and how quota can be applied from this user and groups accounts.

On the other hand, the providers must account for the usage of their resources. This task is independant from the portal and up to every provider (ICT, data, etc) using the :ref:`group___apel_accounting` as illustrated in the following figure for an ICT provider. In the TEP Urban initial scenario, every ICT resources reports the usage based on WPS requests completed.


.. uml::
  :caption: ICT resource provider accounting usage sequence diagram
  :align: center

  box "Cluster" #LightBlue
    participant "WPS Server" as WPS
    participant "APEL Client" as AL
  end box
  participant "APEL Server" as AS
  
  autonumber

  WPS -> WPS : job completed
  activate WPS
  WPS -> WPS : build usage record
  WPS -> AL : usage record
  activate AL 
  AL -> AS : send usage record
  activate AS 
  AS -> AS : save usage record in DB
  AS -> AL : usage record confirmation
  deactivate AS
  AL -> WPS : usage record ok
  deactivate AL
  deactivate WPS
