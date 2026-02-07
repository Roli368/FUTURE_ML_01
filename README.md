# Sales Forecasting System

## Overview
This project builds a time-series forecasting model to predict future sales using historical business data from the `Sample - Superstore` dataset. It utilizes a **SARIMA** (Seasonal AutoRegressive Integrated Moving Average) model to capture trends and seasonality, visualizing the results with actionable confidence intervals using **Matplotlib**.

## Objectives
-   **Data Processing**: Clean and preprocess raw transaction data into monthly time-series.
-   **Analysis**: Analyze historical sales trends and seasonality.
-   **Modeling**: Develop a SARIMA model for 12-month sales forecasting.
-   **Visualization**: Visualize forecasts and confidence intervals for business planning.

## Project Structure
-   `data/`:
    -   `Sample - Superstore.csv`: Raw dataset.
    -   `processed_superstore.csv`: Cleaned transactional data.
    -   `monthly_sales.csv`: Aggregated monthly data used for modeling.
-   `notebooks/`:
    -   `eda.ipynb`: Exploratory Data Analysis (Trends, Seasonality, Decomposition).
    -   `modeling.ipynb`: Model training, evaluation (MAE/RMSE), and parameter tuning.
    -   `visualization_matplotlib.ipynb`: Advanced visualization of the 12-month forecast with confidence intervals.
-   `src/`:
    -   `data_loader.py`: Script for data cleaning, feature engineering, and aggregation.

## Setup & Usage
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run Data Pipeline** (Optional, data is already processed):
    ```bash
    python src/data_loader.py
    ```
3.  **View Results**:
    -   Open `notebooks/visualization_matplotlib.ipynb` to see the latest forecasts and plots.
    -   Explore `notebooks/eda.ipynb` for historical insights.

## Key Outcomes
-   **Model**: SARIMA(1,1,1)(1,1,1,12)
-   **Metrics**: Evaluated using Mean Absolute Error (MAE) and RMSE.
-   **Forecast**: 12-month future sales prediction with 95% confidence intervals.
