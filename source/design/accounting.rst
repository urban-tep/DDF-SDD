.. _dynamic_accounting :

Integrated Accounting: Credit and Quota Flows
=============================================


:ref:`design_apel` component collects the usage records for all the resources providers of the platform via the :ref:`group___apel_accounting`. They are then reported via the :ref:`group___apel_reporting` interface from which the portal gets the aggregated usage records. Those usage records contains unit of cost and the amount of the resource consumed for a certain :ref:`class_terradue_1_1_tep_1_1_user_tep` or :ref:`class_terradue_1_1_tep_1_1_group_tep`. Then this amount is debited from the credit :ref:`class_terradue_1_1_tep_1_1_account` of this user or group.

Section :ref:`group___tep_accounting` decribes in details how the portal carries forward the accounting on the user and groups account and how quota can be applied from this user and groups accounts.

On the other hand, the providers must account for the usage of their resources. This task is independant from the portal and up to every provider (ICT, data, etc) using the :ref:`group___apel_accounting` as illustrated in the following figure for an ICT provider. In the TEP Urban initial scenario, every ICT resources reports the usage based on WPS requests completed.


.. uml::
  :caption: Reporting of completed jobs to APEL server
  :align: center
  
  box "Processing Center" #LightBlue
	  participant "Staging"
	  participant "Production Control" as PC
	  participant "Scheduler"
  end box
  participant "APEL Server" as AS
  
  activate PC
  activate Scheduler
  Staging -> PC : product URL(s) and metadata
  PC -> Scheduler : collect counters for the job
  Scheduler -> PC : usage record
  PC -> PC : format usage record
  PC -> PC : instantiate APEL client
  activate PC #Green
  PC -> AS : send usage record
  activate AS
  AS -> PC : record accepted
  deactivate AS
  deactivate PC
