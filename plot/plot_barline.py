import pandas as pd
import matplotlib.pyplot as plt
import os

# Matplotlib 캐시를 임시 디렉토리로 설정
os.environ['MPLCONFIGDIR'] = '/tmp'

# CSV 파일 불러오기
file_path = '/export2/curiekim/pCQO-mis-benchmark/zero_to_stage_224_of_224_total_stages_2025-03-10 21:46:27.718162.csv'
df = pd.read_csv(file_path)

# 바 플롯용 데이터 (Gurobi_warmfull, CPSAT_warmfull 제거)
selected_columns = df.iloc[:, [2, 3, 4, 6, 7]]
mean_values = selected_columns.mean()
custom_labels = ['pCQO-MIS', 'Gurobi', 'Gurobi_warmpart', 'CPSAT', 'CPSAT_warmpart ']

# 라인 플롯용 데이터 (9, 10, 11, 13, 14번째 열)
runtime_columns = df.iloc[:, [9, 10, 11, 13, 14]]
runtime_means = runtime_columns.mean()

# 플롯 그리기
plt.figure(figsize=(10, 6))

# 바 플롯
bars = plt.bar(custom_labels, mean_values, color='skyblue', label='Average MIS Value')

# 바 위에 값 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', 
             ha='center', va='bottom', fontsize=10)
# 라인 플롯
line, = plt.plot(custom_labels, runtime_means, color='orange', marker='o', label='Average Runtime(s)')

# 각 점 위에 실행 시간 값 표시
for i, txt in enumerate(runtime_means):
    plt.text(custom_labels[i], txt, f'{txt:.2f}', color='black', ha='center', va='bottom', fontsize=10)

# 그래프 꾸미기
plt.title('Average MIS Values and Runtime of ER_700_800_0.05 dataset')
plt.xlabel('Methods')
plt.ylabel('Average Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()

# 그래프를 이미지로 저장
plt.savefig('average_plot.png')

# 그래프 화면에 표시 (선택 사항)
plt.show()