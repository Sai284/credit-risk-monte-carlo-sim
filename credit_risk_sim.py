import numpy as np
import matplotlib.pyplot as plt

credit_quality_to_pd = {
  "good": 0.01,
  "average": 0.05,
  "poor": 0.10,
}

credit_quality_to_lgd = {
  "good": 0.30,
  "average": 0.45,
  "poor": 0.60,
}

def get_float(prompt, default):
    while True:
        try:
            value = input(f"{prompt} (default {default}): ")
            return float(value) if value.strip() != "" else default
        except ValueError:
            print("Please enter a valid number.")
  
def get_credit_quality():
  quality = input("Enter credit quality (good, average, poor) [average]: ").strip().lower()
  if quality in credit_quality_to_pd:
    return quality
  if quality == "":
    return "average"
  print("Invalid input. Please enter 'good', 'average', or 'poor'.")
  return get_credit_quality()

def get_portfolio():
  portfolio = []
  n = int(get_float("Enter number of loans in portfolio", 5))
  for i in range(n):
    print(f"\nLoan {i+1}:")
    ead = get_float("Loan amount (Exposure at Default): ", 100000)
    quality = get_credit_quality()
    pd = get_float(f"Probability of Default (PD, 0-1) [{credit_quality_to_pd[quality]}]: ", credit_quality_to_pd[quality])
    lgd = get_float(f"Loss Given Default (LGD, 0-1) [{credit_quality_to_lgd[quality]}]: ", credit_quality_to_lgd[quality])
    loan = {"PD": pd, "EAD": ead, "LGD": lgd}
    portfolio.append(loan)
  return portfolio

def simulate_portfolio(portfolio, num_simulations=10000):
  losses = []
  for _ in range(num_simulations):
    total_loss = 0
    for loan in portfolio:
      if np.random.rand() < loan["PD"]:
        total_loss += loan["EAD"] * loan["LGD"]
    losses.append(total_loss)
  return np.array(losses)

def main():
  print("Monte Carlo Credit Risk Simulation\n")
  portfolio = get_portfolio()
  num_simulations = int(get_float("\nNumber of simulations [10000]: ", 10000))
  losses = simulate_portfolio(portfolio, num_simulations)
  expected_loss = np.mean(losses)
  var_95 = np.percentile(losses, 95)
  var_99 = np.percentile(losses, 99)
  print(f"\nExpected Loss: {expected_loss:.2f}")
  print(f"Value at Risk (95th percentile): {var_95:.2f}")
  print(f"Value at Risk (99th percentile): {var_99:.2f}")
  plt.hist(losses, bins=30, edgecolor='black')
  plt.xlabel("Total Portfolio Loss")
  plt.ylabel("Frequency")
  plt.title("Monte Carlo Simulated Credit Loss Distribution")
  plt.show()

if __name__ == "__main__":
    main()
  