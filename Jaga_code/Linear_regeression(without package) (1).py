import numpy as np
import matplotlib.pyplot as plt

# Generate sample data (simple instead of big dataset)
np.random.seed(0)
X = np.random.rand(100)
y = 2 + 3*X + np.random.rand(100)   # y = 2 + 3x + noise

# Calculate mean
mean_x = np.mean(X)
mean_y = np.mean(y)

# Calculate slope (b1)
numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x) ** 2)
b1 = numerator / denominator

# Calculate intercept (b0)
b0 = mean_y - b1 * mean_x

# Prediction
y_pred = b0 + b1 * X

# Plot
plt.scatter(X, y)
plt.plot(X, y_pred, 'r')   # regression line
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression without package")
plt.show()

# Print equation
print("Equation: y =", round(b0,2), "+", round(b1,2), "x")