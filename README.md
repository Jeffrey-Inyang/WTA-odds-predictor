# WTA Odds Predictor

## Overview

WTA Odds Predictor is a Python desktop application that uses **Linear Regression** to estimate tennis betting odds based on player rankings and points.

The application loads historical data from a CSV file, trains a regression model, predicts odds for new inputs, and visualizes actual odds against predicted odds.

## Features

- **Load CSV:** Import historical tennis data.
- **Train Model:** Train a linear regression model using player rankings and points.
- **Predict New Odds:** Estimate odds from a player's ranking and points.
- **Plot Results:** Visualize actual odds against predicted odds.
- **Model Evaluation:** Display the model's coefficients, intercept, and mean squared error (MSE).

## Technologies Used

- Python 3.13
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Tkinter

## Project Structure

```text
prediction-model/
├── WTA LR pred.py
├── wta.csv
└── README.md
```

## Requirements

Install Python 3.13 or another compatible Python version.

The following libraries are required:

- pandas
- numpy
- matplotlib
- scikit-learn

Tkinter is also required for the graphical user interface. It is generally included with standard Windows Python installations.

## Installation

### 1. Clone or download the project

Place the Python script and CSV dataset in your project folder.

### 2. Open PowerShell

Navigate to the project directory. For example:

```powershell
cd "$HOME\Documents\prediction-model"
```

### 3. Install dependencies

Run:

```powershell
python -m pip install pandas numpy matplotlib scikit-learn
```

### 4. Verify the project files

Run:

```powershell
Get-ChildItem
```

Ensure that `WTA LR pred.py` and `wta.csv` are present in the project directory.

## Running the Application

Execute the following command in PowerShell:

```powershell
python ".\WTA LR pred.py"
```

The WTA Odds Predictor desktop window should open.

## How to Use

### Step 1: Load Historical Data

Click **Load CSV** and select `wta.csv`.

The dataset must contain the following columns:

| Column | Description |
|---|---|
| `Rank_1` | Ranking of player 1 |
| `Pts_1` | Points of player 1 |
| `Odd_1` | Historical odds for player 1 |

The application converts `Odd_1` to numeric values and removes rows with missing values in the selected columns.

### Step 2: Train the Model

Click **Train Model**.

The application fits a linear regression model using `Rank_1` and `Pts_1` to predict `Odd_1`.

The output includes:

- Rank coefficient
- Points coefficient
- Intercept
- Mean squared error (MSE)

### Step 3: Predict New Odds

Click **Predict New Odd**.

Enter the player's ranking and points when prompted. The application displays the estimated odds.

### Step 4: Plot Results

Click **Plot Results** to display a scatter plot comparing actual historical odds with model predictions. A reference line indicates where predicted values equal actual values.

## Model Description

The application uses multiple linear regression.

The prediction equation is:

\[
\widehat{Odd_1} = \beta_0 + \beta_1 Rank_1 + \beta_2 Pts_1
\]

Where:

- \(\widehat{Odd_1}\) is the predicted odds.
- \(\beta_0\) is the intercept.
- \(\beta_1\) is the coefficient for player ranking.
- \(\beta_2\) is the coefficient for player points.

The model estimates these coefficients from the historical dataset.

## Evaluation

The application calculates mean squared error (MSE) using the training data:

\[
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
\]

A lower MSE indicates smaller average squared prediction errors on the evaluated observations. Since the current implementation evaluates the model on its training data, this result does not independently measure performance on unseen matches.

## Troubleshooting

### Python cannot find the script

If you receive a `can't open file` error, verify your current directory:

```powershell
Get-Location
```

List its files:

```powershell
Get-ChildItem
```

Navigate to the directory containing the Python script, or run the script using its full path.

### Missing Python libraries

Install the required packages:

```powershell
python -m pip install pandas numpy matplotlib scikit-learn
```

### Missing CSV columns

Confirm that the CSV contains the exact column names:

```text
Rank_1
Pts_1
Odd_1
```

Column names are case-sensitive in the script.

### Tkinter errors

If Python reports that Tkinter is unavailable, install or repair a Python distribution that includes Tk support.

## Limitations

- Predictions use only player 1's ranking and points.
- The current model does not incorporate other match characteristics.
- Model evaluation uses the same observations used for training.
- Predictions are estimates and are not guarantees of betting outcomes.

## Disclaimer

This project is intended for educational and statistical analysis purposes. Predicted odds may differ from bookmaker odds and actual match outcomes. No betting profit is guaranteed.

## License

No license has been specified for this project. Add a license file if you intend to distribute the software publicly.
