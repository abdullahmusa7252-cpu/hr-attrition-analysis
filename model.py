import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/hr_attrition.csv')

# Encode categorical variables
df_encoded = df.copy()
for col in df_encoded.select_dtypes(include='object').columns:
    df_encoded[col] = LabelEncoder().fit_transform(df_encoded[col])

# Prepare features and target
X = df_encoded.drop(['Attrition', 'EmployeeNumber', 'Over18', 'StandardHours'], axis=1, errors='ignore')
y = df_encoded['Attrition']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Logistic Regression
print("=" * 50)
print("LOGISTIC REGRESSION RESULTS")
print("=" * 50)
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, lr_pred):.3f}")
print("\nClassification Report:")
print(classification_report(y_test, lr_pred))

# 2. Random Forest
print("\n" + "=" * 50)
print("RANDOM FOREST RESULTS")
print("=" * 50)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, rf_pred):.3f}")
print("\nClassification Report:")
print(classification_report(y_test, rf_pred))

# 3. Feature Importance (Random Forest)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print("\n" + "=" * 50)
print("TOP 10 FEATURE IMPORTANCES (Random Forest)")
print("=" * 50)
print(feature_importance.head(10).to_string(index=False))

# Save feature importance chart
plt.figure(figsize=(10, 8))
top_features = feature_importance.head(10)
plt.barh(top_features['feature'], top_features['importance'], color='steelblue')
plt.xlabel('Importance Score')
plt.title('Top 10 Features Predicting Employee Attrition')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('images/feature_importance.png', dpi=150)
plt.close()
print("\n✅ Feature importance chart saved to images/feature_importance.png")
