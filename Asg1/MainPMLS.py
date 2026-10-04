from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
import os


app = FastAPI(
    title="Skin Clinic Campaign Analysis API",
    description="Campaign analysis API for M10 PMLS Assignment 2.",
    version="2.0.0"
)


# Load dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILE = os.path.join(
    BASE_DIR,
    "skin clinic campaign.csv"
)

df = pd.read_csv(CSV_FILE)


# Convert campaign response to True/False
df["Responded"] = (
    df["Response_to_Campaign"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("yes")
)


# Calculate response rates
def response_rate_table(data, group_column):

    result = (
        data.groupby(group_column, observed=False)
        .agg(
            Total_Customers=("CustID", "size"),
            Responded=("Responded", "sum"),
            Response_Rate=("Responded", "mean")
        )
        .reset_index()
    )

    result["Response Rate (%)"] = (
        result["Response_Rate"] * 100
    ).round(2)

    result = result.drop(
        columns=["Response_Rate"]
    )

    return result


# Create analysis tables
gender_analysis = response_rate_table(
    df,
    "Gender"
)

age_analysis = response_rate_table(
    df,
    "AgeGroup"
)

purchase_analysis = response_rate_table(
    df,
    "Purchase_Last_Quarter"
)


# Create product usage groups
df["Product_Usage"] = pd.cut(
    df["Unique_Products_Purchased"],
    bins=[0, 4, 8, np.inf],
    labels=["1-4", "5-8", ">8"]
)

product_analysis = response_rate_table(
    df,
    "Product_Usage"
)


# Home page
@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <!DOCTYPE html>

    <html>

    <head>
        <title>M10 PMLS Assignment 2</title>
    </head>

    <body style="
        font-family: Arial;
        max-width: 900px;
        margin: 50px auto;
    ">

        <h1>M10 PMLS - Assignment 2</h1>

        <h2>Developing API For Excel</h2>

        <p>Skin Clinic Campaign Analysis</p>

        <hr>

        <h3>Campaign Analysis API</h3>

        <p>
            <a href="/campaign-analysis">
                View Campaign Analysis
            </a>
        </p>

        <p>
            The campaign analysis endpoint can be connected
            to Microsoft Excel using Power Query.
        </p>

        <h3>API Documentation</h3>

        <p>
            <a href="/docs">
                View FastAPI Documentation
            </a>
        </p>

    </body>

    </html>
    """


# Campaign analysis for Excel
@app.get("/campaign-analysis")
def campaign_analysis():

    return {
        "Gender_vs_Campaign_Response":
            gender_analysis.to_dict(
                orient="records"
            ),

        "Age_Group_vs_Campaign_Response":
            age_analysis.to_dict(
                orient="records"
            ),

        "Purchase_Last_Quarter_vs_Campaign_Response":
            purchase_analysis.to_dict(
                orient="records"
            ),

        "Product_Usage_vs_Campaign_Response":
            product_analysis.to_dict(
                orient="records"
            )
    }


# Run locally
if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "MainPMLS:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )