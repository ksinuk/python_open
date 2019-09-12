def my_strrev(strx):
    stry = ''

    for i in range(len(strx)):
        stry+=strx[len(strx) - 1 - i]

    return stry

strx = input()
stry = my_strrev(strx)
print(stry)