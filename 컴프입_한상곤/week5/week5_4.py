def main() :
    for i in range(16) :
        print("fibo({:>3}) = {}".format(i, fibo(i)))

def fibo(num) :
    if(num == 0 or num  == 1) :
        return 1
    return fibo(num - 1) + fibo(num - 2)

main()