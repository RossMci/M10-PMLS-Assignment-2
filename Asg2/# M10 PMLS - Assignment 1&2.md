# M10 PMLS Assignment 2

## Developing API For Excel

This project was completed for M10 Productionization of Machine Learning Systems Assignment 2.

The project analyses a skin clinic marketing campaign containing 10,000 customer records. The aim is to identify which customer groups were more likely to respond to the marketing campaign.

The analysis was completed using Python and Pandas. FastAPI was used to create an API containing the campaign analysis results. The API was deployed publicly using Render and connected to Microsoft Excel using Power Query.

Excel is used to display the campaign analysis in tables and includes a Form Control button that can refresh the data from the deployed API.

## Important Note for Lecturer

Please use the `Asg2` folder when reviewing Assignment 2.

The `Asg1` folder contains my previous Assignment 1 work and is not part of this Assignment 2 submission.

All files required for Assignment 2 are located in the `Asg2` folder.

The deployed Assignment 2 API is:

https://m10-pmls-assignment-2.onrender.com/campaign-analysis

## Dataset

The dataset used for this project is:

`skin clinic campaign.csv`

The dataset contains 10,000 customer records with the following columns:

- `CustID`
- `Gender`
- `AgeGroup`
- `Purchase_Last_Quarter`
- `Unique_Products_Purchased`
- `Response_to_Campaign`

## Analysis

The following four areas were analysed:

1. Gender vs Campaign Response
2. Age Group vs Campaign Response
3. Purchase in Last Quarter vs Campaign Response
4. Product Usage vs Campaign Response

The response rate was calculated for each customer group.

## Gender vs Campaign Response

The campaign response rates by gender were:

| Gender | Total Customers | Responded | Response Rate |
|---|---:|---:|---:|
| Female | 5,024 | 2,199 | 43.77% |
| Male | 4,976 | 1,696 | 34.08% |

Female customers had a higher campaign response rate than male customers.

## Age Group vs Campaign Response

The campaign response rates by age group were:

| Age Group | Response Rate |
|---|---:|
| <30 | 32.93% |
| 30-50 | 47.06% |
| >50 | 32.60% |

Customers aged 30-50 had the highest campaign response rate.

## Purchase in Last Quarter vs Campaign Response

The response rates based on whether the customer purchased in the previous quarter were:

| Purchased Last Quarter | Response Rate |
|---|---:|
| No | 21.69% |
| Yes | 49.65% |

Customers who purchased in the last quarter had a much higher response rate.

## Product Usage vs Campaign Response

Customers were grouped based on the number of unique products they purchased.

| Unique Products | Response Rate |
|---|---:|
| 1-4 | 18.08% |
| 5-8 | 38.48% |
| >8 | 52.00% |

Customers who purchased more products had higher campaign response rates.

Customers who purchased more than 8 unique products had the highest response rate at 52.00%.

These results show associations within the campaign data and do not prove that these customer characteristics caused the campaign responses.

## Main Findings

The main findings from the analysis were:

- Female customers had a higher response rate than male customers.
- Customers aged 30-50 had the highest response rate.
- Customers who purchased in the last quarter had a higher response rate.
- Customers with higher product usage had higher campaign response rates.
- Customers who purchased more than 8 unique products had the highest product usage response rate.

## Project Files

The Assignment 2 files are located inside the `Asg2` folder.

The project contains:

- `MainPMLS.py` - FastAPI application
- `Asg2.ipynb` - Jupyter Notebook containing the analysis
- `skin clinic campaign.csv` - campaign dataset
- `requirements.txt` - required Python packages
- `campaign_analysis.xlsx` - Excel campaign analysis
- `README.md` - project information

If the final Excel workbook contains the VBA refresh macro, it can be saved as:

`M10_PMLS_Assignment_2.xlsm`

## Requirements

The following Python packages are required:

```text
fastapi
uvicorn[standard]
pandas
numpy
```

Install the packages using:

```bash
pip install -r requirements.txt
```

## Running FastAPI Locally

Open the `Asg2` project folder in VS Code.

