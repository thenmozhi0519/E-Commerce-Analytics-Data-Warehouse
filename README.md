# E-Commerce Analytics Data Warehouse

## Project Overview

This project demonstrates the end-to-end design and implementation of a Data Warehouse for E-Commerce Analytics using PostgreSQL, Python, and Power BI.

The solution follows a modern Data Engineering workflow:

Raw CSV Data → Python ETL → PostgreSQL Staging Layer → Star Schema Data Warehouse → SQL Analytics Views → Power BI Dashboard

The objective is to transform raw transactional data into meaningful business insights through dimensional modeling, ETL pipelines, advanced SQL analytics, and interactive dashboards.

---

# Technologies Used

* PostgreSQL
* Python
* Pandas
* SQLAlchemy
* Psycopg2
* Power BI
* SQL (CTE, Window Functions, Views)

---

# Dataset

Brazilian E-Commerce Public Dataset (Olist)

Files Used:

* customers
* products
* orders
* order_items

Total Records Processed: 100,000+

---

# Project Architecture

CSV Files
↓
Python ETL
↓
Staging Tables
↓
Dimension Tables
↓
Fact Table
↓
Business Views
↓
Power BI Dashboard

---

# Step 1: Staging Layer

Purpose:

The staging layer stores raw data exactly as received from source files before applying business transformations.

Tables:

* stg_customers
* stg_products
* stg_orders
* stg_order_items

Why Staging?

* Preserves raw source data
* Simplifies ETL process
* Allows data validation
* Supports data reprocessing

Example:

CSV Data
↓
stg_customers

No business logic is applied at this stage.

---

# Step 2: Python ETL Pipeline

Purpose:

Automate data ingestion and basic data cleaning before loading into PostgreSQL.

Libraries Used:

* Pandas
* SQLAlchemy
* Psycopg2

Transformations Performed:

1. Duplicate Removal

Removed duplicate records using:

drop_duplicates()

Why?

Prevents duplicate business transactions.

---

2. Null Value Handling

String Columns:

Filled missing values with:

"Unknown"

Numeric Columns:

Filled missing values with:

0

Why?

Prevents NULL-related issues during reporting.

---

3. Data Standardization

Customer city names standardized.

Example:

chennai → Chennai

Why?

Ensures consistent reporting.

---

4. Automated Loading

Data loaded directly into PostgreSQL staging tables using:

to_sql()

Benefits:

* No manual imports
* Repeatable ETL process
* Easy automation

---

# Step 3: Star Schema Design

Purpose:

Optimize analytical querying and reporting.

Star Schema Components:

Dimension Tables

* dim_customers
* dim_products
* dim_date

Fact Table

* fact_orders

---

# Why Star Schema?

Advantages:

* Fast analytics
* Simple joins
* Easy reporting
* Widely used in Data Warehousing

Structure:

dim_customers
|
dim_products
|
fact_orders
|
dim_date

---

# Step 4: Loading Warehouse Tables

Purpose:

Move cleaned data from staging layer into dimensional model.

Process:

staging tables
↓
INSERT INTO
↓
dimension tables
↓
fact table

Example:

dim_customers populated from stg_customers

fact_orders populated using:

* stg_orders
* stg_order_items
* dim_date

---

# Step 5: Advanced SQL Analytics

Purpose:

Create reusable business logic for reporting.

---

1. DATE_TRUNC()

Used For:

Monthly revenue analysis.

Example:

DATE_TRUNC('month', full_date)

Why?

Groups transactions by month.

---

2. Window Functions

Used For:

Running revenue calculations.

Example:

SUM(revenue)
OVER(ORDER BY month)

Why?

Tracks cumulative business growth.

---

3. LAG()

Used For:

Previous month comparison.

Example:

LAG(revenue)

Why?

Measures month-over-month growth.

---

4. ROW_NUMBER()

Used For:

Customer ranking.

Example:

ROW_NUMBER()
OVER(ORDER BY revenue DESC)

Why?

Identifies top customers.

---

5. CTE (Common Table Expression)

Used For:

Breaking complex queries into readable components.

Example:

WITH monthly_revenue AS (...)

Why?

Improves readability and maintenance.

---

# Business Views Created

1. vw_monthly_revenue

Purpose:

Monthly revenue reporting.

---

2. vw_running_revenue

Purpose:

Cumulative revenue tracking.

Features:

Window Function

---

3. vw_revenue_growth

Purpose:

Month-over-month revenue analysis.

Features:

LAG()

---

4. vw_top_customers

Purpose:

Identify highest revenue customers.

Features:

ROW_NUMBER()

---

5. vw_product_contribution

Purpose:

Measure product contribution percentage.

Features:

Window Function

---

# Step 6: Power BI Dashboard

Purpose:

Visualize business performance.

Dashboard 1: Executive Dashboard

KPIs:

* Total Revenue
* Total Orders
* Monthly Revenue Trend

Target Audience:

Business Executives

---

Dashboard 2: Advanced SQL Analytics

Visuals:

* Running Revenue Trend
* Revenue Growth Analysis
* Top Customers
* Product Contribution %

Target Audience:

Business Analysts

---

# Key Business Insights

Revenue Trends

Track monthly sales performance.

Customer Insights

Identify high-value customers.

Product Analytics

Measure product contribution to overall revenue.

Growth Analysis

Compare current month revenue with previous month.

---

# Project Outcomes

Designed a Star Schema Data Warehouse.

Built automated ETL pipelines using Python.

Processed 100K+ records.

Implemented advanced SQL analytics.

Created Power BI dashboards for business reporting.

Applied CTEs, Window Functions, DATE_TRUNC, and LAG.

Delivered end-to-end Data Engineering workflow.

---
