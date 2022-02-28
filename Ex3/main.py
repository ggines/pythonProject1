from functions import file_open
from functions import file_read
from functions import file_write
#from functions import check_file
MSG1= "Introduce el nombre del fichero que quieres crear: "
MSG2= "Introduce el nombre del fichero que quieres mostrar: "
MSG3= "Introduce el nombre del fichero que quieres modificar: "
MSG_MENU= "----------Elige una opción----------\n 1- Crear un fichero\n 2- Mostrar contenido de un fichero\n 3- Modificar contenido de un fichero\n 4- Salir"

def main():
    print(MSG_MENU)
    opcion= int(input())

    if opcion == 1:
        archivo = input(MSG1)
        file_open(archivo)
    elif opcion == 2:
        archivo = input(MSG2)
        file_read(archivo)
    elif opcion == 3:
        archivo = input(MSG3)
        file_write(archivo)
    elif opcion == 4:
        exit()
    else:
        print("Error")
if __name__ == '__main__':
    main()
