# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

from define import *

class FrontCoding:
    def __init__(self, string = "", firstPtrBlocks = None):
        self.string = string
        self.firstPtrBlocks = [] if firstPtrBlocks == None else firstPtrBlocks

def saveFile(frontCoding):
    with open(path_frontCoding, "w") as f:
        f.write(frontCoding.string)
        f.write("\n")
        for block_ptr in frontCoding.firstPtrBlocks:
            f.write(str(block_ptr))   
            f.write("\n")

def loadFile(frontCoding):
    t1 = time.time()
    with open(path_frontCoding, "r") as f:
        frontCoding.string = f.readline().replace("\n","")
        for block_ptr in f.readlines():
            frontCoding.firstPtrBlocks.append(int(block_ptr.replace("\n","")))

    t2 = time.time()        
    return [t2 - t1, asizeof.asizeof(frontCoding)/2**20, os.path.getsize(path_frontCoding)/2**10]

def get_common_prefix(input_arr):
    str1 = input_arr[0]
    str2 = input_arr[len(input_arr) - 1]
    len1 = len(str1)
    len2 = len(str2)
    prefix = ""
    i = 0
    j = 0
    while i < len1 and j < len2:
        if str1[i] != str2[j]:
            break
        prefix += str1[i]
        i += 1
        j += 1
    return prefix

if __name__ == '__main__':

    frontCoding = FrontCoding()

    list_words = sorted(list(Inverted_Index.keys()))
    for i in range(0, len(list_words), K):
        frontCoding.firstPtrBlocks.append(len(frontCoding.string))
        common_prefix = get_common_prefix(list_words[i:i+K])
        len_common = len(common_prefix)
        frontCoding.string += str(len(list_words[i])) + common_prefix + "*" + list_words[i][len_common:]
        for j in range(i+1, i+K):
            if j == len(list_words):
                break
            frontCoding.string += str(len(list_words[j])-len_common) + "<>"+ list_words[j][len_common:]
    saveFile(frontCoding)