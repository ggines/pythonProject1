import csv
from functions import file_read
from functions import file_write
from functions import check_file
MSG= "Introduce el nombre del fichero: "
MSG_MENU= "*********Elige una opción*********\n 1-Leer CSV\n 2-Añadir datos al CSV\n"
MSG2= "Introduce los registros separados por comas: "
MSG_Error= "Error"

def main():
    opcion= int(input(MSG_MENU))
    if opcion == 1:
        archivo= input(MSG)
        check_file(archivo)
        file_read(archivo)
    elif opcion == 2:
        registro= input(MSG2)
        file_write('Registre_d_explotacions_ramaderes.csv',registro)
    else:
        print(MSG_Error)
if __name__ == '__main__':
    main()
