# HR Employee Attrition Analysis

**Author:** Abdullah Musa

## Overview

Analyzed 1,470 employees to identify key drivers of attrition using machine learning and AI. The goal was to provide actionable business recommendations to reduce employee turnover.

## Live Dashboard

**[View Interactive Dashboard]([https://your-lovable-link-here.lovable.app/](https://id-preview--d3f8113f-792b-4982-b659-cbc588be8870.lovable.app/)**  
*Dark theme dashboard with KPIs, charts, feature importance, financial impact analysis, and AI-generated insights.*

---

## Key Findings

| Finding | Insight |
|---------|---------|
| **Overall attrition rate** | 16.1% (237 out of 1,470 employees left) |
| **Overtime employees** | 3x more likely to leave (30.5% vs 10.4%) |
| **Sales Representatives** | Highest attrition at 39.8% |
| **Young employees (18-25)** | 34.8% attrition rate |
| **Monthly Income** | Leavers earned $4,787 vs $6,832 for stayers |

---

## Models

| Model | Accuracy | Recall (Leavers) |
|-------|----------|------------------|
| Logistic Regression | 87.1% | 8% |
| Random Forest | 87.8% | 13% |

**Note:** Models are better at predicting who STAYS than who LEAVES. Only 13% of actual leavers are caught by the Random Forest model — suggests additional data (employee engagement, management quality) is needed.

---

## Top 5 Attrition Predictors (Random Forest)

1. **Monthly Income** (0.084)
2. **Overtime** (0.063)
3. **Age** (0.062)
4. **Monthly Rate** (0.054)
5. **Daily Rate** (0.052)

*Values represent Random Forest feature importance scores.*

---

## Financial Impact

| Metric | Amount |
|--------|--------|
| **Total estimated annual cost** | **$20.4 MILLION** |
| Salary loss from leavers | $13.6M |
| Estimated replacement costs (50% of salary) | $6.8M |

**Cost by department:**
- Research & Development: $6.6M (133 leavers)
- Sales: $6.5M (92 leavers)
- Human Resources: $535K (12 leavers)

*Replacement cost estimated at 50% of annual salary (industry conservative estimate). Actual costs vary by role and seniority.*

---

## Charts Generated

| Chart | Purpose |
|-------|---------|
| Attrition by Department | Which departments lose the most employees |
| Attrition by Overtime | Overtime impact on attrition (3x higher risk) |
| Top 10 Job Roles by Attrition | Highest-risk positions |
| Attrition by Age Group | Age segments at highest risk |
| Monthly Income Box Plot | Income comparison (Stayers vs Leavers) |
| Feature Importance Chart | Top predictors from Random Forest |

---

## AI-Generated Insights (Groq)

The Groq API (Llama 3.3 70B) analyzed the findings and provided:

- **Executive summary** of attrition drivers
- **3 actionable recommendations** (overtime management, sales rep support, compensation review)
- **Unexpected insight** about model limitations (poor recall for leavers)

*See `insights.txt` in the outputs folder for the full AI-generated report.*

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Python 3.14 | Core programming language |
| pandas, numpy | Data manipulation and analysis |
| matplotlib, seaborn | Static visualizations |
| scikit-learn | Logistic Regression, Random Forest |
| Groq API (Llama 3.3 70B) | AI-generated business insights |
| Lovable | Interactive dark theme dashboard |

---

## Validation & Testing

All numbers in this project have been verified through 5 separate test scripts:

| Test | Result |
|------|--------|
| Data Quality | ✅ No missing values, no duplicates |
| Chart Numbers | ✅ All percentages match source data |
| Model Accuracy | ✅ 87.8% consistent and reproducible |
| Dashboard KPIs | ✅ All KPI values verified |

Run `python scripts/run_all_tests.py` to verify all numbers.

---

## Key Takeaways for Business

1. **Overtime is the strongest risk factor** — employees working overtime are 3x more likely to leave
2. **Sales Representatives need attention** — 39.8% attrition rate is the highest among all roles
3. **Compensation matters** — leavers earn $2,046 less per month on average
4. **Young employees (18-25) are high risk** — 34.8% attrition rate
5. **Attrition costs the company ~$20.4M annually** — salary loss + replacement costs

---

## Author

**Abdullah Musa**

- [Contra Profile](https://contra.com/your-username-here)
- [GitHub](https://github.com/abdullahmusa7252-cpu)

---

*Data Source: IBM HR Analytics Dataset (Kaggle) | Last updated: May 2026*
