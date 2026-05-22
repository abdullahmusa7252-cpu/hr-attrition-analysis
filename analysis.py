import pandas as pd

df = pd.read_csv('data/hr_attrition.csv')

print("=" * 40)
print("ATTRITION BY DEPARTMENT")
print("=" * 40)
print(pd.crosstab(df['Department'], df['Attrition'], normalize='index').round(3) * 100)

print("=" * 40)
print("ATTRITION BY OVERTIME")
print("=" * 40)
print(pd.crosstab(df['OverTime'], df['Attrition'], normalize='index').round(3) * 100)

print("=" * 40)
print("ATTRITION BY JOB ROLE")
print("=" * 40)
print(pd.crosstab(df['JobRole'], df['Attrition'], normalize='index').round(3) * 100)

print("=" * 40)
print("AVG MONTHLY INCOME BY ATTRITION")
print("=" * 40)
print(df.groupby('Attrition')['MonthlyIncome'].mean().round(2))

print("=" * 40)
print("ATTRITION BY AGE GROUP")
print("=" * 40)
df['AgeGroup'] = pd.cut(df['Age'], bins=[18,25,35,45,60], labels=['18-25','26-35','36-45','46-60'])
print(pd.crosstab(df['AgeGroup'], df['Attrition'], normalize='index').round(3) * 100)
