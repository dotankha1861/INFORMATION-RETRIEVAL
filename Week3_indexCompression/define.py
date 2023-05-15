# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

import numpy as np
from pympler import asizeof
import os
import time

K = 4
Inverted_Index = np.load("./invertedIndex.npy", allow_pickle=True).item()

path_arrayFN = './Storage/arrayFixedWidth.txt'
path_asString = './Storage/asString.txt'
path_blockedStorage = "./Storage/blockedStorage.txt"
path_frontCoding = "./Storage/frontCoding.txt"

path_VBCode = "./Storage/VBCode.txt"
path_gammaCode = "./Storage/gammaCode.txt"

