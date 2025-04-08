import numpy as np

def linear_regression(x, y):
   
    x = np.array(x)
    y = np.array(y)
   
   
    N = len(x)
   
   
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)
   
    beta_1 = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
    beta_0 = (sum_y - beta_1 * sum_x) / N
   
    return beta_0, beta_1

def predict(x, beta_0, beta_1):
    return beta_0 + beta_1 * np.array(x)

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

beta_0, beta_1 = linear_regression(x, y)

print(f"Intercept (beta_0): {beta_0}")
print(f"Slope (beta_1): {beta_1}")


predictions = predict(x, beta_0, beta_1)
print(f"Predictions: {predictions}")
                       
import matplotlib.pyplot as plt

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, predictions, color='red', label='Fitted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
