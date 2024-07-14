import pickle
import streamlit as st
import requests
import base64

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=1f8372ab60a7747a9530ac4b0d4b91b8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

def recommend(movie):
    try:
        index = movies[movies['original_title'] == movie].index[0]
    except IndexError:
        st.error("Selected movie not found in the dataset.")
        return [], []

    if index < 0 or index >= len(similarity):
        st.error("Selected movie index is out of range.")
        return [], []

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        try:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]]['original_title'])
        except IndexError:
            st.error(f"An error occurred fetching details for movie index {i[0]}.")
            continue

    return recommended_movie_names, recommended_movie_posters

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Custom background image
img_bin = get_base64_of_bin_file('image.jpg')
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpeg;base64,{img_bin}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'Helvetica Neue', sans-serif;
    color: #fff;
}}
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
    right: 2rem;
}}
.stButton>button {{
    background-color: #007BFF; /* Blue */
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 10px 2px;
    cursor: pointer;
    border-radius: 25px;
    transition: background-color 0.3s, transform 0.3s;
}}
.stButton>button:hover {{
    background-color: #0056b3;
    transform: scale(1.05);
}}
.css-1wa3eu0-placeholder {{
    color: #ffffff !important;
    font-size: 20px !important;
    font-weight: bold;
}}
.css-1uccc91-singleValue {{
    color: #ffffff !important;
    font-size: 20px !important;
    font-weight: bold;
}}
label.css-145kmo2 {{
    font-size: 24px !important;
    color: #ffffff !important;
    font-weight: bold;
    text-shadow: 1px 1px 2px #000000;
}}
.css-1d391kg {{
    background-color: rgba(0, 0, 0, 0.5) !important;
    border-radius: 10px !important;
    padding: 10px !important;
}}
.stHeader {{
    text-shadow: 2px 2px 4px #000000;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.header('CineMatch: Your Personalized Movie Guide')
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['original_title'].values

# Custom selectbox styling
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,
    index=0,
    format_func=lambda x: '🎬 ' + x
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    if recommended_movie_names:
        cols = st.columns(5)
        for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
            with col:
                st.markdown(f"<h3 style='text-align: center; color: #ffffff; text-shadow: 1px 1px 2px #000000;'>{name}</h3>", unsafe_allow_html=True)
                st.image(poster, use_column_width=True)