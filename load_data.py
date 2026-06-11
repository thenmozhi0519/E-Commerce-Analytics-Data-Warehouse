import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres1234@localhost:5432/ecommerce_dw"
)

# Files and Target Tables
files = {
    "stg_customers": "olist_customers_dataset.csv",
    "stg_products": "olist_products_dataset.csv",
    "stg_orders": "olist_orders_dataset.csv",
    "stg_order_items": "olist_order_items_dataset.csv"
}

for table, file in files.items():

    print(f"\nLoading {file}...")

    # Extract
    df = pd.read_csv(file)

    print(f"Original Rows: {len(df)}")

    # -----------------------------
    # Transformations
    # -----------------------------

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle NULL values
    object_cols = df.select_dtypes(include="object").columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    df[object_cols] = df[object_cols].fillna("Unknown")
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # Customer-specific cleaning
    if table == "stg_customers":
        df["customer_city"] = df["customer_city"].str.title()

    # Orders-specific cleaning
    if table == "stg_orders":
        df["order_status"] = df["order_status"].str.lower()

    print(f"Rows After Cleaning: {len(df)}")

    # -----------------------------
    # Load
    # -----------------------------

    df.to_sql(
        name=table,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{table} loaded successfully!")

print("\nETL Process Completed!")

#pip install pandas sqlalchemy psycopg2-binary
#SQLAlchemy was used to establish database connections and load data into PostgreSQL tables.
#psycopg2 is the PostgreSQL driver that enables communication between Python and PostgreSQL.