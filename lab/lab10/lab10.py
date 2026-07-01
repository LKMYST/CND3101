# Step 0: import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Step 1: load the dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = iris.target


# Step 2: explore the dataset and visualize it
print(df.head())
print(df.describe())
print(df.isnull().sum())

sns.pairplot(df, hue="species")
plt.show()


# Step 3: preprocess the dataset
X = df.drop("species", axis=1)
y = df["species"]


# Step 4: split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)


# Step 5: select and train a machine learning model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)


# Step 6: evaluate the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)
print(cm)

print(classification_report(y_test, y_pred))


# Step 7: allow manual input to predict a new instance of data
sample = pd.DataFrame(
    [[5.1,3.5,1.4,0.2]],
    columns=X.columns
)
prediction = model.predict(sample)
print(prediction)
