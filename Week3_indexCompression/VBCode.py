# N19DCCN085 - Đỗ Tấn Kha
# N19DCCN125 - Cao Thanh Nhàn
# N19DCCN135 - Vũ Thị Hồng Oanh

from define import *
# Variable bytes codes
def vbEncodeNumber(number):
    bytes = []
    while True:
        bytes.insert(0, number % 128)
        if number < 128:
            break
        number //= 128
    bytes[-1] += 128  
    bytes = map(lambda x: ((8-len(bin(x)[2:]))*"0" + bin(x)[2:]), bytes)
    return bytes

def vbEncode(numbers):
    bytes_list = []
    for number in numbers:
        bytes_list.extend(vbEncodeNumber(number))
    return "".join(bytes_list)

def vbDecode(bytes):
    bytes = [bytes[i:i+8] for i in range(0, len(bytes), 8)]
    numbers =[]
    number = 0
    for byte in bytes:
        byte = int(byte, 2)
        if byte < 128:
            number = 128 * number + byte
        else:
            number = 128 * number + (byte - 128)
            numbers.append(number)
            number = 0
    return numbers

if __name__ == '__main__':

    with open(path_VBCode, "w") as f:
        for word in Inverted_Index:
            postings = Inverted_Index[word]
            distances = [postings[0], *[postings[i] - postings[i-1] for i in range(1,len(postings) )]]
            f.write(vbEncode(distances))
            f.write("\n")

