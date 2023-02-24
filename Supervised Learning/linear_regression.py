import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.datasets import make_regression

X, y = make_regression(
    n_samples = 150, n_features = 1, noise = 1
)

# Linear Regression
def linear_regression(x_values, y_values, alpha):
    weight_0 = 0
    weight_1 = 0
    for i in range(len(x_values)):
        current_y = weight_1 * x_values[i][0] + weight_0
        weight_0 = weight_0 + alpha * (y_values[i] - current_y)
        weight_1 = weight_1 + alpha * x_values[i][0] * (y_values[i] - current_y)
    return weight_0, weight_1

weight_0, weight_1 = linear_regression(X, y, 0.1)

print("Weight 0" + str(weight_0))
print("Weight 1" + str(weight_1))

line_x = np.linspace(-3, 3, 100)
line_y = weight_1 * line_x + weight_0

plt.scatter(X, y)
plt.plot(line_x, line_y, "-r")
plt.show()