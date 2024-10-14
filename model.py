from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

# Load data
df = pd.read_csv('cleaned_train.csv')
df = pd.get_dummies(df, columns=['Sex', 'Name'])

# Normalize data
scaler = StandardScaler()
features = ['Age', 'Fare']
df[features] = scaler.fit_transform(df[features])

# Splitting data
X = df.drop('Survived', axis=1) 
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Model accuracy: {accuracy}')

