import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

# Load the dataset
data = pd.read_csv('healthcare-dataset-stroke-data.csv')

# Drop the 'id' column as it's not relevant for prediction
data.drop(columns=['id'], inplace=True)

# Define categorical and numeric columns
categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
numeric_cols = ['age', 'avg_glucose_level', 'bmi']

# Preprocessing steps
numeric_transformer = SimpleImputer(strategy='median')
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Define the model
model = DecisionTreeClassifier(random_state=0)

# Bundle preprocessing and modeling code in a pipeline
clf = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])

# Split data
X = data.drop('stroke', axis=1)
y = data['stroke']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
clf.fit(X_train, y_train)

# Evaluate the model
score = clf.score(X_test, y_test)
print(f"Model accuracy: {score:.2f}")

# Serialize the model
dump(clf, 'stroke.joblib')