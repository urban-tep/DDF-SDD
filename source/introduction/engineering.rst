Engineering Process
===================

The input for design elaboration stems from the following documents:

  - TEP Urban Technical Specification (TS)
    
Each applicable requirement is traced to the above sources in :ref:`requirement_trace` section.

.. _methodology:

Methodology
===========

This section describes the methods applied for the architectural design of the TEP platform. During project analysis and design phase, both structured and object oriented modelling and design methods are applied: 

- The first levels of the system analysis and decomposition (:ref:`Static Architecture <architecture>`) are performed applying a structural decomposition of the platform into subsystems and using UML components diagrams for representation.
- Then the identified components are further decomposed (:ref:`Dynamic Architecture <design>`) using object-oriented methods based on UML and their :ref:`Information Flows <Interfaces>` 
- The dynamical behaviour of the components is described using UML sequence and state diagrams.
- The deployment of the platform on the infrastructure is descrbed using a deployment diagram.
  
The UML uses several kinds of models for system description. For the scope of this document the following diagrams are considered: 

Class diagrams
--------------

The class diagram shows how the different entities (people, things, and data) relate to each other; in other words, it shows the static structures of the system. A class diagram can be used to display logical classes, which are typically the kinds of things the business people in an organization talk about — datasets, products, services; or WPS and providers. Class diagrams can also be used to show implementation classes, which are the things that programmers typically deal with. An implementation class diagram will probably show some of the same classes as the logical classes diagram. The implementation class diagram won't be drawn with the same attributes, however, because it will most likely have references to things to the programming language types like Vectors and HashMaps.

Class diagrams notation
^^^^^^^^^^^^^^^^^^^^^^^

The main item, the class that describes a business object, depicted in the class diagram is a rectangle with three horizontal sections, as shown in Figure 4. The upper section shows the object's name; the middle section contains the object's attributes; and the lower section contains the objects's operations (or "methods").

.. uml::
   :caption: Business Object Notation in a Class Diagram
   :width: 3cm
   :align: center

   class Object {
    +Property:type
    +Method()
   }


Class diagrams contain icons representing classes, and their relationships. In particular, class diagrams may contain: 

- Class
A class captures the common structure and common behavior of a set of objects. A class is an abstraction of real-world items. When these items exist in the real world, they are instances of the class, and referred to as objects. 

-  Association relationships 
An association represents a semantic connection between two classes, or between a class and an interface. Associations are bi-directional; they are the most general of all relationships and the most semantically weak. 

-  Aggregate relationship 
The aggregate relationship is more specific than association and is used to show a "partwhole" or “part-of" relationship between two classes. The class at the client end of the aggregate relationship is sometimes called the aggregate class. An instance of the aggregate class is an aggregate object. The class at the supplier end of the aggregate relationship is the part whose instances are contained or owned by the aggregate object. 
The aggregate relationship is used for showing that the aggregate object is physically constructed from other objects or that it logically contains another object. The aggregate object has ownership of its parts


Component diagrams
------------------

A component diagram provides a physical view of the system. Its purpose is to show the dependencies that the software has on the other software components (e.g., databases, interfaces) in the system. The diagram can be shown at a very high level, with just the large-grain components, or it can be shown at the component package level. 

Component diagrams notation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Components are wired together by using an assembly connector to connect the required interface of one component with the provided interface of another component. This illustrates the service consumer - service provider relationship between the two components.
Component diagrams contain: 

- Component packages 
Component packages represent clusters of logically related components, or major pieces of your system. They allow partitioning the physical model of the system into sub-systems.

- Components 
A component represents a software module (source code, binary code, executable, DLL, etc.) with a well-defined interface. The interface of a component is represented by one or several interface elements that the component provides. Components are used to show compiler and run-time dependencies, as well as interface and calling dependencies among software modules. They also show which components implement a specific class. 

- Interfaces
An interface specifies the externally visible operations of a class and/or component, and has no implementation of its own. An interface typically specifies only a limited part of the behavior of a class or component. 

- Dependency relationships 
The dependency relationship indicates that one entity in a component diagram uses the services or facilities of another. Dependencies in the component diagram represent compilation dependencies. The dependency relationship may also be used to show calling dependencies among components, using dependency arrows from components to interfaces on other components. 
When no caption details the relationship, the default one is “uses” that denotes the usage of one or more functions of a component to another.


Sequence diagrams
-----------------

Sequence diagrams show a detailed flow for a specific use case or even just part of a specific use case. They are almost self-explanatory; they show the calls between the different objects in their sequence and can show, at a detailed level, different calls to different objects.

Sequence diagrams notation
^^^^^^^^^^^^^^^^^^^^^^^^^^

A sequence diagram has two dimensions: The vertical dimension shows the sequence of messages/calls in the time order that they occur; the horizontal dimension shows the object instances to which the messages are sent.
Across the top of the diagram there are the class instances (objects) inside a box. In the box, the class instance name and class name separated by a colon" : " (e.g., myService : Service). If a class instance sends a message to another class instance, a line with an open arrowhead points to the receiving class instance; the name of the message/method is placed above the line. Optionally, for important messages, there can be a dotted line with an arrowhead pointing back to the originating class instance; with return value labeled above the dotted line.


Deployment diagrams
-------------------

Deployment diagrams show the configuration of run-time processing elements and the software components, processes, and objects that live on them. Software component instances represent run-time manifestations of code units. Components that do not exist as run-time entities (because they have been compiled away) do not appear on these diagrams.

Deployment diagrams notation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The deployment diagram shows how a system will be physically deployed in the hardware environment. Its purpose is to show where the different components of the system will physically run and how they will communicate with each other. The notation in a deployment diagram includes the notation elements used in a component diagram, with a couple of additions, including the concept of a node. A node represents either a physical machine or a virtual machine node (e.g., virtualized server) with the naming convention used in sequence diagrams: [instance name] : [instance type] (e.g., "server.terradue.com : Web Server").



   



