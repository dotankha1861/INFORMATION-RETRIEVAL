# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

from define import *

class AsString:
    def __init__(self, string = "", term_ptrs = None):
        self.string = string
        self.term_ptrs = [] if term_ptrs == None else term_ptrs


def saveFile(asString):
    with open(path_asString, "w") as f:
        f.write(asString.string)
        f.write("\n")
        for term in asString.term_ptrs:
            f.write(str(term))
            f.write("\n")

def loadFile(asString):
    t1 = time.time()
    with open(path_asString, "r") as f:
        asString.string = f.readline().replace("\n","")
        for term in f.readlines():
            asString.term_ptrs.append(int(term.replace("\n","")))
    t2 = time.time()        
    return [t2 - t1, asizeof.asizeof(asString)/2**20, os.path.getsize(path_asString)/2**10]

if __name__ == '__main__':

    asString = AsString()

    for word in Inverted_Index:

        asString.term_ptrs.append(len(asString.string)) 
        
        asString.string += word

    saveFile(asString)

