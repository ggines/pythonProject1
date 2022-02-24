MSG_FRASES= "Introdueix un text: "
MSG_True= "El fitxer existeix"
MSG_False= "El fitxer no existeix"

def file_write(fname):
  f= open(fname, "w")
  str = input(MSG_FRASES)
  f.write(str)
  f.close()