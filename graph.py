import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

processor_counts = [1, 2, 4, 8, 16, 32, 64]
all_data = pd.DataFrame([])

# Read the data from the file
data_list = []
for count in processor_counts:
    file_name = str(count) + '-processes.csv'
    data = pd.read_csv(file_name, names=['pi', 'cores', 'dart count', 'run time', 'node', 'convergence'])
    data_list.append(data)

all_data = pd.concat(data_list, ignore_index=True)

# True value of pi
true_pi = np.pi

# Calculate errors
all_data['error'] = np.abs(all_data['pi'] - true_pi) / true_pi
for i in range (0, all_data.shape[0], 3):
    all_data['convergence'][i: i+3] = (all_data['error'][i+2] - all_data['error'][i+1]) / (all_data['error'][i+1] - all_data['error'][i])


# print (all_data.groupby('convergence').mean())
print(all_data)
# Plot errors vs. number of darts with log-log scaling
for count in processor_counts:
    subset_data = all_data[all_data['cores'] == count]
    plt.loglog(subset_data['dart count'], subset_data['error'], label=f'{count} processors')

plt.xlabel('Number of darts')
plt.ylabel('Error')
plt.title('Error in Computed Values of Pi vs. Number of Darts')
plt.legend()
plt.grid(True)
plt.show()
