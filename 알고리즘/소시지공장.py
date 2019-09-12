import sys
sys.stdin = open("소시지공장.txt","r")
N = int(input())
# N = 1
 
class Ham:
    def __init__(self,l=0,w=0,start=0):
        self.l = l
        self.w = w
        self.start = start
 
    def __gt__(self,other):
        if self.l>=other.l and self.w>=other.w:return True
        else: return False
     
    def __lt__(self,other):
        if self.l<=other.l and self.w<=other.w:return True
        else: return False
     
hams = []
 
def cal_main(sizein):
    strx = list(map(int,input().split()))
    for i in range(sizein):
        l,w = strx[i*2] , strx[i*2+1]
 
        for j in range(len(hams)):
            if hams[j].l==l and hams[j].w ==w:
                break
        else:
            hams.append(Ham(l,w,0))
    size = len(hams)
 
    for i in range(size):
        for j in range(size):
            if i==j:continue
            elif hams[i]>hams[j]: hams[i].start+=1
 
    for i in range(size):
        for j in range(i,0,-1):
            if hams[j].start<hams[j-1].start:
                hams[j-1] , hams[j] = hams[j] , hams[j-1]
 
    cnt = 0
    for i in range(size):
        now = i 
        if hams[now].start<0: continue
        cnt+=1
 
        for j in range(now+1,size):
            if hams[j]>hams[now]:
                hams[j].start = -1
                now = j
     
    return cnt
 
 
for i in range(N):
    size = int(input())
    print("{}".format(cal_main(size)))
    hams = []