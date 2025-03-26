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
file_path3 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_128_of_128_total_stages_2025-03-18 17:18:29.908438_ER700800_pCQO30sec_bestbatch.csv'
file_path4 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_3968_of_3968_total_stages_2025-03-24 03:28:29.823566_ER700800_rand0.1_30iters_bestbatch.csv'
file_path5 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_3968_of_3968_total_stages_2025-03-24 03:34:34.298926_ER700800_rand0.15_30iters_bestbatch.csv'
file_path6 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_3968_of_3968_total_stages_2025-03-24 03:34:08.723217_ER700800_rand0.2_30iters_bestbatch.csv'
file_path7 = '/export2/curiekim/pCQO-mis-benchmark/meaningful_results/zero_to_stage_3968_of_3968_total_stages_2025-03-24 03:36:55.996375_ER700800_rand0.25_30iters_bestbatch.csv'



df0 = pd.read_csv(file_path0)
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
df3 = pd.read_csv(file_path3)
df4 = pd.read_csv(file_path4)
df5 = pd.read_csv(file_path5)
df6 = pd.read_csv(file_path6)
df7 = pd.read_csv(file_path7)

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

pcqo30s_columns = df3.iloc[:, 2].copy() 
pcqo30s_columns_means = pcqo30s_columns.mean()

gurobiw10_columns = df4.iloc[:, 2:33].copy() 
gurobiw10_runtime_columns =df4.iloc[:, 33:].copy()
gurobiw10_columns_means = gurobiw10_columns.mean()
gurobiw10_runtime_means = gurobiw10_runtime_columns.mean()

gurobiw15_columns = df5.iloc[:, 2:33].copy() 
gurobiw15_runtime_columns =df5.iloc[:, 33:].copy()
gurobiw15_columns_means = gurobiw15_columns.mean()
gurobiw15_runtime_means = gurobiw15_runtime_columns.mean()

gurobiw20_columns = df6.iloc[:, 2:33].copy() 
gurobiw20_runtime_columns =df6.iloc[:, 33:].copy()
gurobiw20_columns_means = gurobiw20_columns.mean()
gurobiw20_runtime_means = gurobiw20_runtime_columns.mean()

gurobiw25_columns = df7.iloc[:, 2:33].copy() 
gurobiw25_runtime_columns =df7.iloc[:, 33:].copy()
gurobiw25_columns_means = gurobiw25_columns.mean()
gurobiw25_runtime_means = gurobiw25_runtime_columns.mean()


plt.figure(figsize=(12, 8)) 
x_values = range(len(gurobiw_columns_means))


plt.plot(x_values, gurobiw_columns_means, label="Gurobi_wFull", marker='o', linestyle='-')
plt.plot(x_values, gurobiw10_columns_means, label="Gurobi_w0.1", marker='o', linestyle='-')
plt.plot(x_values, gurobiw15_columns_means, label="Gurobi_w0.15", marker='o', linestyle='-')
plt.plot(x_values, gurobiw20_columns_means, label="Gurobi_w0.2", marker='o', linestyle='-')
plt.plot(x_values, gurobiw25_columns_means, label="Gurobi_w0.25", marker='o', linestyle='-')
plt.plot(x_values, pcqo_columns_means, label="pCQO-MIS", marker='^', linestyle='-', color='orange')

plt.axhline(y=pcqo30s_columns_means, color='r', linestyle='--', label="pCQO-MIS_30s")
plt.axhline(y=pcqo_columns_means.iloc[-1], color='g', linestyle='--', label="pCQO-MIS_31st_iter")

plt.xticks([i for i in range(0, 31)])

plt.title('Average MIS Values and Runtime of ER_700-800 dataset over 31 different initializations using 450step and 1-31st iterations')
plt.xlabel('Iterations')
plt.ylabel('Average MIS Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('ER_700-800_30iters_rand.png')
plt.show()
