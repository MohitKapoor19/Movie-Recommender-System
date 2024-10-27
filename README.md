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



