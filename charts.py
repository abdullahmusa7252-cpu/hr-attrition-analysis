import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load data
df = pd.read_csv('data/hr_attrition.csv')

# Create images directory if it doesn't exist
import os
os.makedirs('images', exist_ok=True)

# 1. Attrition by Department (bar chart)
plt.figure()
dept_attrition = pd.crosstab(df['Department'], df['Attrition'], normalize='index') * 100
dept_attrition['Yes'].sort_values(ascending=False).plot(kind='bar', color='salmon')
plt.title('Attrition Rate by Department', fontsize=14)
plt.ylabel('Attrition Rate (%)')
plt.xlabel('Department')
plt.ylim(0, 30)
plt.tight_layout()
plt.savefig('images/attrition_by_department.png', dpi=150)
plt.close()

# 2. Attrition by Overtime (grouped bar)
plt.figure()
overtime_attrition = pd.crosstab(df['OverTime'], df['Attrition'], normalize='index') * 100
overtime_attrition.plot(kind='bar', color=['lightgreen', 'lightcoral'])
plt.title('Attrition Rate by Overtime', fontsize=14)
plt.ylabel('Percentage (%)')
plt.xlabel('Overtime')
plt.ylim(0, 100)
plt.legend(title='Attrition')
plt.tight_layout()
plt.savefig('images/attrition_by_overtime.png', dpi=150)
plt.close()

# 3. Attrition by Job Role (horizontal bar - top 10 highest)
plt.figure()
job_attrition = pd.crosstab(df['JobRole'], df['Attrition'], normalize='index') * 100
job_attrition_sorted = job_attrition['Yes'].sort_values(ascending=True)
job_attrition_sorted.tail(10).plot(kind='barh', color='teal')
plt.title('Top 10 Job Roles with Highest Attrition', fontsize=14)
plt.xlabel('Attrition Rate (%)')
plt.tight_layout()
plt.savefig('images/attrition_by_jobrole.png', dpi=150)
plt.close()

# 4. Monthly Income comparison (box plot)
plt.figure()
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, palette=['lightgreen', 'lightcoral'])
plt.title('Monthly Income Distribution by Attrition Status', fontsize=14)
plt.ylabel('Monthly Income ($)')
plt.tight_layout()
plt.savefig('images/monthly_income_boxplot.png', dpi=150)
plt.close()

# 5. Attrition by Age Group (bar chart)
plt.figure()
df['AgeGroup'] = pd.cut(df['Age'], bins=[18,25,35,45,60], labels=['18-25', '26-35', '36-45', '46-60'])
age_attrition = pd.crosstab(df['AgeGroup'], df['Attrition'], normalize='index') * 100
age_attrition['Yes'].plot(kind='bar', color='skyblue')
plt.title('Attrition Rate by Age Group', fontsize=14)
plt.ylabel('Attrition Rate (%)')
plt.xlabel('Age Group')
plt.ylim(0, 40)
plt.tight_layout()
plt.savefig('images/attrition_by_agegroup.png', dpi=150)
plt.close()

print("✅ All charts saved to images/ folder!")
print("Files created:")
for f in os.listdir('images'):
    if f.endswith('.png'):
        print(f"   - images/{f}")
