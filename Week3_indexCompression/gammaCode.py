# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

from define import *
def gamma_encode(nums):
    string = ""
    for num in nums:
        if num == 1:
            string += '0'
        else:
            binary = bin(num)[2:]
            offset = binary[1:]
            length = '1' * len(offset) +'0'
            gamma_code =length + offset
            string += gamma_code
    return string

def gamma_decode(gamma_code):
    gaps = []
    while gamma_code != "": 
        bit0 = gamma_code.index("0")
        string = gamma_code[:2*bit0+1]
        if string == '0':
            gaps.append(1)
        else:
            length = string.index('0') + 1
            offset = string[length:]
            gaps.append(int('1' + offset, 2))
        gamma_code = gamma_code[2*bit0+1:]
    return gaps

if __name__ == "__main__":

    with open(path_gammaCode, "w") as f:
        for word in Inverted_Index:
            postings = Inverted_Index[word]
            distances = [postings[0], *[postings[i] - postings[i-1] for i in range(1,len(postings) )]]
            f.write(gamma_encode(distances))
            f.write("\n")


