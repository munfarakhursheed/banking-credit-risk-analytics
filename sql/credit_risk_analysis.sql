
-- Banking Credit Risk Analytics | SQLite-compatible SQL
-- Import borrowers.csv, loans.csv and loan_payments.csv as matching tables.

-- 1. Portfolio overview
SELECT COUNT(*) total_loans, COUNT(DISTINCT customer_id) borrowers,
       ROUND(SUM(loan_amount),2) total_exposure,
       ROUND(100.0*SUM(default_flag)/COUNT(*),2) default_rate
FROM loans;

-- 2. Default rate by loan type
SELECT loan_type, COUNT(*) loans,
       ROUND(AVG(default_flag)*100,2) default_rate_pct,
       ROUND(AVG(loan_amount),2) avg_loan_amount
FROM loans GROUP BY loan_type ORDER BY default_rate_pct DESC;

-- 3. Default rate by credit risk band
SELECT risk_band, COUNT(*) loans,
       ROUND(AVG(default_flag)*100,2) default_rate_pct
FROM loans GROUP BY risk_band ORDER BY default_rate_pct DESC;

-- 4. Exposure by region
SELECT b.region, COUNT(l.loan_id) loans,
       ROUND(SUM(l.loan_amount),2) exposure,
       ROUND(AVG(l.default_flag)*100,2) default_rate_pct
FROM loans l JOIN borrowers b USING(customer_id)
GROUP BY b.region ORDER BY exposure DESC;

-- 5. Debt-to-income proxy by loan
SELECT l.loan_id, l.customer_id, l.loan_amount, b.annual_income,
       ROUND(l.loan_amount/NULLIF(b.annual_income,0),2) loan_to_annual_income
FROM loans l JOIN borrowers b USING(customer_id)
ORDER BY loan_to_annual_income DESC LIMIT 25;

-- 6. Default rate by employment type
SELECT b.employment_type, COUNT(*) loans,
       ROUND(AVG(l.default_flag)*100,2) default_rate_pct
FROM loans l JOIN borrowers b USING(customer_id)
GROUP BY b.employment_type ORDER BY default_rate_pct DESC;

-- 7. Payment behaviour
SELECT l.loan_status, COUNT(p.loan_id) scheduled_installments,
       ROUND(100.0*SUM(p.late_payment_flag)/COUNT(*),2) late_payment_pct,
       ROUND(100.0*SUM(p.missed_payment_flag)/COUNT(*),2) missed_payment_pct
FROM loans l JOIN loan_payments p USING(loan_id)
GROUP BY l.loan_status;

-- 8. Monthly origination volume
SELECT strftime('%Y-%m',origination_date) origination_month,
       COUNT(*) loans, ROUND(SUM(loan_amount),2) originations
FROM loans GROUP BY origination_month ORDER BY origination_month;

-- 9. Largest exposures
SELECT loan_id, customer_id, loan_type, loan_amount, credit_score, risk_band, default_flag
FROM loans ORDER BY loan_amount DESC LIMIT 25;

-- 10. Customer-level exposure and default count
SELECT customer_id, COUNT(*) loans, ROUND(SUM(loan_amount),2) exposure,
       SUM(default_flag) defaulted_loans
FROM loans GROUP BY customer_id ORDER BY exposure DESC LIMIT 50;

-- 11. Risk band x loan type matrix
SELECT risk_band, loan_type, COUNT(*) loans,
       ROUND(AVG(default_flag)*100,2) default_rate_pct
FROM loans GROUP BY risk_band, loan_type
ORDER BY risk_band, loan_type;
