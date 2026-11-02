from drone_sim.motor import calculate_thrust

rpm = 10000
k_t = 1e-6  # Illustrative coefficient, not measured data

thrust = calculate_thrust(rpm, k_t)

print(f"Thrust: {thrust:.2f} N")