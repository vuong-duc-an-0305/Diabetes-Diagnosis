# model_training.py
from data_preparation import load_and_prepare_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Gọi hàm load_and_prepare_data từ data_preparation.py
X_train, X_test, y_train, y_test = load_and_prepare_data()

# Mô hình Decision Tree
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)
accuracy_tree = accuracy_score(y_test, y_pred_tree)
print("Độ chính xác của Decision Tree:", accuracy_tree)
print("Báo cáo phân loại Decision Tree:\n", classification_report(y_test, y_pred_tree))
print("Ma trận nhầm lẫn Decision Tree:\n", confusion_matrix(y_test, y_pred_tree))
