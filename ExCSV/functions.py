import csv
MSG= "Hi han"
MSG2= "registres"
MSG3= "i"
MSG4= "dones"

def file_read(fname):
  line_count=0
  suma=0
  with open(fname) as csvfile:
    readCSV= csv.DictReader(csvfile, delimiter=',')
    for row in readCSV:
      line_count += 1
      if row['Sexe'] == 'Dona':
        suma += 1
    print(MSG, line_count, MSG2, MSG3, suma, MSG4)