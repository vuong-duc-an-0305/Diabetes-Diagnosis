import pandas as pd
# Đọc dữ liệu từ tệp CSV
data = pd.read_csv('data/diabetes_standard_data.csv')

# Kiểm tra cấu trúc dữ liệu
check = {
    'thuộc tính': ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DPF', 'Age', 'Outcome'],
    'số lượng': [data[col].count() for col in ['Pregnancies', 'Glucose', 'BloodPressure',  'SkinThickness', 'Insulin', 'BMI','DiabetesPedigreeFunction', 'Age', 'Outcome']],
    'giá trị thiếu': [data[col].isnull().sum() for col in ['Pregnancies', 'Glucose', 
                                                             'BloodPressure', 'SkinThickness', 
                                                             'Insulin', 'BMI', 
                                                             'DiabetesPedigreeFunction', 'Age', 
                                                             'Outcome']],
    'giá trị nhỏ nhất': [data[col].min() for col in ['Pregnancies', 'Glucose', 'BloodPressure', 
                                                      'SkinThickness', 'Insulin', 
                                                      'BMI', 'DiabetesPedigreeFunction', 
                                                      'Age', 'Outcome']],
    'giá trị lớn nhất': [data[col].max() for col in ['Pregnancies', 'Glucose', 'BloodPressure', 
                                                      'SkinThickness', 'Insulin', 
                                                      'BMI', 'DiabetesPedigreeFunction', 
                                                      'Age', 'Outcome']],
    'trung bình': [data[col].mean() for col in ['Pregnancies', 'Glucose', 'BloodPressure', 
                                                  'SkinThickness', 'Insulin', 'BMI', 
                                                  'DiabetesPedigreeFunction', 'Age', 
                                                  'Outcome']],
    'trung vị': [data[col].median() for col in ['Pregnancies', 'Glucose', 'BloodPressure', 
                                                  'SkinThickness', 'Insulin', 'BMI', 
                                                  'DiabetesPedigreeFunction', 'Age', 
                                                  'Outcome']],
    'độ lệch chuẩn': [data[col].std() for col in ['Pregnancies', 'Glucose', 'BloodPressure', 
                                                    'SkinThickness', 'Insulin', 'BMI', 
                                                    'DiabetesPedigreeFunction', 'Age', 
                                                    'Outcome']],
    'kiểu dữ liệu' : [data[col].dtype for col in ['Pregnancies', 'Glucose', 'BloodPressure', 
                                                    'SkinThickness', 'Insulin', 'BMI', 
                                                    'DiabetesPedigreeFunction', 'Age', 
                                                    'Outcome']],
    
}

# Tạo DataFrame từ dict
df = pd.DataFrame(check)

# Hiển thị DataFrame
print(df)


