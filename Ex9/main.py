import csv
from functions import file_header
from functions import file_write
from functions import file_read
#from functions import check_file
MSG= "Quants vídeos vols introduir? "
MSG_grup= "Introdueix el grup/cantant del vídeo: "
MSG_nom= "Introdueix el nom del vídeo: "
MSG_dia= "Introdueix el día de publicació: "
MSG_mes= "Introdueix el mes de publicació: "
MSG_year= "Introdueix l'any de publicació: "
MSG_views= "Introdueix les visites del vídeo: "
MSG_Error= "Error"

def main():
    count= int(input(MSG))
    file_header('videos.csv')
    ID = 0
    for x in range(count):
        video= dict()
        video['grup'] = input(MSG_grup)
        video['nom'] = input(MSG_nom)
        video['dia'] = input(MSG_dia)
        video['mes'] = input(MSG_mes)
        video['year'] = input(MSG_year)
        video['views'] = input(MSG_views)
        ID += 1
        data= video['dia'] + '/' + video['mes'] + '/' + video['year']
        file_write('videos.csv', video, ID, data)
    file_read('videos.csv')
if __name__ == '__main__':
    main()