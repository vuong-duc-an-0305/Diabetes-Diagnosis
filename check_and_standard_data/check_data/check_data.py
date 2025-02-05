import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Tạo DataFrame mẫu
data = pd.read_csv('data\\diabetes.csv')

# heatmap xet tính tương quan giữa các thuộc tính
# Tính ma trận tương quan
correlation_matrix = data.corr()

# Vẽ heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

