import streamlit as st
import pickle
import pandas as pd
import requests


st.set_page_config('Movie Recommender', '🍿', "wide")

#Function to fetch poster for the movie.
def fetch_poster(movie_id):

    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

#Function that recommends 7 movies based on a moviename and it's tags.
def recommend(moviename):

    movie_index = movies[movies['title'] == moviename].index[0]
    distances = similarity[movie_index]                                 #distance from the given 'moviename' using the 'movie_index'.
    recommendations_list = sorted(list(enumerate(distances)), reverse=True, key =lambda x: x[1])[1:8]

    recommended_list = []
    recommended_list_posters = []

    for i in recommendations_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_list.append(movies.iloc[i[0]].title)
        recommended_list_posters.append(fetch_poster(movie_id))         #fetching poster from API and storing in a list.
    return recommended_list, recommended_list_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# 'selectbox' returns the selected option from the provided options.
Selected_Movie = st.selectbox("Search",
                              movies['title'].values)

if st.button('Recommend'):

    names, posters = recommend(Selected_Movie)                      #To get posters with moviename.
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col6:
        st.text(names[5])
        st.image(posters[5])

    with col7:
        st.text(names[6])
        st.image(posters[6])