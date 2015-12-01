Level of abstraction
====================

The computational model is defined is this design as the recipient for the functional decomposition of the system into a set of components that interact at interfaces – enabling system distribution. It thus provides the basis for decisions on how to distribute the components to be handled by the system. It is unique to the system and therefore provides the reference model for ensuring consistency between different engineering and technology specifications (including programming languages and communication mechanisms). This is aiming at open interworking and portability of components in the resulting implementations. For example, the computational specification is used as the baseline for the :ref:`integration_scheme`, the later defining the communications mechanisms supporting the behaviour at the interfaces of the system.

For these reasons, the configuration and degree of distribution of the infrastructure on which the applications are run can be altered, based on the documented environment contracts associated with interfaces, without having a major impact on the application software.

A computational component is defined as a way to model functional decomposition, has state and behaviour, and has interactions achieved through interfaces. 
An environment contract between a component and its environment can cover Quality of Service (QoS) constraints (delays, throughput, availability), usage constraints and component management constraints.

This section describes the design choices to cope with the usage constraints. It describes the computational model that manly consists of :
 
- the components (modules) participating to the real‐time behaviour, from which the system is constructed divided by main subsystems;
- the means of communication between components/objects (e.g. interfaces, format, parameters)
- the service model that the system uses to exchange data flow;

The set of computational components were carried from those defined in the architecture. When applicable the reference to the business object is mentionned