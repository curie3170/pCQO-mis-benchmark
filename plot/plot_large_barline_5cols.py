import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ['MPLCONFIGDIR'] = '/tmp'
file_path = '/export2/curiekim/pCQO-mis-benchmark/zero_to_stage_25_of_25_total_stages_2025-03-11 14:34:49.971997.csv' 
file_path = '/export2/curiekim/pCQO-mis-benchmark/zero_to_stage_25_of_25_total_stages_2025-03-11 14:58:06.677866.csv'
file_path = '/export2/curiekim/pCQO-mis-benchmark/zero_to_stage_25_of_25_total_stages_2025-03-11 15:01:20.776035.csv'
file_path = '/export2/curiekim/pCQO-mis-benchmark/zero_to_stage_25_of_25_total_stages_2025-03-11 15:06:48.246192.csv'
#file_path = '/export2/curiekim/pCQO-mis-benchmark/zero_to_stage_25_of_25_total_stages_2025-03-11 15:08:53.061552.csv'
df = pd.read_csv(file_path)

selected_columns = df.iloc[:, 2:7]
mean_values = selected_columns.mean()
custom_labels = ['pCQO-MIS', 'Gurobi', 'Gurobi_warmpart', 'CPSAT', 'CPSAT_warmpart ']

runtime_columns = df.iloc[:, 7:12]
runtime_means = runtime_columns.mean()

plt.figure(figsize=(10, 6))

bars = plt.bar(custom_labels, mean_values, color='skyblue', label='Average MIS Value')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', 
             ha='center', va='bottom', fontsize=10)

line, = plt.plot(custom_labels, runtime_means, color='orange', marker='o', label='Average Runtime(s)')
for i, txt in enumerate(runtime_means):
    plt.text(custom_labels[i], txt, f'{txt:.2f}', color='black', ha='center', va='bottom', fontsize=10)


plt.title('Average MIS Values and Runtime of gnm_1500_562125 dataset')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('large_graph_results_1500_early.png')

plt.show()