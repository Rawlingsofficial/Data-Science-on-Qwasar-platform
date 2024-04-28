

# Wine Price Prediction

Welcome to the Wine Price Prediction project! This project aims to predict wine prices based on various features such as rating, number of ratings, year, and style. We'll explore the dataset, preprocess the data, analyze correlations, and train machine learning models to make predictions.

## Libraries Used

We utilized several Python libraries for data analysis, visualization, and machine learning:

- [Plotly](https://plotly.com/)
- [Seaborn](https://seaborn.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [CatBoost](https://catboost.ai/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [LightGBM](https://lightgbm.readthedocs.io/en/latest/)

  # Additional Resources

- [Blog Post](https://medium.com/@rawlingsofficial300/my-vivivno-9b85d08052ce)
- [Presentation](https://www.canva.com/design/DAFsOBpadDk/je5Jb0B893FSJSaxWg8OJQ/edit?utm_content=DAFsOBpadDk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


## Project Overview

### Data Collection and Cleaning

We collected wine data from the Vivino dataset and performed data-cleaning tasks such as removing irrelevant columns, converting data types, and handling missing values.

### Exploratory Data Analysis

We explored the dataset's characteristics, including its shape, descriptive statistics, and information about the data. Additionally, we visualized the distribution of wine prices, ratings, and other features.

```python
# Visualize the distribution of wine prices
plt.figure(figsize=(10, 6))
sns.histplot(data=my_wine_data, x='Price', bins=30, kde=True)
plt.title('Distribution of Wine Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()
```

## Data Collection and Cleaning

```python
# Read the dataset
my_wine_data = pd.read_csv("Vivino_dataset.csv")

# Display the first few rows of the dataset
print(my_wine_data.head())

# Check for missing values
print("Columns with missing values:")
print(my_wine_data.isnull().sum())

# Drop irrelevant columns
my_wine_data = my_wine_data.drop(["Name", "Unnamed: 0"], axis=1)
```


### Feature Engineering and Encoding

We preprocessed the data by encoding categorical variables using one-hot encoding and label encoding techniques to prepare it for model training.

### Correlation Analysis

We analyzed the correlations between different features using scatterplot matrices and correlation heatmaps to identify relationships and patterns in the data.

### Machine Learning Model Training

We trained machine learning models, including LightGBM Regressor, to predict wine prices based on the selected features.
```python
# Prepare features and target
X = my_wine_data[['Rating', 'NumberOfRatings', 'Year', 'Style']]
y = my_wine_data['Price']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LGBMRegressor(n_estimators=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
```
## Usage

To use this project:
```python
# Clone the repository
git clone https://github.com/yourusername/your-repo.git

# Navigate to the project directory
cd your-repo

# Install dependencies
pip install -r requirements.txt

# Run Jupyter Notebooks
jupyter notebook

```

1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the Jupyter Notebook files in the `notebooks` directory to explore the project and make predictions.

## Contributor

- [Mbah Rawling Mukhen](https://github.com/Rawlingsofficial/)

## License

This project is licensed under the [MIT License](LICENSE).


### Made At
<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
