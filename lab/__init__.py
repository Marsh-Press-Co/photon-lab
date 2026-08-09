"""Photon Lab shared bench: 2D TMz FDTD engine + material builders.
Grown from experiments (000 ->), never speculatively. See
lab/validation/VALIDATION.md for what has been verified against what."""

from .fdtd2d import Sim, PoyntingLine
from . import materials

__all__ = ["Sim", "PoyntingLine", "materials"]
