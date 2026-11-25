
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
st.set_page_config(page_title="Credit Risk Intelligence",layout="wide")
ROOT=Path(__file__).resolve().parents[1]
@st.cache_data
def load():
    b=pd.read_csv(ROOT/"data"/"borrowers.csv")
    l=pd.read_csv(ROOT/"data"/"loans.csv")
    p=pd.read_csv(ROOT/"data"/"loan_payments.csv")
    return b,l,p
b,l,p=load()
d=l.merge(b,on="customer_id",how="left")
st.title("Credit Risk & Loan Portfolio Intelligence")
st.caption("Synthetic portfolio demonstration. Not real borrower data, lending advice, or a validated credit model.")
types=st.sidebar.multiselect("Loan type",sorted(d.loan_type.unique()),default=sorted(d.loan_type.unique()))
regions=st.sidebar.multiselect("Region",sorted(d.region.unique()),default=sorted(d.region.unique()))
x=d[d.loan_type.isin(types)&d.region.isin(regions)]
c1,c2,c3,c4=st.columns(4)
c1.metric("Loans",f"{len(x):,}")
c2.metric("Portfolio exposure",f"₹ {x.loan_amount.sum()/1e7:,.2f} Cr")
c3.metric("Default rate",f"{x.default_flag.mean()*100:.1f}%")
c4.metric("Average loan",f"₹ {x.loan_amount.mean():,.0f}")
a,bcol=st.columns(2)
risk=x.groupby("risk_band").agg(loans=("loan_id","count"),default_rate=("default_flag","mean")).reset_index()
risk["default_rate"]=risk.default_rate*100
a.plotly_chart(px.bar(risk,x="risk_band",y="default_rate",text_auto=".1f",title="Default rate by credit score band"),use_container_width=True)
typ=x.groupby("loan_type").agg(exposure=("loan_amount","sum"),default_rate=("default_flag","mean")).reset_index()
typ["default_rate"]=typ.default_rate*100
bcol.plotly_chart(px.bar(typ,x="loan_type",y="exposure",title="Exposure by loan type"),use_container_width=True)
c,dcol=st.columns(2)
reg=x.groupby("region").agg(exposure=("loan_amount","sum"),default_rate=("default_flag","mean")).reset_index()
reg["default_rate"]=reg.default_rate*100
c.plotly_chart(px.scatter(reg,x="exposure",y="default_rate",size="exposure",color="region",title="Regional exposure vs default rate"),use_container_width=True)
pay=p.merge(l[["loan_id","loan_status"]],on="loan_id")
pay=pay.groupby("loan_status").agg(late_pct=("late_payment_flag","mean"),missed_pct=("missed_payment_flag","mean")).reset_index()
pay[["late_pct","missed_pct"]]*=100
dcol.plotly_chart(px.bar(pay,x="loan_status",y=["late_pct","missed_pct"],barmode="group",title="Payment behaviour by loan status"),use_container_width=True)
st.subheader("Portfolio by region and loan type")
pivot=x.pivot_table(index="region",columns="loan_type",values="loan_amount",aggfunc="sum",fill_value=0)
st.dataframe(pivot.style.format("₹ {:,.0f}"),use_container_width=True)
st.subheader("Largest loan exposures")
st.dataframe(x.nlargest(20,"loan_amount")[["loan_id","customer_id","loan_type","loan_amount","credit_score","risk_band","default_flag"]],use_container_width=True)
st.warning("Credit-score bands are descriptive groupings only. Do not use this synthetic demonstration to approve, reject, price, or make decisions about real applicants.")
