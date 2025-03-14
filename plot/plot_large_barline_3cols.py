import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ['MPLCONFIGDIR'] = '/tmp'

file_path ='/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_15_of_15_total_stages_2025-03-11 16:11:01.049053_90sec.csv'
file_path= '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_384_of_384_total_stages_2025-03-13 19:16:45.033043_ER700800bestbatch.csv'
df = pd.read_csv(file_path)

selected_columns = df.iloc[:, 2:5]
mean_values = selected_columns.mean()
custom_labels = ['pCQO-MIS', 'Gurobi', 'Gurobi_warmpart']

runtime_columns = df.iloc[:, 5:8]
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


#plt.title('Average MIS Values and Runtime of gnm_500_62375 dataset')
plt.title('Average MIS Values and Runtime of ER_700_800 dataset')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

#plt.savefig('large_graph_results_500_90sec.png')
plt.savefig('ER_700-800_bestbatch_results.png')

plt.show()