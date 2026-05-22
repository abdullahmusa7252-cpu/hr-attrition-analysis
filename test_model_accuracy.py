import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df = pd.read_csv('data/hr_attrition.csv')

# Encode
df_encoded = df.copy()
for col in df_encoded.select_dtypes(include='object').columns:
    df_encoded[col] = LabelEncoder().fit_transform(df_encoded[col])

X = df_encoded.drop(['Attrition', 'EmployeeNumber', 'Over18', 'StandardHours'], axis=1, errors='ignore')
y = df_encoded['Attrition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("MODEL ACCURACY VERIFICATION")
print("=" * 50)
print(f"Random Forest Accuracy: {accuracy:.3f} ({accuracy*100:.1f}%)")

# Check if accuracy matches expected (87-88%)
if 0.87 <= accuracy <= 0.89:
    print("✅ Model accuracy matches expected range (87-88%)")
else:
    print(f"⚠️ Expected 87-88%, got {accuracy*100:.1f}%")

# Feature importance
features = X.columns
importances = rf.feature_importances_
top_features = sorted(zip(features, importances), key=lambda x: x[1], reverse=True)[:5]

print("\n--- Top 5 Feature Importances ---")
for feature, imp in top_features:
    print(f"   {feature}: {imp:.3f}")

print("\n✅ Model verification complete")
