# Internship Projects at Coding Raja Technology

## Overview
During my internship at Coding Raja Technology, I worked on two major projects that focused on applying machine learning techniques to solve real-world problems. These projects are:

1. **Movie Recommender System** (Internship Project 1)
2. **Fraud Detection in Financial Transactions** (Internship Project 2)

# Movie Recommender System - Internship Project 1

This project is a web application that recommends movies similar to those of user interest using machine learning algorithms and the TMDB API for fetching movie posters and additional details. Users can interactively select a movie, and the system suggests similar ones based on similarity. The application also includes a demo video showcasing its functionality. Additionally, users can view visual representations of the project's workflow and download the recommendation model for further use.

# Fraud Detection in financial transactions- Internship Project 2
## Project Introduction

[Click here for the task 2](https://github.com/MohitKapoor19/coding-raja-technologies-internship/blob/main/Task%202%20%3A%20Fraud%20Detection%20in%20Financial%20Transactions/Task%202%20FRAUD%20DETECTION%20IN%20FINANCIAL%20TRANSACTIONS.ipynb)

[Dataset used for this project](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)


This project focuses on anomaly detection in credit card transactions, utilizing a dataset from Kaggle to identify fraudulent activities. The primary goal is to ensure that credit card companies can effectively recognize fraudulent transactions, thereby protecting customers from unauthorized charges.

## Context
Credit card fraud detection is crucial for safeguarding customers and preventing financial losses. This dataset, comprising transactions made by European cardholders in September 2013, spans two days and includes a total of 284,807 transactions. Notably, it features 492 instances of fraud, which account for a mere 0.172% of all transactions, highlighting the significant class imbalance.

## Content
The dataset consists solely of numerical input variables derived from a Principal Component Analysis (PCA) transformation. Due to confidentiality concerns, original features and detailed background information are not provided. The key features include:
- **V1, V2, ..., V28:** Principal components from PCA transformation.
- **Time:** Seconds elapsed between each transaction and the first transaction in the dataset.
- **Amount:** The transaction amount, useful for cost-sensitive learning.
- **Class:** The response variable, where 1 indicates fraud and 0 indicates a legitimate transaction.

## Objective
The project aims to identify fraudulent credit card transactions using machine learning algorithms. Given the severe class imbalance, traditional accuracy metrics are insufficient. Instead, the Area Under the Precision-Recall Curve (AUPRC) is recommended for a more meaningful assessment of the model's performance.

## Methodology
The project involves:
- Preprocessing the dataset to handle the class imbalance.
- Training various machine learning models, including Support Vector Machine (SVM) and Random Forest.
- Evaluating model performance using metrics like AUPRC, precision, recall, and F1-score.
- Comparing the performance of different models to identify the most effective approach for fraud detection.

## Insights and Results
Detailed performance metrics and classification reports for each model will be provided. The project will also include visual representations of the results and downloadable versions of the trained models for further use.

This thorough analysis aims to enhance the understanding and application of machine learning in the context of credit card fraud detection, ultimately contributing to more secure and reliable financial transactions.


# About the Movie Recommender System:

This is a web application that can recommend various kinds of similar movies based on an user interest.
Here is a working demo of my project:

* [Click here to watch the demo on YouTube](https://www.youtube.com/watch?v=sUSU4Iw7nqY)

  
## Features

* **Movie Recommendations**: Get suggestions based on user-selected movies.

* **TMDB API Integration**: Fetch movie posters and additional movie details. For more details [test_cases.ipynb](https://github.com/MohitKapoor19/coding-raja-technologies-internship/blob/main/data%20cleaning/test_cases.ipynb)

* **Interactive UI**: Built with Streamlit for a user-friendly interface.

* **Downloadable Model**: Save and use the recommendation model for further analysis
  
# WorkFlow:

<h4>Image 1: Workflow Step 1</h4>
<img src="demo/demo (1).png" alt="workflow" width="70%">

<br>

<h4>Image 2: Workflow Step 2</h4>
<img src="demo/demo (2).png" alt="workflow" width="70%">

<br>

<h4>Image 3: Workflow Step 3</h4>
<img src="demo/demo (3).png" alt="workflow" width="70%">


# Dataset has been used:

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

# Concept used to build the similarity.pkl file : similarity

1.Cosine Similarity is a metric that measures the similarity between documents.

2.In order to demonstrate the cosine similarity function, we need vectors. Here, the vectors are numpy arrays.

3.Once we have the vectors, we can call the cosine_similarity() function by passing both vectors. This function will calculate the cosine similarity between the two.

4.The result will be a value between 0 and 1. A value of 0 indicates that the vectors are completely different, whereas a value of 1 indicates that they are completely similar.

5.For more details, please refer to the relevant documentation.check URL : https://naomy-gomes.medium.com/the-cosine-similarity-and-its-use-in-recommendation-systems-cb2ebd811ce1

# How to run?

### STEPS TO FOLLOW

Follow these steps and refer to the video for [guidance.](https://youtu.be/matPnZq-Ncs)

### STEP 01:

Clone the repository

```bash
https://github.com/MohitKapoor19/coding-raja-technologies-internship
```
### STEP 02- Execute the following commands in the terminal:l

  ```bash
    pip install -r .\requirements.txt
    
    python.exe -m pip install --upgrade pip
  ```

### STEP 03- Run this file for Models

Run this file to generate the models:

[Recommender system.ipynb](https://github.com/MohitKapoor19/coding-raja-technologies-internship/blob/main/data%20cleaning/Recommender%20system.ipynb)

### STEP 04- Locally Deploy the App
Now run,
```bash
streamlit run app.py
```



