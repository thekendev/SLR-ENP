# SLR-ENP: Electricity Price Prediction Using Linear Regression

## Overview

**SLR-ENP** is an end-to-end machine learning project that predicts average electricity prices for the non-domestic sector. It provides actionable insights for stakeholders by analyzing historical temporal and consumption-based data, enabling informed decisions about pricing trends, energy distribution, and market strategy.

The project implements the full ML lifecycle, from data collection and preprocessing to model training, evaluation, and deployment on Hugging Face Spaces.

---

## Table of Contents

- [Project Workflow](#project-workflow)
- [Problem Statement](#problem-statement)
- [Solution Approach](#solution-approach)
- [Data Collection](#data-collection)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Data Preprocessing & Feature Engineering](#data-preprocessing--feature-engineering)
- [Model Training & Evaluation](#model-training--evaluation)
- [Deployment](#deployment)
- [Tools & Technologies](#tools--technologies)
- [Key Insights](#key-insights)
- [License](#license)

---

## Project Workflow

The TEMPLE project follows a complete machine learning lifecycle:

1. Understanding the problem
2. Data collection
3. Data validation and exploratory data analysis (EDA)
4. Data preprocessing and feature engineering
5. Model training and evaluation
6. Model deployment
7. Continuous integration and deployment (CI/CD) for updates

---

## Problem Statement

Electricity pricing is dynamic and influenced by temporal factors such as seasons, years, and consumption scales. Stakeholders often struggle to understand how these factors impact average electricity costs, making forecasting and strategic decisions challenging.

---

## Solution Approach

- **Predictive Model:** Linear Regression to forecast average electricity prices.  
- **Predictors:** Year, Quarter, and electricity pricing across multiple consumer categories (Very Small → Extra Large).  
- **Target Variable:** `Electricity: Average (Pence per kWh)`  
- **Goal:** Provide an interpretable model that informs energy pricing and strategy.

---

## Data Collection

- **Source:** [UK Government Energy Data](https://www.gov.uk/government/statistical-data-sets/gas-and-electricity-prices-in-the-non-domestic-sector)  
- **Size:** 82 rows, 16 columns  
- **Focus:** Electricity pricing for multiple consumer categories

---

## Exploratory Data Analysis (EDA)

- **Univariate Analysis:** Distribution of electricity prices across categories and years.  
- **Bivariate Analysis:** Variation in electricity prices across quarters and consumer categories.  
- **Outlier Detection:** Identified high variability in small consumer categories.  
- **Missing Values:** Dropped rows with missing `Electricity: Extra Large` values.  
- **Visualization:** Boxplots, line plots, histograms, and heatmaps used to uncover trends and correlations.

---

## Data Preprocessing & Feature Engineering

- Dropped irrelevant gas-related columns.  
- Converted `Quarter` into numeric values (1–4).  
- Aggregated electricity prices across categories to create `Avg_Electricity_Price`.  
- Converted `Year` to categorical for modeling purposes.  
- Checked for duplicates, missing values, and correlations among numeric features.

---

## Model Training & Evaluation

- **Algorithm:** Linear Regression  
- **Process:**  
  1. Train-test split  
  2. Model fitting and prediction  
  3. Evaluation using metrics like RMSE, MAE, and R²  
- **Outcome:** Accurate prediction of average electricity prices based on temporal and category-based features.

---

## Deployment

- **Platform:** Hugging Face Spaces  
- **Web API:** Implemented using FastAPI and Streamlit for interactive UI  
- **Containerization:** Docker for consistent deployment  
- **CI/CD:** Automated pipelines for continuous testing and deployment  
- **Access:** Stakeholders can query the model via Hugging Face spaces UI for predictions [here](https://huggingface.co/spaces/kanayojustice/Deployment-slr-enp-HF)

---

## Tools & Technologies

- **Programming:** Python  
- **Data Manipulation & Analysis:** pandas, numpy  
- **Visualization:** matplotlib, seaborn  
- **Machine Learning:** scikit-learn (Linear Regression)  
- **Web & Deployment:** FastAPI, Streamlit, Hugging Face Spaces, Docker  
- **CI/CD:** GitHub Actions  
- **Configuration & Management:** YAML, Excel  

---

## Key Insights

- Electricity prices decrease as consumer size increases (economies of scale).  
- Yearly trends show fluctuations influenced by temporal factors.  
- Outliers exist, particularly in small consumer categories.  
- The model provides transparent, interpretable insights for stakeholders.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
