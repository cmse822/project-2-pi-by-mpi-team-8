import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# processor_counts = [1, 2, 4, 8, 16, 32, 64]
processor_counts = [1, 2, 3, 4]
node_counts = ['', '_2', '_4', '_8', '_16', '_32']
all_data = pd.DataFrame([])

# Read the data from the file
data_list = []
# for count in processor_counts:
#     file_name = str(count) + '-processes.csv'
#     data = pd.read_csv(file_name, names=['pi', 'cores', 'dart count', 'run time', 'node', 'convergence'])
#     data_list.append(data)

# all_data = pd.concat(data_list, ignore_index=True)

data_list = pd.read_csv('processes-4_3.csv', names=['pi', 'cores', 'dart count', 'run time', 'node'], index_col=False)
subset_data = pd.DataFrame(columns=['cores', 'run time'])
subset_data[['cores', 'run time']] = data_list[['cores', 'run time']]
subset_data = subset_data.groupby(['cores'], as_index=False).mean()

plt.figure()
plt.plot(subset_data['cores'], subset_data['run time'], marker='o', label=f'{processor_counts} ranks')
plt.xlabel('Rank')
plt.ylabel('Run Time')
plt.title(f'Runtime vs. Ranks Count for 1000 darts')
plt.legend()
plt.grid(True)
plt.show()

# True value of pi
# true_pi = np.pi

# # Calculate errors
# all_data['error'] = np.abs(all_data['pi'] - true_pi) / true_pi
# for i in range (0, all_data.shape[0], 3):
#     all_data['convergence'][i: i+3] = (all_data['error'][i+2] - all_data['error'][i+1]) / (all_data['error'][i+1] - all_data['error'][i])


# print (all_data.groupby('convergence').mean())
# print(all_data)
# # Plot errors vs. number of darts with log-log scaling
# for count in processor_counts:
#     subset_data = all_data[all_data['cores'] == count]
#     plt.loglog(subset_data['dart count'], subset_data['error'], label=f'{count} processors')

# plt.xlabel('Number of darts')
# plt.ylabel('Error')
# plt.title('Error in Computed Values of Pi vs. Number of Darts')
# plt.legend()
# plt.grid(True)
# plt.show()


# # Plot runtime vs. processor count for each dart count
# dart_counts = all_data['dart count'].unique()
# flag = 0
# for dart_count in dart_counts:
#     dart_data = all_data[all_data['dart count'] == dart_count]
    
#     plt.figure()
#     for i, count in enumerate(processor_counts):
#         subset_data = dart_data[dart_data['cores'] == count]
#         plt.plot(subset_data['cores'], subset_data['run time'], marker='o', label=f'{count} processors')
    
#     # Calculate ideal scaling line
#     print(dart_data)
#     ideal_scaling = dart_data['run time'][flag] / np.array(processor_counts)
#     flag += 1
#     plt.plot(processor_counts, ideal_scaling, linestyle='--', color='black', label='Ideal Scaling')
    
#     plt.xlabel('Processor Count')
#     plt.ylabel('Run Time')
#     plt.title(f'Runtime vs. Processor Count for {dart_count} darts')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

#     # Calculate parallel scaling efficiency
#     actual_time = np.array(dart_data['run time'])
#     efficiency = ideal_scaling / actual_time
#     print(f"Parallel Scaling Efficiency for {dart_count} darts:")
#     for i, count in enumerate(processor_counts):
#         print(f"{count} processors: {efficiency[i]}")

# data_list = []
# for count in node_counts:
#     file_name = '64-processes' + str(count) + '.csv'
#     data = pd.read_csv(file_name, names=['pi', 'nodes', 'dart count', 'run time', 'node', 'convergence'])
#     data_list.append(data)

# all_data = pd.concat(data_list, ignore_index=True)

# # Group data by dart count
# grouped_data = all_data.groupby('dart count')

# # Plot 1: Runtime vs Nodes for dart count 100
# plt.figure(figsize=(10, 6))
# for name, group in grouped_data:
#     if name == 1000:  # Change 100 to the dart count you want to plot
#         plt.plot(group['nodes'], group['run time'], marker='o', label=f'Dart Count: {name}')

# plt.xlabel('Nodes')
# plt.ylabel('Runtime')
# plt.title('Runtime vs Nodes for Dart Count 10e3 (64 cores)')
# plt.xticks(processor_counts)  # Set processor counts as xticks
# plt.gca().set_xticklabels(processor_counts, rotation=45, ha='right')  # Rotate xticks for better visibility
# plt.legend()
# plt.grid(True, axis='y')  # Only grid lines on y-axis
# plt.grid(True, axis='x', which='major', linestyle='--')  # Grid lines on x-axis aligned with processor counts
# plt.show()

# # Plot 2: Runtime vs Nodes for dart count 500
# plt.figure(figsize=(10, 6))
# for name, group in grouped_data:
#     if name == 1000000:  # Change 500 to the dart count you want to plot
#         plt.plot(group['nodes'], group['run time'], marker='o', label=f'Dart Count: {name}')

# plt.xlabel('Nodes')
# plt.ylabel('Runtime')
# plt.title('Runtime vs Nodes for Dart Count 10e6 (64 cores)')
# plt.xticks(processor_counts)  # Set processor counts as xticks
# plt.gca().set_xticklabels(processor_counts, rotation=45, ha='right')  # Rotate xticks for better visibility
# plt.legend()
# plt.grid(True, axis='y')  # Only grid lines on y-axis
# plt.grid(True, axis='x', which='major', linestyle='--')  # Grid lines on x-axis aligned with processor counts
# plt.show()

# # Plot 3: Runtime vs Nodes for dart count 1000
# plt.figure(figsize=(10, 6))
# for name, group in grouped_data:
#     if name == 1000000000:  # Change 1000 to the dart count you want to plot
#         plt.plot(group['nodes'], group['run time'], marker='o', label=f'Dart Count: {name}')

# plt.xlabel('Nodes')
# plt.ylabel('Runtime')
# plt.title('Runtime vs Nodes for Dart Count 10e9 (64 cores)')
# plt.xticks(processor_counts)  # Set processor counts as xticks
# plt.gca().set_xticklabels(processor_counts, rotation=45, ha='right')  # Rotate xticks for better visibility
# plt.legend()
# plt.grid(True, axis='y')  # Only grid lines on y-axis
# plt.grid(True, axis='x', which='major', linestyle='--')  # Grid lines on x-axis aligned with processor counts
# plt.show()
