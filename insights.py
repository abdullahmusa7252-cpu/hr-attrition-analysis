import pandas as pd
from groq import Groq
from api import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

findings = """
HR Attrition Analysis Key Findings:

- Overall attrition rate: 16.1% (237 out of 1,470 employees left)
- Overtime employees: 30.5% attrition vs 10.4% for non-overtime (3x higher)
- Sales Representatives have the highest attrition: 39.8%
- Young employees (18-25): 34.8% attrition
- Employees who left earned $4,787/month average vs $6,832 for those who stayed
- Logistic Regression accuracy: 87.1% (but poor recall for leavers - only 8%)
- Random Forest accuracy: 87.8% (recall for leavers: 13%)
- Top attrition predictors: Monthly Income, Overtime, Age, Monthly Rate, Daily Rate
"""

prompt = f"""
Based on this HR employee attrition analysis, provide:

1. A short executive summary (2-3 sentences)
2. Top 3 actionable recommendations for reducing attrition
3. One unexpected insight that might help the business

Findings:
{findings}

Be practical and data-driven. Focus on what the company can actually do.
"""

print("🤖 Asking Groq for HR Attrition Insights...\n")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are an HR analytics consultant. Give clear, actionable business advice based on data."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.6,
    max_tokens=800
)

result = response.choices[0].message.content
print(result)

with open("insights.txt", "w") as f:
    f.write(result)
print("\n✅ Insights saved to insights.txt")
