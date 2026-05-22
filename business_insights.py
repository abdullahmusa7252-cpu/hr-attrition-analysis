import pandas as pd

df = pd.read_csv('data/hr_attrition.csv')

print("=" * 60)
print("BUSINESS INSIGHTS - COST OF ATTRITION")
print("=" * 60)

# Number of employees who left
leavers = len(df[df['Attrition'] == 'Yes'])
print(f"\n📊 Employees who left: {leavers}")

# Average monthly income of leavers
avg_monthly_income = df[df['Attrition'] == 'Yes']['MonthlyIncome'].mean()
print(f"💰 Average monthly income of leavers: ${avg_monthly_income:.0f}")

# Estimated annual loss from salaries alone (12 months)
annual_salary_loss = avg_monthly_income * 12 * leavers
print(f"💸 Estimated annual salary loss: ${annual_salary_loss:,.0f}")

# Industry standard: Replacement cost = 50-200% of annual salary
# Using conservative estimate: 50% of annual salary
replacement_cost_percent = 0.50
replacement_cost = avg_monthly_income * 12 * replacement_cost_percent * leavers
print(f"\n📋 Estimated replacement cost (50% of salary): ${replacement_cost:,.0f}")

# Total cost = salary loss + replacement cost (if positions are filled)
total_cost_estimate = annual_salary_loss + replacement_cost
print(f"\n💼 TOTAL ESTIMATED COST (Salary Loss + Replacement): ${total_cost_estimate:,.0f}")

print("\n" + "=" * 60)
print("ASSUMPTIONS:")
print("-" * 60)
print("• Replacement cost estimated at 50% of annual salary (conservative)")
print("• Actual costs vary by role, seniority, and industry")
print("• Does NOT include: lost productivity, training time, team morale impact")
print("=" * 60)

# Additional insight: Cost by department
print("\n📊 COST BY DEPARTMENT:")
dept_cost = df[df['Attrition'] == 'Yes'].groupby('Department').size()
dept_salary = df[df['Attrition'] == 'Yes'].groupby('Department')['MonthlyIncome'].mean()
for dept in dept_cost.index:
    count = dept_cost[dept]
    avg_sal = dept_salary[dept]
    annual_loss = avg_sal * 12 * count
    print(f"   {dept}: {count} leavers, Avg ${avg_sal:.0f}/month → Annual loss ${annual_loss:,.0f}")

print("\n✅ Business insights calculated")
