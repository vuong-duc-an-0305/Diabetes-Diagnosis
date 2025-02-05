from data_preparation import load_and_prepare_data
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
# Gọi hàm load_and_prepare_data từ data_preparation.py
X_train, X_test, y_train, y_test = load_and_prepare_data()

# Mô hình SVM
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("Độ chính xác của SVM:", accuracy_svm)
print("Báo cáo phân loại SVM:\n", classification_report(y_test, y_pred_svm))
print("Ma trận nhầm lẫn SVM:\n", confusion_matrix(y_test, y_pred_svm))

joblib.dump(svm_model,'build_model/model/model_predict.pkl')