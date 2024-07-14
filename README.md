# Movie Recommender System - Internship Project

This project is a web application developed during my internship with Coding Raja. It recommends movies similar to those of user interest using machine learning algorithms and the TMDB API for fetching movie posters and additional details. Users can interactively select a movie, and the system suggests similar ones based on similarity. The application also includes a demo video showcasing its functionality. Additionally, users can view visual representations of the project's workflow and download the recommendation model for further use.

## Features

* **Movie Recommendations**: Get suggestions based on user-selected movies.

* **TMDB API Integration**: Fetch movie posters and additional movie details.For more details [test_cases.ipynb](https://github.com/MohitKapoor19/coding-raja-technologies-internship/blob/main/data%20cleaning/test_cases.ipynb)

* **Interactive UI**: Built with Streamlit for a user-friendly interface.

* **Downloadable Model**: Save and use the recommendation model for further analysis
  
# About this project:

This is a streamlit web application that can recommend various kinds of similar movies based on an user interest.
Here is a working demo of my project:

* [Click here to watch the demo on YouTube](https://www.youtube.com/watch?v=gTy2vlySS_Q)

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

1 . Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3 . Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4 . It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

5 . For more details , check URL : https://naomy-gomes.medium.com/the-cosine-similarity-and-its-use-in-recommendation-systems-cb2ebd811ce1

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/MohitKapoor19/coding-raja-technologies-internship
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n movie python=3.12.4 -y
```

```bash
conda activate movie
```


### STEP 02- Install the requirements
```bash
pip install -r requirements.txt
```
### STEP 03- Run this file for Models

Run this file to generate the models:

[Recommender system.ipynb](https://github.com/MohitKapoor19/coding-raja-technologies-internship/blob/main/data%20cleaning/Recommender%20system.ipynb)

### STEP 04- Locally Deploy the App
Now run,
```bash
streamlit run app.py
```



