# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

import numpy as np
import pandas as pd
from main import tokenize_and_remove_stopwords, computeTFIDF, cosin_similarity, transform_vector_TFIDF

documents = ["Bảo hiểm ô tô bảo hiểm xe máy", "Bảo hiểm tốt nhất", "ô tô tốt hơn xe máy", "bảo hiểm ô tô tốt nhất"]
query = "bảo hiểm ô tô tốt nhất"

if __name__ == "__main__":

    # tokenzie, loại bỏ stop-words
    list_words_docs = list(map(lambda doc: tokenize_and_remove_stopwords(doc), documents))

    feature_names, idf, matrix_tfidf = computeTFIDF(list_words_docs)

    list_words_queries = tokenize_and_remove_stopwords(query)

    vector_query = transform_vector_TFIDF(list_words_queries, feature_names, idf)

    scores, indicies = cosin_similarity(np.array(vector_query), np.array(matrix_tfidf))

    index = ["Query"]
    index.extend(["Doc " + str(i+1) for i in range(len(documents))])

    print("\nBẢNG GIÁ TRỊ TF-IDF")
    df = pd.DataFrame(
        np.concatenate((vector_query, matrix_tfidf), axis=0), 
        columns = feature_names, 
        index = index
    )
    print(df)

    print("\nBẢNG GIÁ TRỊ COSINE")
    df = pd.DataFrame(scores, columns = ["Cosine"], index = index[1:])
    df["Rank"] = [list(indicies).index(i) + 1 for i in range(len(documents))]
    print(df)
