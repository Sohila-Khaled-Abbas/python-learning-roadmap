# Fixture provenance

All records here are small, hand-authored **synthetic learning fixtures**. They are not Egyptian market observations, personal expenses, live prices, or PixelFed production records. EGP values are illustrative. No claim of realism or market representativeness is made.

`orders.csv` has seven input rows: three distinct valid orders, one identical duplicate, and three invalid rows. The reference load stores three orders totaling **36,175 piastres (361.75 EGP)**. A rerun inserts zero new rows. The raw order input stays unchanged. Header order is deliberately strict in this teaching contract.

`expenses.csv` has four unique expense rows: Food totals 200.00 EGP, Transportation 30.00 EGP, Education 250.00 EGP; overall total 480.00 EGP. These are the hand-check values for Build 01.

The optional API extension must add its own source, retrieval time, provider timestamp, freshness policy, and license/access notes. It must not label these fixtures as live data.
