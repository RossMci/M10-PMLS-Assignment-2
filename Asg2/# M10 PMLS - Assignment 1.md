# M10 PMLS Assignment 1

## Model Deployment Using FastAPI

This project was completed for M10 Productionization of Machine Learning Systems Assignment 1.

This project analyses a skin clinic marketing campaign with 10,000 customers. The aim is to find which customer groups were more likely to respond to the campaign.

## Important Note for Lecturer

This is the submission for Assignment 1 only.

Please use the `Asg1` folder when reviewing Assignment 1.

The `Asg2` folder contains my Assignment 2 work and is not part of this Assignment 1 submission.

All files required for Assignment 1 are located in the `Asg1` folder.

## Analysis

The following areas were analysed:

- Gender
- Age group
- Purchase in the last quarter
- Number of unique products purchased

The response rate was calculated for each group.

## Files

The Assignment 1 files are located inside the `Asg1` folder.

The files include:

- `MainPMLS.py` - FastAPI application
- `skin clinic campaign.csv` - dataset
- `requirements.txt` - Python packages
- `ProdofMachineLearningSystemsAS1.ipynb` - analysis notebook
- `README.md` - project information

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

Open the Assignment 1 project folder in VS Code and run:

```bash
uvicorn MainPMLS:app --reload
```

The FastAPI application can then be accessed using these links.

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

The main results from the campaign analysis were:

- Female response rate: 43.77%
- Male response rate: 34.08%
- Age 30-50 had the highest age response rate at 47.06%
- Customers who purchased in the last quarter had a 49.65% response rate
- Customers who purchased more than 8 unique products had a 52.00% response rate

The results show that response rates differed across the customer groups.

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

Replace `YOUR-SERVICE-NAME` with the actual Assignment 1 Render service name.

## GitHub Repository

The project repository contains work for both assignments.

For Assignment 1, please use the `Asg1` folder only.

The `Asg2` folder contains Assignment 2 work and should not be used when reviewing this Assignment 1 submission.

## Assignment Requirements

The following Assignment 1 requirements were completed:

1. The campaign dataset was analysed using Python.
2. Gender vs Campaign Response was analysed.
3. Age Group vs Campaign Response was analysed.
4. Purchase in Last Quarter vs Campaign Response was analysed.
5. Product Usage vs Campaign Response was analysed.
6. The analysis was converted into a FastAPI application.
7. The `/campaign-analysis` endpoint was created.
8. The endpoint displays the results in tabular format.
9. The API was deployed using Render.
10. The deployed API link is included in this README.

## Conclusion

The analysis shows that customer response varied across gender, age, recent purchases and product usage.

Female customers had a higher response rate than male customers. Customers aged 30-50 had the highest response rate of the age groups.

Customers who purchased recently and customers who purchased more products also had higher campaign response rates.

FastAPI was used to display the campaign analysis and Render was used to make the application publicly accessible.

## Assignment 1 Submission

This README and the files in the `Asg1` folder relate to Assignment 1 only.

Please do not use the `Asg2` folder when assessing Assignment 1.
