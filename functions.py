MSG_FRASES= "Introdueix una frase: "
MSG_True= "El fitxer existeix"
MSG_False= "El fitxer no existeix"
def check_file(fichero):
  try:
    f = open(fichero, "r")
    print(MSG_True)
  except FileNotFoundError:
    print(MSG_False)
  else:
    f.close()

def file_open(fichero):
  f = open(fichero, "a+")
  return f

def file_write(fichero, f):
  str = input(MSG_FRASES)
  f.write(str)
  f.close()