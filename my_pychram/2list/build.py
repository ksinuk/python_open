import sys

#-------------------------------------------
def main_cal(size,data):
    out = 0
    for i in range(2,size-2):
        a,b,c,d=data[i-2],data[i-1],data[i+1],data[i+2]
        max = 0
        if a >=b and a>=c and a>=d:max =a
        elif b >=a and b>=c and b>=d:max =b
        elif c >= a and c >= b and c >= d:max = c
        elif d >= a and d >= b and d >= c:max = d

        if data[i]>max:out+=data[i]-max
    return out

# -----------------------------------------
sys.stdin = open("input.txt")

for index in range(1, 11):
    n = int(input())
    li = input().split()
    li = list(map(int, li))
    out = main_cal(n,li)
    print(f"#{index} {out}")