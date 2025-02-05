import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data/diabetes.csv')

columns_with_noise = ['Glucose', 'BMI']

df[columns_with_noise] = df[columns_with_noise].replace(0, pd.NA)

for col in columns_with_noise:
    df[col] = df[col].fillna(df[col].mean())



columns_with_noise = ['BloodPressure', 'SkinThickness', 'Insulin']
df[columns_with_noise] = df[columns_with_noise].replace(0, pd.NA)
for col in columns_with_noise:
    df[col] = df[col].fillna(df[col].median())


columns_to_normalize = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
scaler = MinMaxScaler()
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

df.to_csv('data/diabetes_standard_data.csv',index=False)

print(df)