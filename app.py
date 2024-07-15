import pickle
import streamlit as st
import requests
import base64

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=1f8372ab60a7747a9530ac4b0d4b91b8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_poster_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    watch_url = f"https://www.themoviedb.org/movie/{movie_id}/watch"
    return full_poster_path, watch_url

def recommend(movie):
    try:
        index = movies[movies['original_title'] == movie].index[0]
    except IndexError:
        st.error("Selected movie not found in the dataset.")
        return [], [], []

    if index < 0 or index >= len(similarity):
        st.error("Selected movie index is out of range.")
        return [], [], []

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_watch_urls = []

    for i in distances[1:6]:
        try:
            movie_id = movies.iloc[i[0]].movie_id
            poster, watch_url = fetch_movie_details(movie_id)
            recommended_movie_posters.append(poster)
            recommended_movie_names.append(movies.iloc[i[0]]['original_title'])
            recommended_movie_watch_urls.append(watch_url)
        except IndexError:
            st.error(f"An error occurred fetching details for movie index {i[0]}.")
            continue

    return recommended_movie_names, recommended_movie_posters, recommended_movie_watch_urls

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
/* Card-like styling for movie recommendations */
.movie-card {{
    background-color: rgba(0, 0, 0, 0.7);
    border-radius: 15px;
    padding: 15px;
    margin: 10px;
    transition: transform 0.3s, box-shadow 0.3s;
    text-align: center;
}}
.movie-card:hover {{
    transform: scale(1.05);
    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
}}
.movie-card img {{
    border-radius: 10px;
}}
.movie-card h3 {{
    font-size: 18px;
    color: #ffffff;
    text-shadow: 1px 1px 2px #000000;
}}
.movie-card a {{
    color: #ffffff;
    text-decoration: none;
    font-size: 16px;
    font-weight: bold;
}}
.movie-card a:hover {{
    color: #007BFF;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ffffff; text-shadow: 2px 2px 4px #000000;'>CineMatch: Your Personalized Movie Guide</h1>", unsafe_allow_html=True)
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
    recommended_movie_names, recommended_movie_posters, recommended_movie_watch_urls = recommend(selected_movie)
    if recommended_movie_names:
        cols = st.columns(len(recommended_movie_names))  # Adjust number of columns based on the number of recommendations
        for col, name, poster, watch_url in zip(cols, recommended_movie_names, recommended_movie_posters, recommended_movie_watch_urls):
            with col:
                st.markdown(f"""
                <div class='movie-card'>
                    <h3>{name}</h3>
                    <img src='{poster}' alt='{name}' style='width:100%;'>
                    <a href='{watch_url}' target='_blank'>WATCH</a>
                </div>
                """, unsafe_allow_html=True)
