import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from url_show_chart import linkUrl

data = pd.read_csv(linkUrl())

plt.figure(figsize=(15, 10))

# Histogram
plt.subplot(2, 2, 1)
plt.hist(data['DiabetesPedigreeFunction'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Giá trị DiabetesPedigreeFunction')
plt.ylabel('Tần suất')

# Density Plot
plt.subplot(2, 2, 2)
sns.kdeplot(data['DiabetesPedigreeFunction'], color='blue', fill=True)
plt.title('Density Plot')
plt.xlabel('Giá trị DiabetesPedigreeFunction')

# Box Plot
plt.subplot(2, 2, 3)
sns.boxplot(data['DiabetesPedigreeFunction'], color='lightgreen')
plt.title('Box Plot')

# QQ Plot
plt.subplot(2, 2, 4)
stats.probplot(data['DiabetesPedigreeFunction'], dist="norm", plot=plt)
plt.title('QQ Plot')

plt.tight_layout()
plt.show()

