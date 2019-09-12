import datetime
calday = 1
calsec = 0
calnow = 1

last = datetime.datetime(2019,7,10,18, 0, 0)
now  = datetime.datetime(2019,5,30,23,15, 0)
if calnow:
    now = datetime.datetime.now()
print("last : {}".format(last))
print("now  : {}".format(now))

out = last-now
print(out)

day = out.days if calday else 0
sec = out.seconds
if out.microseconds != 0 :
    sec+=1

sec += day*24*3600
if calsec==0:
    sec += (60-sec%60)%60

if sec>=0:
    sequence_n = int(((sec*8+1)**0.5-1)*0.5)
    sequence_x = sec - sequence_n*(sequence_n+1)/2
    print("sec : {}".format(sec))
    print("sequence : {} , {}".format(sequence_n,sequence_x))

    bin_list = []

    bin_cnt=0
    two = 1
    temp = sec
    while temp !=0:
        if temp%2 :
            bin_list.append(two)
            bin_cnt+=1
        else :
            bin_list.append(0)
        temp //=2
        two=two<<1

    print("bin count : {}".format(bin_cnt))
    print(', '.join(map(str,bin_list)))
else :
    print("time < 0")
    
