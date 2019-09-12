def pi(pattern):
    maps = [-1]*(len(pattern)+1)
    j = -1
    for i in range(len(pattern)):
        while j>=0 and pattern[i] != pattern[j]:
            j = maps[j]
        j+=1
        maps[i+1] = j

    return maps

def find(text,pattern):
    maps = pi(pattern)
    j = 0
    for i in range(len(text)):
        while j>=0 and text[i] != pattern[j]:
            j = maps[j]

        j+=1
        if j==len(pattern):
            return i-j+1

    return -1

text = "Life is short, You need Python."
pattern = "Python"

out = find(text,pattern)
print("func   : {} \nanswer : {}".format(out,text.find(pattern)))

