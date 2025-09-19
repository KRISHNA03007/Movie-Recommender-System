import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.logger import logger
from src.exception import CustomException
from src.preprocess.data_preprocess import PREPROCESSED_FILE

# Ensure models folder exists
MODELS_DIR = "C:\\Users\\krish\\Desktop\\Movie_Recommender_System\\model"
os.makedirs(MODELS_DIR, exist_ok=True)

MOVIE_LIST_FILE = os.path.join(MODELS_DIR, "movie_list.pkl")
SIMILARITY_FILE = os.path.join(MODELS_DIR, "similarity.pkl")

# Load preprocessed data
def load_preprocessed_data(filepath=PREPROCESSED_FILE) -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath)
        logger.info(f"Loaded preprocessed data: {df.shape}")
        return df
    except Exception as e:
        raise CustomException(f"Loading preprocessed CSV failed: {e}")

# TF-IDF Vectorizer
def build_tfidf_matrix(df: pd.DataFrame, max_features=5000):
    try:
        tfidf = TfidfVectorizer(max_features=max_features, stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df['tags']).toarray()
        logger.info(f"TF-IDF matrix created with shape: {tfidf_matrix.shape}")
        return tfidf, tfidf_matrix
    except Exception as e:
        raise CustomException(f"TF-IDF vectorization failed: {e}")

# Cosine Similarity
def compute_similarity(tfidf_matrix):
    try:
        similarity = cosine_similarity(tfidf_matrix)
        logger.info("Cosine similarity matrix computed")
        return similarity
    except Exception as e:
        raise CustomException(f"Computing cosine similarity failed: {e}")

# Save models
def save_models(df: pd.DataFrame, similarity_matrix):
    try:
        pickle.dump(df, open(MOVIE_LIST_FILE, 'wb'))
        pickle.dump(similarity_matrix, open(SIMILARITY_FILE, 'wb'))
        logger.info(f"Models saved at {MODELS_DIR}")
    except Exception as e:
        raise CustomException(f"Saving models failed: {e}")

# Main execution
if __name__ == "__main__":
    try:
        df = load_preprocessed_data()
        tfidf, tfidf_matrix = build_tfidf_matrix(df)
        similarity = compute_similarity(tfidf_matrix)
        save_models(df, similarity)
        print("TF-IDF, similarity matrix built and models saved successfully!")
    except CustomException as e:
        logger.error(e)
