import sys
sys.stdin = open("Forth_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    strx = input().split()
    stack = [0 for i in range(256)]
    index = 0
    cals = ['+', '-', '*', '/']
    out = 'error'

    for c in strx:
        if c in cals:
            if index < 2: break
            b = stack[index - 1]
            index -= 1
            a = stack[index - 1]
            index -= 1

            if c == '+':
                stack[index] = a + b
                index += 1
            elif c == '-':
                stack[index] = a - b
                index += 1
            elif c == '*':
                stack[index] = a * b
                index += 1
            elif c == '/':
                stack[index] = a // b
                index += 1
        elif c == '.':
            if index == 1:
                out = stack[0]
            break
        else:
            stack[index] = int(c)
            index += 1

    print(f"#{test_case} {out}")





