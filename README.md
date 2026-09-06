# Car-Price-Predictor
Real world projects

1. Introduction
Used-car pricing depends on several characteristics such as vehicle model, manufacturer, manufacturing year, usage and fuel type. Because these factors interact in a non-trivial way, a data-driven prediction model can help estimate an expected resale price from historical listings.
The provided notebook, named Quikr_Predictor.ipynb, implements a complete basic machine-learning workflow: data loading, inspection, cleaning, feature preparation, categorical encoding, train-test splitting, model training, evaluation, repeated validation through different random splits, model persistence and a sample prediction.

2. Problem Statement
The problem addressed in this project is to predict the selling price of a used car from information available in a listing. The task is a supervised machine-learning regression problem because the output, Price, is a continuous numeric value.

3. Objectives
The project objectives, as supported by the notebook workflow, are:
• Load and inspect the Quikr car dataset.
• Identify data-quality problems in the raw columns.
• Clean and convert year, Price and kms_driven into usable numeric values.
• Handle the missing fuel_type record.
• Reduce the complexity of the name feature by retaining its first three words.
• Encode categorical variables for machine learning.
• Train a Linear Regression model.
• Evaluate the model using the R² metric.
• Examine model performance across 1,000 train-test random splits.
• Select the split giving the highest observed R² in the notebook.
• Save the trained pipeline as a pickle file.

4. Data Cleaning and Preprocessing
The cleaning sequence is:
1. A backup copy of the original DataFrame is created.

2. Rows whose year is not numeric are removed using str.isnumeric().

3. year is converted from object to integer.

4. Rows with Price equal to "Ask For Price" are removed.

5. Commas are removed from Price and the column is converted to integer.

6. kms_driven is split at the space so that the numeric portion is retained.

7. Commas are removed from kms_driven.

8. Rows whose cleaned kms_driven value is not numeric are removed.

9. kms_driven is converted to integer.

10. The notebook identifies one missing fuel_type value and removes that row.

5. Model Training
The selected regression algorithm is LinearRegression from scikit-learn. The model is placed after the ColumnTransformer inside a Pipeline. This design is useful because the same preprocessing operations are automatically applied when the model is trained and when new data is passed to predict().

6. Model Evaluation
The notebook evaluates predictions using R² (coefficient of determination).

For the first train-test split, the recorded R² score is:
R² = 0.5433072823679849

7. Sample Prediction
The notebook demonstrates prediction for the following input:

Name: Maruti Suzuki Swift

Company: Maruti

Year: 2019

Kms driven: 100

Fuel type: Petrol

The trained pipeline predicts:
Estimated Price ≈ ₹4,58,894.11



Interface of  this Project-

<img width="597" height="627" alt="Screenshot 2026-09-06 171506" src="https://github.com/user-attachments/assets/7ee63064-a2d4-4649-adfb-9652b66c3aa8" />



And After filling all details the model calculated car price like this-

<img width="588" height="697" alt="Screenshot 2026-09-06 171614" src="https://github.com/user-attachments/assets/b770d8e7-30d5-441f-98bc-34c5ee248bfc" />


And also I am used html, CSS, python.... code

1. Technology Stack
Backend: Python with Flask.

Machine Learning model: previously trained Linear Regression pipeline.

Data handling: pandas.

Model persistence: pickle.

Frontend: HTML with CSS.

Client-side interaction: JavaScript.

Template rendering: Flask/Jinja2.


2. Backend File — application.py

The application imports Flask, render_template and request from flask, along with pickle, pandas and NumPy. A Flask application object is created.

The saved model is loaded from LinearRegressionModel.pkl using pickle. The cleaned vehicle dataset is loaded from cleaned Car.csv using pandas. These files are therefore dependencies of the web application.

3. Home Route

The root route "/" is handled by the index() function. It reads unique companies, car models, years and fuel types from the cleaned dataset. Years are converted to integers and sorted in reverse order.

The backend also constructs a company_models dictionary. For each company, it collects the available car models belonging to that company. These values are passed to index.html through render_template along with prediction=None.

4. Prediction Route

The /predict route accepts POST requests. It reads five form values: company, car_model, year, fuel_type and kms_driven.

Year and kms_driven are converted to integers. A one-row pandas DataFrame is then created with the exact feature columns expected by the saved model: name, company, year, fuel_type and kms_driven. The model.predict() method generates the predicted price, which is converted to float and rounded to two decimal places.

The prediction is then returned to the HTML template so the user can see the result.

5. Frontend — index.html

The frontend page is titled "Car Price Predictor". It uses a centered white container with CSS styling, form controls, a prediction-result area and an error-result area.

The form submits data to /predict using the POST method. The interface includes:
• Select Company
• Select Car Model
• Select Year
• Select Fuel Type
• KMs Driven numeric input
• Predict Price button

6. End-to-End Working

Step 1: User opens the home page.
Step 2: Flask loads company, model, year and fuel-type options from cleaned Car.csv.
Step 3: User selects a company.
Step 4: JavaScript updates the car-model dropdown according to the selected company.
Step 5: User selects model, year and fuel type and enters KMs driven.
Step 6: The form sends a POST request to /predict.
Step 7: Flask reads and converts the submitted values.
Step 8: Flask creates a pandas DataFrame in the model's expected feature order.
Step 9: The saved ML pipeline generates the price prediction.
Step 10: Flask renders index.html again with the prediction.
Step 11: The predicted price is displayed to the user.

















