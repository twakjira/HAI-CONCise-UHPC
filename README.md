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

To get started with HAI-CONCise-UHPC, you need to have Python and required libraries installed on your system. You can install the required libraries using the following command:


### Running the Application

To successfully run the HAI-CONCise-UHPC application, please follow these steps:

1. **Install Python**
   - Ensure Python is installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/).

2. **Install Required Libraries**
   - Install the necessary Python libraries by opening your terminal or command prompt and running the following command:
     ```bash
     pip install pandas numpy matplotlib scikit-learn xgboost PySimpleGUI Pillow
     ```

3. **Download the Application Script**
   - Download the `HAI-CONCise-UHPC.py` script to your local machine.

4. **Download the Resources Folder**
   - Also, download and save the "resources" folder in the same directory as the `HAI-CONCise-UHPC.py` script. This folder should contain all necessary resources, such as model files or data, that are required by the application.

5. **Open Your Python Environment**
   - Launch your preferred Python environment. This could be an Integrated Development Environment (IDE) like PyCharm or Visual Studio Code, or a web-based platform like Google Colab.

6. **Load the Script**
   - In your Python environment, open the `HAI-CONCise-UHPC.py` script.

7. **Run the Application**
   - Execute the script to start the application. This is typically done by pressing a 'Run' button in IDEs or using a run command in the console.

Following these instructions will enable you to run the HAI-CONCise-UHPC application in any compatible Python environment. It's crucial to ensure that the "resources" folder is placed in the same directory as the main script for the application to function correctly.


## Using the Application

HAI-CONCise-UHPC offers a user-friendly interface for predicting the stress-strain response of confined UHPC specimens. Here's how to use the application effectively:

### Input Parameters

Before predicting the stress-strain response, you need to input the following parameters for your UHPC specimen:

- **Transverse Reinforcement Ratio (𝜌𝑠𝑡)**: The percentage of transverse reinforcement.
- **Yield Strength of Transverse Reinforcement (fy)**: The yield strength of the transverse reinforcement in megapascals (MPa).
- **Compressive Strength of Unconfined UHPC (fco)**: The compressive strength of unconfined UHPC in MPa.
- **Fiber Volumetric Ratio (vf)**: The fiber volumetric ratio as a percentage.

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

`[Link to Paper]`

## Contact

For inquiries, assistance, or feedback, feel free to reach out through one of the following methods:
- [Contact Form](https://www.tadessewakjira.com/Contact)
- [Email](mailto:contact@tadessewakjira.com)

