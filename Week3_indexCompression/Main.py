# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

import arrayFixedWidth as AFW
import asString as AS
import blockedStorage as BS
import frontCoding as FC
import numpy as np
import pandas as pd
import VBCode
import gammaCode
from define import *

print("\nGIẢI MÃ VBCODE")
postings_VB = []
with open(path_VBCode) as f:
    for gaps in f.readlines():
        gaps = gaps.replace("\n", "")
        postings_VB.append([gaps, VBCode.vbDecode(gaps)])
df = pd.DataFrame(postings_VB, columns=["VB Code", "decode gaps"])
print(df)

print("\nGIẢI MÃ GAMMACODE")
postings_Gamma = []
with open(path_gammaCode) as f:
    for gaps in f.readlines():
        gaps = gaps.replace("\n", "")
        postings_Gamma.append([gaps, gammaCode.gamma_decode(gaps)])    
df = pd.DataFrame(postings_Gamma, columns=["Gamma Code", "decode gaps"])
print(df)

arrayFW = AFW.ArrayFixedWidth()
asString = AS.AsString()
blockedStorage = BS.BlockedStorage()
frontCoding = FC.FrontCoding()

df = pd.DataFrame(
    np.asarray([AFW.loadFile(arrayFW), AS.loadFile(asString), BS.loadFile(blockedStorage), FC.loadFile(frontCoding)]),
    index = ["Array Fixed-With", "As string", "Blocked Storage", "Front-Coding"],
    columns = ["Loading Time (s)", "Size of memory (MB)", "Size of file (KB)"]
)

print(df.to_string(justify='center', col_space=25))

############################################################################################
