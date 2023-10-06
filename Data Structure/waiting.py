def f_add(seats, operand) :
    for i in range(1, len(seats)) : # 앉을 자리 확인
            if(operand < seats[i][0]) : # 앉을 자리 찾음!
                seats[i - 1].append(operand)
                seats[i - 1].sort()
                f_check(i-1) # 사람 수 초과했는지 확인
                break

def f_delete(seats) :
    for i in range(len(seats)) :
        if(operand in seats[i]) :
            seats[i].remove(operand)
            if(not len(seats[i])) :
                seats.remove([])
            break

def f_check(index) :
    if(len(seats[index]) == 2*limit) : # 사람 수 초과했다면
        seats.append(seats[index][:limit])
        seats[index] = seats[index][limit:]
        seats.sort()


# main start

transaction, limit = map(int, input().split())
seats = [[],[10001]]

for i in range(transaction) :
    operator, operand = input().split()
    operand = int(operand)

    if(operator == '+') :
        f_add(seats, operand)
        # print(seats)
    else :
        f_delete(seats)
        # print(seats)

for i in range(len(seats)-1) :
    print(seats[i][0])