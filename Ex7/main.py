import csv
from functions import file_header
from functions import file_write
from functions import file_read
#from functions import check_file
MSG= "Vols introduir més registres? Sí=1 No=0 "
MSG2= "Aquests són tots els registres: "
MSG_Error= "Error"

def main():
    file_header('files/bio.csv')
    opcion=1
    while opcion==1:
        bio= dict()
        bio['Data'] = input("Introdueix la data: ")
        bio['Nom'] = input("Introdueix el nom: ")
        bio['Localització'] = input("Introdueix la localització: ")
        bio['Espècie'] = input("Introdueix l'espècie: ")
        bio['Mida'] = input("Introdueix la mida: ")
        bio['Característiques'] = input("Introdueix les característiques: ")
        opcion=int(input(MSG))
        file_write('files/bio.csv',bio)
    if opcion==0:
        print(MSG2)
        file_read('files/bio.csv')
    else:
        print(MSG_Error)
if __name__ == '__main__':
    main()