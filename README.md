# HR Employee Attrition Analysis

**Author:** Abdullah Musa

## Overview
Analyzed 1,470 employees to identify key drivers of attrition using machine learning and AI. The goal was to provide actionable business recommendations to reduce employee turnover.

## Key Findings

| Finding | Insight |
|---------|---------|
| **Overall attrition rate** | 16.1% (237 out of 1,470 employees left) |
| **Overtime employees** | 3x more likely to leave (30.5% vs 10.4%) |
| **Sales Representatives** | Highest attrition at 39.8% |
| **Young employees (18-25)** | 34.8% attrition rate |
| **Monthly Income** | Leavers earned $4,787 vs $6,832 for stayers |

## Models

| Model | Accuracy | Recall (Leavers) |
|-------|----------|------------------|
| Logistic Regression | 87.1% | 8% |
| Random Forest | 87.8% | 13% |

## Top 5 Attrition Predictors (Random Forest)

1. Monthly Income
2. Overtime
3. Age
4. Monthly Rate
5. Daily Rate

## Charts Generated

- Attrition by Department
- Attrition by Overtime
- Top 10 Job Roles by Attrition
- Attrition by Age Group
- Monthly Income Distribution (Box Plot)
- Feature Importance Chart

## AI-Generated Insights (Groq)

The Groq API (Llama 3.3 70B) analyzed the findings and provided:
- Executive summary
- 3 actionable recommendations
- Unexpected insight about model limitations

## Tools Used

- Python 3.14
- pandas, numpy
- matplotlib, seaborn
- scikit-learn (Logistic Regression, Random Forest)
- Groq API

## Files

| File | Purpose |
|------|---------|
| `verify.py` | Data validation |
| `analysis.py` | Key metrics calculation |
| `charts.py` | Generate all visualizations |
| `model.py` | Train and evaluate models |
| `insights.py` | Groq AI business recommendations |
| `view.html` | Interactive portfolio dashboard |

## Live Dashboard

Open `view.html` in any browser to see an interactive summary of all findings.

## Author

Abdullah Musa — [Contra Profile](https://contra.com)
