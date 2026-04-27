from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = datasets.load_iris()

# Convert to DataFrame (needed for graph)
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# Show first 5 rows
print("First five rows of the Iris dataset:")
print(df.head())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# Train model
model = GaussianNB()
model.fit(X_train, y_train)

# 🔥 Graph (pairplot)
sns.pairplot(df, hue="species")
plt.suptitle("Feature Relationships by Species", y=1.02)
plt.show()

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("\nModel Accuracy:", round(accuracy_score(y_test, y_pred), 2))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Test new sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_sample)

print("\nPredicted Class for sample", new_sample, ":", iris.target_names[prediction][0])