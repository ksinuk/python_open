r = int(input())
out = 0
for x in range(1,r+1):
    out += int((r*r-x*x)**0.5)

out*=4
print(out)