horizon = []
vertical = []
SumHorizon = 0; SumVertical = 0; hor = 0; ver = 0;


temp = list(map(int, input().split()))

for i in range(len(temp)//2) :
    horizon.append(temp[2*i])
    vertical.append(temp[2*i + 1])

SumHorizon = sum(horizon)
SumVertical = sum(vertical)

stair = [[0 for i in range(SuqkrmHorizon)] for j in range(SumVertical)]

ver = 0; hor = 0;

for i in range(len(horizon)) :
    hor += horizon[i]
    for j in range(ver, ver + vertical[i]) :
        for k in range(0, hor) :
            stair[j][k] = 1
    ver += vertical[i]

while(1) :
    try :
        x, y = map(int, input().split())
        if (SumHorizon < x or SumVertical < y) or (SumHorizon == x and vertical[-1] < y) or (horizon[0] < x and SumVertical == y) :
            print("out")

        elif SumHorizon == x or SumVertical == y :
            print("on")

        else :
            if stair[SumVertical - y -1][x] :
                print("in")

            elif stair[SumVertical - y][x - 1] :
                print("on")

            else :
                print("out")

    except :
        break
