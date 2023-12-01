def findindex(line, time) :
    for i in range(1, len(line)) :
        if (line[i-1] <= time and time < line[i]) :
            return (time - line[i-1], i-1)

N = int(input())

cord = []

for i in range(N) :
    temp = list(map(int, input().split()))
    cord.append(temp)

line = [0]

lencord = len(cord)

for i in range(lencord - 1) :
    temp = abs(cord[i][1] - cord[i+1][1]) + abs(cord[i][0] - cord[i+1][0])
    line.append(line[-1] + temp)

line.append(line[-1] + abs(cord[0][1] - cord[-1][1]) + abs(cord[0][0] - cord[-1][0]))

time = [i % line[-1] for i in map(int, input().split())]

cord.append(cord[0])

for i in time :
    length, whatcord = findindex(line, i)

    if(cord[whatcord][0] != cord[whatcord+1][0]) : # x좌표 다름
        if(cord[whatcord][0] < cord[whatcord+1][0]) : # x좌표 증가
            print(cord[whatcord][0] + length, cord[whatcord][1])
        else : # x좌표 감소
            print(cord[whatcord][0] - length, cord[whatcord][1])

    else :
        if(cord[whatcord][1] < cord[whatcord+1][1]) : # y좌표 증가
            print(cord[whatcord][0], cord[whatcord][1] + length)
        else : # y좌표 감소
            print(cord[whatcord][0], cord[whatcord][1] - length)
