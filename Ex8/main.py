import csv
from functions import file_write
#from functions import check_file
MSG= "Vols introduir més registres? Sí=1 No=0 "
MSG_Error= "Error"

def main():
    file_write('projects_board.csv')
if __name__ == '__main__':
    main()