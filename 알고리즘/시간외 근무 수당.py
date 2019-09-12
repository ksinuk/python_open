time = 0.0
for i in range(5):
    a,b = map(float,input().split())
    temp = b-a-1 if b-a > 1.0 else 0.0
    temp = 4 if temp>4 else temp
    time += temp

money = time*10000
if time>=15:
    money *= 0.95
elif time<=5:
    money *= 1.05

print(int(money))



