# Re-netto - Markov chain supermarket simulation

This repository includes the code required to generate simulations
of customers in a supermarket.

## Structure of the repository

### 1. Installation

The recommendation is to simply clone the repository. The environment uses Python 3.9 and basic libraries that are part of Anaconda distribution and/or can be easily pip installed. No known incompatibilities are to be expected.

### 2. Code

- [class_customer](class_customer.py), [supermarket_start](supermarket_start.py), and [simulate_one_day](simulate_one_day.py) are the core files to run the simulations.
- [Main_for_functions](Main_for_functions.ipynb) is the notebook used to calculate the Markov chain sequence of possible events based on the daily [data](data/) provided by the supermarket. All the [functions](functions.py) used by this notebook are organized in this separated file.
- [class_plot_market](class_plot_market.py) and the [visualization](visualization/) folder contains the required files and code for the simulation visualization and can be called from the [simulate_one_day](simulate_one_day.py) script after minor modifications.

### 3. Data
The [data](data/) is split into multiple csv files, one for each working day of the week. This is fictional data for demonstration purposes.

### 4. Results
This repository demonstrates the use of Markov chains to generate customer behavior simulations. This was developed for educational purposes.

## Acknowledgments
The team: [Gerrit](https://github.com/GerritKu), [Helge](https://github.com/helge1991) and [Renato](https://github.com/Kestener)
