"""Demonstration of motor performance calculations."""
from drone_sim.motor import (
    rpm_to_rad_s,
    calculate_thrust,
    calculate_torque
)

# Motor specifications
rpm = input("Enter motor RPM: ")

# Simplified propeller coefficients
k_t = float(input("Enter thrust constant (k_t): Generally between 1e-6 and 1e-5 for small propellers: "))
k_q = float(input("Enter torque constant (k_q): Generally between 1e-8 and 1e-7 for small propellers: "))

# Calculate motor performance
omega = rpm_to_rad_s(rpm)

thrust = calculate_thrust(rpm, k_t)

torque = calculate_torque(rpm, k_q)

# Display results
print("MOTOR SIMULATION")
print("----------------")

print(f"RPM: {rpm}")
print(f"Angular Velocity: {omega:.2f} rad/s")
print(f"Thrust: {thrust:.3f} N")
print(f"Reaction Torque: {torque:.5f} N*m")