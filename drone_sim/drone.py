#This is a drone simulation class that stores drone mass, dimensions, motor positions, and the additional component mass and positions outside of the main drone structure.
#Additionally, it contains classes for the frame, motor, battery, flight controller, and propeller, each with their own mass, position, and other relevant properties.

class Drone:
    def __init__(self, dimensions, motor_positions, add_component_masses, component_positions):
        """Initialize the Drone class with its dimensions, motor positions, additional component masses, and their positions."""
        self.mass = sum(add_component_masses)  # Total mass of the drone
        self.dimensions = dimensions  # Dimensions of the drone (length, width, height)
        self.motor_positions = motor_positions  # Positions of the motors on the drone
        self.component_positions = component_positions  # Positions of individual components

    """Get the total mass of the drone."""
    def get_total_mass(self):
        return self.mass

    def get_dimensions(self):
        return self.dimensions

    def get_motor_positions(self):
        return self.motor_positions

    def get_component_positions(self):
        return self.component_positions

class Frame:
    def __init__(self, mass, dimensions, motor_positions):
        self.mass = mass  # Mass of the frame
        self.dimensions = dimensions  # Dimensions of the frame (length, width, height)
        self.motor_positions = motor_positions  # Positions of the motors on the frame

    def get_mass(self):
        return self.mass

    def get_dimensions(self):
        return self.dimensions

    def get_motor_positions(self):
        return self.motor_positions

class Motor:
    def __init__(self, mass, position, k_t, k_q, input_voltage, max_rpm):
        self.mass = mass  # Mass of the motor
        self.position = position  # Position of the motor on the drone
        self.k_t = k_t  # Thrust coefficient
        self.k_q = k_q  # Torque coefficient
        self.input_voltage = input_voltage  # Input voltage to the motor
        self.max_rpm = max_rpm  # Maximum revolutions per minute

    def get_input_voltage(self):
        return self.input_voltage

    def get_max_rpm(self):
        return self.max_rpm

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position

    def get_thrust_coefficient(self):
        return self.k_t

    def get_torque_coefficient(self):
        return self.k_q

class Battery:
    def __init__(self, mass, position, capacity, voltage):
        self.mass = mass  # Mass of the battery
        self.position = position  # Position of the battery on the drone
        self.capacity = capacity  # Capacity of the battery
        self.voltage = voltage  # Voltage of the battery

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position

    def get_capacity(self):
        return self.capacity

    def get_voltage(self):
        return self.voltage


class FlightController:
    def __init__(self, mass, position, sensors):
        self.mass = mass  # Mass of the flight controller
        self.position = position  # Position of the flight controller on the drone
        self.sensors = sensors  # List of sensors on the flight controller

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position

    def get_sensors(self):
        return self.sensors

class Propeller:
    def __init__(self, mass, position, diameter, pitch):
        self.mass = mass  # Mass of the propeller
        self.position = position  # Position of the propeller on the drone
        self.diameter = diameter  # Diameter of the propeller
        self.pitch = pitch  # Pitch of the propeller

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position

    def get_diameter(self):
        return self.diameter

    def get_pitch(self):
        return self.pitch

class Antenna:
    def __init__(self, mass, position, frequency_range, input_voltage):
        self.mass = mass  # Mass of the antenna
        self.position = position  # Position of the antenna on the drone
        self.frequency_range = frequency_range  # Frequency range of the antenna
        self.input_voltage = input_voltage  # Input voltage to the antenna

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position

    def get_frequency_range(self):
        return self.frequency_range

    def get_input_voltage(self):
        return self.input_voltage

class Component:
    def __init__(self, mass, position):
        self.mass = mass  # Mass of the component
        self.position = position  # Position of the component on the drone

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position
