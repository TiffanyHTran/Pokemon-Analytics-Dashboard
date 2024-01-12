# Pokemon Analytics Dashboard

This project includes three main files: `etl_pipeline.py`, `data_warehouse.py`, and `real_time_dashboard.py`, each serving a specific purpose in building a Pokemon Analytics Dashboard.

## 1. ETL Pipeline (etl_pipeline.py)

### Overview
- **Extracts Data:** Utilizes the Pokemon dataset (`pokemon.csv`) to extract information.
- **Transformation:** Creates a new column 'Total' as the sum of Pokemon stats.
- **Loading:** Loads the transformed data into an SQLite database.

### How to Run
bash
python etl_pipeline.py

## 2. Data Warehousing (data_warehouse.py)

### Overview
- **Data Transformation:** Restructures Pokemon data into a data warehouse with dimension and fact tables.
- **Dimension Tables:** Creates tables for Pokemon, types, and stats.
- **Merging Data:** Combines data to form a fact table for analytics.
- **Database Loading:** Loads the data warehouse into an SQLite database.

### How to Run
python data_warehouse.py
