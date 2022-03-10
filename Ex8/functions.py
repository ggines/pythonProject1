import csv
MSG= "Hi han"
MSG2= "projectes"
MSG3= "El total de facturació és de"
MSG4= "euros"

def file_write(fname):
  line_count=0
  suma=0
  with open(fname) as csvfile:
    readCSV= csv.DictReader(csvfile, delimiter=',')
    for row in readCSV:
      suma += int(row['preu'])
      line_count += 1
    print(MSG, line_count, MSG2)
    print(MSG3, suma, MSG4)