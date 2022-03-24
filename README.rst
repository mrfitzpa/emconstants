EMconstants
===========

``emconstants`` is a small Python library that stores values of physical
constants that are used in electron microscopy.

Setting up emconstants
----------------------

For instructions on installing the ``emconstants`` library, see the
:ref:`installation_instructions_sec` page.

.. Note for those reading the raw .rst file: see file 'docs/INSTALL.rst' for
   instructions on installing the emconstants library as well as instructions
   for compiling the documentation of this library.

Using emconstants
-----------------

``emconstants`` should be used to build other libraries related to electron
microscopy. As mentioned above, ``emconstants`` is a small library that stores
values of physical constants. The following lines of code demonstrate how to
access these physical constants:

.. code-block::

   emconstants.m_e  # Rest mass of electron; in units of kilograms; `float`
   emconstants.e  # Elementary charge; in units of Coulombs; `float`
   emconstants.c  # Speed of light; in units of meters per second; `float`
   emconstants.h  # Planck's constant; in units of Joules*second; `float`
   emconstants.tol  # Equal to 1.0e-10; to be used for comparing numbers.
