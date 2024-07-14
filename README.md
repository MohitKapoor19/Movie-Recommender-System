# Project: Movie Recommender System Using Machine Learning!



Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

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

# Concept used to build the similarity.pkl file : cosine_similarity

1 . Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3 . Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4 . It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

5 . For more details , check URL : https://www.learndatasci.com/glossary/cosine-similarity/

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



