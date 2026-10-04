# M10 PMLS Assignment 1

## Model Deployment Using FastAPI

This project analyses a skin clinic marketing campaign with 10,000 customers. The aim is to find which customer groups were more likely to respond to the campaign.

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
- `ProdofMachineLearningSystemsAS1.ipynb` - analysis notebook

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

The endpoint displays the campaign analysis results in tabular format.

The tables include:

- Gender vs Campaign Response
- Age Group vs Campaign Response
- Purchase in Last Quarter vs Campaign Response
- Product Usage vs Campaign Response

## Results

- Female response rate: 43.77%
- Male response rate: 34.08%
- Age 30-50 had the highest age response rate at 47.06%
- Customers who purchased in the last quarter had a 49.65% response rate
- Customers who purchased more than 8 unique products had a 52.00% response rate

## Render Deployment

The FastAPI application was deployed using Render.

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

## Assignment Requirements

1. The analysis was converted into a FastAPI application.
2. The `/campaign-analysis` endpoint was created.
3. The endpoint displays the results in tabular format.
4. The API was deployed using Render.
5. The deployed API link is included in this README.

## Conclusion

The analysis shows that customer response varied across gender, age, recent purchases and product usage.

Customers who purchased recently and customers who purchased more products had higher response rates.

FastAPI was used to display the campaign analysis and Render was used to make the application publicly accessible.