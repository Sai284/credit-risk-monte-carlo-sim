# Monte Carlo Credit Risk Simulation

This project provides a simple Python script to simulate credit risk in a portfolio of loans using a Monte Carlo approach. The simulation estimates the possible losses a lender might face due to defaults in their loan portfolio, helping to visualize the distribution and likelihood of different loss scenarios.

## How It Works

- **Inputs**: You specify a set of loans, each with key risk parameters:
  - **EAD (Exposure at Default)**: The loan amount at risk.
  - **PD (Probability of Default)**: The likelihood that the loan will default within the simulation horizon.
  - **LGD (Loss Given Default)**: The percentage of the loan amount lost if a default occurs.
  - If you do not know PD or LGD, you can input the credit quality (good, average, poor) and the script will assign reasonable default values for you.

- **Simulation**: For each run, the script randomly determines if each loan defaults and calculates the resulting loss. This is repeated thousands of times to build a distribution of possible portfolio losses.

- **Output**: The script prints summary statistics such as expected loss and value-at-risk (VaR) at different confidence levels, and displays a histogram showing the distribution of simulated losses.

## How to Run

1. **Clone or Download the Repository**

   ```
   git clone <repo-url>
   cd <repo-directory>
   ```

2. **Install Dependencies**

   Make sure you have Python 3 installed. Install the required Python packages:

   ```
   pip install numpy matplotlib
   ```

3. **Run the Simulation**

   ```
   python interactive_monte_carlo_credit_risk.py
   ```

   Follow the prompts to enter loan details and simulation options. If you are unsure about PD or LGD, simply enter the credit quality; the script will fill in reasonable defaults.

4. **View the Results**

   - The script prints expected loss and value-at-risk statistics.
   - A histogram pops up showing the simulated distribution of portfolio losses.

## Example Output

- **Most of the time**, the simulated portfolio loss will be small or zero, but sometimes large losses may occur due to rare default events. This reflects real-world credit risk: defaults are rare but can be costly.

- The histogram helps you visualize how likely different loss amounts are, highlighting both the common small losses and the rare, large loss events.
