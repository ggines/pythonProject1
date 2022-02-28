MSG_FRASES= "Introdueix un text: "
MSG_True= "El fitxer existeix"
MSG_False= "El fitxer no existeix"

def file_open(archivo):
  f= open(archivo, "a+")
  f.close()

def file_read(archivo):
  f= open(archivo, "r")
  print(f.read())
  f.close()

def file_write(archivo):
  f= open(archivo, "w")
  str = input(MSG_FRASES)
  f.write(str)
  f.close()