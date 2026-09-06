from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model
with open("LinearRegressionModel.pkl", "rb") as file:
    model = pickle.load(file)

# Load car data
car = pd.read_csv("cleaned Car.csv")


@app.route("/")
def index():

    companies = sorted(car["company"].dropna().unique().tolist())

    car_models = sorted(car["name"].dropna().unique().tolist())

    years = sorted(
        [int(year) for year in car["year"].dropna().unique()],
        reverse=True
    )

    fuel_types = sorted(car["fuel_type"].dropna().unique().tolist())

    # Company ke according car models
    company_models = {}

    for company in companies:
        models = sorted(
            car[car["company"] == company]["name"]
            .dropna()
            .unique()
            .tolist()
        )

        company_models[company] = models

    return render_template(
        "index.html",
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_types=fuel_types,
        company_models=company_models,
        prediction=None
    )


@app.route("/predict", methods=["POST"])
def predict():

    company = request.form.get("company")
    car_model = request.form.get("car_model")
    year = request.form.get("year")
    fuel_type = request.form.get("fuel_type")
    kms_driven = request.form.get("kms_driven")

    try:

        year = int(year)
        kms_driven = int(kms_driven)

        # Input data
        input_data = pd.DataFrame(
            [[
                car_model,
                company,
                year,
                fuel_type,
                kms_driven
            ]],
            columns=[
                "name",
                "company",
                "year",
                "fuel_type",
                "kms_driven"
            ]
        )

        # Prediction
        prediction = model.predict(input_data)

        price = round(float(prediction[0]), 2)

        return render_template(
            "index.html",
            companies=sorted(car["company"].dropna().unique().tolist()),
            car_models=sorted(car["name"].dropna().unique().tolist()),
            years=sorted(
                [int(y) for y in car["year"].dropna().unique()],
                reverse=True
            ),
            fuel_types=sorted(car["fuel_type"].dropna().unique().tolist()),
            company_models={
                company: sorted(
                    car[car["company"] == company]["name"]
                    .dropna()
                    .unique()
                    .tolist()
                )
                for company in car["company"].dropna().unique()
            },
            prediction=price
        )

    except Exception as e:

        return render_template(
            "index.html",
            companies=sorted(car["company"].dropna().unique().tolist()),
            car_models=sorted(car["name"].dropna().unique().tolist()),
            years=sorted(
                [int(y) for y in car["year"].dropna().unique()],
                reverse=True
            ),
            fuel_types=sorted(car["fuel_type"].dropna().unique().tolist()),
            company_models={},
            prediction="Error: " + str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)