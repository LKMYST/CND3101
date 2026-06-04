import matplotlib.pyplot as plt
import numpy as np

# Creating independent variable
t = np.linspace(-10, 10, 100)

# Formula
sig = 1 / (1 + np.exp(-t))

# Creating figure and axes
figure, axes = plt.subplots()

# Reference lines (original color)
# ax.axhline(y=0, color="black", linestyle="--")
# ax.axhline(y=0.5, color="black", linestyle=":")
# ax.axhline(y=1.0, color="black", linestyle="--")

# Reference lines (modified color)
axes.axhline(y=0, color="red", linestyle="--")      # lower limit
axes.axhline(y=0.5, color="blue", linestyle=":")    # center
axes.axhline(y=1.0, color="red", linestyle="--")    # upper limit

# Y-axis
axes.axvline(color="grey")

# Tangent
axes.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))

# Curve
axes.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")

# Set coordinate range & display plot
axes.set(xlim=(-10, 10), xlabel="t")
axes.legend(fontsize=14)
plt.show()
