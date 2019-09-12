import random

N = 10
size = 12
large = size*10
small = 1

f = open("난수.txt","w")
f.write("{}\n".format(N))
f.write("5\n4 9 5 2 2 1 3 5 1 4\n")

for index in range(1,N):
    f.write("{}\n".format(size))

    for i in range(size*2):
        num = random.randint(small,large)
        text = "{} ".format(num)
        f.write(text)
    f.write('\n')

f.write("\n\n\nㅁㅁㅁㅁ\n\n\n")
f.close() 