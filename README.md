# Netflix Dataset: Cleaning and Preprocessing

##  Objective
The goal of this project was to clean and preprocess the "Netflix Movies and TV Shows" dataset from Kaggle. The process involved handling missing values, removing duplicates, and standardizing data formats to prepare the data for analysis.

##  Tools Used
- Python (3.x)
- Pandas library

##  Cleaning Process
The raw dataset was cleaned using a Python script that performed the following steps:

1.  **Handled Missing Values**:
    -   Replaced missing values in the **`director`** and **`country`** columns with `"Unknown"`.
    -   Filled missing **`cast`** information with `"Not Available"`.
    -   Dropped rows where the **`title`** was missing.

2.  **Removed Duplicates**:
    -   Checked for and removed any fully duplicate records to ensure data integrity.

3.  **Standardized Data & Formats**:
    -   Converted the **`type`** column values to lowercase (e.g., `Movie` → `movie`).
    -   Transformed the **`date_added`** column into a standard `datetime` format.
    -   Ensured the **`release_year`** column was stored as an `integer`.

4.  **Renamed Columns**:
    -   Standardized all column names to lowercase with underscores for easier access (e.g., `Show ID` → `show_id`).

## 🚀 How to Run
To reproduce the results, run the Python script from your terminal:
```bash
python netflix_cleaning.py
