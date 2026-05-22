import pandas as pd

df = pd.read_csv('data/hr_attrition.csv')

print("=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"Missing values: {df.isnull().sum().sum()}")

print("\n--- Duplicates ---")
print(f"Duplicate rows: {df.duplicated().sum()}")

print("\n--- Data Types ---")
print(df.dtypes.value_counts())

print("\n--- Sample columns ---")
print(df[['Age', 'Attrition', 'MonthlyIncome', 'OverTime']].head(3))

print("\n✅ Data quality check complete")
