def main():
    state= "Practica els problemes de list comprehensions per a ser més Pythonic!"
    espacios= [x for x in state if x in " "]
    print(len(espacios))

if __name__ == '__main__':
    main()