import math

class Fraction :
    def __init__(self, a, b) :
        if(isinstance(a, Fraction) or isinstance(b, Fraction)) :
            if(type(a) == int) :
                a = Fraction(a, 1)
            elif(type(b) == int) :
                b = Fraction(b, 1)
            self._numerator = a._numerator * b._denominator
            self._denominator = a._denominator * b._numerator
            self._gcd = math.gcd(self._numerator, self._denominator)
            self._numerator //= self._gcd
            self._denominator //= self._gcd

        else :
            self._gcd = math.gcd(a, b)
            self._numerator = a//self._gcd
            self._denominator = b//self._gcd

    def __add__(self, other) :
        newNumerator = self._numerator * other._denominator + other._numerator * self._denominator
        newDenominator = self._denominator * other._denominator
        newGcd = math.gcd(newNumerator, newDenominator)
        return Fraction(newNumerator//newGcd, newDenominator//newGcd)

def calc(stdin) :
    storage = []
    while(1) :
        if(len(storage) == 3) :
            try :
                return stdin[1:], Fraction(storage[0], 1) + Fraction(storage[1], storage[2])
            except :
                error()
        if(stdin[0] == '(') :
            stdin = stdin[1:]
            stdin, result = calc(stdin)
            storage.append(result)
        elif(stdin[0] == ')') :
            return stdin[1:], result
        else :
            storage.append(int(stdin[0]))
            stdin = stdin[1:]

def check(stdin) : 
    checking = []
    for i in stdin :
        if(i == '(') :
            checking.append(i)
        elif(i == ')' and not checking) :
            error()
        elif(i == ')' and checking) :
            checking = checking[:-1]
            
    if(checking) :
        error()

def error() :
    print(-1)
    exit(0)

def main() :
    temp = input()
    stdin = input().split()
    check(stdin)
    a, result = calc(stdin + [')'])
    print(result._numerator, result._denominator)

main()