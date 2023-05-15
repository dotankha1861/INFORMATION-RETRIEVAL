# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

import processing
import numpy as np
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

class Incidence_Matrix:

    def __init__(self, path_matrix, path_documents, path_vocabs):
        self.matrix = np.load(path_matrix, allow_pickle=True)
        self.vocabs = np.load(path_vocabs, allow_pickle=True)
        self.documents = np.load(path_documents, allow_pickle=True)

    # lấy các docID và doc từ vector bit
    def get_documents(self, vectorResult):
        results = []
        for i in range(len(vectorResult)): 
            if vectorResult[i]==1:
                results.append([i+1, self.documents[i]])
        return results
    
    # lấy binary vector của 1 từ
    def get_row(self, word):
        return self.matrix[np.where(self.vocabs == word)[0][0]]
    
    # and 2 binary vector
    def and_2_binvec(self, word1, word2):
        return [a and b for a, b in zip(word1, word2)]
    
    # lấy kết quả trả về (vector bit) từ câu query truyền vào
    def query(self, str_query):

        # tách các thành phần trong câu query 
        tokens = str_query.lower().split()
        tokens = [word for word in tokens if word not in stop_words]
 
        # Thực hiện câu query      
        try:  
            vectorResult = self.get_row(tokens.pop())
            while len(tokens) != 0:
                vectorResult = self.and_2_binvec(vectorResult , self.get_row(tokens.pop()))
            return vectorResult    
        except IndexError:
            return list(np.zeros(len(self.documents)))

if __name__ == "__main__":

    Matrix = Incidence_Matrix("./incidenceMatrix.npy", "./documents.npy", "./vocabs.npy")

    queries = processing.load_query()

    for j, query in enumerate(queries):
        print("Query", j +1, ":", query)
        vectorResult = Matrix.query(query)
        results = Matrix.get_documents(vectorResult)
        for result in results:
            print("Document", result[0], ":", result[1])
        print("\n/\n")