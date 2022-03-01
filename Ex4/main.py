import csv
from functions import file_write
from functions import file_header
#from functions import check_file
MSG= "Introduce el nombre del fichero: "
MSG_ID= "Introduce el ID (2 primeras letras del nombre, 2 ultimas letras del apellido y la edad, separados por guiones: "
MSG_Nom= "Introduce el nombre: "
MSG_Cognom= "Introduce el apellido: "
MSG_Edat= "Introduce la edad: "
MSG_Tecno= "Elige la tecnologia en que estas interesad@:\n 1-Tecnologia1\n 2-Tecnologia2\n 3-Tecnologia3\n"

def main():
    archivo = input(MSG)
    file_header(archivo)
    while input != 0:
        ID= input(MSG_ID)
        if ID == ('0'):
            exit()
        nom = input(MSG_Nom)
        if nom == ('0'):
            exit()
        cognom = input(MSG_Cognom)
        if cognom == ('0'):
            exit()
        edat = int(input(MSG_Edat))
        if edat == 0:
            exit()
        opcion = int(input(MSG_Tecno))
        if opcion == 1:
            tecno = 'Tecnologia1'
        elif opcion == 2:
            tecno = 'Tecnologia2'
        elif opcion == 3:
            tecno = 'Tecnologia3'
        elif opcion == 0:
            exit()
        else:
            print("Error")
        file_write(archivo, ID, nom, cognom, edat, tecno)
if __name__ == '__main__':
    main()
