#######################################
SPICE syntax highlight for Latex minted
#######################################

This page describes the process to obtain syntax highlight for SPICE netlists using the Latex package `minted <https://www.ctan.org/pkg/minted>`_. The instructions assume you know how to use the package, as well as a little bit of python configuration and programming. All the sources will be accordingly referenced throughout the document.

`minted` config
===============
The `minted` package requires the option `-shell-escape` during the Latex compile process so make sure to add it. Additionally, the package uses the `pygments` Pyhton library, you can easily install it with pip:

`pip install pygments`

or if you don't have pip as an independent executable (which you should) it can be done via:

`python -m pip install pygments`
