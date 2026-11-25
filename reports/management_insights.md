# Management Insights — Northstar Bank

## Data and scope
This portfolio demonstration uses synthetic data for a fictional bank. It contains 5,000 borrower profiles, 6,200 loans and 92,941 scheduled instalment records.

## Demonstration KPI snapshot
- Loans: 6,200
- Unique borrowers: 3,595
- Total loan exposure: ₹ 266,700,800.08
- Simulated default rate: 45.69%
- Average loan amount: ₹ 43,016.26
- Late instalment rate: 28.49%
- Missed instalment rate: 7.07%

## Analytical use cases
1. Portfolio monitoring by product, region and credit-score band.
2. Exposure concentration and large-loan review.
3. Payment behaviour monitoring using late and missed instalment indicators.
4. Descriptive comparison of default incidence across segments.

## Recommended management actions
1. Monitor portfolio exposure and simulated/default incidence by loan type and geography.
2. Investigate segments with higher observed late-payment incidence using verified operational data.
3. Establish concentration limits only after validating risk appetite, capital requirements and regulatory obligations.
4. Validate any scorecard with representative historical data, out-of-time testing, calibration, fairness assessment and documented governance.
5. Keep human review, explainability, privacy controls and applicable lending regulations central to any real credit process.

## Definitions and limitations
- Default rate = loans with `default_flag = 1` / total loans.
- Exposure = sum of original loan principal; this is not current outstanding balance.
- Late/missed instalment rates are calculated over the included payment schedule rows.
- The simulated default label is not a trained prediction and is not suitable for underwriting or customer-level decisions.
- Interest income, recoveries, write-offs, collateral, expenses, regulatory capital and time-varying outstanding balances are not modelled.

## Important responsible-use note
This dataset and analysis are educational portfolio materials only. They must not be used to assess real applicants, approve or reject credit, set interest rates, or infer the creditworthiness of any person.
