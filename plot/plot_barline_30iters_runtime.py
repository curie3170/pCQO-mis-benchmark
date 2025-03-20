import pandas as pd
import matplotlib.pyplot as plt
import os

os.environ['MPLCONFIGDIR'] = '/tmp'
file_path0 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-14 16:26:21.973541_ERdense_bestbatch.csv'
file_path1 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_3090_of_3840_total_stages_2025-03-16 05:33:29.099883_ERdense_Gurobiw30iter.csv'
file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-15 03:34:21.394469_ERdense_pCQO30iter_bestbatch.csv'

file_path0 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_512_of_512_total_stages_2025-03-14 16:26:54.368642_ER700800_bestbatch.csv'
file_path1 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_3840_of_3840_total_stages_2025-03-19 01:41:44.129660_ER700800_Gurobiw30iter.csv'
file_path2 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-15 03:31:21.855861_ER700800_pCQO30iter_bestbatch.csv'

df0 = pd.read_csv(file_path0)
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)


gurobiw_columns = df1.iloc[:, 2:32].copy()
gurobiw_runtime_columns = df1.iloc[:, 32:].copy()
gurobiw_columns.insert(0, 'GurobiwFull_450step', df0.iloc[:, 5].values)  #insert 450step's val
gurobiw_runtime_columns.insert(0, 'GurobiwFull_450step', df0.iloc[:, 9].values) 
gurobiw_columns_means = gurobiw_columns.mean()
gurobiw_runtime_means = gurobiw_runtime_columns.mean()

pcqo_columns = df2.iloc[:, 2:33].copy() #starting from 450
pcqo_runtime_columns =df2.iloc[:, 33:].copy()
pcqo_columns_means = pcqo_columns.mean()
pcqo_runtime_means = pcqo_runtime_columns.mean()

plt.figure(figsize=(12, 8)) 
x_values = range(len(gurobiw_columns_means))


plt.plot(x_values, gurobiw_columns_means, label="Gurobi_wFull", marker='o', linestyle='-')
plt.plot(x_values, pcqo_columns_means, label="pCQO-MIS", marker='^', linestyle='-')
plt.plot(x_values, gurobiw_runtime_means, label="Gurobi_wFull_runtime", marker='o', linestyle='-')
plt.plot(x_values, pcqo_runtime_means, label="pCQO-MIS_runtime", marker='^', linestyle='-')

# plt.plot(gurobiw_columns_means, label="Gurobi_wFull", marker='o', linestyle='-')
# #plt.plot(gurobiw_runtime_means, label="Gurobi_wFull Runtime", marker='s', linestyle='--')
# plt.plot(pcqo_columns_means, label="pCQO-MIS", marker='^', linestyle='-')
# # plt.plot(pcqo_runtime_means, label="pCQO-MIS Runtime", marker='d', linestyle='--')
plt.xticks([])
plt.xticks([i for i in range(0, 31)])

plt.title('Average MIS Values and Runtime of ER_700-800 dataset over 31 different initializations using 450step and 1-30th iterations')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('ER_700800_30iters_runtime.png')
plt.show()
