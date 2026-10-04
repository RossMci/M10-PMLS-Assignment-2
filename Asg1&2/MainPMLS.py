# ============================================================
# M10 PMLS - ASSIGNMENTS 1 & 2
# Skin Clinic Campaign Analysis
#
# Assignment 1:
#   Model Deployment Using FastAPI
#
# Assignment 2:
#   Developing API for Excel
#
# Main application file: MainPMLS.py
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import pandas as pd
import numpy as np
import os


# ============================================================
# 2. CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Skin Clinic Campaign Analysis API",
    description=(
        "FastAPI application for analysing customer responses "
        "to the Skin Clinic marketing campaign."
    ),
    version="1.0.0"
)


# ============================================================
# 3. LOAD DATASET
# ============================================================

# Get the directory containing this Python file.
# This makes the CSV easier to locate when running locally
# or when deployed to Render.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILE = os.path.join(
    BASE_DIR,
    "skin clinic campaign.csv"
)

df = pd.read_csv(CSV_FILE)


# ============================================================
# 4. CREATE RESPONSE VARIABLE
# ============================================================

# Convert Response_to_Campaign from Yes/No into True/False.
#
# Yes  -> True
# No   -> False

df["Responded"] = (
    df["Response_to_Campaign"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("yes")
)


# ============================================================
# 5. RESPONSE RATE FUNCTION
# ============================================================

def response_rate_table(data, group_column):
    """
    Calculate campaign response statistics for a selected
    customer group.

    Returns:
        Total Customers
        Number Responded
        Response Rate (%)
    """

    result = (
        data.groupby(
            group_column,
            observed=False
        )
        .agg(
            Total_Customers=(
                "CustID",
                "size"
            ),

            Responded=(
                "Responded",
                "sum"
            ),

            Response_Rate=(
                "Responded",
                "mean"
            )
        )
        .reset_index()
    )

    # Convert response rate to percentage
    result["Response Rate (%)"] = (
        result["Response_Rate"] * 100
    ).round(2)

    # Remove temporary decimal response-rate column
    result = result.drop(
        columns="Response_Rate"
    )

    return result


# ============================================================
# 6. GENDER ANALYSIS
# ============================================================

gender_analysis = response_rate_table(
    df,
    "Gender"
)


# ============================================================
# 7. AGE GROUP ANALYSIS
# ============================================================

age_analysis = response_rate_table(
    df,
    "AgeGroup"
)


# ============================================================
# 8. PURCHASE LAST QUARTER ANALYSIS
# ============================================================

purchase_analysis = response_rate_table(
    df,
    "Purchase_Last_Quarter"
)


# ============================================================
# 9. PRODUCT USAGE ANALYSIS
# ============================================================

# Categorise customers based on number of unique products:
#
# 1-4
# 5-8
# >8

df["Product_Usage"] = pd.cut(
    df["Unique_Products_Purchased"],
    bins=[
        0,
        4,
        8,
        np.inf
    ],
    labels=[
        "1-4",
        "5-8",
        ">8"
    ]
)


product_analysis = response_rate_table(
    df,
    "Product_Usage"
)


# ============================================================
# 10. HOME PAGE
# ============================================================

@app.get(
    "/",
    response_class=HTMLResponse
)
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
                margin: 40px;
                background-color: #f5f5f5;
            }

            .container {
                max-width: 900px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
            }

            h1 {
                text-align: center;
            }

            .button {
                display: inline-block;
                padding: 12px 20px;
                margin: 10px;
                background: #333;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }

            .buttons {
                text-align: center;
            }

        </style>

    </head>


    <body>

        <div class="container">

            <h1>
                Skin Clinic Campaign Analysis
            </h1>

            <p>
                M10 PMLS - Campaign Analysis API
            </p>

            <p>
                This FastAPI application analyses customer
                response to the Skin Clinic marketing campaign.
            </p>


            <div class="buttons">

                <a
                    class="button"
                    href="/campaign-analysis"
                >
                    View Campaign Analysis
                </a>


                <a
                    class="button"
                    href="/campaign-analysis-json"
                >
                    View JSON API
                </a>


                <a
                    class="button"
                    href="/download-excel"
                >
                    Download Excel
                </a>


                <a
                    class="button"
                    href="/docs"
                >
                    API Documentation
                </a>

            </div>

        </div>

    </body>

    </html>
    """


# ============================================================
# 11. CAMPAIGN ANALYSIS HTML ENDPOINT
# ============================================================

@app.get(
    "/campaign-analysis",
    response_class=HTMLResponse
)
def campaign_analysis():

    # Convert Pandas DataFrames into HTML tables

    gender_table = gender_analysis.to_html(
        index=False,
        classes="analysis-table"
    )

    age_table = age_analysis.to_html(
        index=False,
        classes="analysis-table"
    )

    purchase_table = purchase_analysis.to_html(
        index=False,
        classes="analysis-table"
    )

    product_table = product_analysis.to_html(
        index=False,
        classes="analysis-table"
    )


    # Build HTML page

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
                background-color: #f4f6f8;
                margin: 0;
                padding: 30px;
            }}


            .container {{
                max-width: 1000px;
                margin: auto;
                background: white;
                padding: 40px;
                border-radius: 10px;
            }}


            h1 {{
                text-align: center;
            }}


            h2 {{
                margin-top: 40px;
                border-bottom: 2px solid #333;
                padding-bottom: 10px;
            }}


            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 15px;
                margin-bottom: 20px;
            }}


            th {{
                background-color: #333;
                color: white;
                padding: 10px;
            }}


            td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: center;
            }}


            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}


            .finding {{
                background-color: #f4f4f4;
                padding: 15px;
                border-left: 5px solid #333;
            }}


            .navigation {{
                text-align: center;
                margin-bottom: 30px;
            }}


            .navigation a {{
                margin: 5px;
                padding: 10px 15px;
                background: #333;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}

        </style>

    </head>


    <body>

        <div class="container">

            <h1>
                Skin Clinic Campaign Analysis
            </h1>


            <div class="navigation">

                <a href="/">
                    Home
                </a>

                <a href="/campaign-analysis-json">
                    JSON
                </a>

                <a href="/download-excel">
                    Download Excel
                </a>

                <a href="/docs">
                    API Docs
                </a>

            </div>


            <!-- GENDER -->

            <h2>
                1. Gender vs Campaign Response
            </h2>

            {gender_table}

            <div class="finding">

                <strong>Finding:</strong>

                Female customers recorded a higher campaign
                response rate than male customers.

            </div>


            <!-- AGE -->

            <h2>
                2. Age Group vs Campaign Response
            </h2>

            {age_table}

            <div class="finding">

                <strong>Finding:</strong>

                Customers aged 30-50 recorded the highest
                campaign response rate.

            </div>


            <!-- PURCHASE -->

            <h2>
                3. Purchase in Last Quarter vs Campaign Response
            </h2>

            {purchase_table}

            <div class="finding">

                <strong>Finding:</strong>

                Customers who purchased during the previous
                quarter were considerably more likely to
                respond to the campaign.

            </div>


            <!-- PRODUCT USAGE -->

            <h2>
                4. Product Usage vs Campaign Response
            </h2>

            {product_table}

            <div class="finding">

                <strong>Finding:</strong>

                Campaign response increased with product usage.
                Customers purchasing more than eight unique
                products had the highest response rate.

            </div>


            <h2>
                Overall Conclusion
            </h2>

            <p>

                The campaign analysis suggests that recent
                purchasing behaviour and higher product
                engagement are associated with higher campaign
                response rates.

            </p>

            <p>

                These results are descriptive associations and
                do not by themselves prove that these customer
                characteristics caused the campaign response.

            </p>

        </div>

    </body>

    </html>
    """

    return html


# ============================================================
# 12. JSON API ENDPOINT
# ============================================================

@app.get("/campaign-analysis-json")
def campaign_analysis_json():
    """
    Return all campaign analysis results as JSON.

    This endpoint can be used by other applications,
    spreadsheets or external systems.
    """

    return {

        "gender":
            gender_analysis.to_dict(
                orient="records"
            ),

        "age_group":
            age_analysis.to_dict(
                orient="records"
            ),

        "last_quarter_purchase":
            purchase_analysis.to_dict(
                orient="records"
            ),

        "product_usage":
            product_analysis.to_dict(
                orient="records"
            )
    }


# ============================================================
# 13. EXCEL DOWNLOAD ENDPOINT
# ============================================================

@app.get("/download-excel")
def download_excel():
    """
    Generate an Excel workbook containing the four campaign
    analysis tables and return the workbook to the user.
    """

    excel_file = os.path.join(
        BASE_DIR,
        "campaign_analysis.xlsx"
    )


    # Create Excel workbook

    with pd.ExcelWriter(
        excel_file,
        engine="openpyxl"
    ) as writer:

        # Gender worksheet
        gender_analysis.to_excel(
            writer,
            sheet_name="Gender",
            index=False
        )

        # Age worksheet
        age_analysis.to_excel(
            writer,
            sheet_name="Age Group",
            index=False
        )

        # Purchase worksheet
        purchase_analysis.to_excel(
            writer,
            sheet_name="Last Quarter",
            index=False
        )

        # Product usage worksheet
        product_analysis.to_excel(
            writer,
            sheet_name="Product Usage",
            index=False
        )


    # Send Excel workbook to browser

    return FileResponse(
        path=excel_file,
        filename="campaign_analysis.xlsx",
        media_type=(
            "application/"
            "vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )


# ============================================================
# 14. RUN APPLICATION DIRECTLY
# ============================================================

# This section allows the application to be started using:
#
# python MainPMLS.py
#
# It is mainly useful for local development.
#
# Render should use:
#
# uvicorn MainPMLS:app --host 0.0.0.0 --port $PORT

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "MainPMLS:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )