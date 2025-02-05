import datetime
import pandas as pd
import joblib
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QSpinBox, QDateEdit, QRadioButton, 
    QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout, QButtonGroup, QMessageBox
)
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont

class PersonalInfoForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Dự đoán bệnh tiểu đường")
        self.setGeometry(100, 100, 500, 550)
        font = QFont("Arial", 10)
        
        # Layout for the entire form
        main_layout = QVBoxLayout()

        # Group box for personal information
        personal_info_group = QGroupBox("Thông tin cá nhân")
        personal_layout = QFormLayout()

        # Add fields for personal information
        self.name_input = QLineEdit()
        personal_layout.addRow("Họ và tên:", self.name_input)
        
        self.birth_date_input = QDateEdit()
        self.birth_date_input.setCalendarPopup(True)
        self.birth_date_input.setDate(QDate.currentDate())
        personal_layout.addRow("Ngày sinh:", self.birth_date_input)

        self.pregnancy_input = QSpinBox()
        self.pregnancy_input.setRange(0, 20)
        personal_layout.addRow("Số lần mang thai:", self.pregnancy_input)

        self.glucose_input = QSpinBox()
        self.glucose_input.setRange(0, 500)
        personal_layout.addRow("Glucose:", self.glucose_input)

        self.insulin_input = QSpinBox()
        self.insulin_input.setRange(0, 500)
        personal_layout.addRow("Insulin:", self.insulin_input)

        self.height_input = QSpinBox()
        self.height_input.setRange(0, 250)
        personal_layout.addRow("Chiều cao (cm):", self.height_input)

        self.weight_input = QSpinBox()
        self.weight_input.setRange(0, 300)
        personal_layout.addRow("Cân nặng (kg):", self.weight_input)

        self.skin_thickness_input = QSpinBox()
        self.skin_thickness_input.setRange(0, 100)
        personal_layout.addRow("Lớp dày da (mm):", self.skin_thickness_input)

        self.blood_pressure_input = QSpinBox()
        self.blood_pressure_input.setRange(0, 200)
        personal_layout.addRow("Huyết áp:", self.blood_pressure_input)

        # Radio buttons for family medical history with default "No" (Không) selected
        self.family_history_yes = QRadioButton("Có")
        self.family_history_no = QRadioButton("Không")
        self.family_history_no.setChecked(True)  # Set default to "Không" (No)

        # Connect the radio buttons to the toggle function
        self.family_history_yes.toggled.connect(self.toggle_family_history_group)

        # Layout for the radio buttons
        family_history_layout = QHBoxLayout()
        family_history_layout.addWidget(self.family_history_yes)
        family_history_layout.addWidget(self.family_history_no)
        personal_layout.addRow("Tiền sử bệnh gia đình:", family_history_layout)

        personal_info_group.setLayout(personal_layout)
        main_layout.addWidget(personal_info_group)

        # Group box for other family history (initially disabled)
        self.other_family_history_group = QGroupBox("Tiền sử khác gia đình")
        self.other_family_history_group.setEnabled(False)  # Disable by default
        other_family_layout = QFormLayout()

        self.parents_input = QSpinBox()
        self.parents_input.setRange(0, 2)
        other_family_layout.addRow("Bố mẹ:", self.parents_input)

        self.siblings_input = QSpinBox()
        self.siblings_input.setRange(0, 2)
        other_family_layout.addRow("Anh, chị, em ruột:", self.siblings_input)

        self.relatives_input = QSpinBox()
        self.relatives_input.setRange(0, 20)
        other_family_layout.addRow("Họ hàng bên cha mẹ:", self.relatives_input)

        self.other_family_history_group.setLayout(other_family_layout)
        main_layout.addWidget(self.other_family_history_group)

        # Predict Button
        predict_button = QPushButton("Dự đoán")
        predict_button.clicked.connect(self.handle_prediction)  # Connect the button to the prediction method
        main_layout.addWidget(predict_button)

        # Set main layout
        self.setLayout(main_layout)

    def toggle_family_history_group(self):
        # Enable group if "Có" (Yes) is selected, disable if "Không" (No) is selected
        self.other_family_history_group.setEnabled(self.family_history_yes.isChecked())

    def receiveData(self):
        # Retrieve data from all fields
        name = self.name_input.text()
        birth_date = self.birth_date_input.date().toPyDate()
        pregnancy_count = self.pregnancy_input.value()
        glucose = self.glucose_input.value()
        insulin = self.insulin_input.value()
        height_cm = self.height_input.value()
        weight_kg = self.weight_input.value()
        skin_thickness = self.skin_thickness_input.value()
        blood_pressure = self.blood_pressure_input.value()

        # Retrieve radio button selection for family medical history
        family_history = "Có" if self.family_history_yes.isChecked() else "Không"
        
        # Retrieve data from other family history fields if family history is selected
        parents = self.parents_input.value() if self.family_history_yes.isChecked() else 0
        siblings = self.siblings_input.value() if self.family_history_yes.isChecked() else 0
        relatives = self.relatives_input.value() if self.family_history_yes.isChecked() else 0

        # Collect data into a dictionary
        data = {
            "Name": [name],
            "Birth Date": [birth_date],
            "Pregnancies": [pregnancy_count],
            "Glucose": [glucose],
            "Insulin": [insulin],
            "Height (cm)": [height_cm],
            "Weight (kg)": [weight_kg],
            "SkinThickness": [skin_thickness],
            "BloodPressure": [blood_pressure],
            "Family History": [family_history],
            "Parents with History": [parents],
            "Siblings with History": [siblings],
            "Relatives with History": [relatives],
        }
        print("data received:\n", pd.DataFrame(data))
        return data
    
    def DataPreprocessing(self):
        dataReceived = self.receiveData()
        df = pd.DataFrame(dataReceived)
        dataDiabetes = pd.read_csv('data/diabetes.csv')

        # Calculate Age
        current_date = datetime.datetime.now().date()
        age = current_date.year - dataReceived['Birth Date'][0].year - ((current_date.month, current_date.day) < (dataReceived['Birth Date'][0].month, dataReceived['Birth Date'][0].day))

        # Calculate BMI
        height_m = dataReceived['Height (cm)'][0] / 100  # Convert height from cm to meters
        bmi = dataReceived['Weight (kg)'][0] / (height_m ** 2) if height_m > 0 else 0

        # Calculate Approximate Diabetes Pedigree Function (DPF)
        dpf = 0.2 * dataReceived['Parents with History'][0] + 0.1 * dataReceived['Siblings with History'][0] + 0.05 * dataReceived['Relatives with History'][0]

        cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin']
        for col in cols:
            df[col] = df[col].replace(0, pd.NA)
            df[col] = df[col].fillna(dataDiabetes[col].mean())

        # Preparing the final data dictionary
        data = {
            "Name": dataReceived["Name"],
            "Age": age,
            "Pregnancies": df["Pregnancies"],
            "Glucose": df["Glucose"],
            "Insulin": df["Insulin"],
            "BloodPressure": df["BloodPressure"],
            "SkinThickness": df["SkinThickness"],
            "BMI": bmi,
            "DiabetesPedigreeFunction": dpf
        }
        print("data preprocessing:\n", data)

        return data
    
    def standardData(self):
        data = self.DataPreprocessing()
        dataDiabetes = pd.read_csv('data/diabetes.csv')
        data = pd.DataFrame(data)
    
        # Chuẩn hóa Min-Max cho các cột cần thiết
        cols_to_normalize = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        
        # Tính toán min và max từ dữ liệu gốc
        min_vals = dataDiabetes[cols_to_normalize].min()
        max_vals = dataDiabetes[cols_to_normalize].max()

        # Áp dụng chuẩn hóa Min-Max
        for col in cols_to_normalize:
            data[col] = (data[col] - min_vals[col]) / (max_vals[col] - min_vals[col])
        
        return data

    def predictData(self):
        # Chuẩn hóa dữ liệu
        normalized_data = self.standardData()
        
        # Lấy các đặc trưng để dự đoán
        features = normalized_data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction','Age']]
        
        # Tải mô hình và thực hiện dự đoán
        model = joblib.load('build_model/model/model_predict.pkl')
        predictions = model.predict(features)
        
        # Thêm kết quả dự đoán vào DataFrame
        normalized_data['Prediction'] = predictions
        
        return normalized_data

    def handle_prediction(self):
        # Gọi hàm dự đoán và nhận kết quả
        prediction_results = self.predictData()
        # Tạo thông báo hiển thị kết quả
        prediction_text = "Dự đoán bệnh tiểu đường cho {}: {}".format(prediction_results['Name'][0], "Có tiểu đường" if prediction_results['Prediction'][0] == 1 else "Không có tiểu đường")
        
        # Hiển thị hộp thoại thông báo
        QMessageBox.information(self, "Kết quả dự đoán", prediction_text)

# Run the application
app = QApplication(sys.argv)
form = PersonalInfoForm()
form.show()
sys.exit(app.exec_())
