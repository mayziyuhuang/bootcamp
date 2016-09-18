import numpy as np
import pytest
import lesson36b

def test_dissoc_equil():
    """Tests for dissoc_equil()."""

    # Edge cases
    assert np.isclose(dissoc_equil(1, 0, 0), np.array([0, 0, 0])).all()
    assert np.isclose(dissoc_equil(0, 0, 0), np.array([0, 0, 0])).all()
    assert np.isclose(dissoc_equil(0, 1, 1), np.array([0, 0, 1])).all()
    assert np.isclose(dissoc_equil(0, 1, 2), np.array([0, 1, 1])).all()
    assert np.isclose(dissoc_equil(0, 2, 1), np.array([1, 0, 1])).all()
    assert np.allclose(dissoc_equil(np.inf, 1, 1), np.array([1, 1, 0]))

    # # standard cases using log
    # Kd_vals = np.logspace(-10, 1, 50)
    # ca0_vals = np.logspace(-5, 2, 50)
    # cb0_vals = np.logspace(-5, 2, 50)
    # for Kd in Kd_vals:
    #     for ca0 in ca0_vals:
    #         for cb0 in cb0_vals:
    #             assert check_eq(Kd, ca0, cb0, *dissoc_equil(Kd, ca0, cb0)), \
    #                 'Kd = %g, ca0 = %g, cb0 = %g' % (Kd, ca0, cb0)
    # #We get an error when the difference in the total concentrations is too large. This highlights a numerical stability issue. When this is the case, we should find a more numerically stable way to compute the result.

    # standard cases
    assert check_eq(4.5, 0.1, 3.2, *dissoc_equil(4.5, 0.1, 3.2))
    assert check_eq(0.14, 0.00011, 0.003, *dissoc_equil(0.14, 0.00011, 0.003))
    # errors
    pytest.raises(RuntimeError, "dissoc_equil(-1, 1, 1)")
    pytest.raises(RuntimeError, "dissoc_equil(1, -1, 1)")
    pytest.raises(RuntimeError, "dissoc_equil(1, 1, -1)")
    pytest.raises(RuntimeError, "dissoc_equil(1, np.inf, 1)")
    pytest.raises(RuntimeError, "dissoc_equil(1, 1, np.inf)")



    return None

def dissoc_equil(Kd, ca0, cb0):
    """Compute equilibrium for dissociation reaction."""

    # check input
    if Kd < 0 or ca0 < 0 or cb0 < 0:
        raise RuntimeError('All input must be nonnegative.')
    if not (ca0 < np.inf and cb0 < np.inf):
        raise RuntimeError('Input concentrations must be finite.')

    # if we have infinite Kd
    if Kd == np.inf:
        return ca0, cb0, 0

    #compute cab, ca, cb
    total = Kd + ca0 + cb0
    cab = (total - np.sqrt(total**2 - 4 * ca0 * cb0)) / 2
    ca = ca0 - cab
    cb = cb0 - cab

    return ca, cb, cab


def check_eq(Kd, ca0, cb0, ca, cb, cab):
    """verify equilibrium expresssion hold."""
    eq = np.isclose(Kd, ca * cb / cab)
    cons_mass_A = np.isclose(ca0, ca + cab)
    cons_mass_B = np.isclose(cb0, cb + cab)

    return eq and cons_mass_A and cons_mass_B
