import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
from mpl_toolkits.mplot3d import Axes3D

# Define the input variables with ranges
soil_humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'soil_humidity')
temperature = ctrl.Antecedent(np.arange(0, 46, 1), 'temperature')
water_amount = ctrl.Consequent(np.arange(0, 101, 1), 'water_amount')

# Define membership functions for Soil Humidity
soil_humidity['dry'] = fuzz.trimf(soil_humidity.universe, [0, 0, 30])
soil_humidity['moderate'] = fuzz.trimf(soil_humidity.universe, [30, 50, 70])
soil_humidity['wet'] = fuzz.trimf(soil_humidity.universe, [70, 100, 100])

# Define membership functions for Temperature
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 15])
temperature['moderate'] = fuzz.trimf(temperature.universe, [15, 22.5, 30])
temperature['high'] = fuzz.trimf(temperature.universe, [30, 45, 45])

# Define membership functions for Water Amount
water_amount['low'] = fuzz.trimf(water_amount.universe, [0, 0, 30])
water_amount['medium'] = fuzz.trimf(water_amount.universe, [30, 50, 70])
water_amount['high'] = fuzz.trimf(water_amount.universe, [70, 100, 100])

# Define rules
rules = [
    ctrl.Rule(soil_humidity['dry'] & temperature['high'], water_amount['high']),
    ctrl.Rule(soil_humidity['dry'] & temperature['moderate'], water_amount['high']),
    ctrl.Rule(soil_humidity['dry'] & temperature['low'], water_amount['medium']),
    ctrl.Rule(soil_humidity['moderate'] & temperature['high'], water_amount['medium']),
    ctrl.Rule(soil_humidity['moderate'] & temperature['moderate'], water_amount['medium']),
    ctrl.Rule(soil_humidity['moderate'] & temperature['low'], water_amount['low']),
    ctrl.Rule(soil_humidity['wet'] & temperature['high'], water_amount['low']),
    ctrl.Rule(soil_humidity['wet'] & temperature['moderate'], water_amount['low']),
    ctrl.Rule(soil_humidity['wet'] & temperature['low'], water_amount['low'])
]

# Control system setup
water_ctrl = ctrl.ControlSystem(rules)
watering = ctrl.ControlSystemSimulation(water_ctrl)

# Function to test output with example inputs
def test_output(soil_humidity_value, temperature_value):
    watering.input['soil_humidity'] = soil_humidity_value
    watering.input['temperature'] = temperature_value
    watering.compute()
    print(f"Input - Soil Humidity: {soil_humidity_value}%, Temperature: {temperature_value}°C")
    print(f"Output - Water Amount: {watering.output['water_amount']}%")

# Function to plot membership functions
def plot_membership_functions():
    fig, ax = plt.subplots(3, 1, figsize=(10, 10))

    ax[0].plot(soil_humidity.universe, soil_humidity['dry'].mf, label='Dry', color='blue')
    ax[0].plot(soil_humidity.universe, soil_humidity['moderate'].mf, label='Moderate', color='green')
    ax[0].plot(soil_humidity.universe, soil_humidity['wet'].mf, label='Wet', color='red')
    ax[0].set_title('Soil Humidity Membership')
    ax[0].legend()

    ax[1].plot(temperature.universe, temperature['low'].mf, label='Low', color='blue')
    ax[1].plot(temperature.universe, temperature['moderate'].mf, label='Moderate', color='green')
    ax[1].plot(temperature.universe, temperature['high'].mf, label='High', color='red')
    ax[1].set_title('Temperature Membership')
    ax[1].legend()

    ax[2].plot(water_amount.universe, water_amount['low'].mf, label='Low', color='blue')
    ax[2].plot(water_amount.universe, water_amount['medium'].mf, label='Medium', color='green')
    ax[2].plot(water_amount.universe, water_amount['high'].mf, label='High', color='red')
    ax[2].set_title('Water Amount Membership')
    ax[2].legend()

    plt.tight_layout()
    plt.show()

# Function to create a heatmap
def plot_heatmap():
    soil_values = np.arange(0, 101, 5)
    temp_values = np.arange(0, 46, 5)
    output_values = np.zeros((len(soil_values), len(temp_values)))

    for i, soil in enumerate(soil_values):
        for j, temp in enumerate(temp_values):
            watering.input['soil_humidity'] = soil
            watering.input['temperature'] = temp
            watering.compute()
            output_values[i, j] = watering.output.get('water_amount', np.nan)  # Use NaN if missing

    plt.figure(figsize=(8, 6))
    plt.imshow(output_values, extent=[0, 45, 0, 100], origin='lower', aspect='auto', cmap='coolwarm')
    plt.colorbar(label='Water Amount (%)')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Soil Humidity (%)')
    plt.title('Water Amount Heatmap by Soil Humidity and Temperature')
    plt.show()

# Function to create a 3D surface plot
def plot_surface():
    soil_values = np.arange(0, 101, 5)
    temp_values = np.arange(0, 46, 5)
    soil_grid, temp_grid = np.meshgrid(soil_values, temp_values)
    output_grid = np.zeros_like(soil_grid)

    for i in range(soil_grid.shape[0]):  # Correctly use the shape of soil_grid
        for j in range(soil_grid.shape[1]):  # Correctly use the shape of soil_grid
            watering.input['soil_humidity'] = soil_grid[i, j]
            watering.input['temperature'] = temp_grid[i, j]
            watering.compute()
            output_value = watering.output.get('water_amount', np.nan)  # Use NaN if missing
            output_grid[i, j] = output_value

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(soil_grid, temp_grid, output_grid, cmap='viridis')
    ax.set_xlabel('Soil Humidity (%)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_zlabel('Water Amount (%)')
    ax.set_title('3D Surface Plot of Water Amount')
    plt.show()

# Main execution
plot_membership_functions()
plot_heatmap()
plot_surface()

# Example usage of the test_output function
test_output(20, 25)  # Example inputs: Soil Humidity = 20%, Temperature = 25°C