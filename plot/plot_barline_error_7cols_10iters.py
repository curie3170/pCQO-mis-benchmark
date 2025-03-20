import pandas as pd
import matplotlib.pyplot as plt
import os

os.environ['MPLCONFIGDIR'] = '/tmp'

file_path1 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-15 03:34:21.394469_ERdense_pCQO30iter_bestbatch.csv' #pcqo_1stfile_path1 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-15 03:31:21.855861_ER700800_pCQO30iter_bestbatch.csv'
file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_3090_of_3840_total_stages_2025-03-16 05:33:29.099883_ERdense_Gurobiw30iter.csv' #gurobi_wfull
file_path3 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-14 16:26:21.973541_ERdense_bestbatch.csv' #gurobi_wfull_450
file_path4 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1408_of_1408_total_stages_2025-03-17 23:16:24.473628_ERdense_10iter_rand0.1_bestbatch.csv' # 0.1
file_path5 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1408_of_1408_total_stages_2025-03-17 23:24:50.857506_ERdense_10iter_rand0.15_bestbatch.csv' #0.15
file_path6 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_1408_of_1408_total_stages_2025-03-18 02:14:11.501925_ERdense_10iter_rand0.2_bestbatch.csv' # 0.2



df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
df3 = pd.read_csv(file_path3)
df4 = pd.read_csv(file_path4)
df5 = pd.read_csv(file_path5)
df6 = pd.read_csv(file_path6)


pcqo_columns = df1.iloc[:, 2:13].copy()
pcqo_runtime_columns =df1.iloc[:, 32:42].copy()
# pcqo_columns = df1.iloc[:, 2:32].copy() #30iters
# pcqo_runtime_columns =df1.iloc[:, 32:].copy()
pcqo_runtime_means = pcqo_runtime_columns.values.mean()
pcqo_err = pcqo_columns.mean().max()
pcqo_base = pcqo_columns.mean().min()


#df2: 2250~ 10개
#bestbatch: 450 1개
prob100_columns = df2.iloc[:, 2:13].copy()
prob100_runtime_columns =df2.iloc[:, 32:42].copy()
# prob100_columns = df2.iloc[:, 2:32].copy() #30iters
# prob100_runtime_columns =df2.iloc[:, 32:].copy()
prob100_columns.insert(0, 'Gurobi_warm_450', df3.iloc[:, 5])
prob100_runtime_columns.insert(0, 'Gurobi_warm_450_runtime', df3.iloc[:, 9])
prob100_runtime_means = prob100_runtime_columns.values.mean()
prob100_err = prob100_columns.mean().max()
prob100_base = prob100_columns.mean().min()

pcqo30s_column =  df3.iloc[:, 3]
pcqo30s_runtime_column =  df3.iloc[:, 7]
pcqo30s_runtime_mean = pcqo30s_runtime_column.values.mean()
pcqo30s_err = 0.0
pcqo30s_base = pcqo30s_column.mean()

gurobi_column =  df3.iloc[:, 4]
gurobi_runtime_column =  df3.iloc[:, 8]
gurobi_runtime_mean = gurobi_runtime_column.values.mean()
gurobi_err = 0.0
gurobi_base = gurobi_column.mean()

prob10_columns = df4.iloc[:, 2:13].copy()
prob10_runtime_columns =df4.iloc[:, 13:24].copy()
prob10_runtime_means = prob10_runtime_columns.values.mean()
prob10_err = prob10_columns.mean().max()
prob10_base = prob10_columns.mean().min()

prob15_columns = df5.iloc[:, 2:13].copy()
prob15_runtime_columns =df5.iloc[:, 13:24].copy()
prob15_runtime_means = prob15_runtime_columns.values.mean()
prob15_err = prob15_columns.mean().max()
prob15_base = prob15_columns.mean().min()

prob20_columns = df6.iloc[:, 2:13].copy()
prob20_runtime_columns =df6.iloc[:, 13:24].copy()
prob20_runtime_means = prob20_runtime_columns.values.mean()
prob20_err = prob20_columns.mean().max()
prob20_base = prob20_columns.mean().min()

bases = [
    pcqo_base,
    pcqo30s_base,
    gurobi_base,
    prob100_base,
    prob10_base,
    prob15_base,
    prob20_base
]
errors = [
    pcqo_err - bases[0],
    pcqo30s_err,
    gurobi_err,
    prob100_err - bases[3],
    prob10_err - bases[4],
    prob15_err - bases[5],
    prob20_err - bases[6]
]
runtime_means = [
    pcqo_runtime_means,
    pcqo30s_runtime_mean,
    gurobi_runtime_mean,
    prob100_runtime_means,
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
    if i !=1 and i !=2:
        plt.text(bar.get_x() + bar.get_width()/2, bases[i], f'{bases[i]:.2f}', 
                ha='center', va='top', fontsize=10, color='black')
    # Base + Error
    plt.text(bar.get_x() + bar.get_width()/2, bases[i] + errors[i], f'{(bases[i] + errors[i]):.2f}', 
            ha='center', va='bottom', fontsize=10, color='black')

line, = plt.plot(custom_labels, runtime_means, color='orange', marker='o', label='Average Runtime(s)')
for i, txt in enumerate(runtime_means):
    plt.text(custom_labels[i], txt, f'{txt:.2f}', color='black', ha='center', va='top', fontsize=10)

plt.title('Average MIS Values and Runtime of ER_dense dataset over 10 iters')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('ER_dense_10iters.png')
plt.show()
