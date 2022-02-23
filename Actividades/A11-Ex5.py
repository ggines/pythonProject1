def main():
    state= "Practica els problemes de list comprehensions per a ser més Pythonic!"
    vocales= [x for x in state if not x in "aeiou"]
    print(vocales)
if __name__ == '__main__':
    main()