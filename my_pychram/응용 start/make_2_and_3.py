import random
fin = open("정식이의_은행업무_input.txt", "w")
fout = open("정식이의_은행업무_check.txt","w")

def make2and3(x,n):
    out = ''
    while x>=n:
        x , temp = divmod(x,n)
        out+=str(temp)
    out+=str(x)
    out = out[::-1]
    # 변화 완료 , 오류 생성 시작
    out = list(out)
    point = random.randint(0,len(out)-1)
    temp = (int(out[point])+random.randint(1,n-1))%n
    out[point] = str(temp)

    return ''.join(out)
    

size = 20
fin.write(str(size)+'\n')
out="1010\n212\n"
fin.write(out)
fout.write("#1 14\n")

for index in range(2,size+1):
    num = random.randint(2**40,2**41)
    fout.write("#{} {}\n".format(index,num))

    num2 = make2and3(num,2)
    num3 = make2and3(num,3)
    fin.write("{}\n{}\n".format(num2,num3))  

fin.close()
fout.close()

