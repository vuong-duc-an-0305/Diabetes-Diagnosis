import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def load_and_prepare_data():
    # Đọc dữ liệu từ file
    df = pd.read_csv('data/diabetes_standard_data.csv')

    # Tách cột mục tiêu ra khỏi các cột đầu vào
    X = df.drop(columns=['Outcome'])
    y = df['Outcome']

    # Chuẩn hóa các cột đầu vào
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

