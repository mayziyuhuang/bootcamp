import numpy as np
import pytest

def dissoc_equil(Kd, ca0, cb0):
    """Compute equilibrium for dissociation reaction."""

    #compute cab, ca, cb
    total = Kd + ca0 + cb0
    cab = (total - np.sqrt(total**2 - 4 * ca0 * cb0)) / 2
    ca = ca0 - cab
    cb = cb0 - cab

    return ca, cb, cab
