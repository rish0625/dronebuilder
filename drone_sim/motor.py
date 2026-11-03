"Drone movement comes directly fromt the motors, and this file serves to model a motor "
"and its behavior. The motor is modeled as a simple first-order system with a time constant "
"and a maximum speed. "

# Motor Basics: T = k_t*omega^2, where T is thrust, k_t is the thrust constant, and omega is the angular velocity in rad/s.
# Q = k_q * omega, where Q is torque, k_q is the torque constant, and omega is the angular velocity in rad/s.



import numpy as np

def rpm_to_rad_s(rpm):
    """Convert motor speed from RPM to rad/s."""
    return rpm * (2 * np.pi / 60)


def calculate_thrust(rpm, k_t):
    """Calculate static propeller thrust in Newtons."""
    omega = rpm_to_rad_s(rpm)
    thrust = k_t * omega**2

    return thrust

def calculate_torque(rpm, k_q):
    """Calculate static propeller torque in Newton-meters."""
    omega = rpm_to_rad_s(rpm)

    torque = k_q * omega**2

    return torque