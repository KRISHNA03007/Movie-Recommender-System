from src.data_ingestion.data_loader import load_data
from src.preprocess.data_preprocess import (
    merge_movies_credits,
    select_and_dropna,
    preprocess_movies,
    save_preprocessed
)
from src.models.model import build_tfidf_matrix, compute_similarity
from src.logger import logger
from src.exception import CustomException

def main():
    try:
        movies_df, credits_df = load_data()
        merged_df = merge_movies_credits(movies_df, credits_df)
        cleaned_df = select_and_dropna(merged_df)
        preprocessed_df = preprocess_movies(cleaned_df)
        save_preprocessed(preprocessed_df)
        tfidf, tfidf_matrix = build_tfidf_matrix(preprocessed_df)
        similarity = compute_similarity(tfidf_matrix)
        print(preprocessed_df.head())
        print("Similarity matrix shape:", similarity.shape)
    except CustomException as e:
        logger.error(e)

if __name__ == "__main__":
    main()
