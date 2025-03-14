import pandas as pd
import matplotlib.pyplot as plt
import os

os.environ['MPLCONFIGDIR'] = '/tmp'

file_path1 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_640_of_640_total_stages_2025-03-11 18:47:54.443404.csv'
file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-11 19:33:04.302491.csv'

df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

selected_columns = df1.iloc[:, 2:7].copy()
runtime_columns = df1.iloc[:, 7:12].copy()

selected_columns.insert(1, 'pCQO-MIS_30s', df2.iloc[:, 2])
runtime_columns.insert(1, 'pCQO-MIS_30s_runtime', df2.iloc[:, 3])

mean_values = selected_columns.mean()
runtime_means = runtime_columns.mean()

custom_labels = ['pCQO-MIS', 'pCQO-MIS_30s', 'Gurobi', 'Gurobi_warmpart', 'CPSAT', 'CPSAT_warmpart']

plt.figure(figsize=(10, 6))

bars = plt.bar(custom_labels, mean_values, color='skyblue', label='Average MIS Value')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', 
             ha='center', va='bottom', fontsize=10)

line, = plt.plot(custom_labels, runtime_means, color='orange', marker='o', label='Average Runtime(s)')
for i, txt in enumerate(runtime_means):
    plt.text(custom_labels[i], txt, f'{txt:.2f}', color='black', ha='center', va='bottom', fontsize=10)

plt.title('Average MIS Values and Runtime of ER_700_800 dataset')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('ER_700-800_results_merged.png')
plt.show()
