import pandas as pd
import matplotlib.pyplot as plt
import os

os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib'

file_path = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-12 04:09:34.747369_ER700800.csv'
df = pd.read_csv(file_path)

selected_columns = df.iloc[:, 2:6]
mean_values = selected_columns.mean()
print(mean_values)
custom_labels = ['pCQO-MIS', 'pCQO-MIS_30s', 'Gurobi', 'Gurobi_warmpart']

runtime_columns = df.iloc[:, 6:10]
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


plt.title('Average MIS Values and Runtime of ER_700_800 dataset')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.legend(loc='lower right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('ER_700-800_results_redo.png')

# 그래프 화면에 표시 (선택 사항)
plt.show()