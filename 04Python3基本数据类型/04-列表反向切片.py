#!/usr/bin/python3

def reverseWords(input):

    # 用空格将字符串分隔成列表
    stringList = input.split(' ')

    # 列表反向切片，input自动转换成列表
    input = stringList[-1::-1]

    output = ' '.join(input)

    return output

if __name__ == "__main__":
    input = 'I like OpFancy'
    rw = reverseWords(input)
    print(rw)
