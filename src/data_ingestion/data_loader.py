import os
import pandas as pd
from src.logger import logger
from src.exception import CustomException

# project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# paths
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")

def load_data():
    try:
        movies_path = os.path.join(RAW_DIR, "C:\\Users\\krish\\Desktop\\Movie_Recommender_System\\data\\raw\\tmdb_5000_movies.csv")
        credits_path = os.path.join(RAW_DIR, "C:\\Users\\krish\\Desktop\\Movie_Recommender_System\\data\\raw\\tmdb_5000_credits.csv")

        movies = pd.read_csv(movies_path)
        credits = pd.read_csv(credits_path)

        logger.info(f"Movies loaded: {movies.shape}")
        logger.info(f"Credits loaded: {credits.shape}")

        return movies, credits

    except Exception as e:
        raise CustomException(f"Loading CSVs failed: {e}")


if __name__ == "__main__":
    movies_df, credits_df = load_data()
    print(movies_df.head())
    print(credits_df.head())
