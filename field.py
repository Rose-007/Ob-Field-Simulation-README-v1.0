import numpy as np


def generate_field(X, Y, t):
    """Generate a nonlinear wave-field pattern.

    Parameters
    ----------
    X, Y : np.ndarray
        Meshgrid arrays.
    t : float
        Time/phase value.

    Returns
    -------
    np.ndarray
        Stabilized field values.
    """
    R = np.sqrt(X**2 + Y**2)
    theta = np.arctan2(Y, X)

    z = (
        np.sin(1.15 * X + 1.55 * Y + t)
        + np.sin(1.85 * X - 1.25 * Y - 0.75 * t)
        + 0.9 * np.sin(1.15 * R - 1.4 * t)
        + 0.65 * np.sin(4 * theta + 0.9 * np.sin(t))
        + 0.35 * np.sin(0.28 * X * Y + 0.5 * t)
    )

    return np.tanh(z)
