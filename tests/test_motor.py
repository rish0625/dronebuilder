from drone_sim.motor import calculate_thrust

rpm = 10000
k_t = 1e-6  # Illustrative coefficient, not measured data

thrust = calculate_thrust(rpm, k_t)

print(f"Thrust: {thrust:.2f} N")


def test_zero_rpm():
    assert calculate_thrust(0, 1e-6) == 0


def test_thrust_increases_with_rpm():
    thrust_1 = calculate_thrust(5000, 1e-6)
    thrust_2 = calculate_thrust(10000, 1e-6)

    assert thrust_2 > thrust_1


def test_double_rpm_quadruples_thrust():
    thrust_1 = calculate_thrust(5000, 1e-6)
    thrust_2 = calculate_thrust(10000, 1e-6)

    assert abs(thrust_2 / thrust_1 - 4) < 1e-9