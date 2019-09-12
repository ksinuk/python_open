import sys
sys.stdin = open("pizza_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    size , pizza_num = map(int , input().split())
    pizzas = list(map(int , input().split()))
    ok = [-1 for i in range(pizza_num)]
    ok_i = 0
    pizza_i = 0
    obun = [-1 for i in range(size)]
    index = 0
    
    while 1:
        if obun[index]==-1 and pizza_i < pizza_num:
            obun[index] = pizza_i
            pizzas[pizza_i] //=2
            pizza_i +=1
        elif obun[index]>=0:
            pizza = obun[index]
            if pizzas[pizza]:
                pizzas[pizza] //=2
            else:
                ok[ok_i] = pizza
                ok_i+=1
                if pizza_i < pizza_num:
                    obun[index] = pizza_i
                    pizzas[pizza_i] //=2
                    pizza_i +=1
                else:
                    obun[index] = -1
        index = (index+1)%size
        if ok_i == pizza_num:break      
    
    
    out = ok[ok_i-1]
    print(f"#{test_case} {out+1}")
