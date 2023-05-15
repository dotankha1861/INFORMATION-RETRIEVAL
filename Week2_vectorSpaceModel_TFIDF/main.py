# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

import numpy as np
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

stop_words = set(stopwords.words('english'))

def load_data(path):
    with open(path, 'r') as f:
        data = f.read()
    ID_data = data.lower().replace("\n"," ").split("/")
    ID_data.pop()
    data = []
    for datum in ID_data:
        datum = datum.strip()
        index = datum.find(" ")
        data.append(datum[index+1:]) 
    return data

def tokenize_and_remove_stopwords(doc):
    tokens = word_tokenize(re.sub(r'[^\w\s]', '', doc).lower())
    filtered_tokens = filter(lambda token: token not in stop_words, tokens)
    return list(filtered_tokens)

def computeTFIDF(list_words_docs):  
    # Tạo tập từ 
    unique_words = list(set.union(*map(set, list_words_docs)))

    # Tạo ma trận biểu diễn w_tf
    counters = list(map(Counter, list_words_docs))
    matrix = np.zeros((len(list_words_docs), len(unique_words)))
    word_dict = {word: i for i, word in enumerate(unique_words)}
    for i, counter in enumerate(counters):
        word_indices = [word_dict[word] for word in counter.keys()]
        tf = np.fromiter(counter.values(), dtype=int)
        w_tf = 1 + np.log10(tf)
        matrix[i][word_indices] = w_tf
    # Time ~ 0.42s

    # Tạo vector biểu diễn idf  
    df = dict.fromkeys(unique_words, 0)
    for row in counters:
        for word in row.keys():
            df[word] += 1
    idf = np.asarray(list(map(lambda word: np.log10(len(list_words_docs)/df[word]), unique_words)))  
    # Time ~ 0.09s
    # Other: matrix_idf = np.log10(len(wordDocs)/np.count_nonzero(matrix_w_tf, axis=0)) ~ 0.4s
    
    # Tạo ma trận tf-idf
    for i in range(matrix.shape[0]):
        matrix[i] *= idf
    # Time ~ 0.3s
    # Other: w_tf_idf_matrix = matrix_w_tf * matrix_idf[np.newaxis,:] ~ 0.37s
    return  unique_words, idf, matrix

def cosin_similarity(vector_query, matrix):

    # Tính giá trị Cosine = (chia mỗi phần tử cho độ dài vector chứa nó) * (vector đầu <biểu diễn doc hỏi>)
    vector_query = vector_query / np.sqrt(np.sum(np.square(vector_query)))
    
    for row in range(matrix.shape[0]):
       matrix[row] = matrix[row] / np.sqrt(np.sum(np.square(matrix[row]))) * vector_query

    cosineSims = np.sum(matrix, axis = 1)
    return  cosineSims, np.argsort(-cosineSims)

def transform_vector_TFIDF(tokens, feature_names, idf):
    # transform
    counter = Counter(tokens)
    vector_query = np.zeros((1, len(feature_names)))
    for word in counter.keys():
        if word in feature_names:
            vector_query[0][feature_names.index(word)] = 1 + np.log10(counter[word])

    return vector_query * idf

if __name__ == "__main__":

    # tokenzie, loại bỏ stop-words
    documents = load_data("./doc-text")
    list_words_docs = list(map(lambda doc: tokenize_and_remove_stopwords(doc), documents))

    print("Generating TFIDF matrix from documents...")
    feature_names, idf, matrix_tfidf = computeTFIDF(list_words_docs)
    
    # Phần truy vấn
    queries = load_data("./query-text")
    list_words_queries = list(map(lambda doc: tokenize_and_remove_stopwords(doc), queries))

    for i in range(len(list_words_queries)):
        # transform:
        vector_query = transform_vector_TFIDF(list_words_queries[i], feature_names, idf)
        # ranking
        scores, indicies = cosin_similarity(np.array(vector_query), np.array(matrix_tfidf))
        print("Query", i+1, ":", queries[i])
        print("Best (doc", indicies[0] + 1, ",", "score", scores[indicies][0], "):", documents[indicies[0]])
        print("Ranking (top 10):", indicies[:10] + 1)
        print("\n/\n")

