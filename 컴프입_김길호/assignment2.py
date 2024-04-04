def main() :
    n = int(input())
    for i in range(n, 1, -1) :
        if(isPrime(i)) :
            print(i)
            break

def isPrime(num) :
    now = 2
    while(now * now <= num) :
        if(num % now == 0) :
            return False
        now += 1
    return True

main()