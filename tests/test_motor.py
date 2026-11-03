#Code to test the motor.py module

from drone_sim.motor import (
    rpm_to_rad_s,
    calculate_thrust,
    calculate_torque
)

def test_rpm_conversion():

    omega = rpm_to_rad_s(10000)

    assert abs(omega - 1047.1976) < 0.001


def test_zero_rpm():

    assert calculate_thrust(0, 1e-6) == 0


def test_double_rpm_quadruples_thrust():

    t1 = calculate_thrust(5000, 1e-6)
    t2 = calculate_thrust(10000, 1e-6)

    assert abs(t2 / t1 - 4) < 1e-9


def test_torque_calculation():

    torque = calculate_torque(10000, 1e-8)

    assert abs(torque - 0.010966) < 0.00001