# California House Price Prediction

A GTC machine learning internship project that explores California housing data and provides a Streamlit interface for median house value estimation.

**Technology:** Python · LightGBM · scikit-learn · pandas · Streamlit

## Features

- Collect location, housing age, room and bedroom counts, population, households, income, and ocean proximity.
- Load the saved LightGBM model and display a median house value estimate.
- Compare linear, tree-based, ensemble, and neural regression models in the notebook.

## Repository guide

| Path | Purpose |
|---|---|
| [app.py](app.py) | Housing form and prediction output. |
| [california-house-price-prediction.ipynb](california-house-price-prediction.ipynb) | EDA and regression experiments. |
| [house_price_model_lgm.pkl](house_price_model_lgm.pkl) | Saved model. |
| [housing - housing.csv](housing%20-%20housing.csv) | Housing dataset. |
| [requirements.txt](requirements.txt) | Inference dependencies. |

## Requirements and current limitations

The app multiplies the model output by `100000` when displaying USD. Verify this target scaling and the manual ocean-proximity encoding against the training export before interpreting values.

The notebook uses a Kaggle path; change it to the included housing CSV for local execution. Its training dependencies include packages beyond the inference requirements. Estimates reflect the dataset and model, not current property valuations.

## Getting started

```bash
git clone https://github.com/IbrahimAbdelsattar/GTC-ML-Internship-California-House-Price-Prediction.git
cd GTC-ML-Internship-California-House-Price-Prediction
```

Use a Python virtual environment:

```bash
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\Activate.ps1` in PowerShell.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```
