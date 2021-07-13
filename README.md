# HR Analytics- Job Change of Data Scientists


#### Abstract
Would you be interested in knowing who really wants to work for your company in the world of Big Data and Data Science? After all, training and looking for the right candidate costs time and money. What if you could reduce the cost and time as well as find quality candidates for your company? If your interest is peaked by the questions listed then this project is for you.

I chose this dataset for the factors included in the data which may help HR understand why a candidate such as a Data Scientist would leave a current job.

The ability to target whether a candidate will leave a job may allow for the savings of money, time, and may assist in finding methods to improve retention.

The main goal of this project is to create a model that with specific features can accurately predict a candidate's decision to stay or leave a company. A classification model was constructed to predict the target of job change. The model performed slightly better than the baseline thus it has some value.




#### Project Goals
> - Find features for Job Change of Data Scientist

> - Construct a ML classification model that accurately predicts who will move to a new job


#### Dataset
> - This data is being pulled from Kaggle.

> - The following link contains the dataset: https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists?select=sample_submission.csv

> - When downloaded, you will have a three .csv files. The dataset I used was aug_train.csv


### Project Planning 

The following link contains my project planning process on my Trello Board: https://trello.com/b/u97V2VhP/individual-project-hr-analytics

Here is a snapshot of my project planning from my Trello Board

![image](https://user-images.githubusercontent.com/80718476/125339051-8ed45d80-e316-11eb-85ad-434217fcf4ce.png)

### Project Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>


#### Audience
> - Instructors and Peers

#### Project Deliverables
> - Github Repo w/ Final Notebook and README
> - Project summary and writeup for your resume or other professional portfolio pieces


#### Data Dictionary
    
- This is a data dictionary as a reference for the variables used within in the data set. A sample of what is included in data dictionary is below. Please refer to HR_analytics_data_dictionary.csv for more details.


 |   Target    |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
| target| float64|  0– Not looking for job change, 1 – Looking for a job change



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  enrollee_id | int64   | Unique ID for candidate |
| city   | object | City code|
| city_ development _index  | float64 | Development index of the city (scaled) |
| gender | object   | Gender of candidate|
| relevent_experience | object | Relevant experience of candidate|
| enrolled_university  | object |  Type of University course enrolled if any|
| education_level | object | Education level of candidate|
| major_discipline | object | Education major discipline of candidate|



#### Initial Hypotheses

### Hypothesis 1:
> - **Hypothesis 1 -** I rejected the Null Hypothesis; there is a relationship.
> - alpha = .05
> - $H_0$: Company type has no affect on data scientist who leave their job or not (they are independent). 
> - $H_a$: Company type has an affect on data scientist who leave their job or not (they are dependent). 

### Hypothesis 2:
> - **Hypothesis 2 -** I rejected the Null Hypothesis; there is a relationship.
> - alpha = .05
> - $H_0$:  Relevant experience has no affect on data scientist who leave their job or not (they are independent). 
> - $H_a$:  Relevant experience has an affect on data scientist who leave their job or not (they are dependent).

### Hypothesis 3:
> - **Hypothesis 3 -** I rejected the Null Hypothesis; there is a relationship.
> - alpha = .05
> - $H_0$: Status of university enrollment has no affect on data scientist who leave their job or not (they are independent). 
> - $H_a$: Status of university enrollment has an affect on data scientist who leave their job or not (they are dependent).


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>
<b>Findings:</b>

  -There is not one main driver for job change of Data Scientists.
 
  - All models performed similarly except for KNeighbors had a lower accuracy score than the baseline
  
  - The models I created were a Decision tree, Logistic Regression Model, KNeighbors, and Random Forest Model predicted similar accuracy scores for the training dataset except for KNeighbors. The model I chose was the Decision Tree model 2 as my best model with a 75.52% accuracy rate for predicting features of company type, relevent experience, status of university enrollment, and last new job.
  
  -  The Decision Tree model 2 (75.52%) outperformed my baseline score of 75.09% thus it has some value.
  

- With more time:
  - I would have encoded and binned the experience and company_size columns
  - I would have worked with more hyperparameters to improve the models
  - I would utilize clustering to create more features


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Data Acquisition
> - Data Preparation
> - Exploration 
> - Modeling


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download HR Analytics Dataset from Kaggle into your working directory
- [ ] Download the aquire.py, prepare.py, explore.py and Final_notebook.ipynb files into your working directory
- [ ] Run the Final_notebook.ipynb notebook