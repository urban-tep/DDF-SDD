Implementation choices
======================

.. req:: TS-DES-120
  :show:

  This section describes the implementation choices and the development framework to be infrastructure independent.


Modular Software
----------------

The TEP system is built with several building bricks developed as inter-dependent modules integrated together to provide with the complete platform. The WebServer provides with most of the basics functionalities. Such a division ensure the modularity and the flexibility of the whole system.


Portable Programming Languages
------------------------------

Most of the software bricks of the TEP platform are developed using high-level (as opposed to machine-level) programming language that are platform independent.

The Web Server software high-level programming language uses the `mono framework <http://www.mono-project.com/>`_, which is a multi-platform open source implementation of Microsoft's .NET framework. Mono is widely compatible with .NET and provides compilers for the C# programming language, the most important of the .NET programming languages, translating it into an intermediate language (defined by .NET). The byte code of this intermediate language is executed by a Virtual Machine. By abstracting the machine-level aspects like memory, processor and operating system, it brings portability to the developed software. Unlike .NET, the mono framework runs not only on Windows, but also on Linux and Mac OS X operating systems.

Many other third party software are also developed using .Net or Java such as Elasticsearch or Hadoop.


Long Lifetime Web Architecture
------------------------------

MVC computational model presents many advantages for maintaining the software in a long lifetime. User interface logic tends to change more frequently than business logic, especially in Web-based applications. For example, new user interfaces may be added, or existing interfaces may be shuffled around.


Processors as Docker Containers
-------------------------------

Wide usage of virtualization and possibility to start virtual environments within cloud services significantly simplifies creation of environments and provisioning of resources. However it still leaves a problem of portability of complete environments where applications are developed unresolved. Previous virtualization solutions are not light and flexible enough partially due to the size of the images. Docker fills this gap providing with a platform designated both for developers and system administrators. The main difference between a Docker container and a virtual machine lies in the fact that a virtual machine consists of, besides an application itself, also an operating system with binary files needed. Docker image works as an isolated process in a host’s operating system, which shares a kernel with other containers. Thereby, still using benefits of virtualization, it is more portable – an application uses less disk space – and more effective.






