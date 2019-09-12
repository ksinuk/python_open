import sys
sys.stdin = open("이진수_input.txt", "r")

def change(c):
    c = ord(c)
    return c-ord('A')+10 if c>=ord('A') else c-ord('0')

table = [i for i in range(16)]
for i in range(16):
    temp = ''
    for j in range(3,-1,-1):
        temp += '1' if i&(1<<j) else '0'
    table[i] = temp

T = int(input())
for test_case in range(1, T + 1):
    size,strx = input().split()
    size = int(size)

    out = ''
    for c in strx:
        out += table[change(c)]
    
    print("${} {}".format(test_case,out))

