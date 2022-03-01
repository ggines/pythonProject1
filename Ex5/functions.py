import csv
#MSG_True= "El fitxer existeix"
MSG_False= "El fitxer no existeix, torna a introduir un (Tens 3 intents):"

def check_file(archivo):
  x=0
  try:
    f= open(archivo,"r")
  except FileNotFoundError:
    while x<3:
      archivo= input(MSG_False)
      x=x+1
    if x==3:
      exit()

def file_read(archivo):
  with open(archivo) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
      print(' '.join(row))

def file_write(fname, registro):
  with open(fname, 'a') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    writeCSV.writerow([registro])