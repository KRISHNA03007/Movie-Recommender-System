import pandas as pd
from src.preprocess.data_preprocess import PREPROCESSED_FILE
from src.models.model import build_tfidf_matrix, compute_similarity

# Load preprocessed data
df = pd.read_csv(PREPROCESSED_FILE)

# Build TF-IDF and similarity matrix
tfidf, tfidf_matrix = build_tfidf_matrix(df)
similarity = compute_similarity(tfidf_matrix)

# Recommendation function
def recommend(movie):
    movie = movie.lower()
    if movie not in df['title'].str.lower().values:
        print(f"Movie '{movie}' not found.")
        return
    index = df[df['title'].str.lower() == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    print(f"Top 5 recommendations for '{movie.title()}':")
    for i in distances[1:6]:
        print("-", df.iloc[i[0]]['title'])

# Example test
recommend("The Dark Knight")
