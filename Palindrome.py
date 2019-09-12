def palindrome(strx):
    index = len(strx)//2

    for i in range(index):
        if strx[i] !=strx[len(strx)-1-i]:
            return 'false'
    
    return 'true'



# -------------------------
strx = 'aaabbcbbaaa'

print(palindrome(strx))