import matplotlib.pyplot as plt
import numpy as np

# 1. Define the function
def quadratic_function(x):
    return x**2 + 2*x - 1

# 2. Generate x-values
x_data = np.linspace(-4, 2, 100)

# 3. Calculate corresponding y-values
y_data = quadratic_function(x_data)

# 4. Create the plot
plt.plot(x_data, y_data, label="y = x^2 + 2x - 1")

# 5. Add labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of a Quadratic Function")
plt.legend() # Display the label

# 6. Display the plot
plt.grid(True) # Add a grid for better readability
plt.show()