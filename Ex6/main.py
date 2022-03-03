import csv
from functions import file_header
from functions import file_write
#from functions import check_file
MSG= "Vols introduir més registres? Sí=1 No=0 "
MSG_Error= "Error"

def main():
    file_header('files/books.csv')
    opcion=1
    while opcion==1:
        book= dict()
        book['isbn'] = input("Introdueix l'isbn del llibre: ")
        book['title'] = input("Introdueix el títol del llibre: ")
        book['author'] = input("Introdueix l'autor del llibre: ")
        book['editorial'] = input("Introdueix l'editorial del llibre: ")
        book['pub_date'] = input("Introdueix la data de publicació del llibre: ")
        opcion=int(input(MSG))
        file_write('files/books.csv',book)
    if opcion==0:
        exit()
    else:
        print(MSG_Error)
if __name__ == '__main__':
    main()
