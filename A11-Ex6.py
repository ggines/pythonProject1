def main():
    state= "Practica els problemes de list comprehensions per a ser més Pythonic!"
    palabras= [x for x in state if len(x)< 5]
    print(palabras)
if __name__ == '__main__':
    main()