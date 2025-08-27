# Full-Stack-Data-Pipeline-for-E-Commerce

**End-to-end data pipeline simulation** for a mid-sized e-commerce company. The project covers the entire workflow from raw data to actionable business insights, including ETL (Extract, Transform, Load) processes and front/back office analytics.

## 🎯 Project Goals

* **Simulate real-world e-commerce data flows** across orders, customers, sessions, and returns
* **ETL pipelines**: Extract, Transform, and Load data efficiently
* **Data-driven insights**: Generate reports and dashboards to support business decisions

## 📁 Project Structure

* **data/** – source CSV files:

  * `customers.csv`
  * `orders.csv`
  * `products.csv`
  * `returns.csv`
  * `support_tickets.csv`
  * `sessions.csv`
* **scripts/** – Python scripts for data cleaning, enrichment, and analysis:

  * `clean_orders.py`
  * `enrich_customers.py`
  * `analyze_sessions.py`
  * `kpi_generator.py`
* **report/** – reporting scripts and outputs:

  * `report_generator.py`
  * `summary_report.pdf`
* **README.md** – project documentation

## 🔧 Tech Stack

* **Python**: Pandas (data manipulation), Matplotlib (visualization), ReportLab (PDF reports)
* **ETL workflow**: data cleaning, enrichment, transformation, and aggregation

## 📊 Business Questions Addressed

* Which products are **most returned** and why?
* What is the **abandonment rate of carts** (users adding products to cart but not completing purchase)?
* When is **customer support overloaded** and which **channels** are most used (email, chat, phone)?
* Which **customer segments** generate the highest profitability?

## ✅ Deliverables

* **Clean, documented CSV datasets** ready for analysis
* **Python scripts** implementing ETL, KPIs, and data analysis
* **Summary reports** highlighting insights and metrics
