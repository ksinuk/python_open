def mystrcmp(str1,str2):
    if len(str1)==len(str2):
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                return False
        return True
    return False

a="abcde"
b="abcde"
print(mystrcmp(a,b))