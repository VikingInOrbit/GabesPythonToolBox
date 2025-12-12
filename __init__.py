import os

# Insert the inner package directory at the front of the package search path.
__path__.insert(0, os.path.join(os.path.dirname(__file__), "GabesPythonToolBox"))
