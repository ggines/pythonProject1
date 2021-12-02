# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    num = int(input("Introdueix un nombre: "))
    suma = 1
    sumaFinal = 0
    for x in range(num):
        suma = x + suma
        if suma < num:
            print(x, end=" ")
            sumaFinal = x + sumaFinal
    print("\nLa suma final es: ", sumaFinal)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
