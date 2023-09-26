# HAI-CONCise-UHPC

Welcome to the HAI-CONCise-UHPC repository! HAI-CONCise-UHPC is an innovative and intelligent Constitutive Stress-Strain model for Confined Ultra-High-Performance Concrete (UHPC) that leverages Hybrid Artificial Intelligence (HAI) techniques for fast, accurate, and intelligent predictions.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Using the Application](#using-the-application)
  - [Input Parameters](#input-parameters)
  - [Predict and Plot](#predict-and-plot)
  - [Export to Excel](#export-to-excel)
- [Citing](#citing)
- [Contact](#contact)
- [License](#license)

## Features

- Predicts the stress-strain response of confined UHPC using Hybrid Artificial Intelligence.
- Provides an interactive plot of the predicted stress-strain curve.
- Allows exporting the predicted data to an Excel file for further analysis.

## Getting Started

### Installation

To get started with HAI-CONCise-UHPC, you need to have Python and several libraries installed on your system. You can install the required libraries using the following command:


### Running the Application

To run the HAI-CONCise-UHPC application, follow these steps:

1. Make sure you have Jupyter Notebook installed. If you don't have it, you can install it using pip:


2. Launch Jupyter Notebook by running the following command in your terminal or command prompt:


3. In the Jupyter Notebook interface, navigate to the directory where the `HAI-CONCise-UHPC.ipynb` script is located.

4. Open the `HAI-CONCise-UHPC.ipynb` notebook.

5. Execute the notebook cells to use the application.

## Using the Application

HAI-CONCise-UHPC offers a user-friendly interface for predicting the stress-strain response of confined UHPC specimens. Here's how to use the application effectively:

### Input Parameters

Before predicting the stress-strain response, you need to input the following parameters for your UHPC specimen:

- **Transverse Reinforcement Ratio (rohsy)**: The percentage of transverse reinforcement.
- **Yield Strength of Transverse Reinforcement (fy)**: The yield strength of the transverse reinforcement in megapascals (MPa).
- **Compressive Strength of Unconfined UHPC (fco)**: The compressive strength of unconfined UHPC in MPa.
- **Fiber Volumetric Ratio (Vf)**: The fiber volumetric ratio as a percentage.

### Predict and Plot

1. Input the desired values for the parameters mentioned above.

2. Execute the notebook cell that corresponds to the "Predict and Plot" operation to generate the stress-strain curve for the confined UHPC specimen.

3. The interactive plot will display the predicted stress-strain response, providing insights into the behavior of the material.

### Export to Excel

- After generating the stress-strain curve, you can export the predicted data to an Excel file for further analysis.

- Execute the notebook cell that corresponds to the "Export to Excel" operation, and a file dialog will appear to choose the destination and filename for the Excel file.

## Citing

If you use this software for your work, we kindly request that you cite the corresponding paper as a reference.

Authors: `[Author Name]`

`[Link to Paper (if available)]`

## Contact

For inquiries, assistance, or feedback, you can contact the authors via email:

`[Author Name]`: `[author@email.com](mailto:author@email.com)`

## License

This project is licensed under the `[Your License Name]` License - see the `LICENSE.md` file for details.
