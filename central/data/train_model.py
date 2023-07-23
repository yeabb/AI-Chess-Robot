import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from create_dataset import CreateDataset
import joblib

createDataset = CreateDataset()
X, y = createDataset.dataset()
X = np.array(X)
y = np.array(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an SVM classifier
svm_model = SVC(kernel='linear', C=1.0, random_state=42)

# Train the SVM model on the training data
svm_model.fit(X_train, y_train)

model_filename = 'svm_model.pkl'
joblib.dump(svm_model, model_filename)

# y_pred = svm_model.predict(X_test)

# # # Evaluate the model's performance
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy:.4f}")

# Generate a detailed classification report
# print(classification_report(y_test, y_pred))