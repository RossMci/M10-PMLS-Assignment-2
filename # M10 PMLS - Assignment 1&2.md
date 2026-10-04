# M10 PMLS Assignment 2

## Developing API For Excel

This project analyses a skin clinic marketing campaign with 10,000 customers. The aim is to find which customer groups were more likely to respond to the campaign.

The campaign analysis is provided through FastAPI and connected to Microsoft Excel using Power Query.

## Analysis

The following areas were analysed:

- Gender
- Age group
- Purchase in the last quarter
- Number of unique products purchased

The response rate was calculated for each group.

## Files

- `MainPMLS.py` - FastAPI application
- `skin clinic campaign.csv` - dataset
- `requirements.txt` - Python packages
- `ProdofMachineLearningSystemsAS2.ipynb` - analysis notebook
- `M10_PMLS_Assignment_2.xlsm` - Excel workbook

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

Packages used:

```text
fastapi
uvicorn[standard]
pandas
numpy
```

## Run FastAPI

Open the project folder in VS Code and run:

```bash
uvicorn MainPMLS:app --reload
```

The FastAPI application can then be accessed using these links:

Home page:

```text
http://127.0.0.1:8000/
```

Campaign analysis:

```text
http://127.0.0.1:8000/campaign-analysis
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

To stop the server, press:

```text
Ctrl + C
```

## FastAPI Application

The Python analysis was converted into a FastAPI application using `MainPMLS.py`.

The required endpoint is:

```text
/campaign-analysis
```

The endpoint provides the campaign analysis results for:

- Gender vs Campaign Response
- Age Group vs Campaign Response
- Purchase in Last Quarter vs Campaign Response
- Product Usage vs Campaign Response

The results are returned in a structured format that can be converted into tables using Excel Power Query.

## Results

- Female response rate: 43.77%
- Male response rate: 34.08%
- Age 30-50 had the highest age response rate at 47.06%
- Customers who purchased in the last quarter had a 49.65% response rate
- Customers who purchased more than 8 unique products had a 52.00% response rate

## Render Deployment

The FastAPI application was deployed using Render so that Excel can access the API online.

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
uvicorn MainPMLS:app --host 0.0.0.0 --port $PORT
```

## Deployed API Links

Home page:

```text
https://YOUR-SERVICE-NAME.onrender.com/
```

Campaign analysis:

```text
https://YOUR-SERVICE-NAME.onrender.com/campaign-analysis
```

Swagger documentation:

```text
https://YOUR-SERVICE-NAME.onrender.com/docs
```

ReDoc documentation:

```text
https://YOUR-SERVICE-NAME.onrender.com/redoc
```

Replace `YOUR-SERVICE-NAME` with the actual Render service name.

## Excel Power Query

Microsoft Excel was connected to the deployed FastAPI endpoint using Power Query.

In Excel:

```text
Data > Get Data > From Web
```

The deployed campaign analysis URL was used:

```text
https://YOUR-SERVICE-NAME.onrender.com/campaign-analysis
```

The API results were loaded into four Excel tables:

- Gender
- Age Group
- Last Quarter
- Product Usage

The tables can also be refreshed using:

```text
Data > Refresh All
```

## Excel Refresh Button

A Form Control button was added to the Excel workbook to refresh the campaign analysis.

The button runs the following VBA macro:

```vb
Sub RefreshCampaignAnalysis()

    ThisWorkbook.RefreshAll
    Application.CalculateUntilAsyncQueriesDone

    MsgBox "Campaign analysis refreshed successfully."

End Sub
```

The button is named:

```text
Refresh Campaign Analysis
```

When clicked, Excel refreshes the Power Query connection and gets the latest results from the FastAPI endpoint.

## Assignment Requirements

1. The analysis was converted into a FastAPI application.
2. The `/campaign-analysis` endpoint was created.
3. The endpoint provides the campaign analysis results in a structured tabular format.
4. The API was deployed using Render.
5. Excel Power Query was connected to the hosted API using From Web.
6. The analysis results were loaded into Excel tables.
7. A Form Control button was created to refresh the latest campaign analysis.
8. The completed Excel workbook is saved as `M10_PMLS_Assignment_2.xlsm`.

## Conclusion

The campaign analysis was completed using Python and FastAPI.

The API was deployed using Render and connected to Microsoft Excel using Power Query.

The Excel workbook displays the campaign analysis tables and includes a refresh button to retrieve the latest results from the API.