Run:

```bash
uvicorn MainPMLS:app --reload
```

Home page:

```text
http://127.0.0.1:8000/
```

Campaign analysis:

```text
http://127.0.0.1:8000/campaign-analysis
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## FastAPI Application

The FastAPI application is contained in:

`MainPMLS.py`

The application loads the campaign dataset, calculates the campaign response rates and makes the results available through the API.

The required endpoint is:

```text
/campaign-analysis
```

The endpoint returns four analysis sections:

- `Gender_vs_Campaign_Response`
- `Age_Group_vs_Campaign_Response`
- `Purchase_Last_Quarter_vs_Campaign_Response`
- `Product_Usage_vs_Campaign_Response`

The results are returned in a structured format that Microsoft Excel Power Query can convert into tables.

## Render Deployment

The FastAPI application was deployed publicly using Render.

The following Render configuration was used:

```text
Language:
Python 3

Branch:
main

Root Directory:
Asg2

Build Command:
pip install -r requirements.txt

Start Command:
uvicorn MainPMLS:app --host 0.0.0.0 --port $PORT
```

## Deployed API

The application is publicly available at:

https://m10-pmls-assignment-2.onrender.com/

Campaign analysis endpoint:

https://m10-pmls-assignment-2.onrender.com/campaign-analysis

FastAPI documentation:

https://m10-pmls-assignment-2.onrender.com/docs

ReDoc documentation:

https://m10-pmls-assignment-2.onrender.com/redoc

## Excel Power Query

Microsoft Excel was connected to the deployed FastAPI application using Power Query.

The connection was created using:

```text
Data > Get Data > From Web
```

The deployed API URL used in Power Query is:

```text
https://m10-pmls-assignment-2.onrender.com/campaign-analysis
```

The four API analysis sections were converted into separate Excel tables.

The Excel workbook contains:

- Gender
- Age Group
- Last Quarter
- Product Usage

Using the Render URL means Excel can retrieve the analysis without the FastAPI application running locally.

## Excel Refresh Button

A Form Control button was added to the Excel workbook to refresh the campaign analysis.

The button is named:

```text
Refresh Campaign Analysis
```

The VBA macro used for the button is:

```vb
Sub RefreshCampaignAnalysis()

    ThisWorkbook.RefreshAll

    Application.CalculateUntilAsyncQueriesDone

    MsgBox "Campaign analysis refreshed successfully.", _
           vbInformation, _
           "Campaign Analysis"

End Sub
```

When the button is clicked, Excel refreshes the Power Query data from the deployed API.

The workbook should be saved as an Excel Macro-Enabled Workbook if the VBA macro is included:

```text
M10_PMLS_Assignment_2.xlsm
```

## GitHub Repository

The project repository is:

https://github.com/RossMci/M10-PMLS-Assignment-2

For Assignment 2, please use the `Asg2` folder only.

The `Asg1` folder contains previous Assignment 1 work and is not part of the Assignment 2 submission.

## Assignment Requirements Completed

The following Assignment 2 requirements were completed:

1. Analysed Gender vs Campaign Response.
2. Analysed Age Group vs Campaign Response.
3. Analysed Purchase in Last Quarter vs Campaign Response.
4. Analysed Product Usage vs Campaign Response.
5. Converted the solution into a FastAPI application.
6. Created the `/campaign-analysis` endpoint.
7. Returned the campaign analysis results in a structured tabular format.
8. Deployed the FastAPI application publicly using Render.
9. Connected Microsoft Excel to the hosted API using Power Query.
10. Loaded the campaign analysis results into Excel tables.
11. Added a Form Control button to refresh the campaign analysis results.

## Submission Links

Deployed campaign analysis API:

https://m10-pmls-assignment-2.onrender.com/campaign-analysis

FastAPI documentation:

https://m10-pmls-assignment-2.onrender.com/docs

GitHub repository:

https://github.com/RossMci/M10-PMLS-Assignment-2

Please use the `Asg2` folder in the GitHub repository when reviewing Assignment 2.
