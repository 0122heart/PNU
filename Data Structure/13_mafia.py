class Mafia :
    def __init__(self, name = "", boss = "") :
        self.name = name
        self.boss = boss
        self.under = []
        self.numUnder = 0
        self.bossExist = True
        self.numBoss = 0

    def addUnder(self, under) :
        self.under.append(under)

    def addBoss(self, boss) :
        self.bossNode = boss


def main() :
    mafiaGroup = f_input()
    f_setUnder(mafiaGroup)
    f_setBoss(mafiaGroup)
    f_sort(mafiaGroup)
    f_print(mafiaGroup)

def f_input() :
    numMafia = int(input())
    allMafia = set() # 모든 마피아 조직원
    withoutBoss = set() # 보스 뺀 마피아 조직원들
    listMafia = []

    for i in range(numMafia - 1) :
        name, boss = input().split()
        allMafia.add(boss)
        allMafia.add(name)
        withoutBoss.add(name)
        listMafia.append(Mafia(name, boss))

    chiefBoss = (allMafia - withoutBoss).pop() # 최종 보스 구하기

    temp = Mafia(chiefBoss)
    temp.bossExist = False
    listMafia.append(temp)

    return listMafia

def f_setUnder(mafiaGroup) :
    for i in mafiaGroup :
        for j in mafiaGroup :
            if(i.name == j.boss) :
                i.addUnder(j)

def f_setBoss(mafiaGroup) :
    for i in mafiaGroup :
        for j in mafiaGroup :
            if(i.boss == j.name) :
                i.addBoss(j)

def f_sort(mafiaGroup) :
    for i in mafiaGroup :
        i.numUnder = f_getNumUnder(i)
        i.numBoss = f_getNumBoss(i)
    mafiaGroup.sort(key = f_standard)

def f_getNumUnder(mafia) :
    if(mafia.under) : # 부하가 한명이라도 있다면
        num = 0
        for i in mafia.under : # 후임이 한명이라도 있다면
            num += 1 + f_getNumUnder(i)
        return num
    else :
        return 0

def f_getNumBoss(mafia) :
    num = 0
    if(mafia.bossExist) :
        num += 1 + f_getNumBoss(mafia.bossNode)
        return num
    else :
        return 0



def f_standard(x) :
    return (-x.numUnder, x.numBoss, x.name)

def f_print(mafiaGroup) :
    for i in mafiaGroup :
        print(i.name)

main()
