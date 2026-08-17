from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent; OUT=BASE/'outputs'; OUT.mkdir(exist_ok=True)
df=pd.read_csv(BASE/'data'/'customer_churn.csv')
summary=pd.DataFrame([{'customers':len(df),'churn_rate_pct':100*df.churned.mean(),'avg_monthly_charge':df.monthly_charge.mean(),'avg_tenure_months':df.tenure_months.mean()}]); summary.to_csv(OUT/'summary_kpis.csv',index=False)
contract=df.groupby('contract_type',as_index=False).churned.mean(); contract['churn_rate_pct']=100*contract.churned; contract.to_csv(OUT/'churn_by_contract.csv',index=False)
tickets=df.groupby('support_tickets_90d',as_index=False).churned.mean(); tickets['churn_rate_pct']=100*tickets.churned; tickets.to_csv(OUT/'churn_by_support_tickets.csv',index=False)
auto=df.groupby('autopay',as_index=False).churned.mean(); auto['churn_rate_pct']=100*auto.churned; auto.to_csv(OUT/'churn_by_autopay.csv',index=False)
plt.figure(figsize=(7,5)); plt.bar(contract.contract_type,contract.churn_rate_pct); plt.title('Churn Rate by Contract Type'); plt.ylabel('Churn Rate (%)'); plt.xticks(rotation=20); plt.tight_layout(); plt.savefig(OUT/'churn_by_contract.png',dpi=160); plt.close()
plt.figure(figsize=(7,5)); plt.scatter(df.tenure_months,df.monthly_charge,alpha=.15); plt.title('Customer Tenure vs Monthly Charge'); plt.xlabel('Tenure (months)'); plt.ylabel('Monthly Charge ($)'); plt.tight_layout(); plt.savefig(OUT/'tenure_vs_charge.png',dpi=160); plt.close()
print(summary.round(2).to_string(index=False))
