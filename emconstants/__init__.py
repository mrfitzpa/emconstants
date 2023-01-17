"""``emconstants`` is a small Python library that stores values of physical
constants that are used in electron microscopy.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# Import child modules and packages of current package.
import emconstants.version



############################
## Authorship information ##
############################

__author__       = "Matthew Fitzpatrick"
__copyright__    = "Copyright 2023"
__credits__      = ["Matthew Fitzpatrick"]
__version__      = emconstants.version.version
__full_version__ = emconstants.version.full_version
__maintainer__   = "Matthew Fitzpatrick"
__email__        = "mrfitzpa@uvic.ca"
__status__       = "Development"



###################################
## Useful background information ##
###################################

# See e.g. ``https://docs.python.org/3/reference/import.html#regular-packages``
# for a brief discussion of ``__init__.py`` files.



##################################
## Define classes and functions ##
##################################

# List of public objects in package.
__all__ = ["show_config"]



def show_config():
    """Print information about the version of ``emconstants`` and libraries it 
    uses.

    """
    print(version.version_summary)

    return None



######################
## Define constants ##
######################

tol = 1.0e-10  # Primarily for comparing floats.
m_e = 9.109383e-31  # Rest mass of electron, in units of kilograms.
e = 1.602177e-19  # Elementary charge, in units of Coulombs
c = 299792458  # Speed of light, in units of meters per second.
h = 6.62607e-34  # Planck's constant, in units of Joules*second.



###########################
## Define error messages ##
###########################
