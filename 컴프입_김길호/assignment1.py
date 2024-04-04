def main() :
    num = int(input())
    while(num) :
        print(num % 10, end = "")
        num //= 10

main()