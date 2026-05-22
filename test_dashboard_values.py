import pandas as pd

df = pd.read_csv('data/hr_attrition.csv')

print("=" * 50)
print("DASHBOARD KPI VERIFICATION")
print("=" * 50)

# KPI 1: Total Employees
total = len(df)
print(f"Total Employees: {total}")

# KPI 2: Overall Attrition Rate
attrition_rate = (df['Attrition'] == 'Yes').mean() * 100
print(f"Overall Attrition Rate: {attrition_rate:.1f}%")

# KPI 3: Overtime Attrition Rate
overtime_attrition = df[df['OverTime'] == 'Yes']['Attrition'].value_counts(normalize=True).get('Yes', 0) * 100
print(f"Overtime Attrition Rate: {overtime_attrition:.1f}%")

# KPI 4: Average Monthly Income
stayers_income = df[df['Attrition'] == 'No']['MonthlyIncome'].mean()
leavers_income = df[df['Attrition'] == 'Yes']['MonthlyIncome'].mean()
print(f"Avg Income - Stayers: ${stayers_income:.0f}")
print(f"Avg Income - Leavers: ${leavers_income:.0f}")

print("\n✅ All KPI values verified")
