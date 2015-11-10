## Urban Thematic Exploitation Platform Design Document

[![Build Status](https://build.terradue.com/buildStatus/icon?job=esa-tep-urban-ddf)](https://build.terradue.com/job/esa-tep-hydro-ddf/)

This is the official repository of the TEP Urban Software Design Document. 

This documentation is live at: http://docs.terradue.com/esa-tep-urban-ddf/

user / pass : tep / urban

### Getting started

Here's the procedure to install the required packages

1) Install sphinx

see here: http://sphinx-doc.org/latest/install.html

2) If needed, set your github information:

```bash
$ git config --global user.name <github username>
$ git config --global user.email <email address>
```

3) To build the PDF, install rst2pdf

see here: https://github.com/rst2pdf/rst2pdf

### Building locally

Build the documentation by running ``make html`` or ``make pdf``

### Continuous build

The PDF is generated at http://docs.terradue.com/esa-tep-urban-ddf/UrbanTEP-SDD.pdf every time a change is pushed on the repo.

#### This documentation is built with [sphinx](http://sphinx-doc.org/).
