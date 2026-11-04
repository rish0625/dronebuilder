#This will test the mass properties calculations for a drone, including total mass, center of mass, and moments of inertia.
import unittest

class TestMassProperties(unittest.TestCase):
    def setUp(self):
        """Set up the test case with a sample drone and its components."""
        from drone_sim.drone import Drone, Frame, Motor
        from drone_sim.mass_properties import calculate_total_mass, calculate_center_of_mass, calculate_moments_of_inertia

        # Sample dimensions and positions
        dimensions = (1.0, 1.0, 0.5)  # Length, Width, Height
        motor_positions = [(0.5, 0.5, 0), (-0.5, 0.5, 0), (-0.5, -0.5, 0), (0.5, -0.5, 0)]
        add_component_masses = [1.0]  # Additional component mass
        component_positions = [(0, 0, 0)]  # Position of additional component

        # Create a sample drone
        self.drone = Drone(dimensions, motor_positions, add_component_masses, component_positions)

        # Create a sample frame
        self.frame = Frame(2.0, dimensions, motor_positions)

        # Create sample motors
        self.motors = [Motor(0.5, pos, 1.0, 1.0, 12.0, 10000) for pos in motor_positions]

        # Create a sample battery
        self.battery = type('Battery', (object,), {'get_mass': lambda self: 1.5})()

        # Create a sample flight controller
        self.flight_controller = type('FlightController', (object,), {'get_mass': lambda self: 0.3})()

        # Create sample propellers
        self.propellers = [type('Propeller', (object,), {'get_mass': lambda self: 0.2})() for _ in range(4)]

        # Create sample antennas
        self.antennas = [type('Antenna', (object,), {'get_mass': lambda self: 0.1})() for _ in range(2)]

    def test_total_mass(self):
        """Test the total mass calculation."""
        from drone_sim.mass_properties import calculate_total_mass
        total_mass = calculate_total_mass(self.drone, self.frame, self.motors, self.battery, self.flight_controller, self.propellers, self.antennas)
        expected_mass = (
            self.drone.get_total_mass() +
            self.frame.get_mass() +
            sum(motor.get_mass() for motor in self.motors) +
            self.battery.get_mass() +
            self.flight_controller.get_mass() +
            sum(propeller.get_mass() for propeller in self.propellers) +
            sum(antenna.get_mass() for antenna in self.antennas)
        )
        self.assertEqual(total_mass, expected_mass)