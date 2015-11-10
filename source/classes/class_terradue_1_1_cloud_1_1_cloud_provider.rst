.. _class_terradue_1_1_cloud_1_1_cloud_provider:

Terradue::Cloud::CloudProvider
------------------------------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/classes/class_terradue_1_1_cloud_1_1_cloud_provider.iuml



Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+--------+-------------+---------+
| Type   | Name        | Summary |
+========+=============+=========+
| string | AccessPoint |         |
+--------+-------------+---------+

Methods
^^^^^^^

.. cssclass:: propertiestable

====================== ============================= =============================================================================================================
Type                   Name                          Summary
====================== ============================= =============================================================================================================
VirtualMachineTemplate FindVirtualMachineTemplates() In a derived class, queries the cloud provider to get a list of the virtual machine templates defined on it.

VirtualDisk            FindVirtualDisks()            In a derived class, queries the cloud provider to get a list of the virtual disks defined on it.

VirtualNetwork         FindVirtualNetworks()         In a derived class, queries the cloud provider to get a list of the virtual networks defined on it.

CloudAppliance         FindAppliances()              In a derived class, queries the cloud provider to get a list of the cloud appliances created on it.

CloudAppliance         CreateInstance()              
====================== ============================= =============================================================================================================

