# Online-Retail-Customer-and-Revenue-Analytics


Author: Tshiamo Medupe
Date: 04 September 2025
Project: Customer Behavior and Revenue Analysis

---
## Overview

This project analyzes the Online Retail transactional dataset to uncover insights into customer behavior and revenue dynamics. The goal is to transform raw data into actionable marketing and operational strategies. The analysis focuses on three core pillars:
	1.	Time-series revenue trends
	2.	Product and customer value concentration
	3.	RFM (Recency, Frequency, Monetary) segmentation for targeted retention and growth strategies

Python 3 and VS Code were used to perform all data cleaning, analysis, and visualization.

---

Features
	•	Monthly Revenue Analysis: Identifies seasonal trends and revenue volatility to inform promotions and engagement strategies.
	•	Customer Recency Analysis: Highlights engaged versus dormant customers for targeted campaigns.
	•	Customer Frequency & Monetary Analysis: Determines high-value and high-frequency customers to prioritize retention and upselling.
	•	Top Products & Customers: Identifies key revenue drivers.
	•	Integrated Strategic Recommendations: Provides actionable marketing, loyalty, and segmentation strategies.
	•	RFM Segmentation: Categorizes customers based on recency, frequency, and monetary value for personalized targeting.
---

Technical Details
	•	Data Cleaning:
	•	Removed duplicates and handled missing values
	•	Filtered negative or zero quantities
	•	Standardized pricing and calculated total purchase price
	•	Feature Engineering:
	•	Created TotalPrice = Quantity × Price
	•	Computed Recency, Frequency, Monetary metrics for RFM analysis
	•	Visualizations:
	•	Monthly revenue trends
	•	Revenue distribution
	•	Quantity distribution
	•	Customer recency, frequency, and monetary value histograms
	•	Scripts:
	•	rfm_analysis.py: Modular Python script for loading, cleaning, analyzing, and visualizing data
	•	Outputs:
	•	Cleaned dataset: online_retail_cleaned.csv
	•	Plots saved in plots/ folder (e.g., monthly_revenue_trend.png, rfm_recency.png)
---

Dependencies
	•	Python 3.x
	•	pandas
	•	numpy
	•	matplotlib
	•	seaborn
	•	datetime
	•	os

Install dependencies using:
```

pip install pandas numpy matplotlib seaborn
```

⸻

Usage
	1.	Place the raw dataset (online_retail_listing.csv) in the project folder.
	2.	Run the script:
```
python3 rfm_analysis.py
```

	
   3.	
 The script will output:
	•	Cleaned CSV: online_retail_cleaned.csv
	•	Plots in the plots/ folder
	•	Console output of top products and customers

---

Key Insights
	•	Revenue shows seasonal spikes, particularly around holidays.
	•	Top 5% of customers contribute ~60% of total revenue (Pareto principle).
	•	Majority of customers are low-frequency buyers; small subset are super-repeat buyers.
	•	RFM segmentation identifies VIP customers, dormant customers, and frequent buyers for tailored marketing strategies.

---

Recommendations
	1.	Diversify Revenue Streams: Reduce dependency on peak seasons.
	2.	Lapsed Customer Re-engagement: Launch targeted win-back campaigns.
	3.	Segmented Marketing: Use RFM segmentation for personalized promotions.
	4.	VIP Customer Management: Formalize high-value customer programs.
	5.	Analytical Monitoring: Automate RFM and revenue tracking for trend detection.

---

Contact

Author: Tshiamo Medupe
Email: medupet35@icloud.com

