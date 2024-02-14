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


print (all_data.groupby('convergence').mean())
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


# Plot runtime vs. processor count for each dart count
dart_counts = all_data['dart count'].unique()
flag = 0
for dart_count in dart_counts:
    dart_data = all_data[all_data['dart count'] == dart_count]
    
    plt.figure()
    for i, count in enumerate(processor_counts):
        subset_data = dart_data[dart_data['cores'] == count]
        plt.plot(subset_data['cores'], subset_data['run time'], marker='o', label=f'{count} processors')
    
    # Calculate ideal scaling line
    print(dart_data)
    ideal_scaling = dart_data['run time'][flag] / np.array(processor_counts)
    flag += 1
    plt.plot(processor_counts, ideal_scaling, linestyle='--', color='black', label='Ideal Scaling')
    
    plt.xlabel('Processor Count')
    plt.ylabel('Run Time')
    plt.title(f'Runtime vs. Processor Count for {dart_count} darts')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Calculate parallel scaling efficiency
    actual_time = np.array(dart_data['run time'])
    efficiency = ideal_scaling / actual_time
    print(f"Parallel Scaling Efficiency for {dart_count} darts:")
    for i, count in enumerate(processor_counts):
        print(f"{count} processors: {efficiency[i]}")