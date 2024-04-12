def main() :
    for i in range(100, 1000) :
        x = i // 100
        y = i // 10 % 10
        z = i % 10
        if(i == x ** 3 + y ** 3 + z ** 3) :
            print(i)

main()
