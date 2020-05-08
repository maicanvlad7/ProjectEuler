init = 2520
flag = 0

while not flag:
    count = 0
    print(init)
    for x in range(1,21):
        if init % x == 0:
            count = count + 1
    if count == 20:
        flag = 1
        print(init)
    else:
        init = init + 2520

