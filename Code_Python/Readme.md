# Python ETL Scripts

## Overview

This folder contains the Python notebooks used to transform and structure accounting data exported from Holded before importing it into Power BI.

## Usage

1. Select the Holded CSV file to transform.
2. Select the reporting period type:
   - Annual
   - Quarterly

The selected period is used to classify the financial data and allows Power BI dashboards to distinguish between annual and quarterly analysis.

3. Run the notebook.
4. The transformed CSV file will be generated and can be manually imported into Power BI.

## Notebooks

### Balance Sheet Transformation

Transforms Holded Balance Sheet reports by cleaning and restructuring accounting data into an analysis-ready format.

### Income Statement Transformation

Transforms Holded Profit & Loss reports by organizing income and expense information into a structured dataset.
