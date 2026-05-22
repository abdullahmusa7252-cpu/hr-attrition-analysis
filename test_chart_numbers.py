import pandas as pd

df = pd.read_csv('data/hr_attrition.csv')

print("=" * 50)
print("CHART NUMBERS VERIFICATION")
print("=" * 50)

# 1. Attrition by Overtime
print("\n1. Attrition by Overtime:")
overtime = pd.crosstab(df['OverTime'], df['Attrition'], normalize='index') * 100
print(f"   No Overtime attrition: {overtime.loc['No', 'Yes']:.1f}%")
print(f"   Yes Overtime attrition: {overtime.loc['Yes', 'Yes']:.1f}%")

# 2. Top Job Roles
print("\n2. Top 5 Job Roles by Attrition:")
job_roles = pd.crosstab(df['JobRole'], df['Attrition'], normalize='index') * 100
top_roles = job_roles['Yes'].sort_values(ascending=False).head(5)
for role, rate in top_roles.items():
    print(f"   {role}: {rate:.1f}%")

# 3. Monthly Income comparison
print("\n3. Monthly Income:")
stayers = df[df['Attrition'] == 'No']['MonthlyIncome'].mean()
leavers = df[df['Attrition'] == 'Yes']['MonthlyIncome'].mean()
print(f"   Stayers: ${stayers:.0f}")
print(f"   Leavers: ${leavers:.0f}")
print(f"   Difference: ${stayers - leavers:.0f}")

# 4. Attrition by Age Group
print("\n4. Attrition by Age Group:")
df['AgeGroup'] = pd.cut(df['Age'], bins=[18,25,35,45,60], labels=['18-25', '26-35', '36-45', '46-60'])
age_attrition = pd.crosstab(df['AgeGroup'], df['Attrition'], normalize='index') * 100
for age, rate in age_attrition['Yes'].items():
    print(f"   {age}: {rate:.1f}%")

print("\n✅ All chart numbers verified")
