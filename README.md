### Project Overview
This project aims to build a machine learning model for predicting house prices. It uses various features to train different models and provides accurate predictions, along with model evaluation.

### Features
- Built with Python and Jupyter Notebooks.
- Implements data preprocessing and multiple machine learning models.
- Streamlit GUI for user interaction and visualization.

### Usage
To run the program, follow these steps:

1. Open a terminal and navigate to the directory containing `Main.py` (e.g., `cd c:\house`).
2. Run the following command:
   ```bash
   streamlit run filename.py
   ```
This will launch the app in your default web browser.

### Necessary Packages (if needed)
- `streamlit`
- `pickle`
- `scikit-learn` (`sklearn`)

### Importing Libraries and Defining Functions
First, the necessary libraries for data manipulation (pandas, numpy), visualization (matplotlib), machine learning (sklearn), and statistical analysis (scipy) are imported. The `Plot_features` function is used to visualize the feature importance based on the model's results.

### Data Loading and Preprocessing
- The dataset is loaded, and several new features are created:
  - `Rooms_per_Household`
  - `Bedrooms_per_Household`
  - `Population_Density`
  - `Income_per_Person`
  - `Bedrooms_per_Room`
- The data is sorted by `Median_Income` and columns are reordered for consistency.
  
### Feature Scaling and Balancing
- Features (X) and target (y) are separated. 
- `RandomOverSampler` is used to balance the data.
- `StandardScaler` is applied to normalize the features, and a new DataFrame is created with the normalized data.

### Outlier Removal
Outliers are identified using Z-scores and removed to ensure the data is clean for model training.

### Models Used
- **Linear Regression**  
  A Linear Regression model is trained and evaluated using Mean Squared Error (MSE) and Mean Absolute Error (MAE).
  
- **Random Forest Regressor**  
  A Random Forest Regressor model is trained with hyperparameter tuning using `GridSearchCV` to find the best model parameters.
  
- **Decision Tree Regressor**  
  A Decision Tree Regressor model is trained with hyperparameter tuning using `RandomizedSearchCV`.

### Model Comparison
The performance of the three models is compared and visualized in a bar chart to determine which one performs the best.

In summary, this project provides a comprehensive approach to predicting house prices by creating new features, balancing and normalizing the data, removing outliers, and employing multiple machine learning models with hyperparameter tuning. The final step compares the models' performances to select the best one for predictions.

### Team Members  
- [Mohammad Hossein Khojoii](https://github.com/Khojoii) 
- [Amir Salajegheh](https://github.com/AmirSalajegheh) 
- [Hossein Arabpor](https://github.com/hozzeyn00) 

