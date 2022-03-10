import csv
from functions import file_check
from functions import file_write
from functions import file_header
MSG= "Introdueix la quantitat de registres que vols introduir: "
MSG_any= "Introdueix l'any: "
MSG_nom= "Introdueix el nom: "
MSG_personalitat= "És personalitat o entitat? "
MSG_sexe= "És home o dona? "
MSG_desc= "Introdueix la descripció: "
MSG_title= "Té títol pòstum? "
MSG_decret= "Introdueix el decret: "
MSG_url= "Introdueix la URL: "
MSG_Error= "Error"

def main():
    count = int(input(MSG))
    check = file_check('Creus_de_Sant_Jordi.csv')
    if check == False:
        file_header('Crus_de_Sant_Jordi.csv')
    for x in range(count):
        creus = dict()
        creus['year'] = input(MSG_any)
        creus['Nom'] = input(MSG_nom)
        creus['Personalitat'] = input(MSG_personalitat)
        creus['Sexe'] = input(MSG_sexe)
        creus['Description'] = input(MSG_desc)
        creus['title'] = input(MSG_title)
        creus['decret'] = input(MSG_decret)
        creus['url'] = input(MSG_url)
        file_write('Creus_de_Sant_Jordi.csv', creus)
    #file_read('Crus_de_Sant_Jordi.csv')
if __name__ == '__main__':
    main()