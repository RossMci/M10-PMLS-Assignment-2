# ============================================================
# M10 PMLS - ASSIGNMENT 1
# Model Deployment Using FastAPI
# Skin Clinic Marketing Campaign Analysis
# ============================================================

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
import uvicorn
import webbrowser
import threading


# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Skin Clinic Campaign Analysis",
    description=(
        "Analysis of customer response to the "
        "Skin Clinic marketing campaign."
    ),
    version="1.0"
)


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("skin clinic campaign.csv")


# ============================================================
# RESPONSE RATE FUNCTION
# ============================================================

def response_rate_table(data, group_column):

    temp = data.copy()

    # Convert Yes/No response into True/False
    temp["Responded"] = (
        temp["Response_to_Campaign"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
    )

    # Calculate total customers, responses and response rate
    result = (
        temp.groupby(group_column, observed=False)
        .agg(
            Total_Customers=("CustID", "size"),
            Responded=("Responded", "sum"),
            Response_Rate=("Responded", "mean")
        )
        .reset_index()
    )

    # Convert response rate to percentage
    result["Response Rate (%)"] = (
        result["Response_Rate"] * 100
    ).round(2)

    # Remove temporary decimal response rate
    result = result.drop(columns=["Response_Rate"])

    return result


# ============================================================
# TASK 1
# GENDER VS CAMPAIGN RESPONSE
# ============================================================

gender_analysis = response_rate_table(
    df,
    "Gender"
)


# ============================================================
# TASK 2
# AGE GROUP VS CAMPAIGN RESPONSE
# ============================================================

age_analysis = response_rate_table(
    df,
    "AgeGroup"
)

# Put age groups in the assignment's required order
age_order = ["<30", "30-50", ">50"]

# Only reorder if the labels in the dataset match
if set(age_order).issubset(set(age_analysis["AgeGroup"].astype(str))):
    age_analysis["AgeGroup"] = pd.Categorical(
        age_analysis["AgeGroup"],
        categories=age_order,
        ordered=True
    )

    age_analysis = (
        age_analysis
        .sort_values("AgeGroup")
        .reset_index(drop=True)
    )


# ============================================================
# TASK 3
# PURCHASE IN LAST QUARTER VS CAMPAIGN RESPONSE
# ============================================================

purchase_analysis = response_rate_table(
    df,
    "Purchase_Last_Quarter"
)


# ============================================================
# TASK 4
# PRODUCT USAGE VS CAMPAIGN RESPONSE
# ============================================================

# Create product usage categories:
# 1-4 products
# 5-8 products
# More than 8 products

df["Product_Usage"] = pd.cut(
    df["Unique_Products_Purchased"],
    bins=[0, 4, 8, np.inf],
    labels=["1-4", "5-8", ">8"]
)

product_analysis = response_rate_table(
    df,
    "Product_Usage"
)


# ============================================================
# HOME PAGE
# ============================================================

@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>
            Skin Clinic Campaign Analysis
        </title>

        <style>

            body {
                font-family: Arial, sans-serif;
                margin: 50px;
                background-color: #f5f5f5;
                text-align: center;
            }

            .container {
                max-width: 900px;
                margin: auto;
                background-color: white;
                padding: 40px;
                border-radius: 10px;
            }

            h1 {
                margin-bottom: 10px;
            }

            p {
                font-size: 18px;
            }

            a {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 20px;
                background-color: #333333;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }

            a:hover {
                background-color: #555555;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <h1>
                M10 PMLS - Assignment 1
            </h1>

            <h2>
                Skin Clinic Campaign Analysis
            </h2>

            <p>
                Model Deployment Using FastAPI
            </p>

            <p>
                This API analyses customer response to
                the Skin Clinic marketing campaign.
            </p>

            <a href="/campaign-analysis">
                View Campaign Analysis
            </a>

        </div>

    </body>

    </html>
    """


# ============================================================
# CAMPAIGN ANALYSIS ENDPOINT
# ============================================================

@app.get(
    "/campaign-analysis",
    response_class=HTMLResponse
)
def campaign_analysis():

    # Convert pandas DataFrames to HTML tables

    gender_table = gender_analysis.to_html(
        index=False,
        classes="analysis-table",
        border=0
    )

    age_table = age_analysis.to_html(
        index=False,
        classes="analysis-table",
        border=0
    )

    purchase_table = purchase_analysis.to_html(
        index=False,
        classes="analysis-table",
        border=0
    )

    product_table = product_analysis.to_html(
        index=False,
        classes="analysis-table",
        border=0
    )


    # ========================================================
    # HTML PAGE
    # ========================================================

    html = f"""
    <!DOCTYPE html>

    <html>

    <head>

        <title>
            Skin Clinic Campaign Analysis
        </title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f5f5f5;
            }}

            .container {{
                width: 85%;
                max-width: 1000px;
                margin: 40px auto;
                background-color: white;
                padding: 40px;
                border-radius: 10px;
            }}

            h1 {{
                text-align: center;
                margin-bottom: 5px;
            }}

            .subtitle {{
                text-align: center;
                margin-bottom: 40px;
            }}

            h2 {{
                margin-top: 40px;
                border-bottom: 2px solid #333;
                padding-bottom: 8px;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
                margin-bottom: 20px;
            }}

            th {{
                background-color: #333333;
                color: white;
                padding: 12px;
                text-align: center;
            }}

            td {{
                padding: 12px;
                text-align: center;
                border-bottom: 1px solid #dddddd;
            }}

            tr:hover {{
                background-color: #f2f2f2;
            }}

            .finding {{
                background-color: #f2f2f2;
                padding: 15px;
                border-left: 4px solid #333333;
                margin-bottom: 25px;
            }}

            .summary {{
                margin-top: 40px;
                padding: 20px;
                background-color: #eeeeee;
                border-radius: 5px;
            }}

            .footer {{
                text-align: center;
                margin-top: 40px;
                font-size: 14px;
            }}

        </style>

    </head>


    <body>

        <div class="container">

            <h1>
                M10 PMLS - Assignment 1
            </h1>

            <p class="subtitle">
                Model Deployment Using FastAPI
                <br>
                Skin Clinic Campaign Analysis
            </p>


            <!-- ========================================= -->
            <!-- GENDER ANALYSIS -->
            <!-- ========================================= -->

            <h2>
                1. Gender vs Campaign Response
            </h2>

            {gender_table}

            <div class="finding">

                <strong>Finding:</strong>

                Female customers had a response rate of
                <strong>43.77%</strong>, compared with
                <strong>34.08%</strong> for male customers.

            </div>


            <!-- ========================================= -->
            <!-- AGE ANALYSIS -->
            <!-- ========================================= -->

            <h2>
                2. Age Group vs Campaign Response
            </h2>

            {age_table}

            <div class="finding">

                <strong>Finding:</strong>

                Customers aged 30-50 recorded the highest
                campaign response rate at
                <strong>47.06%</strong>.

            </div>


            <!-- ========================================= -->
            <!-- PURCHASE ANALYSIS -->
            <!-- ========================================= -->

            <h2>
                3. Purchase in Last Quarter
                vs Campaign Response
            </h2>

            {purchase_table}

            <div class="finding">

                <strong>Finding:</strong>

                Customers who purchased in the last quarter
                had a response rate of
                <strong>49.65%</strong>, compared with
                <strong>21.69%</strong> among customers
                who did not.

            </div>


            <!-- ========================================= -->
            <!-- PRODUCT USAGE ANALYSIS -->
            <!-- ========================================= -->

            <h2>
                4. Product Usage vs Campaign Response
            </h2>

            {product_table}

            <div class="finding">

                <strong>Finding:</strong>

                Customers who purchased more than eight
                unique products had the highest response
                rate at <strong>52.00%</strong>.

            </div>


            <!-- ========================================= -->
            <!-- SUMMARY -->
            <!-- ========================================= -->

            <div class="summary">

                <h2>
                    Campaign Analysis Summary
                </h2>

                <p>
                    The analysis indicates that customer
                    engagement and recent purchasing
                    behaviour are associated with higher
                    campaign response rates.
                </p>

                <p>
                    Customers aged 30-50, customers who
                    purchased during the last quarter,
                    and customers who purchased more than
                    eight unique products showed particularly
                    high response rates.
                </p>

                <p>
                    These customer segments may therefore
                    be useful targets for future marketing
                    campaigns.
                </p>

            </div>


            <div class="footer">

                M10 PMLS - Assignment 1
                <br>
                Skin Clinic Campaign Analysis API

            </div>

        </div>

    </body>

    </html>
    """

    return HTMLResponse(content=html)


# ============================================================
# RUN APPLICATION LOCALLY
# ============================================================

if __name__ == "__main__":

    # Correct FastAPI URL
    url = "http://127.0.0.1:8000/campaign-analysis"

    # Automatically open the correct page after 2 seconds
    threading.Timer(
        2.0,
        lambda: webbrowser.open_new(url)
    ).start()

    # Start FastAPI server
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )