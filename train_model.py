import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the Excel file
df = pd.read_excel('Crop Recommendation Dataset.xlsx')

# The file has: Temperature, Humidity, pH, Rainfall, Label
X = df[['Temperature', 'Humidity', 'pH', 'Rainfall']]
y = df['Label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest is excellent for this size (7000 rows)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
with open('crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print(f"Success! AgriOracle AI trained on {len(df)} rows.")