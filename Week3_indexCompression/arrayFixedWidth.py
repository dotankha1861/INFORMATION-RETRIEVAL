# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

from define import *

class ArrayFixedWidth:
    def __init__(self, terms = None):
        self.terms = [] if terms == None else terms

def saveFile(arrayFW):
    with open(path_arrayFN, "w") as f:
        for term in arrayFW.terms:
            f.write(term)
            f.write("\n")

def loadFile(arrayFW):
    t1 = time.time()
    with open(path_arrayFN, "r") as f:
        data = f.readlines()
    for term in  data:    
        arrayFW.terms.append(term.replace("\n",""))
    t2 = time.time()        
    return [t2 - t1, asizeof.asizeof(arrayFW)/2**20, os.path.getsize(path_arrayFN)/2**10]

if __name__ == '__main__':

    arrayFW = ArrayFixedWidth()

    for word in Inverted_Index:

        arrayFW.terms.append(word) 

    saveFile(arrayFW)

