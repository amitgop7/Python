import matplotlib.pyplot as plt

# Creates a grid of 1 row and 2 columns
fig, axes = plt.subplots(1, 2)

axes[0].plot([1, 2, 3], [4, 5, 6])  # First plot
axes[1].bar([1, 2, 3], [4, 5, 6])  # Second plot

plt.show()
