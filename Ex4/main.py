import csv
from functions import file_write
from functions import file_header
#from functions import check_file
MSG= "Introduce el nombre del fichero: "
MSG_Nom= "Introduce el nombre: "
MSG_Cognom= "Introduce el apellido: "
MSG_Edat= "Introduce la edad: "
MSG_Tecno= "Elige la tecnologia en que estas interesad@:\n 1-Ciberseguridad\n 2-Realidad virtual\n 3-Realidad aumentada\n"

def main():
    archivo = input(MSG)
    file_header(archivo)
    while input != 0:
        nom = input(MSG_Nom)
        if nom == ('0'):
            exit()
        cognom = input(MSG_Cognom)
        if cognom == ('0'):
            exit()
        edat = input(MSG_Edat)
        if edat == 0:
            exit()
        opcion = int(input(MSG_Tecno))
        if opcion == 1:
            tecno = 'Ciberseguridad'
        elif opcion == 2:
            tecno = 'Realidad virtual'
        elif opcion == 3:
            tecno = 'Realidad aumentada'
        elif opcion == 0:
            exit()
        else:
            print("Error")
        ID=nom.upper()[:2]+'-'+cognom.upper()[-2:]+'-'+edat
        file_write(archivo, ID, nom, cognom, edat, tecno)
if __name__ == '__main__':
    main()