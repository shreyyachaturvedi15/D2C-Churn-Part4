### FastAPI Churn Scoring Service

#### 

#### Overview

In this part of the project, the churn prediction model developed earlier was converted into a FastAPI service. The goal was to make the model easy to use by other teams within the organization, such as customer support, CRM, and retention teams.

The API accepts customer information as input and returns a churn prediction, the probability of churn, and a simple risk classification.

Features

The service includes the following functionality:

Health check endpoint to verify that the API is running

Single customer churn prediction

Batch prediction for multiple customers

Input validation using Pydantic models

Automated API testing using Pytest

Monitoring and responsible-use documentation
Model: Logistic Regression

##### 

##### Endpoints

###### 

###### GET /health



Returns API health status.

###### 

###### POST /predict



Predicts churn for a single customer.

###### 

###### POST /batch\_predict



Predicts churn for multiple customers.

###### 

###### Run



uvicorn app.main:app --reload

###### 

###### Run Tests



pytest tests/test\_api.py -v

###### 

###### Sample Request



{
"gross\_amount":1000.0,
"quantity":2,
"returned":0.0,
"rating":4.5,
"discount\_pct":0.2,
"delivery\_days":3,
"city\_tier":0,
"age\_group":1,
"acquisition\_channel":2,
"loyalty\_tier":3,
"preferred\_category":3,
"skin\_type":0,
"marketing\_consent":1
}



###### Sample Response



{
"churn\_prediction":1,
"churn\_probability":0.6546,
"risk\_level":"High Risk"
}



**Monitoring**



A separate monitoring plan has been included in the repository. The plan outlines how model performance, prediction quality, API reliability, and business outcomes should be monitored after deployment.

Responsible Use

This API is intended to support customer retention efforts by identifying customers who may be at risk of churn. Predictions should be used as decision-support information and should not be the only factor considered when 

making business decisions. Human review and business context should always be taken into account.



**Conclusion**



The churn prediction model was successfully deployed as a FastAPI service with validated inputs, prediction endpoints, automated tests, and deployment documentation. The solution provides a simple and reusable interface for internal teams to access churn predictions and support retention initiatives.

