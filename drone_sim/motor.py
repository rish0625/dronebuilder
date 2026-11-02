"Drone movement comes directly fromt the motors, and this file serves to model a motor "
"and its behavior. The motor is modeled as a simple first-order system with a time constant "
"and a maximum speed. "

import numpy as np

def rpm_to_rad_s(rpm):
    """Convert motor speed from RPM to rad/s."""
    return rpm * (2 * np.pi / 60)


def calculate_thrust(rpm, k_t):
    """Calculate static propeller thrust in Newtons."""
    omega = rpm_to_rad_s(rpm)
    thrust = k_t * omega**2

    return thrust