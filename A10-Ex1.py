def main():
    num1 = int(input("Introduce un valor entero: "))
    num2 = int(input("Introduce otro valor entero: "))

    if num1 < num2:
        for x in range(num1, num2):
            print(x, end=" ")
    else:
        print("Error")

if __name__ == '__main__':
    main()
