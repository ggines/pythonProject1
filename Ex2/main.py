from functions import file_write
#from functions import check_file
MSG_FRASES= "Introdueix un text (no més de 100 caracters): "
MSG_Error= "Torna a introduir un text amb menys 100 caracters: "

def main():
    str = input(MSG_FRASES)
    while len(str) > 100:
        str = input(MSG_Error)
    file_write('text.txt', str)
if __name__ == '__main__':
    main()
