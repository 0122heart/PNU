N = int(input())

bid = {}
for i in range(N) :
    name, money = input().split()
    money = int(money)
    if money in bid :
        bid[money].append(name)
    else :
        bid[money] = [name]

bidders = [i for i in bid.keys()]; bidders.sort(reverse = True)

winner = ''

for i in bidders :
    temp = bid[i]
    if(len(temp) == 1) :
        winner = temp[0]
        break

if(winner) :
    print(winner)
else :
    print('NONE')
