import matplotlib.pyplot as plt

# Data for visualization
categories = [
    "Ease of Learning",
    "Panel Data",
    "IV / 2SLS",
    "DiD",
    "Time Series",
    "Causal Inference",
    "Machine Learning Integration",
    "Visualization",
    "Big Data Handling"
]

stata_scores = [9, 10, 9, 9, 10, 8, 5, 6, 6]
r_scores = [7, 9, 9, 9, 9, 9, 7, 10, 8]
python_scores = [6, 7, 7, 7, 9, 9, 10, 9, 10]

# Create figure
plt.figure(figsize=(10, 6))
bar_width = 0.25
positions = range(len(categories))

# Plot bars
plt.barh([p - bar_width for p in positions], stata_scores, bar_width, label="Stata", color="#1F77B4")
plt.barh(positions, r_scores, bar_width, label="R", color="#2CA02C")
plt.barh([p + bar_width for p in positions], python_scores, bar_width, label="Python", color="#FF7F0E")

# Formatting
plt.yticks(positions, categories)
plt.xlabel("Performance (1–10 scale)")
plt.title("Econometrics Software Comparison: Stata vs R vs Python (2025)")
plt.legend()
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()

plt.show()
