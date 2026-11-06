#This file serves to calculate the mass properties of a drone, including its total mass, center of mass, and moments of inertia.

"d -> drone, f -> frame, m -> motors, b -> battery, fc -> flight controller, p -> propellers, a -> antennas"


import numpy as np

#Logic for total mass: sum the masses of all components (drone, frame, motors, battery, flight controller, propellers, antennas).
def calculate_total_mass(d, f, m, b, fc, p, a):
    """Calculate the total mass of the drone."""
    return d.get_total_mass() + f.get_mass() + sum(motor.get_mass() for motor in m) + b.get_mass() + fc.get_mass() + sum(propeller.get_mass() for propeller in p) + sum(antenna.get_mass() for antenna in a)


#Logic for center of mass: calculate the weighted average position of all components, by multiplying each component's mass by its position, 
#summing these products, and dividing by the total mass.
def calculate_center_of_mass(d, f, m, b, fc, p, a):
    """Calculate the center of mass of the drone."""
    total_mass = calculate_total_mass(d, f, m, b, fc, p, a)

    # Calculate the weighted positions of each component
    weighted_positions = (
        d.get_total_mass() * np.array(d.get_dimensions()) +
        f.get_mass() * np.array(f.get_dimensions()) +
        sum(motor.get_mass() * np.array(motor.get_position()) for motor in m) +
        b.get_mass() * np.array(b.get_position()) +
        fc.get_mass() * np.array(fc.get_position()) +
        sum(propeller.get_mass() * np.array(propeller.get_position()) for propeller in p) +
        sum(antenna.get_mass() * np.array(antenna.get_position()) for antenna in a)
    )
    
    # Calculate the center of mass
    center_of_mass = weighted_positions / total_mass
    
    return center_of_mass

def calculate_moments_of_inertia(d, f, m, b, fc, p, a):
    """Calculate the moments of inertia of the drone."""
    total_mass = calculate_total_mass(d, f, m, b, fc, p, a)
    center_of_mass = calculate_center_of_mass(d, f, m, b, fc, p, a)

    # Initialize moments of inertia
    I_xx = 0
    I_yy = 0
    I_zz = 0

    # Calculate moments of inertia for each component
    for component in [d, f] + m + [b] + [fc] + p + a:
        mass = component.get_mass()
        position = np.array(component.get_position())
        r = position - center_of_mass
        
        # Parallel axis theorem
        I_xx += mass * (r[1]**2 + r[2]**2)
        I_yy += mass * (r[0]**2 + r[2]**2)
        I_zz += mass * (r[0]**2 + r[1]**2)

    return np.array([I_xx, I_yy, I_zz])