# 📊 HR Employee Attrition & Workforce Analytics

> An end-to-end data science and business intelligence project identifying key drivers of employee turnover using machine learning, Python, and AI-assisted workflows.

---

## 🔗 Live Demo & Links
* 🌐 **Interactive Dashboard:** [View Live BI Dashboard](#) *(Replace with your Lovable link)*
* 📂 **Source Code & Scripts:** [GitHub Repository](https://github.com/your-username/your-repo-name)
* 🗄️ **Dataset:** IBM HR Analytics Dataset (Kaggle)

---

## 🎯 Executive Summary
Employee turnover is a silent killer of company revenue. This project analyzes **1,470 employee records** to pinpoint *why* people leave, *who* is most at risk, and what it costs the business.

* **Total Annual Cost of Attrition:** 💰 **$20.4 Million** ($13.6M in salary loss + $6.8M in replacement costs).
* **Overall Turnover Rate:** 16.1% (237 employees left).

---

## 🔍 Key Findings & Risk Factors

| Category | Key Insight | Data Point |
| :--- | :--- | :--- |
| **🚨 Overtime** | Strongest risk factor; overworked staff are vastly more likely to quit. | **3x higher risk** (30.5% vs 10.4%) |
| **📈 Department Risk** | Sales Representatives experience the most critical brain drain. | **39.8% attrition rate** |
| **👥 Demographics** | Younger staff members have higher early-career mobility/turnover. | **34.8% attrition rate** (Ages 18–25) |
| **💵 Compensation** | A clear pay gap exists between those who stay and those who leave. | Leavers earn **$2,046 less/month** ($4,787 vs $6,832) |

---

## 🤖 Machine Learning Models & Limitations

Two classification models were built using `scikit-learn` to predict employee churn:

* **Logistic Regression:** 87.1% Accuracy | 8% Recall (Leavers)
* **Random Forest:** 87.8% Accuracy | 13% Recall (Leavers)

> **⚠️ Critical Insight / Model Limitation:**
> Both models are exceptional at predicting who *stays*, but poor at catching who *leaves* (only capturing 13% of actual leavers). This proves that financial metrics alone aren't enough—predicting real-world human behavior requires qualitative data like employee engagement, management quality, and burnout metrics.

### Top 5 Attrition Predictors (Random Forest Feature Importance)
1. **Monthly Income** (0.084)
2. **Overtime** (0.063)
3. **Age** (0.062)
4. **Monthly Rate** (0.054)
5. **Daily Rate** (0.052)

---

## 🛠️ Tech Stack & Workflow

### Tools Used
* **Core Language:** Python 3.x
* **Data Manipulation & Stats:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` (Logistic Regression, Random Forest)
* **Visualizations:** `matplotlib`, `seaborn`, Jupyter Notebooks
* **AI Business Insights:** Groq API (Llama 3.3 70B)
* **BI Dashboard:** Lovable (Dark theme interactive UI)

### Rigorous Verification Workflow
1. **Data Benchmarking:** Cleaned and filtered core pain points from raw data to optimize processing.
2. **Local Validation:** Built and tested models locally in Jupyter, cross-verifying metrics across 5 separate validation test scripts (`run_all_tests.py`).
3. **BI Reconciliation:** Deployed findings to the interactive dashboard. *Note: Minor rounding discrepancies (<1%) between Python arrays and BI UI elements have been documented inline on the dashboard for absolute transparency.*

---

## 🚀 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the validation test suite:

   ```bash
   python scripts/run_all_tests.py
   ```

---

## 👤 Author

**Abdullah Musa**
**Abdullah(Nickname)**

* Aspiring Software & Data Engineer
* [GitHub Profile](https://github.com)

---

*License: MIT*
