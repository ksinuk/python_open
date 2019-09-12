import sys
sys.stdin = open("초콜릿_공장.txt","r")

def two_choco(company):
    is_error = 0
    for i in range(len(company)):
        c = company[i]
        company[i] = 0
        if c in company:
            is_error = 1
            break
        else:
            company[i] = c
    return is_error

test_case = int(input())
out = 0
for __ in range(test_case):
    lotte , haetae = input().split()
    lotte , haetae = list(lotte) , list(haetae)

    if two_choco(lotte) or two_choco(haetae):
        out +=1
        continue

    same = 0
    for c in lotte:
        if c in haetae:
            same+=1
    
    if same>2:
        out+=1 
#--------------------
print(out)

    



