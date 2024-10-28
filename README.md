# Fuzzy-System-for-Crop-Distribution
This project implements a fuzzy logic-based irrigation system designed to optimize water usage based on soil humidity and temperature. Using the `scikit-fuzzy` library, the system defines input variables, membership functions, and fuzzy rules to determine the appropriate amount of water needed for irrigation.

## Prerequisites
Before running the project, ensure you have the following Python libraries installed:
<ol>
  <li>  **NumPy:** For numerical operations.</li>
  <li>  **Matplotlib:** For plotting graphs and visualizations.</li>
  <li>  **scikit-fuzzy:** For fuzzy logic computations.</li>
</ol>
You can install these libraries using `pip`. Open your terminal or command prompt and run the following command:

```
pip install numpy matplotlib scikit-fuzzy
```

## Features
<ul>
  <li> Dynamic Input Variables: Models soil humidity and temperature as fuzzy inputs to assess irrigation needs. </li>
  <li> Fuzzy Membership Functions: Defines linguistic terms for input variables to simulate real-world conditions. </li>
  <li> Rule-Based Decision Making: Employs a set of fuzzy rules to compute water requirements based on varying conditions. </li>
  <li> Visual Outputs: Generates plots for membership functions, heatmaps, and 3D surface plots for a comprehensive analysis of irrigation decisions. </li>
  <li> Test Output Function: Easily test and compute irrigation outputs using example input values. </li>
</ul>

## Usage
To test the system, you can modify the `test_output` function with desired soil humidity and temperature values. The system will output the computed water amount based on the provided inputs.




