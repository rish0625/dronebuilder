#Code to plot thrust vs RPM for a given motor and propeller combination.

import numpy as np
import matplotlib.pyplot as plt

from drone_sim.motor import calculate_thrust

rpm_values = np.linspace(0, 20000, 100)  # RPM range from 0 to 20,000
k_t = 1e-6  # Example thrust constant for a specific propeller

thrust_values = [calculate_thrust(rpm, k_t) for rpm in rpm_values]

plt.figure(figsize=(10, 6))
plt.plot(rpm_values, thrust_values, label='Thrust')
plt.xlabel('RPM')
plt.ylabel('Thrust (N)')
plt.title('Thrust vs RPM')
plt.legend()
plt.grid(True)
plt.show()