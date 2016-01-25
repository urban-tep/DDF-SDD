.. _group___apel:

Apel
----




.. uml::
  :align: center
  :caption: Apel component diagram

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___apel.iuml

APEL is an accounting tool that collects accounting data from sites participating in the EGI and WLCG infrastructures as well as from sites belonging to other Grid organisations that are collaborating with EGI, including OSG, NorduGrid and INFN.

The accounting information is gathered from different resource providers into a central accounting database where it is processed to generate statistical summaries that are available through the reporting interface

We use this system in TEP to record the usage on the different resources provider of the platform in order to provide a central accounting mechanism for the platform. 


This component contains the sub-components described in the following sections.


.. toctree::
  :maxdepth: 0

  group___apel_server
  group___apel_reporting

