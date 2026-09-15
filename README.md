# Customer Churn Analysis

Customer churn analysis using Python, exploratory data analysis, and predictive modeling.

## Project Overview

This project analyzes customer churn using the Telco Customer Churn dataset. The goal is to identify customer characteristics associated with churn, compare predictive modeling approaches, and translate model results into a practical customer retention framework.

The analysis includes data cleaning, exploratory analysis, feature interaction analysis, predictive modeling, threshold tuning, cross-validation, and customer risk segmentation.

## Dataset

The project uses the Telco Customer Churn dataset, originally published as an IBM sample dataset and accessed through Kaggle.

The dataset contains 7,043 customer records and includes information about:

- customer demographics
- account tenure
- contract type
- subscribed services
- payment method
- monthly and total charges
- customer churn status

The raw dataset is stored in:

`data/raw/`

A cleaned version used for downstream analysis is stored in:

`data/processed/`

## Project Structure

```text
customer-churn-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_analysis.ipynb
│   └── 03_churn_modeling.ipynb
├── outputs/
│   ├── figures/
│   └── model_results/
├── src/
│   ├── data_cleaning.py
│   └── feature_engineering.py
├── README.md
└── requirements.txt
'''markdown

## Analysis Workflow

### 1. Data Exploration

The first notebook reviews data quality and explores relationships between customer characteristics and churn.

Key areas examined include:

- contract type
- tenure
- monthly charges
- internet service
- payment method
- support services

### 2. Feature Analysis

The second notebook examines how important customer characteristics interact with one another.

Examples include:

- contract type and tenure
- monthly charges and internet service
- payment method and contract type

### 3. Predictive Modeling

The third notebook compares logistic regression and random forest models.

Model performance was evaluated using:

- accuracy
- precision
- recall
- F1 score
- ROC-AUC

Logistic regression produced the stronger overall results.

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| --- | ---: | ---: | ---: | ---: | ---: |
| Logistic Regression | 80.6% | 65.9% | 55.9% | 60.5% | 84.2% |
| Random Forest | 78.2% | 61.4% | 48.1% | 54.0% | 82.1% |

Five-fold cross-validation produced an average ROC-AUC of approximately **0.846**, suggesting that logistic regression performance was reasonably stable across different training samples.

## Threshold Tuning

Because identifying customers at risk of churn is important for retention efforts, the logistic regression classification threshold was evaluated below the default value of 0.50.

Using a threshold of **0.40** increased churn recall from approximately **55.9% to 66.8%**, while reducing precision.

This provides a different tradeoff for situations where identifying more potential churners is more important than minimizing false positives.

## Customer Risk Segmentation

Predicted churn probabilities were grouped into three customer risk tiers:

| Risk Tier | Customers | Actual Churn Rate |
| --- | ---: | ---: |
| Low | 865 | 10.5% |
| Medium | 335 | 39.7% |
| High | 209 | 71.8% |

The high-risk segment showed a much greater concentration of actual churners, making the model output useful for prioritizing customer retention outreach.

## Key Findings

Several characteristics were consistently associated with higher churn risk:

- month-to-month contracts
- shorter customer tenure
- fiber optic internet service
- electronic check payment
- lack of online security or technical support

The high-risk customer segment was especially concentrated among newer, month-to-month fiber optic customers using electronic checks.

## Business Recommendations

The analysis suggests several potential retention strategies:

- prioritize outreach to customers with high predicted churn probabilities
- focus early retention efforts on newer customers
- pay particular attention to month-to-month customers
- review the customer experience for fiber optic subscribers
- consider incentives for longer-term contracts or automatic payment methods
- use model-generated risk scores to prioritize limited retention resources

These relationships identify patterns associated with churn but should not be interpreted as direct causes.

## Technologies Used

- Python
- pandas
- NumPy
- Matplotlib
- scikit-learn
- Jupyter Notebook
- Git
- GitHub

## Repository Outputs

The project generates:

- cleaned customer data
- model performance results
- customer-level churn probabilities and risk tiers
- model comparison visualizations
- churn risk segmentation visualizations

These outputs are stored in the `outputs/` directory.

## How to Run

1. Clone the repository.

2. Create and activate a Python virtual environment.

3. Install the required packages:

    pip install -r requirements.txt

4. Run the notebooks in order:

    01_data_exploration.ipynb
    02_feature_analysis.ipynb
    03_churn_modeling.ipynb

## Potential Next Steps

Possible extensions to this project include:

- additional model tuning
- testing additional classification algorithms
- customer-level retention cost analysis
- incorporating retention campaign response data
- deploying the model as a scoring pipeline