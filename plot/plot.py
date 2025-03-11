import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ['MPLCONFIGDIR'] = '/tmp'
file_path = '/export2/curiekim/pCQO-mis-benchmark/zero_to_stage_224_of_224_total_stages_2025-03-10 21:46:27.718162.csv'  # CSV 파일 경로로 변경하세요.
df = pd.read_csv(file_path)

# 각 열의 평균 계산
selected_columns = df.iloc[:, 2:9]
mean_values = selected_columns.mean()

custom_labels = ['pCQO-MIS', 'Gurobi', 'Gurobi_warmpart', 'Gurobi_warmfull', 'CPSAT', 'CPSAT_warmpart', 'CPSAT_warmfull']

# 바 플롯 그리기
plt.figure(figsize=(10, 6))
bars = plt.bar(custom_labels, mean_values, color='skyblue')
plt.title('Average MIS Values of ER_700_800_0.05 dataset')
plt.xlabel('Methods')
plt.ylabel('Average MIS Value')
plt.grid(axis='y', linestyle='--', alpha=0.7)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', 
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()

plt.savefig('average_plot.png')