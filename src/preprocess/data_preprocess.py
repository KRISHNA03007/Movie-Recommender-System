import os
import pandas as pd
import ast
from src.logger import logger
from src.exception import CustomException
from src.data_ingestion.data_loader import load_data

# -----------------------------
# Paths
# -----------------------------
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREPROCESSED_DIR = PREPROCESSED_DIR = r"C:\Users\krish\Desktop\Movie_Recommender_System\data\preprocessed"
os.makedirs(PREPROCESSED_DIR, exist_ok=True)
PREPROCESSED_FILE = os.path.join(PREPROCESSED_DIR, "movies_preprocessed.csv")

# -----------------------------
# Preprocessing Functions
# -----------------------------
def merge_movies_credits(movies: pd.DataFrame, credits: pd.DataFrame) -> pd.DataFrame:
    """Merge movies and credits on title."""
    try:
        merged_df = movies.merge(credits, on="title")
        logger.info(f"Merged movies and credits: {merged_df.shape}")
        return merged_df
    except Exception as e:
        raise CustomException(f"Merging movies and credits failed: {e}")


def select_and_dropna(df: pd.DataFrame) -> pd.DataFrame:
    """Select relevant columns and drop rows with missing values."""
    try:
        df = df[['movie_id','title','overview','genres','keywords','cast','crew']]
        df.dropna(inplace=True)
        logger.info(f"After selecting columns and dropping NA: {df.shape}")
        return df
    except Exception as e:
        raise CustomException(f"Selecting columns and dropping NA failed: {e}")


def convert_column_to_list(text: str) -> list:
    """Convert stringified list of dicts to list of 'name' values."""
    try:
        return [i['name'] for i in ast.literal_eval(text)]
    except Exception as e:
        raise CustomException(f"Converting column to list failed: {e}")


def get_top_n_items(text: str, n=3) -> list:
    """Return top n items from a list of dicts."""
    try:
        return [i['name'] for i in ast.literal_eval(text)][:n]
    except Exception as e:
        raise CustomException(f"Fetching top {n} items failed: {e}")


def fetch_director(text: str) -> list:
    """Fetch director(s) from crew column."""
    try:
        return [i['name'] for i in ast.literal_eval(text) if i['job'] == "Director"]
    except Exception as e:
        raise CustomException(f"Fetching director failed: {e}")


def collapse_list(L: list) -> list:
    """Remove spaces from strings in a list."""
    return [i.replace(" ","") for i in L]


def preprocess_movies(movies: pd.DataFrame) -> pd.DataFrame:
    """Full preprocessing pipeline."""
    try:
        # Convert columns
        movies['genres'] = movies['genres'].apply(convert_column_to_list)
        movies['keywords'] = movies['keywords'].apply(convert_column_to_list)
        movies['cast'] = movies['cast'].apply(get_top_n_items)
        movies['crew'] = movies['crew'].apply(fetch_director)

        # Collapse lists
        for col in ['cast','crew','genres','keywords']:
            movies[col] = movies[col].apply(collapse_list)

        # Split overview into list of words
        movies['overview'] = movies['overview'].apply(lambda x: x.split())

        # Create combined 'tags' column
        movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

        # Final DataFrame with only necessary columns
        df_final = movies[['movie_id','title','tags']].copy()
        df_final['tags'] = df_final['tags'].apply(lambda x: " ".join(x))

        logger.info(f"Preprocessing complete: {df_final.shape}")
        return df_final
    except Exception as e:
        raise CustomException(f"Preprocessing movies failed: {e}")


def save_preprocessed(df: pd.DataFrame, filepath: str = PREPROCESSED_FILE):
    """Save the preprocessed DataFrame to CSV."""
    try:
        df.to_csv(filepath, index=False)
        logger.info(f"Preprocessed CSV saved at {filepath}")
    except Exception as e:
        raise CustomException(f"Saving preprocessed CSV failed: {e}")


# -----------------------------
# Main execution
# -----------------------------
if __name__ == "__main__":
    try:
        # Load raw data
        movies_df, credits_df = load_data()

        # Preprocessing pipeline
        merged_df = merge_movies_credits(movies_df, credits_df)
        cleaned_df = select_and_dropna(merged_df)
        preprocessed_df = preprocess_movies(cleaned_df)

        # Save preprocessed CSV
        save_preprocessed(preprocessed_df)

        print(preprocessed_df.head())
    except CustomException as e:
        logger.error(e)
