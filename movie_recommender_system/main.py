import streamlit as st
import pickle
import pandas as pd

def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    rec_m = []

    for i in movies_list:
        rec_m.append(movies.iloc[i[0]].title)
    return rec_m

movie_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie = st.selectbox(
    'How would you like to be contacted',
    movies['title'].values
)

if st.button('Find'):
    rec_m = recommended(selected_movie)
    for i in rec_m:
        st.write(i)