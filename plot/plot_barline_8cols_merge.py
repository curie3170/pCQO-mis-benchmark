import pandas as pd
import matplotlib.pyplot as plt
import os

os.environ['MPLCONFIGDIR'] = '/tmp'

# file_path1 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-14 16:26:54.368642_ER700800_bestbatch.csv'
# file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-14 17:10:04.949939_ER700800_rand0.1_bestbatch.csv'
# file_path3 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-14 14:22:09.914384_ER700800_rand0.3_bestbatch.csv'
# file_path4 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-14 15:47:08.712226_ER700800_rand0.5_bestbatch.csv'
# file_path5 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-14 17:19:25.686515_ER700800_rand0.7_bestbatch.csv'
# file_path6 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-18 17:18:29.908438_ER700800_pCQO30sec_bestbatch.csv'

file_path1 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-14 16:26:21.973541_ERdense_bestbatch.csv'
file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-14 17:10:00.893851_ERdense_rand0.1_bestbatch.csv'
file_path3 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-14 14:26:05.814101_ERdense_rand0.3_bestbatch.csv'
file_path4 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-14 15:52:28.873645_ERdense_rand0.5_bestbatch.csv'
file_path5 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-14 17:19:44.549291_ERdense_rand0.7_bestbatch.csv'
file_path6 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-18 17:21:31.923477_ERdense_pCQO30sec_bestbatch.csv'


df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
df3 = pd.read_csv(file_path3)
df4 = pd.read_csv(file_path4)
df5 = pd.read_csv(file_path5)
df6 = pd.read_csv(file_path6)

selected_columns = df1.iloc[:, 2:6].copy()
runtime_columns = df1.iloc[:, 6:10].copy()

selected_columns = df1.iloc[:, [2, 4, 5]].copy()
selected_columns.insert(1, 'pCQO-MIS_30s', df6.iloc[:, 2].values) #new pCQO_30s
runtime_columns = df1.iloc[:, [6, 8, 9]].copy()
runtime_columns.insert(1, 'pCQO-MIS_30s_runtime', df6.iloc[:, 3].values)

selected_columns.insert(4, 'Gurobi_warm_0.1', df2.iloc[:, 2])
runtime_columns.insert(4, 'Gurobi_warm_0.1_runtime', df2.iloc[:, 3])

selected_columns.insert(5, 'Gurobi_warm_0.3', df3.iloc[:, 2])
runtime_columns.insert(5, 'Gurobi_warm_0.3_runtime', df3.iloc[:, 3])

selected_columns.insert(6, 'Gurobi_warm_0.5', df4.iloc[:, 2])
runtime_columns.insert(6, 'Gurobi_warm_0.5_runtime', df4.iloc[:, 3])

selected_columns.insert(7, 'Gurobi_warm_0.7', df5.iloc[:, 2])
runtime_columns.insert(7, 'Gurobi_warm_0.7_runtime', df5.iloc[:, 3])

mean_values = selected_columns.mean()
runtime_means = runtime_columns.mean()

custom_labels = ['pCQO-MIS', 'pCQO-MIS_30s', 'Gurobi', 'Gurobi_wFull', 'Gurobi_w0.1', 'Gurobi_w0.3', 'Gurobi_w0.5', 'Gurobi_w0.7']

plt.figure(figsize=(10, 6))

bars = plt.bar(custom_labels, mean_values, color='skyblue', label='Average MIS Value')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', 
             ha='center', va='bottom', fontsize=10)

line, = plt.plot(custom_labels, runtime_means, color='orange', marker='o', label='Average Runtime(s)')
for i, txt in enumerate(runtime_means):
    plt.text(custom_labels[i], txt, f'{txt:.2f}', color='black', ha='center', va='bottom', fontsize=10)

#plt.title('Average MIS Values and Runtime of ER_700-800 dataset')
plt.title('Average MIS Values and Runtime of ER_dense dataset')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

#plt.savefig('ER_700-800_rand.png')
plt.savefig('ER_dense_rand.png')
plt.show()
