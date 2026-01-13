# Renewable Energy & Solar Compliance Insights

## Executive Summary

#### Business Context

The transition to decentralised reneable energy has fundamentally disrupted the traditional one-way electricity distribution model. In high-penetration markets, the rapid scaling rooftop solar has introduced non-linear two-way power flows, creating significant challenges for voltafe stability and network reliability. 

Traditionally, distribution networks were built for predictable, centralised delivery; today, they function as complex, bi-directional ecosystems. This evolution has intorduced systemic complian risks, specifically volatfe breaches and thermal constraints, that vary significantly across diverse regional demographics and installation profiles. Managing these emerging risks at scale requires a shift form reactive maintenance to proactice, data-driven forecasting. By leveraging advance analytics to predict compliance failures before they occure, we aim to ensure grid safety while maximising the integration of renewable assets, to which is a critical requirement for the modern energy landscape. 


#### Core Business Question

**"Quantifying Grid Volatility: A Predictive Framework for Regional Solar Compliance Risk and Targeted Netwrok Intervention in High-Penetration Distributed Energy Markets."**

#### Summary of Insights

#### Recommendations and Next Steps


## Exploratory Data Analysis 
Visually diagnose the "Solar Complaince Gap" - the window where traditional grid management fails under high renewable penetration. Our analysis would be devised into 3 different direction:

1. Time (Duck Curve)
2. Economics (Volatility)
3. Seasonality

## Methodology
#### Feature Engineering & Determinant Discovery
Objective: Identify primary leading indicators for voltage compliance breaches (e.g., cloud-induced ramp rates, transformer saturation levels).

Data Ingestion: Aggregated 5-minute interval data from AEMMO(NEM) and BOM(Bureay of Meteorology) to correlate weather events with grid instability.

Technical focus: SQL window functions for time-lagged features, handling missing telemetry via interpolation, and feature importance ranking.

#### Predictive Modelling & Forecasting
Objective: Develop a robust classifier to forecast regional instbaility with a 24-hour lead time.

Model Selection: Implemented and compared XGBoost and Random forest regressors, optimised for high-dimensional time-series data.

Evaluation Metrics: Focused on Mean Absolute Error (MAE) and PRecision-Recall curves to minimised "false negatives" in grid safety alerts.

#### Market Impact & Strategy /simulation
Objetice: Quantify the reduction in "Value-at-Risk"(VaR) through model-driven targeted interventions.

Analysis: Back-tested a simulated "Dynamic Export Limit" strategy against history network outages.


## Technical Stack
* Languages: Python (Pandas, NumPy, Scikit-Learn), SQL
* Visualisation: Matplotlib, Seaborn, Tableau.
* Infrastructure: GitHub Actions (CI/CD), requirements.txt for environment consistency.


