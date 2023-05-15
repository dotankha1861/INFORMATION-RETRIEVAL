# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

from define import *


class BlockedStorage:
    def __init__(self, string = "", firstPtrBlocks = None):
        self.string = string
        self.firstPtrBlocks = [] if firstPtrBlocks == None else firstPtrBlocks

def saveFile(blockedStorage):
    with open(path_blockedStorage, "w") as f:
        f.write(blockedStorage.string)
        f.write("\n")
        for block_ptr in blockedStorage.firstPtrBlocks:
            f.write(str(block_ptr))   
            f.write("\n")

def loadFile(blockedStorage):
    t1 = time.time()
    with open(path_blockedStorage, "r") as f:
        blockedStorage.string = f.readline().replace("\n","")
        for block_ptr in f.readlines():
            blockedStorage.firstPtrBlocks.append(int(block_ptr.replace("\n","")))

    t2 = time.time()        
    return [t2 - t1, asizeof.asizeof(blockedStorage)/2**20, os.path.getsize(path_blockedStorage)/2**10]

if __name__ == '__main__':

    blockedStorage = BlockedStorage()

    for i, word in enumerate(Inverted_Index):

        if( i % K == 0):
            blockedStorage.firstPtrBlocks.append(len(blockedStorage.string))

        blockedStorage.string += str(len(word)) + word

    saveFile(blockedStorage)

        
