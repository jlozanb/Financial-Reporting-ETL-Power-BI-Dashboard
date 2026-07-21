# Financial Reporging ETL & Power BI Dashboard
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![ETL & Data Transformation](https://img.shields.io/badge/ETL%20%26%20Data%20Transformation-6c757d)

## Overview

Financial data transformation workflow developed to convert accounting reports exported from Holded (Accounting Software) into structured datasets ready for financial analysis and Power BI dashboards.

The project processes raw Balance Sheet and financial reports from CSV files using Python, cleaning, transforming and restructuring accounting information into an analytical format suitable for Business Intelligence reporting.

The final output is integrated into Power BI to create interactive dashboards focused on financial reporting and business performance analysis.

## Features

- Financial data extraction from Holded CSV exports
- Data cleaning and transformation using Python
- Standardization of accounting information
- Preparation of structured datasets for Power BI
- Financial reporting dashboard development
- KPI visualization and business performance analysis

## Technologies

- Python
- Pandas
- Power BI
- ETL
- Financial Reporting
- Data Transformation

## Workflow

- Financial reports are exported from Holded in CSV format.
- Raw accounting data is processed and cleaned using Python.
- Financial datasets are transformed into a structured format suitable for analysis.
- The processed data is loaded into Power BI.
- Interactive dashboards are created to monitor financial performance indicators.

## Dashboard

The Power BI dashboard provides insights into:

- Profit & Loss analysis
- Balance Sheet overview
- Revenue and expense evolution
- Financial KPIs
- Business performance indicators

## Project Purpose

The objective of this project was to develop a structured ETL workflow capable of transforming raw accounting data from Holded into clean and reusable datasets for Business Intelligence reporting.

The project aims to improve data preparation processes, reduce manual transformation tasks and enable more efficient financial analysis through Power BI.

## Repository Contents

```
├── Code_Python
│ ├── Balance_Script.ipynb
│ └── Income_Script.ipynb
│ └── Readme.md
│
├── Data_Original
│  ├── Balance
│  │   └── Balance_2025.csv
│  │   └── Balance_2024.csv
│  │   └── Balance_2023.csv
│  │   └── Readme.md
│  ├── Income
│  │   └── Income_2025.csv
│  │   └── Income_2024.csv
│  │   └── Income_2023.csv
│  │   └── Readme.md
│
├── Data_Transformed
│  ├── Balance
│  │   └── Balance_2025_Transformed.csv
│  │   └── Balance_2024_Transformed.csv
│  │   └── Balance_2023_Transformed.csv
│  │   └── Readme.md
│  ├── Income
│  │   └── Income_2025_Transformed.csv
│  │   └── Income_2024_Transformed.csv
│  │   └── Income_2023_Transformed.csv
│  │   └── Readme.md
│
├── PowerBI
│ └── Balance_Dashboard.png
│ └── Income_Dashboard.png
│
└── README.md
```

## Author

Jorge Lozano



