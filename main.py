#demana nom del fitxer, que vol introduïr i ho mostri
from functions import file_open
from functions import file_write
from functions import check_file
MSG= "Introdueix el nombre del fitxer: "

def main():
    fichero = input(MSG)
    check_file(fichero)
    f= file_open(fichero)
    file_write(fichero,f)
if __name__ == '__main__':
    main()
