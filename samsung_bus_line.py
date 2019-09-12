
text=[]
out_text_list=[]

test_case = int(input())

for index in range(1,test_case+1):
    line_num = int(input())
    line_list = []
    for i in range(line_num):
        temp = input()
        temp = temp.split()
        temp = list(map(int,temp))

        line_list.append(temp)
    
    station_num = int(input()) 
    station_list = []
    for i in range(station_num):
        station_list.append(int(input()))

    out_list = []

    for station in station_list:
        temp=0
        for line in line_list:
            if line[0] <= station and station<= line[1]:
                temp+=1
        out_list.append(str(temp))

    out_text = f'#{str(index)}'
    for c in out_list:
        out_text += ' '+c

    out_text_list.append(out_text)

for stry in out_text_list:
    print(stry)


    

    


