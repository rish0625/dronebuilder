#This will test the mass properties calculations for a drone, including total mass, center of mass, and moments of inertia.
import unittest
import numpy as np

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
        battery_units = [1.5, (0, 0, 0)]  # Mass, Positions, and other properties of the battery
        flight_controller_units = [0.3, (0, 0, 0)]  # Mass, Positions, and other properties of the flight controller
        propeller_units = [0.2, (0, 0, 0)]  # Mass, Positions, and other properties of the propellers
        antenna_units = [0.1, (0, 0, 0)]  # Mass, Positions, and other properties of the antennas

        # Create a sample drone
        self.drone = Drone(dimensions, motor_positions, add_component_masses, component_positions)

        # Create a sample frame
        self.frame = Frame(2.0, dimensions, motor_positions)

        # Create sample motors
        self.motors = [Motor(0.5, pos, 1.0, 1.0, 12.0, 10000) for pos in motor_positions]

        # Create a sample battery
        self.battery = type('Battery', (object,), {'get_mass': lambda self: battery_units[0], 'get_position': lambda self: battery_units[1]})()

        # Create a sample flight controller
        self.flight_controller = type('FlightController', (object,), {'get_mass': lambda self: flight_controller_units[0], 'get_position': lambda self: flight_controller_units[1]})()

        # Create sample propellers
        self.propellers = [type('Propeller', (object,), {'get_mass': lambda self: propeller_units[0], 'get_position': lambda self: propeller_units[1]})() for _ in range(4)]

        # Create sample antennas
        self.antennas = [type('Antenna', (object,), {'get_mass': lambda self: antenna_units[0], 'get_position': lambda self: antenna_units[1]})() for _ in range(2)]

        #Create sample extra components
        self.extra_components = [type('ExtraComponent', (object,), {'get_mass': lambda self: add_component_masses[i], 'get_position': lambda self: component_positions[i]})() for i in range(2)]

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


    def test_center_of_mass(self):
        """Test the center of mass calculation."""
        from drone_sim.mass_properties import calculate_center_of_mass
        center_of_mass = calculate_center_of_mass(self.drone, self.frame, self.motors, self.battery, self.flight_controller, self.propellers, self.antennas)
        
        # Calculate expected center of mass manually
        total_mass = (
            self.drone.get_total_mass() +
            self.frame.get_mass() +
            sum(motor.get_mass() for motor in self.motors) +
            self.battery.get_mass() +
            self.flight_controller.get_mass() +
            sum(propeller.get_mass() for propeller in self.propellers) +
            sum(antenna.get_mass() for antenna in self.antennas)
        )
        
        weighted_positions = (
            self.drone.get_total_mass() * np.array(self.drone.get_dimensions()) +
            self.frame.get_mass() * np.array(self.frame.get_dimensions()) +
            sum(motor.get_mass() * np.array(motor.get_position()) for motor in self.motors) +
            self.battery.get_mass() * np.array((0, 0, 0)) +  # Assuming battery at origin
            self.flight_controller.get_mass() * np.array((0, 0, 0)) +  # Assuming flight controller at origin
            sum(propeller.get_mass() * np.array((0, 0, 0)) for propeller in self.propellers) +  # Assuming propellers at origin
            sum(antenna.get_mass() * np.array((0, 0, 0)) for antenna in self.antennas)  # Assuming antennas at origin
        )
        
        expected_center_of_mass = weighted_positions / total_mass
        
        np.testing.assert_array_almost_equal(center_of_mass, expected_center_of_mass)

    def test_moments_of_inertia(self):
        """Test the moments of inertia calculation."""
        from drone_sim.mass_properties import calculate_moments_of_inertia
        from drone_sim.mass_properties import calculate_center_of_mass
        moments_of_inertia = calculate_moments_of_inertia(self.drone, self.frame, self.motors, self.battery, self.flight_controller, self.propellers, self.antennas)
        
        # Calculate expected moments of inertia manually
        total_mass = (
            self.drone.get_total_mass() +
            self.frame.get_mass() +
            sum(motor.get_mass() for motor in self.motors) +
            self.battery.get_mass() +
            self.flight_controller.get_mass() +
            sum(propeller.get_mass() for propeller in self.propellers) +
            sum(antenna.get_mass() for antenna in self.antennas)
        )
        
        center_of_mass = calculate_center_of_mass(self.drone, self.frame, self.motors, self.battery, self.flight_controller, self.propellers, self.antennas)
        
        I_xx = 0
        I_yy = 0
        I_zz = 0
        
        for component in [self.drone, self.frame] + self.motors + [self.battery] + [self.flight_controller] + self.propellers + self.antennas:
            mass = component.get_mass()
            position = np.array(component.get_position())
            r = position - center_of_mass
            
            I_xx += mass * (r[1]**2 + r[2]**2)
            I_yy += mass * (r[0]**2 + r[2]**2)
            I_zz += mass * (r[0]**2 + r[1]**2)
        
        expected_moments_of_inertia = np.array([I_xx, I_yy, I_zz])
        
        np.testing.assert_array_almost_equal(moments_of_inertia, expected_moments_of_inertia)