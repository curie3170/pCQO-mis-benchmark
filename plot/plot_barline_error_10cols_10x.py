import pandas as pd
import matplotlib.pyplot as plt
import os

os.environ['MPLCONFIGDIR'] = '/tmp'

file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-18 17:21:31.923477_ERdense_pCQO30sec_bestbatch.csv' #pCQO_30s
file_path3 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-14 16:26:21.973541_ERdense_bestbatch.csv'
file_path4 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:45:17.376503_ERdense_10x_rand0.1_bestbatch.csv' # 0.1
file_path5 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:43:48.502700_ERdense_10x_rand0.15_bestbatch.csv' #0.15
file_path6 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:47:55.010923_ERdense_10x_rand0.2_bestbatch.csv' # 0.2

#ER700800
file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-18 17:18:29.908438_ER700800_pCQO30sec_bestbatch.csv' #pCQO_30s
file_path3 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-14 16:26:54.368642_ER700800_bestbatch.csv' 
file_path4 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:48:50.795747_ER700800_10x_rand0.1_bestbatch.csv' # 0.1
file_path5 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:51:16.456813_ER700800_10x_rand0.15_bestbatch.csv' #0.15
file_path6 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:52:48.177507_ER700800_10x_rand0.2_bestbatch.csv' # 0.2
file_path7 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1080_of_1280_total_stages_2025-03-18 19:57:40.369207_ER700800_10x_rand0.25_bestbatch.csv'  # 0.25
file_path8 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1080_of_1280_total_stages_2025-03-18 19:57:58.523736_ER700800_10x_rand0.3_bestbatch.csv'  # 0.3
file_path9 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-19 07:46:09.583011_ER700800_10x_rand0.05_bestbatch.csv'


df2 = pd.read_csv(file_path2)
df3 = pd.read_csv(file_path3)
df4 = pd.read_csv(file_path4)
df5 = pd.read_csv(file_path5)
df6 = pd.read_csv(file_path6)
df7 = pd.read_csv(file_path7)
df8 = pd.read_csv(file_path8)
df9 = pd.read_csv(file_path9)

# selected_columns = df3.iloc[:, 2:6].copy() #2:pCQO 3:pCQO_30s 4:Gurobi 5:Gurobi_wFull
selected_columns = df3.iloc[:, [2, 4, 5]].copy()
selected_columns.insert(1, 'pCQO-MIS_30s', df2.iloc[:, 2].values) #new pCQO_30s
# runtime_columns = df3.iloc[:, 6:].copy()
runtime_columns = df3.iloc[:, [6, 8, 9]].copy()
runtime_columns.insert(1, 'pCQO-MIS_30s_runtime', df2.iloc[:, 3].values)
selected_columns_mean = selected_columns.mean()
runtime_columns_mean = runtime_columns.mean()


prob05_columns = df9.iloc[:, 2:12].copy()
prob05_runtime_columns =df9.iloc[:, 12:].copy()
prob05_runtime_means = prob05_runtime_columns.values.mean()
prob05_err = prob05_columns.mean().max()
prob05_base = prob05_columns.mean().min()

prob10_columns = df4.iloc[:, 2:12].copy()
prob10_runtime_columns =df4.iloc[:, 12:].copy()
prob10_runtime_means = prob10_runtime_columns.values.mean()
prob10_err = prob10_columns.mean().max()
prob10_base = prob10_columns.mean().min()

prob15_columns = df5.iloc[:, 2:12].copy()
prob15_runtime_columns =df5.iloc[:, 12:].copy()
prob15_runtime_means = prob15_runtime_columns.values.mean()
prob15_err = prob15_columns.mean().max()
prob15_base = prob15_columns.mean().min()

prob20_columns = df6.iloc[:, 2:12].copy()
prob20_runtime_columns =df6.iloc[:, 12:].copy()
prob20_runtime_means = prob20_runtime_columns.values.mean()
prob20_err = prob20_columns.mean().max()
prob20_base = prob20_columns.mean().min()

prob25_columns = df7.iloc[:, 2:12].copy()
prob25_runtime_columns =df7.iloc[:, 12:].copy()
prob25_runtime_means = prob25_runtime_columns.values.mean()
prob25_err = prob25_columns.mean().max()
prob25_base = prob25_columns.mean().min()

prob30_columns = df8.iloc[:, 2:12].copy()
prob30_runtime_columns =df8.iloc[:, 12:].copy()
prob30_runtime_means = prob30_runtime_columns.values.mean()
prob30_err = prob30_columns.mean().max()
prob30_base = prob30_columns.mean().min()

bases = list(selected_columns_mean.values) + [
    prob05_base,
    prob10_base,
    prob15_base,
    prob20_base,
    prob25_base,
    prob30_base,
]
errors = [0]*len(selected_columns_mean) + [
    prob05_err - bases[4],
    prob10_err - bases[5],
    prob15_err - bases[6],
    prob20_err - bases[7],
    prob25_err - bases[8],
    prob30_err - bases[9],
]
runtime_means = list(runtime_columns_mean) + [
    prob05_runtime_means,
    prob10_runtime_means,
    prob15_runtime_means,
    prob20_runtime_means,
    prob25_runtime_means,
    prob30_runtime_means,
]
lower_errors = [0] * len(errors)
upper_errors = errors
asymmetric_errors = [lower_errors, upper_errors]
custom_labels = ['pCQO-MIS', 'pCQO-MIS_30s', 'Gurobi', 'Gurobi_wFull', 'Gurobi_w0.05', 'Gurobi_w0.1', 'Gurobi_w0.15', 'Gurobi_w0.2', 'Gurobi_w0.25', 'Gurobi_w0.3']

plt.figure(figsize=(12, 6))

bars = plt.bar(
    custom_labels, 
    bases, 
    yerr=asymmetric_errors, 
    capsize=5, 
    color='skyblue', 
    error_kw={'ecolor': 'skyblue', 'elinewidth': 2},  
    label='Average MIS Value'
)
for i, bar in enumerate(bars):
    # Base
    if i > 3:
        plt.text(bar.get_x() + bar.get_width()/2, bases[i], f'{bases[i]:.2f}', 
                ha='center', va='top', fontsize=10, color='black')
    # Base + Error
    plt.text(bar.get_x() + bar.get_width()/2, bases[i] + errors[i], f'{(bases[i] + errors[i]):.2f}', 
            ha='center', va='bottom', fontsize=10, color='black')

line, = plt.plot(custom_labels, runtime_means, color='orange', marker='o', label='Average Runtime(s)')
for i, txt in enumerate(runtime_means):
    plt.text(custom_labels[i], txt, f'{txt:.2f}', color='black', ha='center', va='top', fontsize=10)

# plt.title('Average MIS Values and Runtime of ER_dense dataset (10 runs for random sampling)')

plt.title('Average MIS Values and Runtime of ER_700-800 dataset (10 runs for random sampling)')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

#plt.savefig('ER_dense_10x_rand.png')
plt.savefig('ER_700-800_10x_rand.png')
plt.show()
