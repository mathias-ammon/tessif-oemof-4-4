# src/tessif_oemof_4_4/__init__.py
"""tessif-oemof-4-4."""
from importlib.metadata import version

from .solve import optimize
from .tsf2omf import transform


__version__ = version(__name__)
