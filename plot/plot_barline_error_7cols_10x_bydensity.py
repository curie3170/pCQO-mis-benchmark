import pandas as pd
import matplotlib.pyplot as plt
import os

os.environ['MPLCONFIGDIR'] = '/tmp'

file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-18 17:21:31.923477_ERdense_pCQO30sec_bestbatch.csv' #pCQO_30s
file_path3 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-14 16:26:21.973541_ERdense_bestbatch.csv'
file_path4 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:45:17.376503_ERdense_10x_rand0.1_bestbatch.csv' # 0.1
file_path5 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:43:48.502700_ERdense_10x_rand0.15_bestbatch.csv' #0.15
file_path6 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1280_of_1280_total_stages_2025-03-18 04:47:55.010923_ERdense_10x_rand0.2_bestbatch.csv' # 0.2

df2 = pd.read_csv(file_path2)
df3 = pd.read_csv(file_path3)
df4 = pd.read_csv(file_path4)
df5 = pd.read_csv(file_path5)
df6 = pd.read_csv(file_path6)


selected_columns = df3.iloc[96:, [2, 4, 5]].copy() #2:pCQO 3:pCQO_30s 4:Gurobi 5:Gurobi_wFull
selected_columns.insert(1, 'pCQO-MIS_30s', df2.iloc[96:, 2].values) #new pCQO_30s
runtime_columns = df3.iloc[96:, [6, 8, 9]].copy()
runtime_columns.insert(1, 'pCQO-MIS_30s_runtime', df2.iloc[96:, 3].values)
selected_columns_mean = selected_columns.mean()
runtime_columns_mean = runtime_columns.mean()

# selected_columns = df3.iloc[96:, 2:6].copy()
# runtime_columns = df3.iloc[96:, 6:].copy()
# selected_columns_mean = selected_columns.mean()
# runtime_columns_mean = runtime_columns.mean()


prob10_columns = df4.iloc[96:, 2:12].copy()
prob10_runtime_columns =df4.iloc[96:, 12:].copy()
prob10_runtime_means = prob10_runtime_columns.values.mean()
prob10_err = prob10_columns.mean().max()
prob10_base = prob10_columns.mean().min()

prob15_columns = df5.iloc[96:, 2:12].copy()
prob15_runtime_columns =df5.iloc[96:, 12:].copy()
prob15_runtime_means = prob15_runtime_columns.values.mean()
prob15_err = prob15_columns.mean().max()
prob15_base = prob15_columns.mean().min()

prob20_columns = df6.iloc[96:, 2:12].copy()
prob20_runtime_columns =df6.iloc[96:, 12:].copy()
prob20_runtime_means = prob20_runtime_columns.values.mean()
prob20_err = prob20_columns.mean().max()
prob20_base = prob20_columns.mean().min()

bases = list(selected_columns_mean.values) + [
    prob10_base,
    prob15_base,
    prob20_base
]
errors = [0]*len(selected_columns_mean) + [
    prob10_err - bases[4],
    prob15_err - bases[5],
    prob20_err - bases[6]
]
runtime_means = list(runtime_columns_mean) + [
    prob10_runtime_means,
    prob15_runtime_means,
    prob20_runtime_means
]
lower_errors = [0] * len(errors)
upper_errors = errors
asymmetric_errors = [lower_errors, upper_errors]
custom_labels = ['pCQO-MIS', 'pCQO-MIS_30s', 'Gurobi', 'Gurobi_wFull', 'Gurobi_w0.1', 'Gurobi_w0.15', 'Gurobi_w0.2']

plt.figure(figsize=(10, 6))

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
    if i in [4, 5, 6]:
        plt.text(bar.get_x() + bar.get_width()/2, bases[i], f'{bases[i]:.2f}', 
                ha='center', va='top', fontsize=10, color='black')
    # Base + Error
    plt.text(bar.get_x() + bar.get_width()/2, bases[i] + errors[i], f'{(bases[i] + errors[i]):.2f}', 
            ha='center', va='bottom', fontsize=10, color='black')

line, = plt.plot(custom_labels, runtime_means, color='orange', marker='o', label='Average Runtime(s)')
for i, txt in enumerate(runtime_means):
    plt.text(custom_labels[i], txt, f'{txt:.2f}', color='orange', ha='center', va='top', fontsize=10)

plt.title('Average MIS Values and Runtime of ER_20 dataset (10 runs for random sampling)')

plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('ER_20_10x_rand.png')
plt.show()
