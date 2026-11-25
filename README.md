# Banking Credit Risk & Loan Portfolio Analytics

**Role simulation:** Banking Business Intelligence Analyst  
**Institution:** Northstar Bank (fictional)  
**Stack:** SQL (SQLite-compatible), Python, pandas, Jupyter, Streamlit, Plotly, Power BI-ready CSVs.

> **Data disclosure and responsible use:** All records and default labels are synthetic. This project is educational only, not a validated credit-risk model, and must not be used for real credit decisions.

## Business objective
Explore loan portfolio exposure, default incidence, payment behaviour and segment-level patterns to demonstrate a management reporting workflow.

## Repository contents
- `data/` — borrower, loan and payment tables.
- `sql/credit_risk_analysis.sql` — documented SQL queries.
- `notebooks/credit_risk_analysis.ipynb` — reproducible Python analysis.
- `dashboard/app.py` — interactive Streamlit dashboard.
- `reports/management_insights.md` — KPI snapshot, definitions, limitations and recommendations.

## Quick start
1. Install Python 3.10+.
2. Run `pip install -r requirements.txt`.
3. Launch `streamlit run dashboard/app.py`.
4. Open `notebooks/credit_risk_analysis.ipynb` in Jupyter and run all cells.
5. Import the CSVs into SQLite or Power BI using filenames as table names.

## Suggested Power BI relationships
- `loans[customer_id]` → `borrowers[customer_id]`
- `loan_payments[loan_id]` → `loans[loan_id]`

A Power BI `.pbix` is not included; the CSV model and dashboard are ready to import and the Streamlit dashboard provides an immediately runnable interactive version.

## KPI definitions
See `reports/management_insights.md`. Exposure represents original principal, not current outstanding balance. Default labels are simulated.

## Responsible use
The dataset, labels and analyses are synthetic and are not appropriate for underwriting, pricing, approval, rejection or other real-world decisions about individuals.
