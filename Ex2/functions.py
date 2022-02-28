#MSG_True= "El fitxer existeix"
#MSG_False= "El fitxer no existeix"

def file_write(fname,str):
  f= open(fname, "a")
  f.write(str)
  f.close()