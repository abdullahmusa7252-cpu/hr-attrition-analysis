import pandas as pd

df = pd.read_csv('data/hr_attrition.csv', encoding='utf-8-sig')

print("Shape:", df.shape)
missing = df.isnull().sum()
print("Missing values:", missing[missing > 0] if missing.sum() > 0 else "No missing values!")
print("ATTRITION BALANCE")
print(df['Attrition'].value_counts())
print(df['Attrition'].value_counts(normalize=True).round(3) * 100)
print(df.head(3))
